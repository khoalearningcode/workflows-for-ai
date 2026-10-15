"""Self-contained tests for the optional clean-source gate; no dependencies beyond Python/Git."""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parent / "require_clean_source.py"


def git(cwd, *args):
    subprocess.run(["git", *args], cwd=cwd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


class SourceGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        git(self.repo, "init", "-q")
        git(self.repo, "config", "user.name", "Test")
        git(self.repo, "config", "user.email", "test@example.invalid")
        (self.repo / ".gitignore").write_text("results/\n")
        (self.repo / "model.py").write_text("x = 1\n")
        git(self.repo, "add", ".gitignore", "model.py")
        git(self.repo, "commit", "-qm", "Initial")

    def gate(self, classification="decision", allow=False):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--run-class", classification] + (["--allow-dirty"] if allow else []),
            cwd=self.repo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    def test_clean_committed_state(self):
        self.assertEqual(self.gate().returncode, 0)

    def test_ignored_outputs_allowed(self):
        (self.repo / "results").mkdir()
        (self.repo / "results" / "log.json").write_text("{}")
        self.assertEqual(self.gate().returncode, 0)

    def test_modified_tracked_source_denied(self):
        (self.repo / "model.py").write_text("x = 2\n")
        self.assertEqual(self.gate().returncode, 1)

    def test_untracked_source_denied(self):
        (self.repo / "new_script.py").write_text("pass\n")
        self.assertEqual(self.gate().returncode, 1)

    def test_dirty_diagnostic_labeled(self):
        (self.repo / "new_script.py").write_text("pass\n")
        r = self.gate("diagnostic", allow=True)
        self.assertEqual(r.returncode, 0)
        self.assertIn('"evidence_grade": "provisional_dirty"', r.stdout)
        self.assertEqual(self.gate("promotion", allow=True).returncode, 1)


if __name__ == "__main__":
    unittest.main()
