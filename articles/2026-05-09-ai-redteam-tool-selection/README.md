# W3 — AI 红队工具选型指南（6 类 18 款）

> 配套公众号文章：《AI 红队工具怎么选？6 类 18 款对比》（2026-05-09 上线）
>
> 数据采集：2026-05-08 GitHub API 实时拉取
>
> 持续更新：每周更新一次 Stars / 维护活跃度 / 新增工具

---

## 4 大权威分类背书

| 来源 | 时间 | 链接 |
|------|------|------|
| OWASP LLM Top 10 2025 | 2024-11 | https://owasp.org/www-project-top-10-for-large-language-model-applications/ |
| OWASP GenAI Red Teaming Guide | 2025-01 | https://genai.owasp.org/resource/genai-red-teaming-guide/ |
| NIST AI 600-1 + AI RMF | 2024-07 | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf |
| CSA Agentic AI Red Teaming Guide | 2025-05 | https://cloudsecurityalliance.org/artifacts/agentic-ai-red-teaming-guide |

---

## 6 大类 × 18 款工具对照表

### A 提示注入测试（Prompt Injection Testing）

| 工具 | Stars | 维护 | 语言 | License | 一句话 |
|------|------|------|------|---------|------|
| [microsoft/PyRIT](https://github.com/microsoft/PyRIT) | 3,805 | 0d ago | Python | MIT | 微软出品工业级，prompt injection / jailbreak / 多模态 |
| [cyberark/FuzzyAI](https://github.com/cyberark/FuzzyAI) | 1,360 | 90d | Jupyter | Apache-2.0 | CyberArk 出品，自动化 LLM fuzzing |
| [utkusen/promptmap](https://github.com/utkusen/promptmap) | 1,189 | 157d ⚠️ | Python | GPL-3.0 | 自定义 LLM 应用扫描器，维护减弱 |

**直接选**：PyRIT。微软维护，今天还在 push，社区生态好。

### B 越狱+综合红队（Jailbreak + LLM Red Teaming）

| 工具 | Stars | 维护 | 语言 | License | 一句话 |
|------|------|------|------|---------|------|
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 20,965 ⭐ | 0d ago | TypeScript | MIT | 顶流。Test prompts/agents/RAGs，红队+渗透+漏扫 |
| [msoedov/agentic_security](https://github.com/msoedov/agentic_security) | 1,864 | 93d | Python | Apache-2.0 | Agentic LLM 漏扫 + AI 红队工具包 |
| [confident-ai/deepteam](https://github.com/confident-ai/deepteam) | 1,683 | 10d ago | Python | Apache-2.0 | 红队 LLM 与 LLM 系统的框架 |

**直接选**：promptfoo。事实工业标准，21k stars。

### C Agent / MCP 安全（Agent Security & MCP）

| 工具 | Stars | 维护 | 语言 | License | 一句话 |
|------|------|------|------|---------|------|
| [snyk/agent-scan](https://github.com/snyk/agent-scan) | 2,364 | 0d ago | Python | Apache-2.0 | Snyk 出品，扫 AI agents / MCP servers |
| [splx-ai/agentic-radar](https://github.com/splx-ai/agentic-radar) | 966 | 161d ⚠️ | Python | Apache-2.0 | LLM agentic workflows 安全扫描，维护减弱 |
| [slowmist/MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist) | 828 | 374d ⚠️ | - | MIT | SlowMist 出品 MCP 清单（spec 类型，更新频率天然低） |

**直接选**：snyk/agent-scan。商业公司维护，跟 Snyk SCA 工具栈打通。

### D LLM Gateway / Guardrail（安全控制层）

| 工具 | Stars | 维护 | 语言 | License | 一句话 |
|------|------|------|------|---------|------|
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | 46,122 ⭐ | 0d ago | Python | NOASSERTION | AI Gateway 顶流。100+ LLM 统一接入 |
| [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) | 11,638 | 43d ago | TypeScript | MIT | 1600+ LLM + 50+ AI Guardrails 集成 |
| [protectai/llm-guard](https://github.com/protectai/llm-guard) | 2,931 | 143d ⚠️ | Python | MIT | LLM 安全工具包，维护减弱 |

**直接选**：LiteLLM + Portkey 二选一。LiteLLM 占用率高但有 CVE 历史（参考 W2 文章），Portkey 出生即带 Guardrail。

### E 可观测 / Eval（质量层）

| 工具 | Stars | 维护 | 语言 | License | 一句话 |
|------|------|------|------|---------|------|
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | 26,799 ⭐ | 0d ago | TypeScript | NOASSERTION | LLM 工程平台顶流。Observability + Eval + Prompt 管理 |
| [comet-ml/opik](https://github.com/comet-ml/opik) | 19,239 | 0d ago | Python | Apache-2.0 | Comet ML 出品。Debug + Eval + Monitor |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | 15,227 | 0d ago | Python | Apache-2.0 | LLM Eval Framework，跟 deepteam 同公司 |

**直接选**：langfuse。社区最大、教程最多。**注意：langfuse 是事后审计，不能拦攻击。要实时拦截去 D 类。**

### F 综合 AI 红队平台

| 工具 | Stars | 维护 | 语言 | License | 一句话 |
|------|------|------|------|---------|------|
| [aliasrobotics/cai](https://github.com/aliasrobotics/cai) | 8,432 | 17d ago | Python | NOASSERTION | Cybersecurity AI (CAI) Framework |
| [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) | 3,650 | 4d ago | Python | Apache-2.0 | 腾讯出品全栈 AI 红队平台 |
| [microsoft/AI-Red-Teaming-Playground-Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs) | 1,927 | 83d ago | TypeScript | MIT | 微软 AI 红队培训实验室（含基础设施） |

**直接选**：腾讯 AI-Infra-Guard。国内项目，活跃维护，腾讯背书，全栈型平台。

---

## 5 场景决策矩阵

| 你的场景 | 必装 | 推荐加 | 可选 |
|---------|------|--------|------|
| 单 LLM 应用（chatbot / 客服） | promptfoo (B) + LiteLLM (D) | langfuse (E) | PyRIT (A) |
| RAG 系统（文档问答） | promptfoo (B) + langfuse (E) | Portkey (D) | FuzzyAI (A) |
| Agent / MCP 系统 | snyk/agent-scan (C) + langfuse (E) | LiteLLM (D) | deepteam (B) |
| 多智能体编排 | snyk/agent-scan (C) + AI-Infra-Guard (F) | promptfoo (B) | langfuse (E) |
| 企业一站式 SOP | AI-Infra-Guard (F) + langfuse (E) | promptfoo (B) | snyk/agent-scan (C) |

### 3 条决策规则

1. **必装三件套：B + D + E** — promptfoo 红队 + Gateway 拦截 + langfuse 监控，少一个都漏
2. **Agent 系统必上 C 类** — 传统 LLM 工具不覆盖 Agent 特殊威胁（CSA 12 类）
3. **F 类是替代不是补充** — 平台型工具适合小团队（≤3 人），不要又装 F 又装 A B C D E

---

## 不推荐的工具（避坑）

| 工具 | 原因 | 替代 |
|------|------|------|
| promptmap | 157 天没更新，社区已转向 PyRIT | A 类 → PyRIT |
| agentic-radar | 跟 splx-ai 商业产品绑定深，开源版功能阉割，161 天没更新 | C 类 → snyk/agent-scan |
| llm-guard | 曾是 D 类标杆，团队精力转移，143 天没更新 | D 类 → Portkey gateway |

---

## D 类 vs E 类边界（90% 的人画错）

- **D = 安全控制（实时拦截）**：请求进来先过 Guardrail → 发现攻击 → **直接拒绝**。代表：LiteLLM / Portkey / llm-guard
- **E = 质量工程（事后评估）**：跑了 N 条 prompt → 把日志/token/质量记下来 → **复盘看哪条出了问题**。代表：langfuse / opik / deepeval

混用后果：你以为 langfuse 能拦住攻击，结果它只能告诉你"刚才那条攻击成功了"。

---

## 维护活跃度图谱

| 区间 | 工具 |
|------|------|
| 🟢 活跃区（0-30d）| promptfoo / LiteLLM / langfuse / opik / deepeval / PyRIT / snyk/agent-scan / 腾讯/AI-Infra-Guard / deepteam / cai |
| 🟡 慢节奏区（31-90d）| Portkey / Microsoft Labs / FuzzyAI / agentic_security |
| 🔴 维护减弱区（91-180d）| llm-guard / promptmap / agentic-radar |
| ⚠️ 接近停滞（>180d）| MCP-Security-Checklist（spec 类型，更新频率天然低，不是停滞） |

---

## 持续更新

- 每周一次 Stars / 维护活跃度数据更新
- 新工具发现 → 加到对应类别
- 有重大事件（CVE / 厂商点名 / 商业化）→ 在工具备注栏标注

---

## 反馈 / 加新工具

- Issue：https://github.com/taielab/ai-security-workshop/issues
- Pull Request：欢迎补充新工具或更新数据

---

**配套阅读**：

- 公众号原文：《AI 红队工具怎么选？6 类 18 款对比》
- 上一篇 W2：[CVE-2026-30623 LiteLLM 实战 + 加固](../2026-05-13-mcp-cve-30623/README.md)
