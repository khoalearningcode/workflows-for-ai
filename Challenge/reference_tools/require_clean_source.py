#!/usr/bin/env python3
"""Optional reference Git source gate for agent-driven experimental runs.

This is NOT a complete reproducibility checker: data/model/config revisions,
external services, checkpoints and GPU conditions must be separately recorded.

Usage (from anywhere inside a Git repo):
    python require_clean_source.py --run-class decision
    python require_clean_source.py --run-class diagnostic --allow-dirty

Prints machine-readable JSON to stdout. Fails closed when source is dirty,
except explicitly permitted scratch/diagnostic work (which remains ineligible
for official/promotion evidence). Git-ignored files, such as run outputs,
are excluded from the working-tree dirtiness check by design.
"""

import argparse
import datetime as dt
import hashlib
import json
import subprocess
import sys
from pathlib import Path


def git(*args: str) -> bytes:
    proc = subprocess.run(["git", *args], capture_output=True, check=False)
    if proc.returncode:
        raise RuntimeError(proc.stderr.decode("utf-8", errors="replace").strip() or "git command failed")
    return proc.stdout


def check(run_class: str, allow_dirty: bool) -> tuple[dict, int]:
    if run_class not in {"scratch", "diagnostic", "decision", "promotion", "submission"}:
        return {"error": f"Invalid run class: {run_class}"}, 2
    try:
        root = Path(git("rev-parse", "--show-toplevel").decode().strip())
        sha = git("rev-parse", "HEAD").decode().strip()
        # -z is critical: paths containing newlines and Unicode are safe.
        status_raw = git("status", "--porcelain=v1", "-z", "--untracked-files=all")
        statuses = [item[:2].decode("ascii", "replace") for item in status_raw.split(b"\x00") if item]
        dirty = bool(statuses)
        tracked_diff = git("diff", "--binary", "HEAD", "--")
        # Untracked file contents aren't in the tracked diff.  The digest below
        # is only a diagnostic fingerprint; it is NOT a recoverable patch.
        status_fingerprint = hashlib.sha256(status_raw + b"\n" + tracked_diff).hexdigest()
    except (RuntimeError, OSError) as exc:
        return {"error": str(exc), "accepted": False}, 2

    dirty_allowed = allow_dirty and run_class in {"scratch", "diagnostic"}
    accepted = not dirty or dirty_allowed
    record = {
        "source_sha": sha,
        "repo_root": str(root),
        "run_class": run_class,
        "git_dirty": dirty,
        "dirty_entry_count": len(statuses),
        "status_fingerprint_sha256": status_fingerprint if dirty else None,
        "evidence_grade": "provisional_dirty" if dirty else "clean_source",
        "accepted": accepted,
        "checked_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "notice": (
            "Dirty scratch/diagnostic evidence is not promotion-grade."
            if dirty and accepted else
            "Refused: tracked or nonignored untracked changes exist."
            if dirty else
            "Source state clean; external artifact lineage not validated."
        ),
    }
    return record, (0 if accepted else 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-class", choices=["scratch", "diagnostic", "decision", "promotion", "submission"], required=True)
    parser.add_argument("--allow-dirty", action="store_true", help="Only for scratch/diagnostic; output remains provisional")
    args = parser.parse_args()
    record, returncode = check(args.run_class, args.allow_dirty)
    print(json.dumps(record, ensure_ascii=False, indent=2))
    return returncode


if __name__ == "__main__":
    sys.exit(main())
