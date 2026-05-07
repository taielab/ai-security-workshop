# Changelog

按时间倒序追加。

## [Unreleased]

## [v1.0.0] — 2026-05-13

### Added

- W2 主轨第 2 篇配套：CVE-2026-30623 LiteLLM MCP STDIO 命令注入实战
  - `articles/2026-05-13-mcp-cve-30623/poc/poc_vulnerable.py` — 真实 RCE 复现（直接攻击 mcp.client.stdio）
  - `articles/2026-05-13-mcp-cve-30623/poc/poc_hardened.py` — allowlist 拦截对照
  - `articles/2026-05-13-mcp-cve-30623/hardening/litellm_hardening.py` — 3 维度加固层（command + args + env）
  - `articles/2026-05-13-mcp-cve-30623/reproduction/` — docker 完整版（备选）
- 仓库初始化：README / LICENSE / 目录结构

### Hooks

- Issue 模板：bug-report / feature-request / new-cve-report
- CI：Python lint workflow

---

## 即将上线

- **2026-05-20**：W3 LiteLLM 供应链投毒溯源（PyPI 投毒事件 / 30+ 项目影响清单）
- **2026-05-27**：W4 企业 MCP 部署 18 项自检清单 + SOP
