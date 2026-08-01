from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CliTests(unittest.TestCase):
    def _run(self, *arguments: str):
        return subprocess.run(
            [sys.executable, "tools/psak.py", *arguments],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_offline_commands_pass_on_repository(self):
        for arguments in (
            ("validate",),
            ("render", "--check"),
            ("check",),
        ):
            with self.subTest(arguments=arguments):
                result = self._run(*arguments)
                self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("OK: all offline checks passed", self._run("check").stdout)


if __name__ == "__main__":
    unittest.main()
