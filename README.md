# Engineering Skills v0.2

一套根据上游原始材料研究、融合和改写的工程 Skills。包含 10 个不带统一品牌前缀的入口，覆盖 16 项能力。指令与方法参考使用英文，交流和交付语言跟随用户。

这是 v0.2 开发分支上的源码版本，尚未安装到任何宿主。v0.2 将通用 `prototype` 收窄为 `frontend-prototype`，并把前端设计能力拆成可按需复用的方法：原型负责探索与验证前端体验，`implement` 只加载生产实现所需的前端约束，`tech-review` 只加载前端评审 lens。当前已完成源码和来源账本更新；**尚未完成 v0.2 的独立模型行为评估或跨宿主验收**。

## 入口如何划分

按用户要完成的工作划分入口，而不是把每项内部能力都变成一个命令。一个任务可以用到多个方法，但不要求依次走完全部入口。

| 入口 | 负责的能力 | 适用请求与边界 |
|---|---|---|
| [tech-design](skills/tech-design/SKILL.md) | requirements-design、domain-modeling、solution-evaluation、architecture-design | 定义行为、概念、选型或职责边界；按问题选模式，不把四项当作固定阶段 |
| [research](skills/research/SKILL.md) | research | 解决事实不确定性、证据冲突和版本问题；不强行替用户重做选型 |
| [work-plan](skills/work-plan/SKILL.md) | planning | 整理待决问题或可验收任务、依赖和迁移顺序；不推翻已定设计 |
| [frontend-prototype](skills/frontend-prototype/SKILL.md) | frontend-prototype | 用低成本、可操作的轻量原型回答具体布局或交互问题；只做影响判断的部分，不提前建设生产前端 |
| [implement](skills/implement/SKILL.md) | implementation、test-design | 实现、重构、测试设计或补测；测试方案可以独立交付 |
| [diagnose](skills/diagnose/SKILL.md) | debugging | 原因不明的故障调查与已授权修复，形成症状到原因的证据链 |
| [tech-review](skills/tech-review/SKILL.md) | architecture-review、design-review、code-review | 架构、设计、代码评审；不同对象采用不同检查方法，默认只读 |
| [handover](skills/handover/SKILL.md) | handoff | 为继续任务整理必要上下文，或核实交接后恢复工作 |
| [doc-archive](skills/doc-archive/SKILL.md) | document-archival | 判断积累资料的去留，执行归档、查找历史或恢复；不绑定日常任务收尾 |
| [skill-dev](skills/skill-dev/SKILL.md) | skill-development | 新建和修改可复用 Skills，完成实际文件与可执行检查；来源融合及模型评估按需开展 |

`tech-design` 负责形成业务与技术决策，`research` 负责事实证据，`work-plan` 负责工作安排，`frontend-prototype` 负责用最少实现让用户判断具体界面方案；独立原型优先 HTML/CSS/少量 JavaScript，复用项目以是否省事或影响判断为准。技术 spike 不再由单独的通用 prototype 入口拥有；独立实验取证由 `research` 的实验参考承接，设计、实现与诊断中的局部实验留在原任务内。`implement` 与 `tech-review` 保持通用入口，只在前端任务中加载各自的 frontend lens。

名称采用短词或必要的语义限定，不使用统一品牌前缀。v0.2 将原 `prototype` 重构为 `frontend-prototype`，并把前端原型、生产实现、前端评审统一到同一套方法家族下，但保持不同的交付标准。

## 名称调整与安装约束

| 原名 | 当前名 | 原因 |
|---|---|---|
| `design` | `tech-design` | 区分软件工程设计与宿主视觉设计功能，避免替换同名捆绑 Skill |
| `plan` | `work-plan` | 避开宿主计划模式入口，同时覆盖待决问题与实施任务安排 |
| `debug` | `diagnose` | 区分代码故障诊断与宿主日志、报告上传功能 |
| `review` | `tech-review` | 避开内置评审命令及别名，保留架构、设计、代码三种模式 |
| `handoff` | `handover` | 区分工程上下文交接与宿主会话迁移 |
| `prototype` | `frontend-prototype` | v0.1 的通用原型同时覆盖业务状态、工程实验和 UI，职责与设计/研究重叠；v0.2 收窄为前端交互与视觉原型 |

