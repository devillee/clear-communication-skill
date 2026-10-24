# Clear Communication

让 Agent 从组织内容时就写得自然、清楚，尤其改善中文表达。覆盖日常回答、进度汇报、技术解释、故障分析、代码审查、commit 消息和文档。

技能要求直接回答问题，写清主体、动作、条件和因果，保留必要解释；同时保护事实、数字、否定、范围、动作状态和不确定性。代码、原始日志、逐字引用和机器格式不随文风调整而改变。

“自然”指容易理解，不是伪装身份、添加语气词或强制口语化。没有固定句长、禁词表或统一的输出模板。

## 安装与使用

运行所需文件只有 [skills/clear-communication/SKILL.md](skills/clear-communication/SKILL.md)。把 `clear-communication` 目录安装到 Agent 支持的技能目录即可，README、许可证和测试文件不需要进入运行目录。

在 Codex 中，可以请求：

```text
从 https://github.com/devillee/clear-communication-skill 安装 skills/clear-communication 到我的全局技能目录。
```

Codex 的默认全局目录是 `~/.codex/skills`；设置了 `CODEX_HOME` 时使用其下的 `skills` 目录。其他 Agent 按各自的技能加载方式安装。

使用时可以明确要求“使用 clear-communication 完成当前任务”。技能只有加载后才能影响生成；是否自动选用、能否持续应用，取决于宿主和模型，不能保证覆盖每次输出。

## 测试

测试文件位于 `tests/`，使用固定输入材料，不操作真实设备、账号或仓库。每次修改技能后，应让 Agent 读取当前 `SKILL.md`，独立回答 [cases.json](tests/cases.json)，并将答复保存为以场景 ID 为键的 JSON 对象。

运行不依赖第三方包的保护检查：

```sh
python3 tests/check_outputs.py
```

也可以检查自行生成的答复文件：

```sh
python3 tests/check_outputs.py path/to/answers.json
```

脚本检查场景是否齐全、指定原文是否保留以及 JSON 格式契约。自然度、语义保真和因果是否成立仍需按 [criteria.json](tests/criteria.json) 逐项审阅，不能只凭脚本通过判断技能有效。

最近一次验证见 [测试报告](tests/report.md)。它只说明指定场景中的观察结果，不代表所有模型或 Agent 的表现。

## License

[MIT](LICENSE)
