<div align="center">

<img src="assets/brand/logo.jpg" alt="AI Security Workshop" width="160"/>

# AI Security Workshop

**企业 AI 落地的安全实战工具集**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/taielab/ai-security-workshop?style=social)](https://github.com/taielab/ai-security-workshop/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/taielab/ai-security-workshop?style=social)](https://github.com/taielab/ai-security-workshop/network/members)
[![Last commit](https://img.shields.io/github/last-commit/taielab/ai-security-workshop)](https://github.com/taielab/ai-security-workshop/commits/main)
[![Issues](https://img.shields.io/github/issues/taielab/ai-security-workshop)](https://github.com/taielab/ai-security-workshop/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](docs/contributing.md)

**[中文](README.md)** · [English](README_EN.md)

[**快速开始**](#快速开始) · [**最新文章**](#最新文章) · [**主题归类**](#主题归类) · [**贡献**](#贡献) · [**扫码联系**](#扫码联系)

</div>

---

> 配套公众号「AI 安全工坊」高频更新 · CVE 实战复现 + 生产级加固代码 + 企业自检脚本 · MIT License

## 这是什么

公众号「**AI 安全工坊**」高频更新主轨技术文章，配套：

- **可复现 PoC 脚本**（Python / Docker）
- **加固代码**（生产可用）
- **检测脚本**（一键排查公司是否中招）
- **自检清单**（PDF / Markdown）

本仓库是这些脚本和工具的**官方代码仓库**，所有代码 MIT License，欢迎 Star / Fork / Issue / PR。

---

## 最新文章

| 日期 | 文章 | 主题 | 内容 |
|------|------|------|------|
| **2026-05-09** | [AI 红队工具怎么选？6 类 18 款对比](articles/2026-05-09-ai-redteam-tool-selection/) | 工具选型 / 决策矩阵 | 6 类 18 款工具对照表 + 5 场景决策矩阵 + 4 大权威分类背书 |
| 2026-05-07 | [我在 30 行 Python 里拿到 LiteLLM 的 root：CVE-2026-30623 实战 + 加固](articles/2026-05-13-mcp-cve-30623/) | MCP STDIO 命令注入 | poc_vulnerable / poc_hardened / litellm_hardening |
| TBD | W4 主题待定（视 W3 数据后定） | TBD | TBD |

---

## 主题归类

- 🔒 **MCP 安全**：协议级漏洞、STDIO 攻击、Anthropic Agent 安全
- 🛡️ **Agent 安全**：越权访问、权限隔离、Agent 失控复盘
- 🔍 **红队工具**：渗透测试脚本、CVE 复现、Bug Bounty
- 📋 **企业自检**：合规清单、部署 SOP、检测脚本
- 🌊 **供应链溯源**：PyPI 投毒、镜像中毒、依赖审计
- 🐍 **Python 加固**：allowlist、参数校验、env 注入防御

---

## 快速开始

### Clone

```bash
git clone https://github.com/taielab/ai-security-workshop
cd ai-security-workshop
```

### 跑某篇文章的 PoC

```bash
# 例：跑 W2 主轨第 2 篇的 CVE-2026-30623 复现
cd articles/2026-05-13-mcp-cve-30623/poc
pip install -r requirements.txt
python3 poc_vulnerable.py
cat /tmp/pwned.txt    # 看到 RCE 证据
```

### 集成共享加固层到自己生产

```python
from shared.mcp_security.allowlist import validate_mcp_command

# 在你的 LiteLLM proxy / Agent 框架的 add_mcp_server 入口前调
validate_mcp_command(cmd, args, env)
```

---

## 目录结构

```
ai-security-workshop/
├── articles/                            # 按文章组织（一篇一目录）
│   ├── 2026-05-13-mcp-cve-30623/       # 每周主轨配套代码
│   │   ├── README.md                    # 本篇简介 + 公众号链接
│   │   ├── poc/                         # 复现脚本
│   │   ├── hardening/                   # 加固代码
│   │   └── reproduction/                # docker 完整版（备选）
│   └── ...
├── shared/                              # 跨文章共享代码（去重 / 生产可用）
│   └── mcp_security/
│       ├── allowlist.py
│       └── detection.py
├── checklists/                          # 自检清单（Markdown 源 / 可生成 PDF）
│   └── 18-mcp-deploy-self-check.md
├── docs/                                # 长文档（GitHub Pages 友好）
│   ├── getting-started.md
│   ├── faq.md
│   └── contributing.md
└── .github/                             # Issue 模板 + CI
```

---

## 为什么做这个

我是 [taielab](https://github.com/taielab) — AI + 安全方向技术工程师，长期专注企业级 AI 安全的研究与工程化落地。

研究 → 工程化 → 生产部署 → 服务真实企业，全链路都跑过。

99% AI 博主告诉你**怎么用 AI**。我告诉你**怎么用 AI 不踩雷**。

把每周文章里的脚本沉淀到这里，让你：

1. 公司部署前，能跑 PoC 自查是否中招
2. 中招后，能直接抄加固代码救命
3. 长期用，能积累一套企业 AI 落地的安全合规工具集

---

## 相关链接

| 渠道 | 内容 | 链接 |
|---|---|---|
| 公众号 | 主轨深度文（每周一篇）| 「AI 安全工坊」（扫码关注 ↓） |
| 知识星球 | CVE 第一手分析 + 企业落地避坑 | 扫码加入 ↓ |
| GitHub | 代码工具集（本仓库）| [taielab/ai-security-workshop](https://github.com/taielab/ai-security-workshop) |
| 个人微信 | 工程师交流 / 企业 AI 安全咨询（备注来意） | 扫码加好友 ↓ |

### 扫码联系

<table>
  <tr>
    <td align="center">
      <img src="assets/contact/wechat-official.png" alt="公众号「AI 安全工坊」" width="200"/><br/>
      <sub><b>公众号「AI 安全工坊」</b><br/>每周一篇主轨深度文</sub>
    </td>
    <td align="center">
      <img src="assets/contact/zsxq-aff.png" alt="知识星球「AI 安全工坊」" width="200"/><br/>
      <sub><b>知识星球</b><br/>CVE 第一手 + 企业落地</sub>
    </td>
    <td align="center">
      <img src="assets/contact/wechat-personal.jpg" alt="个人微信" width="200"/><br/>
      <sub><b>个人微信</b><br/>工程师交流 / 企业 AI 安全（备注「GitHub」）</sub>
    </td>
  </tr>
</table>

---

### 其他相关项目 / 知识资源

**自营知识资源**

- 🧰 [aiseckit.com](https://aiseckit.com/) — **AI 安全工具导航站**，找工具 / 找入口
- 📚 [飞书 AI 安全开放知识库](https://my.feishu.cn/wiki/TTAkwC0GliX141kZBSuccucrnDb) — 中文 AI 安全完整知识库（数据 / 模型 / Agent / RAG / MCP / A2A / 供应链 / 治理）

**GitHub 开源项目**

- [taielab/awesome-hacking-lists](https://github.com/taielab/awesome-hacking-lists) — 1.3k+ Stars · 渗透测试 + AI 攻防工具索引
- [taielab/Taie-Bugbounty-killer](https://github.com/taielab/Taie-Bugbounty-killer) — 自动化漏赏挖掘
- [taielab/Taie-RedTeam-OS](https://github.com/taielab/Taie-RedTeam-OS) — 定制 Ubuntu 红队 OS
- [taielab/YinVulnKiller](https://github.com/taielab/YinVulnKiller) — 企业漏扫平台

---

## 贡献

欢迎贡献！

- 发现新的 AI 安全 CVE / 漏洞？提 Issue（用 `new-cve-report` 模板）
- 用脚本踩到 bug？提 Issue（用 `bug-report` 模板）
- 想加新工具 / 改进现有脚本？欢迎 PR

详见 [CONTRIBUTING.md](docs/contributing.md)。

---

## 风险声明

- 本仓库所有 PoC 仅用于**安全研究 / 自查 / 修复验证**
- 在他人系统上未经授权运行 PoC 等同于非法入侵，**法律责任自负**
- 复现脚本仅在本地容器或隔离环境运行
- 加固代码已自测，但不替代专业安全审计
- 生产部署前请人工审计

---

## License

[MIT](LICENSE) — 自由使用，商用前请审计代码。

如果本仓库帮你识别 / 修复了一个真实的企业 AI 安全风险，欢迎 ⭐ Star 让我知道值得继续维护。