不注册旧名别名，避免重新引入冲突。若已经安装过旧草稿，先确认旧目录的来源和用户修改，再用完整的新目录替换对应的旧入口，并按宿主要求刷新；不要只改 frontmatter，也不要把新旧两套同时放入发现范围。`manifest.json` 的 `renamed_entries` 是迁移记录，不是运行时别名。

**不要将本集合与上游同名 Skill 未经消歧地混装。**检查范围应包括宿主实际发现的用户目录、项目目录、父目录、插件及捆绑资源，而不只是一个安装文件夹。原版与本集合仍需重点检查的重名入口包括 `implement`、`research`；`prototype` 和 `handoff` 作为旧安装残留检查。`frontend-prototype` 需要按实际宿主验证发现与解析行为。发现同名时，明确选择来源，或使用经验证可区分的命名空间；禁止静默覆盖、拼接正文、合并资源目录或猜测优先级。

下面是 2026-09-20 对关键规则的文档核查，**不是八宿主运行验收**。不同类型的占用不应统一计作“无法调用”。

| 宿主 | 已知机制及占用 | 本集合的处理 |
|---|---|---|
| Claude Code | 内置 `/plan`；`/review` 是 `/code-review` 的别名；自定义同名 Skill 可以替换捆绑 Skill，`/design` 和 `/debug` 属于捆绑能力 | 使用新名，避免覆盖与别名歧义；目录名、frontmatter 和 UI 名称同步更新。[命令](https://code.claude.com/docs/en/commands)、[同名解析](https://code.claude.com/docs/en/skills#resolve-skills-that-share-a-name) |
| Codex CLI / IDE | `/plan`、`/review` 是宿主命令，Skill 可通过 `$name` 或 `/skills` 选择；不是同一个调用空间。相同 `name` 的多个 Skill 可能同时出现在选择器中 | 例如 `$work-plan`、`$tech-review`；检查实际 Skill 来源，不把 `/plan` 误记为拦截 `$plan`。[Skill 调用](https://learn.chatgpt.com/docs/build-skills)、[宿主命令](https://learn.chatgpt.com/docs/developer-commands?surface=cli) |
| Hermes | 内置命令及别名优先；同名 Skill 可用 `/skill <name>`。`/plan`、`/review` 已占用；`/debug` 上传报告，`/handoff` 迁移会话 | 使用新名；显式解析测试不得为了试旧名而上传日志或迁移真实会话。[命令与冲突规则](https://hermes-agent.nousresearch.com/docs/reference/slash-commands) |
| Kimi Code | 外部 Skill 使用 `/skill:<name>`；只有未被系统命令占用时才支持 `/<name>` 简写。`/plan` 为系统入口 | 如 `/skill:work-plan`；显式区分系统命令、简写与完整 Skill 入口。[官方命令说明](https://www.kimi.com/code/docs/en/kimi-code-cli/reference/slash-commands.html) |
| agy | 官方执行模式页记载 `1.1.0` 移除旧 `/planning`，改用模式切换或 `/plan`；需按实际版本核对 | 不把旧矩阵中的“只有 `/planning`”作为长期无冲突保证。[执行模式](https://www.antigravity.google/docs/cli/modes/) |
| ZCode / Pi / DSH | 收到过占用矩阵，但本轮未完成这三者的逐版本独立核验 | 保持待验证，不将“未发现”写成“已兼容”，也不提供未经验证的调用语法 |

安装验收应确认新入口实际加载了本集合对应的 `SKILL.md`，并且宿主原有命令行为未被改变。候选名未出现在命令表中，只能作为检查线索，不能替代安装后的实际解析证据。当前 v0.2 分支仍仅生成源码，没有安装或修改宿主配置。

## 方法深度放在哪里

每个入口包含 `SKILL.md`、`agents/openai.yaml`、本地 `references/` 和第三方来源声明。入口负责选路、共通约束与完成标准；v0.2 当前 35 份参考文件保留分支方法，当前篇幅见结构检查记录。读取条件直接写在入口中，每个 Skill 的运行说明不依赖同级其他 Skill 或作者机器上的路径。

当前选择任务入口加条件加载的本地参考，保留足够的执行方法，不以“正文越短越好”为目标。参考文件按职责组织：不同 Skill 中同名的 `frontend.md` 可以分别讲架构、实现和评审；共同原则保持一致，但不要求整篇内容相同。暂不新增统一方法库、生成步骤或前端专用实现／评审入口，具体取舍见 [组织依据](provenance/v0.2-frontend-method-family.md#organization-chosen-for-this-revision)。

清晰的实现请求可以直接落实，必要的局部设计属于任务本身，不要求先产出设计文档或原型。已有决策从项目材料读取并尊重；方法与验证范围按受影响行为和风险选择，小改不自动扩成完整产品审查。

保留的具体方法包括：完整调用方负担与模块深度、同题不同接口设计、指定技术尽调、前后端目录边界、决策依赖与渐进迁移、真实依赖保真度、独立测试预期、复现与逆向追踪、失败语义回归、WIP 全范围评审、交接状态核实、隔离评估与公平基线。

上游规则不是照单全收。例如：固定两个评审代理、固定假设数量、无法复现便禁止继续分析、三次修复失败便认定架构错误、自动提交、强制 tracker，都被改为有条件的方法或明确拒绝。精确取舍见 [方法融合记录](provenance/method-map.md)。v0.1 来源核对及取舍见 [历史来源复核记录](provenance/source-audit.md)；v0.2 修正与实测结果见 [验证状态](evals/status.md)。

## 设计组织与实施拆解

设计文档是否拆分，与实施任务是否拆分分别判断。现有单篇设计默认保留；确有独立维护收益时先提出具体组织方案，取得同意后拆分，已有授权不重复确认。用户要求保持完整时，使用章节定位和按需阅读。

`work-plan` 根据结果边界、依赖、上下文负担、验证及独立接续需要选择执行方式：简单修改直接做，相关多步骤使用简短清单，需要独立执行的单元准备 task spec。它是任务执行说明，可放在计划章节、已有 issue 或独立文件中；不要求每个编码步骤再建文件。高风险任务补充必要的兼容、恢复和集成条件。

`implement` 在入口应用这一判断，复杂工作先完成必要的局部规划，不依赖另一个 Skill 的安装。执行当前单元时读取其说明与必要来源，发现设计或前置成果变化就修正受影响说明。单元完成后继续已授权的后续任务；整体完成仍需整体验收。`handover` 保留当前单元与接续依据，不复制所有任务或重新拆票。

设计描述行为与决策，计划安排结果和依赖，task spec 给出任务边界、依据和验收；共享事实引用其维护位置。仅在消除关键歧义时保留简短接口或数据示例，不在三层材料中重复预写完整实现与测试。执行材料按需要逐步细化，关键约束不能因追求简短而遗漏。

## 项目文档如何维护

日常文档维护仍纳入各工作入口：开始时读取相关材料，事实或决策确定时及时记录，完成前检查本次工作是否使维护中的文档失真；文档仍准确就不修改。`doc-archive` 处理资料积累后的去留、历史组织与恢复，不替代这些日常责任。

| 入口 | 维护责任 |
|---|---|
| `tech-design` | 修订当前设计；及时记录已确定术语；按需创建、更新或替代 ADR |
| `research` / `frontend-prototype` | 保留可追溯证据，指出对设计的影响；原型结论不自动成为已接受决策 |
| `work-plan` | 将必要文档同步纳入受影响任务的验收，计划阶段不提前宣称实施完成 |
| `implement` | 实施中处理设计偏差，完成前同步授权范围内失真的文档并记录实际验证证据 |
| `diagnose` | 依据文档判断预期行为；授权修复时维护受影响资料，纯调查保持只读 |
| `tech-review` | 检查代码与当前设计、决策和上下文的一致性；未经修订授权不修改 |
| `handover` | 链接正式资料，明确待同步位置与后续动作，不替代正式文档 |
| `doc-archive` | 区分当前资料与历史资料，保留有效信息和未决义务，维护归档引用、检索入口及恢复依据 |
| `skill-dev` | 交付实际 Skill 修改，按需同步既有来源、许可和受影响的验证记录；不把单项目约定推广成通用规则 |

设计承载行为与方案，ADR 保留重要取舍及历史理由，计划和交接承载临时进度。`CONTEXT.md` 的职责以项目约定为准，不默认等于术语表或任意内容的记录本。沿用现有位置，有实质内容和读者才创建新材料。

ADR 可以维护状态、追加注明日期的结果和证据；推翻核心决策时创建替代记录并双向关联。轻量 ADR 优先链接计划和验证材料。既有模板若混淆状态或缺少关键依据，应在授权范围内改进。方案接受、实现完成、验证通过分别记录。

本集合采用以下默认状态规范。这是结合上游方法形成的综合设计，不是所有上游共同规定的状态机，也不是必须逐级推进的审批流程。

| 维度 | 默认状态 | 维护位置 |
|---|---|---|
| 决策 | `draft`、`proposed`、`accepted`、`rejected`、`deprecated`、`superseded` | 设计文档或 ADR，记录状态变更日期与决策依据 |
| 实施 | `not-started`、`in-progress`、`blocked`、`implemented` | 优先由计划维护，设计链接；部分完成注明已完成和剩余范围 |
| 验证 | 按验收项记录 `not-run`、`passed`、`failed`、`blocked`、`stale` | 验证记录，标明范围或版本、检查、日期和证据 |

`deprecated` 表示曾生效但已不再指导新工作的决策，没有直接替代；`superseded` 必须链接替代记录。评审通过不自动接受决策，实现完成不自动验证通过。没有独立计划或验证记录的小任务可在原文简短记录，不为填字段创建空文件。

实际决策、实施进展、检查结果或证据适用范围变化时更新相应状态。设计、代码或环境发生实质变化时，仅重新评估受影响的旧结论并标记 `stale`，保留历史证据。不要把局部测试通过写成整体运行验收，也不要因实现失败自动否定已接受决策。

旧约定不自动等于合理规范。可保留语义明确的中文或自定义标签；如果只有含义混杂的“完成”“通过”，则依据实际证据在本次授权文档范围内拆分。无法确认的状态明确标注未知并保留旧记录，不虚构审批人、历史日期或验证。调整时保护历史理由、稳定引用和工具兼容，不借机批量迁移无关文档。

已授权任务内的必要同步不重复请求批准；明确的只读、指定文件范围仍然有效。无法在范围内修正的矛盾应指出具体位置与所需变更。相关行为用例已准备，尚未完成独立模型执行验证。

## 积累资料如何归档

`doc-archive` 支持只评估、实际归档、历史查找和恢复。阶段结束、方案替代或目录积压都是盘点的触发因素，不能据此自动退休文档。工作结果、文档权威和归档状态分别判断：已实现设计可能仍是当前规范，取消方案可以保留为历史，暂停计划不自动归档。

根据现有约定、引用成本和资料是否继续演进，选择移动文件、原位更新状态与索引，或保存历史快照。不预设年份／主题目录、不安装上游 CLI，也不自动提交、打标签或删除。授权执行按具体处置清单推进，处理冲突、中断恢复、链接和索引；已授权范围不逐文件重复确认。

可直接提出“评估这些文档哪些适合归档，先不修改”“按已确定的清单归档并修复引用”或“找回这份归档方案，核对是否仍适用”。归档结果应让读者找到当前入口和历史入口；恢复文件位置不代表恢复决策权威或验证有效性。此入口按需使用，不成为每次任务完成后的强制步骤。

## 来源与可追溯性

主要研究了 Matt Pocock、citypaul、Anthropic、obra/superpowers、arjunprabhulal、klittle32 的相关 Skills，以及 Vercel ADR、Warp review-spec、OpenSpec、Spec Kit 的相关材料。v0.2 前端方法家族另外对照了 Anthropic `frontend-design`、Impeccable、UI/UX Pro Max、Taste Skill 与 Vercel Web Interface Guidelines；研究范围限于来源锁定中列出的文件，不代表完整评估各项目的子参考、脚本或知识库；当前整合说明见 [v0.2 frontend method family](provenance/v0.2-frontend-method-family.md)。

- [来源锁定文件](provenance/sources.lock.json)：v0.2 当前 102 个文件的仓库、固定 commit、原始链接、SHA-256 和阅读范围。此前 80 份记录保留；归档入口补充 OpenSpec、GSD、PACEflow、SDLC Studio、llm-wiki 的方法与许可来源，选段阅读标明行号。只锁定实际使用的来源，不把整个检索范围写成全文评估。
- [方法映射](provenance/method-map.json)：v0.2 当前 30 组方法的原始材料、保留内容、调整理由和最终文件。归档新增三组方法；此前判别用例保留，新增入口没有为缺少执行器的模型评估制造题库。
- 各 Skill 的 `THIRD_PARTY_NOTICES.md`：独立复制时保留的来源、修改声明和适用许可文本。没有为整个新集合擅自选定统一发布许可证。

来源锁定表示研究时的固定版本，不声称是各项目当前最新版；选段阅读也不代表完整评估整个框架。本地格式复核使用宿主提供的 `skill-creator` 校验脚本，不是运行这些 Skills 的前提。

## 验证到什么程度

v0.2 当前是分支开发版本。已完成入口、manifest、旧 prototype 评估引用和 provenance 目标的结构迁移；旧 generic prototype 的历史用例没有强行改写成前端用例，因此 **frontend-prototype 暂无独立行为基线**。`implement` 和 `tech-review` 的既有行为题仍保留，但新增 frontend lens 也尚未做独立模型执行验证。

已通过本地结构校验和 9 项工具回归测试，结果见 [v0.2 验证状态](evals/status.md)。结构校验检查入口/manifest 一致性、引用闭包、用例声明、来源映射和宿主名称场景，不证明方法效果。独立模型评估在问题、执行机制与授权具备时开展，不作为本次源码修订的强制前置。

原通用 prototype 的 4 个用例保留在 [历史用例](evals/retired-cases.json) 中，其中 SQLite 作者演练仍可复现；它们不计入 v0.2 的 53 个活动用例，也不证明新的前端能力。历史日志保持原样。

## 本地复核

以下命令在本目录执行。Skills 本身没有 Python 运行依赖；PyYAML 仅用于维护校验。

```bash
python3 -m venv /tmp/engineering-skills-check
/tmp/engineering-skills-check/bin/pip install -r tooling/requirements.txt
/tmp/engineering-skills-check/bin/python tooling/validate.py
/tmp/engineering-skills-check/bin/python -B -m unittest discover -s tooling -p 'test_*.py' -v
python3 -B tooling/materialize.py debug-wrong-theory /tmp/cart-case
python3 -B tooling/run_author_exercises.py /tmp/engineering-author-run
```

导出和演练目标必须是新目录，已有目录会被拒绝。导出工具只产生请求和原始工作文件，不附评分标准；真正的模型隔离还要由评估环境限制可读目录和上下文，临时目录本身不是安全沙箱。

源码入口位于 `skills/`。如需单独取用某项，保留对应目录的完整内容，包括参考文件与第三方声明。当前目录下的评估材料、工具和来源总表用于维护，不应一起作为执行模型的额外提示。
