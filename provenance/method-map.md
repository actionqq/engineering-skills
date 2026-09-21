# 方法融合记录

根据固定版本原文取舍；来源锁定与阅读范围见 [sources.lock.json](sources.lock.json)。判别用例是评估定义，不代表已执行通过。

## requirements

- 保留：沿决策依赖澄清，区分现状与行为变更，用可观察场景形成验收。 设计保持行为、关键决策和验收的完整性，文档组织与实施拆解分别判断。
- 调整或拒绝：不把每个事实变成用户访谈，不要求已授权工作重新审批，也不强制固定规格目录或 CLI。 单篇设计的拆分尊重用户选择及既有授权；代码只保留消除关键歧义的最小示例，不堆叠完整实现。
- 落点：[skills/tech-design/references/requirements.md](../skills/tech-design/references/requirements.md), [skills/tech-design/SKILL.md](../skills/tech-design/SKILL.md)
- 来源：[mattpocock/skills:skills/productivity/grilling/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/grilling/SKILL.md), [mattpocock/skills:skills/engineering/grill-with-docs/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/grill-with-docs/SKILL.md), [mattpocock/skills:skills/engineering/to-spec/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/to-spec/SKILL.md), [Fission-AI/OpenSpec:docs/concepts.md](https://raw.githubusercontent.com/Fission-AI/OpenSpec/bae58cf61479986431bb798acbe5a688a591c18c/docs/concepts.md), [obra/superpowers:skills/brainstorming/SKILL.md](https://raw.githubusercontent.com/obra/superpowers/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/brainstorming/SKILL.md)
- 判别用例：`design-requirements`, `design-preserve-single-document`

## domain

- 保留：概念身份、生命周期、不变量、决策原因与被拒方案；以现有上下文减少重新推理。
- 调整或拒绝：沿用有效文档位置与明确语义；对混淆的旧状态按授权范围改进。保留决策历史，不把建议或写代码自动标记为接受，也不越过明确只读或文件范围。
- 落点：[skills/tech-design/references/domain.md](../skills/tech-design/references/domain.md)
- 来源：[mattpocock/skills:skills/engineering/domain-modeling/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/domain-modeling/SKILL.md), [mattpocock/skills:skills/engineering/domain-modeling/ADR-FORMAT.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/domain-modeling/ADR-FORMAT.md), [mattpocock/skills:skills/engineering/domain-modeling/CONTEXT-FORMAT.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/domain-modeling/CONTEXT-FORMAT.md), [vercel/ai:skills/adr-skill/SKILL.md](https://raw.githubusercontent.com/vercel/ai/20dd00abba618d5a516e0fee40ccd3e18a2bd1fb/skills/adr-skill/SKILL.md)
- 判别用例：`design-domain`

## selection

- 保留：区分轻量预查、指定技术尽调、完整选型；硬约束、现有方案、构建成本、退出路径与证据时效。
- 调整或拒绝：不以功能打分覆盖硬约束；不把用户指定技术改成无边界市场调查。
- 落点：[skills/tech-design/references/selection.md](../skills/tech-design/references/selection.md)
- 来源：[citypaul/.dotfiles:claude/.claude/skills/evaluate-existing-solutions/SKILL.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/evaluate-existing-solutions/SKILL.md), [citypaul/.dotfiles:claude/.claude/skills/evaluate-existing-solutions/references/evaluation-dimensions.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/evaluate-existing-solutions/references/evaluation-dimensions.md), [citypaul/.dotfiles:claude/.claude/skills/evaluate-existing-solutions/references/evidence-and-currentness.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/evaluate-existing-solutions/references/evidence-and-currentness.md)
- 判别用例：`design-options`, `design-prescribed`

## module-depth

- 保留：以接口背后隐藏的复杂度衡量模块深度；把调用顺序、失败、所有权等完整调用方负担计入；用反事实内联检查薄封装。
- 调整或拒绝：保留有独立授权、观测、兼容责任的薄边界，不以减少类数或统一层次为目标。
- 落点：[skills/tech-design/references/architecture.md](../skills/tech-design/references/architecture.md), [skills/tech-review/references/architecture.md](../skills/tech-review/references/architecture.md)
- 来源：[citypaul/.dotfiles:claude/.claude/skills/codebase-design/SKILL.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/codebase-design/SKILL.md), [citypaul/.dotfiles:claude/.claude/skills/codebase-design/references/deepening.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/codebase-design/references/deepening.md), [citypaul/.dotfiles:claude/.claude/skills/improve-codebase-architecture/SKILL.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/improve-codebase-architecture/SKILL.md)
- 判别用例：`design-caller-burden`, `review-architecture`

## alternatives

- 保留：同一中性题目下构造实质不同接口，用相同场景评估并寻找最强反对理由。
- 调整或拒绝：只有已授权且可用时采用独立代理；单作者方案比较不冒充独立探索；小改动不强制多个方案。
- 落点：[skills/tech-design/references/alternatives.md](../skills/tech-design/references/alternatives.md)
- 来源：[citypaul/.dotfiles:claude/.claude/skills/codebase-design/references/design-it-twice.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/codebase-design/references/design-it-twice.md)
- 判别用例：`design-caller-burden`, `review-independence`

## structure

- 保留：按真实变化归属决定目录；保留模块深度；依据真实内外边界显式隔离；检查依赖、源码根、深层目录和迁移阶段。 迁移计划包含包索引、架构记录、术语、图示及入门文档的同步和链接检查。
- 调整或拒绝：不把 hexagon 或 DDD 层次作为全项目模板，不用编译通过替代包路径规范检查。
- 落点：[skills/tech-design/references/structure.md](../skills/tech-design/references/structure.md)
- 来源：[citypaul/.dotfiles:claude/.claude/skills/structure-codebase/SKILL.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/structure-codebase/SKILL.md), [citypaul/.dotfiles:claude/.claude/skills/structure-codebase/references/backend-patterns.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/structure-codebase/references/backend-patterns.md), [citypaul/.dotfiles:claude/.claude/skills/structure-codebase/references/visible-hexagon.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/structure-codebase/references/visible-hexagon.md), [citypaul/.dotfiles:claude/.claude/skills/structure-codebase/references/enforcement-and-migration.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/structure-codebase/references/enforcement-and-migration.md)
- 判别用例：`design-architecture`, `design-deep-path`, `plan-migration`, `docs-plan-maintenance`

## frontend

- 保留：区分路由编排、领域特性、真正共享元素；显式判断数据/状态和服务端/客户端边界。
- 调整或拒绝：组件行数或 shared 名字不足以证明抽取合理；不把前端硬塞进后端分层。
- 落点：[skills/tech-design/references/frontend.md](../skills/tech-design/references/frontend.md)
- 来源：[citypaul/.dotfiles:claude/.claude/skills/structure-codebase/references/frontend-patterns.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/structure-codebase/references/frontend-patterns.md)
- 判别用例：`design-frontend`

## research

- 保留：拆解问题、优先一手来源、寻找反证、比较矛盾资料、区分观察与推断。
- 调整或拒绝：不强制来源数量和统一长报告；同源转述不算独立证据；离线结论明确版本范围。
- 落点：[skills/research/references/evidence.md](../skills/research/references/evidence.md)
- 来源：[arjunprabhulal/agent-skills:skills/research/deep-research/SKILL.md](https://raw.githubusercontent.com/arjunprabhulal/agent-skills/42dd24080fce6d731d00e2a1134f398c3da4171b/skills/research/deep-research/SKILL.md), [citypaul/.dotfiles:claude/.claude/skills/evaluate-existing-solutions/references/evidence-and-currentness.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/evaluate-existing-solutions/references/evidence-and-currentness.md)
- 判别用例：`research-conflict`, `research-unavailable`

## planning

- 保留：先画决策依赖，决策具备后按可验证行为切片；意图、任务和验收保持关联；保留扩展、迁移、收缩顺序。 按结果、依赖、上下文负担、验证与接续需求选择清单或独立执行说明；任务引用设计，明确依赖解除条件和整体验收。
- 调整或拒绝：不强制外部 tracker、每次会话一个工单、token 估算、library-first 或完整框架流程。 轻量 task spec、按需细化及上下文恢复规则是本集合的综合设计；不把设计拆文档作为拆任务前提，不强制每步独立文件、新会话或代理，不预写完整实现与测试。
- 落点：[skills/work-plan/references/delivery.md](../skills/work-plan/references/delivery.md), [skills/work-plan/SKILL.md](../skills/work-plan/SKILL.md), [skills/implement/SKILL.md](../skills/implement/SKILL.md)
- 来源：[mattpocock/skills:skills/engineering/wayfinder/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/wayfinder/SKILL.md), [mattpocock/skills:skills/engineering/to-tickets/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/to-tickets/SKILL.md), [github/spec-kit:spec-driven.md](https://raw.githubusercontent.com/github/spec-kit/d4229c071c7ea3885b43e8a7739847300f618f13/spec-driven.md), [Fission-AI/OpenSpec:docs/concepts.md](https://raw.githubusercontent.com/Fission-AI/OpenSpec/bae58cf61479986431bb798acbe5a688a591c18c/docs/concepts.md)
- 判别用例：`plan-decisions`, `plan-migration`, `plan-lightweight-checklist`, `plan-independent-briefs`, `implement-small-without-spec`, `implement-stale-unit-brief`

## interactive-prototype

- 保留：状态/实体实验提供可操纵输入和可观察状态；UI 方案用相同任务和数据比较。
- 调整或拒绝：形式由问题决定；原型允许必要断言，不自动提交或升级成生产功能。
- 落点：[skills/prototype/references/interactive.md](../skills/prototype/references/interactive.md)
- 来源：[mattpocock/skills:skills/engineering/prototype/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/prototype/SKILL.md), [mattpocock/skills:skills/engineering/prototype/LOGIC.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/prototype/LOGIC.md), [mattpocock/skills:skills/engineering/prototype/UI.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/prototype/UI.md)
- 判别用例：`prototype-state`

## faithful-experiment

- 保留：依赖替身按行为保真度选择；明确观察与结论的适用边界。
- 调整或拒绝：补充数据库、并发、性能及迁移实验的真实关键边界；模拟器不能证明目标数据库保证。
- 落点：[skills/prototype/references/experiments.md](../skills/prototype/references/experiments.md), [skills/implement/references/fidelity.md](../skills/implement/references/fidelity.md)
- 来源：[mattpocock/skills:skills/engineering/prototype/LOGIC.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/prototype/LOGIC.md), [mattpocock/skills:skills/engineering/tdd/mocking.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/tdd/mocking.md), [citypaul/.dotfiles:claude/.claude/skills/codebase-design/references/deepening.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/codebase-design/references/deepening.md)
- 判别用例：`prototype-boundary`, `prototype-sqlite`, `implement-test-plan`

## implementation

- 保留：有意义的 red/green、逐个行为切片、通过稳定行为边界验证、成功与失败路径、独立期望值。 完成前对照验收追踪实际成功与失败行为，不以测试成功替代自审。
- 调整或拒绝：不要求为机械小改制造测试，不排斥确有价值的内部算法测试，不自动提交；测试设计可独立交付。
- 落点：[skills/implement/SKILL.md](../skills/implement/SKILL.md), [skills/implement/references/testing.md](../skills/implement/references/testing.md)
- 来源：[mattpocock/skills:skills/engineering/implement/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/implement/SKILL.md), [mattpocock/skills:skills/engineering/tdd/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/tdd/SKILL.md), [mattpocock/skills:skills/engineering/tdd/tests.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/tdd/tests.md)
- 判别用例：`implement-feature`, `implement-test-plan`, `implement-test-code`, `implement-baseline`

## refactor

- 保留：相关行为有保护时整理结构；将机械迁移与行为变更分开，逐步验证真实依赖。 授权迁移后同步反映当前结构的文档，保留历史决策理由。
- 调整或拒绝：补充失败语义等价、用户脏工作区保护、源码根路径和基线区分，不把全部重构推迟到仪式性末尾。
- 落点：[skills/implement/references/refactoring.md](../skills/implement/references/refactoring.md)
- 来源：[mattpocock/skills:skills/engineering/tdd/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/tdd/SKILL.md), [citypaul/.dotfiles:claude/.claude/skills/structure-codebase/references/enforcement-and-migration.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/structure-codebase/references/enforcement-and-migration.md)
- 判别用例：`review-code-regression`, `design-deep-path`, `implement-baseline`

## reproduce

- 保留：构建能抓住目标症状的反馈回路；缩减、重放、差分、二分、性能基线；间歇问题记录发生率和条件。
- 调整或拒绝：拒绝无回路禁止读代码/提出假设、必须完全最小化、固定 3–5 假设；不可复现仍能给有边界的静态证据。 本轮补回正文缺失的二分边界方法；跳过环境失败，保留候选范围，因果确认与定位分开。
- 落点：[skills/diagnose/references/reproduction.md](../skills/diagnose/references/reproduction.md)
- 来源：[mattpocock/skills:skills/engineering/diagnosing-bugs/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/diagnosing-bugs/SKILL.md), [obra/superpowers:skills/systematic-debugging/SKILL.md](https://raw.githubusercontent.com/obra/superpowers/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/systematic-debugging/SKILL.md), [obra/superpowers:skills/systematic-debugging/condition-based-waiting.md](https://raw.githubusercontent.com/obra/superpowers/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/systematic-debugging/condition-based-waiting.md)
- 判别用例：`debug-wrong-theory`, `debug-intermittent`, `debug-no-repro`, `debug-bisect-unknown`

## causal-tracing

- 保留：从坏值向来源回溯，比较正常路径，对可证伪预测逐次探测，根因修复后重跑原场景并清理探针。
- 调整或拒绝：不把三次失败等同架构错误；校验放在实际责任边界，不要求每层重复；区分紧急缓解和根因证明。
- 落点：[skills/diagnose/references/tracing.md](../skills/diagnose/references/tracing.md)
- 来源：[obra/superpowers:skills/systematic-debugging/root-cause-tracing.md](https://raw.githubusercontent.com/obra/superpowers/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/systematic-debugging/root-cause-tracing.md), [obra/superpowers:skills/systematic-debugging/defense-in-depth.md](https://raw.githubusercontent.com/obra/superpowers/5bf4e78011075bcfc0dc295f0724994cd123ee71/skills/systematic-debugging/defense-in-depth.md), [mattpocock/skills:skills/engineering/diagnosing-bugs/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/diagnosing-bugs/SKILL.md)
- 判别用例：`debug-wrong-theory`, `debug-intermittent`, `debug-no-repro`

## design-review

- 保留：检查需求、接口、依赖、缺项、矛盾与可实施性，以具体位置和场景提出建议。
- 调整或拒绝：完整复审重读全文及治理材料；默认只读，已有修订授权则落实；不借评审擅自重写治理文件。
- 落点：[skills/tech-review/references/design.md](../skills/tech-review/references/design.md)
- 来源：[warpdotdev/oz-for-oss:.agents/skills/review-spec/SKILL.md](https://raw.githubusercontent.com/warpdotdev/oz-for-oss/a2bb45f231fd56ea28c1b381999d11b277a0b0e2/.agents/skills/review-spec/SKILL.md), [vercel/ai:skills/adr-skill/SKILL.md](https://raw.githubusercontent.com/vercel/ai/20dd00abba618d5a516e0fee40ccd3e18a2bd1fb/skills/adr-skill/SKILL.md)
- 判别用例：`review-design-full`

## code-review

- 保留：规范与需求双维度；审查真实变更及上下文；独立上下文可以减轻作者锚定。
- 调整或拒绝：修正 HEAD diff 无法覆盖 WIP 的问题；不强制 tracker/两个代理/代码坏味道清单；保留双维度并合并去重、按影响排序。
- 落点：[skills/tech-review/references/code.md](../skills/tech-review/references/code.md), [skills/tech-review/references/independence.md](../skills/tech-review/references/independence.md)
- 来源：[mattpocock/skills:skills/engineering/code-review/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/code-review/SKILL.md), [citypaul/.dotfiles:claude/.claude/skills/improve-codebase-architecture/SKILL.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/improve-codebase-architecture/SKILL.md)
- 判别用例：`review-code-regression`, `review-mixed-wip`, `review-independence`

## handoff

- 保留：按下一任务选择必要上下文、决策、文件阅读顺序、执行状态和启动提示。 按当前执行单元链接 brief、前置成果、剩余工作及集成验证，恢复时核对实际状态。
- 调整或拒绝：补充脏工作区、跨机器可达性、接收端核实和陈旧验证；交接不自动更新记忆或创建/发送任务。 交接不复制所有任务说明、不重新拆解已确定工作，也不把历史完成标签作为依赖已满足的证明。
- 落点：[skills/handover/references/record.md](../skills/handover/references/record.md)
- 来源：[klittle32/handoff-skill:SKILL.md](https://raw.githubusercontent.com/klittle32/handoff-skill/57089b6e1ce61498ec70852e46d41b2f8f12fa00/SKILL.md), [klittle32/handoff-skill:workflows/Handoff.md](https://raw.githubusercontent.com/klittle32/handoff-skill/57089b6e1ce61498ec70852e46d41b2f8f12fa00/workflows/Handoff.md), [klittle32/handoff-skill:references/template.md](https://raw.githubusercontent.com/klittle32/handoff-skill/57089b6e1ce61498ec70852e46d41b2f8f12fa00/references/template.md), [klittle32/handoff-skill:references/destinations.md](https://raw.githubusercontent.com/klittle32/handoff-skill/57089b6e1ce61498ec70852e46d41b2f8f12fa00/references/destinations.md)
- 判别用例：`handoff-write`, `handoff-resume`, `handover-current-unit`

## authoring

- 保留：围绕用途、触发边界和交付定义入口；按分支组织可达资源；新建交付实际文件，修改定位原因并保留无关有效行为。
- 调整或拒绝：主流程聚焦创建与修改，研究只服务于明确的来源融合或方法缺口；保留必要来源与许可，不强制每次建研究档案或评估用例。独立运行不依赖作者私有路径或另一 Skill。
- 落点：[skills/skill-dev/references/authoring.md](../skills/skill-dev/references/authoring.md)
- 来源：[anthropics/skills:skills/skill-creator/SKILL.md](https://raw.githubusercontent.com/anthropics/skills/34040c9c568585f6929bedeaad110ad08f079624/skills/skill-creator/SKILL.md), [mattpocock/skills:skills/productivity/writing-for-agents/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/writing-for-agents/SKILL.md), [mattpocock/skills:skills/productivity/writing-for-agents/SKILL-MECHANICS.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/writing-for-agents/SKILL-MECHANICS.md)
- 判别用例：`skill-dev-create`, `skill-dev-collision`

## evaluation

- 保留：需要且能执行时，使用真实请求、执行轨迹和产物检验行为；修改以旧版检查回归，效果比较采用公平基线；可按请求独立设计评估。
- 调整或拒绝：先确认执行机制和授权，缺少条件就跳过模型评估及准备产物，不用作者演练冒充替代；日常保留可执行的结构、引用、脚本检查。不要求 Claude Code、固定代理或跨宿主评测；原有未执行题库保留为历史材料，不强制续建。
- 落点：[skills/skill-dev/references/evaluation.md](../skills/skill-dev/references/evaluation.md), [skills/skill-dev/references/discovery.md](../skills/skill-dev/references/discovery.md)
- 来源：[anthropics/skills:skills/skill-creator/SKILL.md](https://raw.githubusercontent.com/anthropics/skills/34040c9c568585f6929bedeaad110ad08f079624/skills/skill-creator/SKILL.md), [anthropics/skills:skills/skill-creator/agents/grader.md](https://raw.githubusercontent.com/anthropics/skills/34040c9c568585f6929bedeaad110ad08f079624/skills/skill-creator/agents/grader.md), [anthropics/skills:skills/skill-creator/agents/comparator.md](https://raw.githubusercontent.com/anthropics/skills/34040c9c568585f6929bedeaad110ad08f079624/skills/skill-creator/agents/comparator.md)
- 判别用例：`skill-dev-create`, `skill-dev-collision`, `skill-dev-eval-leak`

## document-ownership

- 保留：重要变更中及时保留有效发现，按信息归属写入现有正式文档；临时进度与长期规则分开，避免重复记录。
- 调整或拒绝：不新增文档入口，不强制每次修改全部文档；读取项目对 CONTEXT 的定义，遵守只读和指定文件边界。将检查落实到各入口职责，非依赖安装 expectations。
- 落点：[skills/diagnose/SKILL.md](../skills/diagnose/SKILL.md), [skills/handover/SKILL.md](../skills/handover/SKILL.md), [skills/implement/SKILL.md](../skills/implement/SKILL.md), [skills/prototype/SKILL.md](../skills/prototype/SKILL.md), [skills/research/SKILL.md](../skills/research/SKILL.md), [skills/skill-dev/SKILL.md](../skills/skill-dev/SKILL.md), [skills/tech-design/SKILL.md](../skills/tech-design/SKILL.md), [skills/tech-review/SKILL.md](../skills/tech-review/SKILL.md), [skills/work-plan/SKILL.md](../skills/work-plan/SKILL.md)
- 来源：[citypaul/.dotfiles:claude/.claude/skills/expectations/SKILL.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/expectations/SKILL.md)
- 判别用例：`docs-design-context`, `docs-design-supersede`, `docs-implement-sync`, `docs-implement-no-churn`, `docs-implement-file-limit`, `docs-research-evidence`, `docs-prototype-promotion`, `docs-plan-maintenance`, `docs-diagnose-readonly`, `docs-review-consistency`, `docs-handover-pending`, `docs-skill-dev-source-chain`, `docs-design-lazy-create`

## document-lifecycle

- 保留：术语确定后即时记录、材料按需创建；设计随约束和方案变化更新；ADR 状态、替代关联、索引及实施证据持续维护，保留历史理由。 明确接受、替代、进度变化和检查结果产生时的维护触发点，保留过往验证的实际适用范围。
- 调整或拒绝：CONTEXT 不固定为术语表；轻量 ADR 链接计划与证据，不强制复制实施细节或引入 OpenSpec 目录/CLI；已授权决策不重复审批，未验证结果不得写为通过。 决策、实施、验证三类状态的分离及失效检查是本集合基于这些来源的综合设计，并非上游共同规定的状态机；经用户确认采用明确的默认状态及最小状态记录要求；具体枚举、三维分离和 stale 语义是本集合的综合设计，不冒充上游原文。允许语义等价标签，授权范围内改进误导性的旧格式；历史或证据不足时保留未知，不推断批准或通过。
- 落点：[skills/tech-design/references/domain.md](../skills/tech-design/references/domain.md), [skills/implement/references/documents.md](../skills/implement/references/documents.md), [skills/tech-design/references/requirements.md](../skills/tech-design/references/requirements.md), [skills/work-plan/SKILL.md](../skills/work-plan/SKILL.md), [skills/tech-review/SKILL.md](../skills/tech-review/SKILL.md), [skills/tech-review/references/design.md](../skills/tech-review/references/design.md)
- 来源：[mattpocock/skills:skills/engineering/domain-modeling/SKILL.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/domain-modeling/SKILL.md), [citypaul/.dotfiles:claude/.claude/skills/ubiquitous-language/SKILL.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/ubiquitous-language/SKILL.md), [vercel/ai:skills/adr-skill/SKILL.md](https://raw.githubusercontent.com/vercel/ai/20dd00abba618d5a516e0fee40ccd3e18a2bd1fb/skills/adr-skill/SKILL.md), [Fission-AI/OpenSpec:docs/concepts.md](https://raw.githubusercontent.com/Fission-AI/OpenSpec/bae58cf61479986431bb798acbe5a688a591c18c/docs/concepts.md)
- 判别用例：`docs-design-context`, `docs-design-supersede`, `docs-design-lazy-create`, `docs-implement-sync`, `docs-implement-no-churn`, `docs-implement-file-limit`, `docs-review-consistency`, `docs-legacy-status`

## published-contracts

- 保留：按实际消费者、序列化、未知值和旧新版本检查兼容；明确重试身份、对象与属性授权、边界资源约束。
- 调整或拒绝：不强制 HTTP、特定版本策略或框架；拒绝规则高于用户要求的措辞。允许明确授权的协调破坏性变更；宽容解析不等于任意字段可写。
- 落点：[skills/tech-design/references/contracts.md](../skills/tech-design/references/contracts.md)
- 来源：[citypaul/.dotfiles:claude/.claude/skills/api-design/SKILL.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/api-design/SKILL.md), [citypaul/.dotfiles:claude/.claude/skills/api-design/resources/api-evolution.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/api-design/resources/api-evolution.md), [citypaul/.dotfiles:claude/.claude/skills/api-design/resources/api-security.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/api-design/resources/api-security.md)
- 判别用例：`design-wire-compatibility`, `design-authorized-break`

## runtime-systems

- 保留：把跨进程依赖、重试和副作用边界补到系统设计，而不止画模块目录。
- 调整或拒绝：综合工程补强：按持久化转移检查故障窗口，结合容量、恢复、可观察性。不是上游完整分布式系统方法的逐条转录；不强制队列、微服务或虚构容量目标。
- 落点：[skills/tech-design/references/systems.md](../skills/tech-design/references/systems.md)
- 来源：[citypaul/.dotfiles:claude/.claude/skills/api-design/SKILL.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/api-design/SKILL.md), [citypaul/.dotfiles:claude/.claude/skills/codebase-design/references/deepening.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/codebase-design/references/deepening.md)
- 判别用例：`design-worker-crash`

## migration-recovery

- 保留：保留渐进迁移、真实边界实验和兼容演进，实施入口可独立获得所需方法。
- 调整或拒绝：综合工程补强：历史数据、检查点、并发写入、值级不变量、发布顺序及代码回滚/数据恢复。条件加载；本地实现不意味着生产操作已获授权。
- 落点：[skills/implement/references/evolution.md](../skills/implement/references/evolution.md)
- 来源：[citypaul/.dotfiles:claude/.claude/skills/structure-codebase/references/enforcement-and-migration.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/structure-codebase/references/enforcement-and-migration.md), [mattpocock/skills:skills/engineering/prototype/LOGIC.md](https://raw.githubusercontent.com/mattpocock/skills/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/prototype/LOGIC.md), [citypaul/.dotfiles:claude/.claude/skills/api-design/resources/api-evolution.md](https://raw.githubusercontent.com/citypaul/.dotfiles/a109f9972bb46671c624fc05752031523e1cf6fc/claude/.claude/skills/api-design/resources/api-evolution.md)
- 判别用例：`implement-backfill-restart`
