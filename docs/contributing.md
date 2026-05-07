# 贡献指南 · Contributing

欢迎贡献！

---

## 怎么贡献

### 1. 提报新 CVE / 安全事件

发现 AI 生态新的安全事件？提 Issue（用 `new-cve-report` 模板）。

如果该事件值得写一篇公众号 + 配套代码，我会跟你联系协作。

### 2. 报 Bug

跑脚本遇到问题？提 Issue（用 `bug-report` 模板）。粘贴完整 traceback + 环境信息。

### 3. 加新工具 / 改进脚本

直接 PR：

```bash
git clone https://github.com/taielab/ai-security-workshop
git checkout -b feature/your-feature
# 改代码
git commit -m "feat: 一句话描述"
git push origin feature/your-feature
# 在 GitHub 上提 PR
```

PR checklist：

- [ ] 代码自测通过
- [ ] 含 README / docstring 说明用法
- [ ] 不引入新外部依赖（除非必要 / PR 中说明）
- [ ] 风险声明：仅用于自查 / 修复 / 不教别人怎么搞破坏

### 4. 翻译 / 文档

公众号文章的英文版翻译、新文章的英文 README — 都欢迎。

---

## 代码风格

- Python：PEP 8 + 类型注解（见 `.github/workflows/lint.yml`）
- 注释：英文为主（项目国际化路线）
- 文档：中文为主 + 英文 fallback

---

## 不接受的 PR

- 教人怎么入侵他人系统（白帽研究除外）
- 含恶意 payload（哪怕"只是演示"）
- 与 AI / 安全无关的话题

---

## 联系

- GitHub Issue（推荐）
- 公众号「AI 安全工坊」群
- 微信 1V1（公众号文章末尾）
