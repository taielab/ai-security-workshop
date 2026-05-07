"""Smoke tests for shared.mcp_security.validate_mcp_command (4 layered cases)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared.mcp_security import validate_mcp_command


class TestValidateMcpCommand(unittest.TestCase):
    def test_layer1_blocks_unlisted_command(self) -> None:
        with self.assertRaisesRegex(ValueError, r"\[Layer 1 blocked\]"):
            validate_mcp_command("/bin/sh", ["-c", "whoami"], {})

    def test_layer2_blocks_shell_metacharacters_in_args(self) -> None:
        with self.assertRaisesRegex(ValueError, r"\[Layer 2 blocked\]"):
            validate_mcp_command("python3", ["-c", "import os; os.system('id')"], {})

    def test_layer3_blocks_loader_env_injection(self) -> None:
        with self.assertRaisesRegex(ValueError, r"\[Layer 3 blocked\]"):
            validate_mcp_command("python3", ["-V"], {"LD_PRELOAD": "/tmp/evil.so"})

    def test_legitimate_invocation_passes(self) -> None:
        validate_mcp_command("npx", ["@some-mcp-server/cli"], {})


if __name__ == "__main__":
    unittest.main(verbosity=2)
