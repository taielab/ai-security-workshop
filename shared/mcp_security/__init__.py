"""
shared.mcp_security — Production-grade defenses for the MCP STDIO transport layer.

Public API:
    validate_mcp_command(cmd, args, env)
        Three-dimensional pre-flight check before passing user-controlled fields
        to mcp.client.stdio.StdioServerParameters. Raises ValueError on any
        violation; the caller is expected to surface it as HTTP 4xx.

See `allowlist.py` for the implementation, threat model, and tunable knobs.

Reference articles:
    - W2 (2026-05-13) CVE-2026-30623 walkthrough
    - articles/2026-05-13-mcp-cve-30623/README.md
"""

from .allowlist import validate_mcp_command

__all__ = ["validate_mcp_command"]
