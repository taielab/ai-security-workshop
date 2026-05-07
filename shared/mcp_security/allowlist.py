"""
Three-dimensional defense for the MCP STDIO transport layer.

Threat model:
    The MCP Python SDK's StdioServerParameters.command is propagated directly
    to subprocess.Popen by mcp.client.stdio. Any host that lets external input
    influence command/args/env (LiteLLM, LangChain, LangFlow, Windsurf, Flowise,
    DocsGPT, Agent Zero, GPT Researcher, ...) inherits an authenticated RCE
    primitive. The protocol authors declined to fix this at the spec level
    (calling it "expected behavior"), so every host implementation must enforce
    its own validation.

Defense layers:
    Layer 1 — command allowlist        : basename must be in ALLOWED_COMMANDS
    Layer 2 — args shell metacharacters: blocks ; && || | ` $( and friends
    Layer 3 — env loader hijacks       : blocks LD_PRELOAD / PYTHONPATH / ...

Skipping any layer is exploitable in isolation:
    - Layer 1 alone: bypass via `python -c 'os.system(...)'` (python is allowed)
    - Layer 1+2:     bypass via `python` + `LD_PRELOAD=/tmp/evil.so`

Relationship with LiteLLM official patch (PR #25343, v1.83.7-stable):
    Layer 1 (command allowlist) is byte-equivalent to MCP_STDIO_ALLOWED_COMMANDS
    in litellm/constants.py. Layers 2 and 3 are additional hardening on top of
    the official fix — LiteLLM's patch does NOT validate args/env content, it
    relies on PROXY_ADMIN role-gating of the /mcp-rest/test/* endpoints to
    contain the residual args-based risk (e.g. `docker run --privileged ...`).
    For non-LiteLLM hosts that don't have an equivalent role gate, Layers 2+3
    raise the bar meaningfully without breaking legitimate MCP launchers.

Tunable via env var LITELLM_MCP_STDIO_EXTRA_COMMANDS (comma-separated). The
name is kept for drop-in compatibility with LiteLLM v1.83.7-stable; downstream
consumers may rename freely.

Usage:
    from shared.mcp_security import validate_mcp_command
    validate_mcp_command(cmd, args, env)  # raises ValueError on violation

License: MIT (vendored under shared/ for re-use across articles).
"""

import os
from pathlib import Path
from typing import Dict, List, Optional


ALLOWED_COMMANDS = {"npx", "uvx", "python", "python3", "node", "docker", "deno"}

DANGER_SHELL_CHARS = (";", "&&", "||", "|", "`", "$(", ">/", "</", "&\n")

BLOCKED_ENV_VARS = {
    "LD_PRELOAD",
    "LD_LIBRARY_PATH",
    "PYTHONPATH",
    "PYTHONSTARTUP",
}


def _build_allowlist() -> set:
    """Merge ALLOWED_COMMANDS with the LITELLM_MCP_STDIO_EXTRA_COMMANDS env var."""
    extra = {
        c.strip()
        for c in os.getenv("LITELLM_MCP_STDIO_EXTRA_COMMANDS", "").split(",")
        if c.strip()
    }
    return ALLOWED_COMMANDS | extra


def validate_mcp_command(
    cmd: str,
    args: Optional[List[str]] = None,
    env: Optional[Dict[str, str]] = None,
) -> None:
    """Pre-flight check before StdioServerParameters(command=cmd, args=args, env=env).

    Raises:
        ValueError: any of the three layers rejects the input. Callers should
            translate to HTTP 4xx (do not 5xx — this is user-input rejection,
            not a server fault).
    """
    args = args or []
    env = env or {}
    allowlist = _build_allowlist()

    # Layer 1 — command basename must be in allowlist.
    if not cmd or not cmd.strip():
        raise ValueError("MCP STDIO command must not be empty")
    base = Path(cmd.strip()).name  # /bin/sh -> sh; /usr/bin/python3 -> python3
    if base not in allowlist:
        raise ValueError(
            f"[Layer 1 blocked] MCP STDIO command '{base}' not in allowlist "
            f"{sorted(allowlist)}; extend cautiously via "
            f"LITELLM_MCP_STDIO_EXTRA_COMMANDS"
        )

    # Layer 2 — args must not contain shell metacharacters.
    for a in args:
        if not isinstance(a, str):
            continue
        if any(d in a for d in DANGER_SHELL_CHARS):
            raise ValueError(
                f"[Layer 2 blocked] args contain shell metacharacters: {a[:80]}"
            )

    # Layer 3 — env must not inject loader-hijack variables.
    bad = [k for k in env if k in BLOCKED_ENV_VARS]
    if bad:
        raise ValueError(
            f"[Layer 3 blocked] env contains forbidden loader variables: {bad}"
        )
