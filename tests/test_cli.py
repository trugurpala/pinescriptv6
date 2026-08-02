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

    def test_successful_commands_disclose_local_validation_limits(self):
        limits = (
            "NOT CHECKED: TradingView compilation",
            "NOT CHECKED: Runtime/chart behavior",
            "NOT CHECKED: Repaint behavior",
            "NOT CHECKED: Alert delivery",
            "NOT CHECKED: Market data",
            "NOT CHECKED: Profitability",
        )
        expected = {
            ("validate",): "OK: repository data is valid\n" + "\n".join(limits) + "\n",
            ("check",): "OK: all offline checks passed\n" + "\n".join(limits) + "\n",
            ("render", "--check"): "OK: generated outputs are current\n",
        }
        for arguments, stdout in expected.items():
            with self.subTest(arguments=arguments):
                result = self._run(*arguments)
                self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
                self.assertEqual(result.stdout, stdout)
                self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
