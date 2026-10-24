# Clear Communication

让 Agent 从组织内容时就写得自然、清楚，尤其改善中文表达。覆盖日常回答、进度汇报、技术解释、故障分析、代码审查、commit 消息和文档。

技能要求直接回答问题，写清主体、动作、条件和因果，保留必要解释；同时保护事实、数字、否定、范围、动作状态和不确定性。代码、原始日志、逐字引用和机器格式不随文风调整而改变。

“自然”指容易理解，不是伪装身份、添加语气词或强制口语化。没有固定句长、禁词表或统一的输出模板。

## 安装与使用

技能采用 [Agent Skills](https://agentskills.io/specification) 格式。把下面这段话发给你使用的 Agent，让它自行读取并安装：

```text
请阅读 https://github.com/devillee/clear-communication-skill ，
将其中的 clear-communication 技能安装到你支持的技能目录。
```

技能入口是 [skills/clear-communication/SKILL.md](skills/clear-communication/SKILL.md)。安装时保留 `clear-communication/SKILL.md` 的目录结构，具体位置由 Agent 按自身的技能加载方式确定。

如果只想在当前会话使用，也可以直接让 Agent 读取这个 `SKILL.md`，并按其中要求完成当前任务，无需先安装。

安装后，可以明确要求“使用 clear-communication 完成当前任务”。是否自动选用、能否在后续会话中持续应用，取决于 Agent 的技能加载机制和模型。

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
