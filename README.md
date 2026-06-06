# Codex Stata for Economists

**面向经管实证研究的 Codex 可复现工作流**

**最后更新：** 2026-06-04

---

## 定位

本仓库是一个**公开 workflow 仓库**，保存可复用的研究流程、Stata 流水线、Codex 配置、agents、skills、模板和质量管理规则。

真实个人研究项目应放在**独立的私有工作区**中，并可以作为 private GitHub 仓库保存。

重要的规则只有两条：

- 公开仓库只放 workflow，真实研究内容放私有项目仓库。
- 没有日志或输出表格支撑，就不报告任何数值结论。

---

## 为什么这样设计

经济学实证研究很容易在几个地方失控：研究问题太宽、数据和代码散落、回归规格没有记录、结果解释脱离识别设计、论文中的数字无法追溯。

本仓库的核心思想：

| 原则                 | 说明                                                         |
| -------------------- | ------------------------------------------------------------ |
| **问题先行**   | 先判断研究问题是否重要、具体、可证伪、可 pilot               |
| **私有隔离**   | 每个真实研究项目有独立的私有工作区和 private GitHub 仓库     |
| **流水线复现** | Stata do-file、日志、表格、图形和报告使用固定目录结构        |
| **日志验证**   | 所有系数、标准误、样本量、描述统计都必须能回到 log 或 table  |
| **论文衔接**   | 结果解释、理论诊断、paper QA 和 R&R 回复都接在同一套证据链上 |

---

## 公开仓库与私有研究工作区

推荐结构：**一个公开 workflow 仓库 + 每个研究一个私有 GitHub 仓库**。

```
./
├── workflow-for-economists/          ← 公开 workflow 仓库
│   ├── AGENTS.md                        ← Codex 主规则
│   ├── skills/                          ← 可复用技能包
│   ├── agents/                          ← 专用 Agent 配置
│   ├── templates/                       ← do-file、memo、私有项目骨架等模板
│   ├── scripts/                         ← 运行脚本、质量检查、私有项目创建
│   ├── dofiles/                         ← 公开模板流水线
│   ├── quality_reports/                 ← 质量报告模板
│   ├── reports/                         ← Quarto 报告模板
│   └── results_memos/                   ← 结果解释 memo 模板
│
└── private-research/                    ← 私有研究工作区（示例）
    ├── AGENTS.project.md                ← 本项目专用规则
    ├── data/                            ← 原始数据与中间数据
    ├── dofiles/                         ← 项目 do-file
    ├── logs/                            ← Stata 日志
    ├── output/                          ← 输出表格与图形
    ├── reports/                         ← 论文草稿与 Quarto 报告
    ├── quality_reports/                 ← 问题卡、规格说明、决策记录
    └── results_memos/                   ← 结果解释 memo
```

真实研究项目按 **年月 + 关键词** 命名，例如：

```
202606数字化转型与企业创新
202608平台治理与劳动者福利
202612最低工资与就业结构
```

### 公开 workflow 仓库保存

- Stata 流水线模板（`dofiles/`）
- Agent 和 Skill 定义（`agents/`、`skills/`）
- 可复用模板（`templates/`）
- 质量规则和检查脚本（`scripts/`）
- 工作流文档（`AGENTS.md`、`README.md` 等）

> **注意：** 公开仓库不存放 `data/`、`logs/`、`output/` 目录。这些目录仅在私有研究工作区中创建和使用。

### 私有研究工作区保存

- 原始数据和中间数据（`data/`）
- 项目 do-file（`dofiles/`）
- Stata 日志（`logs/`）
- 输出表格和图形（`output/`）
- Good Question Card（`quality_reports/good_questions/`）
- Requirements Spec（`quality_reports/specs/`）
- 结果解释 memo（`results_memos/`）
- 论文草稿和审稿回复（`reports/`）

> **注意：** 如果数据协议、伦理审查或机构规则禁止把数据放到 GitHub，即使 private repo 也不要提交数据。此时应使用加密磁盘、机构服务器、Git LFS、DVC 或其他合规存储，并在 `data/README.md` 中记录再现路径。

---

## 快速开始

### 第一步：获取 workflow 仓库

```bash
git clone https://github.com/YOUR_USERNAME/workflow-for-economists.git
cd workflow-for-economists
```

### 第二步：创建私有研究工作区

在 workflow 仓库根目录运行：

```powershell
# 创建项目目录
powershell -ExecutionPolicy Bypass -File scripts/new_private_study.ps1 -Keyword "数字化转型与企业创新"

# 同时初始化 Git
powershell -ExecutionPolicy Bypass -File scripts/new_private_study.ps1 -Keyword "数字化转型与企业创新" -InitGit
```

这会创建：

```
~/research/202606数字化转型与企业创新/
```

### 第三步：在私有工作区启动 Codex

**方式一：以私有项目为工作区（推荐）**

```powershell
cd "~/research/202606数字化转型与企业创新"
codex
```

**方式二：以科研根目录为工作区**

在 VS Code 中打开 `~/research/`，所有子项目在同一窗口中可见。需要在对话中明确当前项目：

```text
当前项目：202606数字化转型与企业创新
请读取 workflow-for-economists/AGENTS.md。
```

> 如果你习惯根目录方式，建议在 `~/research/AGENTS.md` 中写入工作区总入口信息，供 Codex 启动时自动读取。

第一条 prompt 示例（私有项目为工作区时）：

```text
请把当前目录当成一个私有经济学实证研究项目。
公开 workflow 仓库在：
~/research/workflow-for-economists

请先阅读本项目的 AGENTS.project.md，以及 workflow 仓库中的 AGENTS.md。
我的研究方向是：数字化转型与企业创新。
我目前还不确定具体问题。

请先用 good-question workflow 帮我生成 2-3 张 Good Question Card，
比较每个问题的重要性、可行性、竞争性解释、可证伪性和两周 pilot。
不要开始写 Stata 代码，先帮我判断哪个问题值得推进。
```

---

## 完整研究流程

整个流程把一个经济学实证研究从"模糊想法"推进到"可复现、可审计、可写成论文"：

```
Good Question → 私有研究工作区 → Requirements Spec → 数据审计
    → Stata 清洗与分析 → 日志验证 → 结果解释与理论诊断
    → 论文写作 / QA / 审稿回复
```

---

### 阶段一：打磨研究问题

**适用场景：** 你只有一个方向、文献 gap、proposal 摘要，或者几个想法都看起来能做。

**产物位置：** `quality_reports/good_questions/`

**基本用法：**

```text
请使用 good-question workflow。
我的粗略想法是：[写下你的想法]

请生成 Good Question Card，并重点检查：
1. 这个问题为什么值得做
2. 它挑战了什么默认假设
3. 至少两个竞争性解释是什么
4. 什么证据可以区分这些解释
5. 什么结果会推翻或削弱它
6. 两周内可做的 pilot 是什么
7. 是否值得进入 Stata 实证阶段
```

**文献 gap 场景：**

```text
请用 good-question 帮我检查这个文献 gap 是否真的值得做：
[gap 描述]

请不要直接接受我的 gap。
请区分：已有证据、合理推断、未知部分。
如果需要 source audit，请先列出需要核查的文献和 claim。
```

**Proposal 压力测试：**

```text
请用 good-question 作为严格评审，压力测试这个 proposal 摘要：
[proposal 摘要]

请输出：
1. 最可能被 desk reject 的原因
2. 最强评审质疑
3. 哪些地方需要理论重写
4. 哪些地方需要数据或识别策略补强
5. 修补后的核心研究问题
```

---

### 阶段二：确定任务边界

**适用场景：** 任务范围不清楚时，先写 requirements spec，再写代码。

**产物位置：** `quality_reports/specs/`

```text
请先不要写代码。
请根据我的研究问题和数据情况，在 quality_reports/specs/ 下生成一个 requirements spec。

要求区分：
MUST：本轮必须完成
SHOULD：最好完成
MAY：有时间再做
BLOCKED：必须向我确认的问题
```

---

### 阶段三：数据审计与变量梳理

**适用场景：** 有数据但不知道变量质量、样本结构、缺失情况和可行规格。

```text
数据已经放在 data/raw/。
请先做数据审计，不要立刻回归。

请完成：
1. 识别数据格式和变量列表
2. 检查样本量、时间范围、面板结构或截面结构
3. 检查核心变量缺失和异常值
4. 判断哪些变量可能是类别编码，不能直接当连续变量
5. 生成 data-audit.md 和初步变量字典
6. 给出下一步清洗和构造建议
```

---

### 阶段四：Stata 清洗、构造与分析

正式 do-file 按下列结构组织：

```
dofiles/01_clean/      ← 原始数据清洗
dofiles/02_construct/  ← 变量构造与样本筛选
dofiles/03_analysis/   ← 描述统计、基准回归、稳健性
dofiles/04_output/     ← 表格和图形组装
```

**基本分析 prompt：**

```text
请根据 data-audit.md 和 requirements spec 编写第一版 Stata 分析流程。

要求：
1. 新建或更新 dofiles/ 下的 do-file
2. 使用中文注释
3. 使用相对路径
4. 每个可运行 do-file 打开并关闭日志
5. 输出描述统计表、核心图形和基准回归表
6. 图形同时导出 png 和 pdf
7. 表格输出到 output/tables/
8. 日志输出到 logs/
9. 运行后检查 log，不要报告没有日志支撑的数字
```

**DID / Event Study 场景：**

```text
请帮我设计 DID / event study 分析。

请先确认：
1. 个体维度是什么
2. 时间维度是什么
3. treatment 如何定义
4. 是否存在 staggered adoption
5. 聚类标准误应放在哪一层
6. pre-trend 和 placebo 如何做

然后再写 Stata do-file，并输出事件研究表和图。
```

**IV 场景：**

```text
请帮我设计 IV 回归。

请先写清楚：
1. 内生变量
2. 工具变量
3. 排除限制的经济学理由
4. 第一阶段应该如何报告
5. 弱工具变量风险如何检查
6. 表格如何分 panel 呈现

确认后再写 Stata do-file。
```

---

### 阶段五：日志验证与结果解释

所有数值解释必须以 `logs/` 和 `output/tables/` 为唯一来源。

**结果解释 prompt：**

```text
请根据最新 logs/ 和 output/tables/ 做 results-analysis。

要求：
1. 逐列还原每个回归规格
2. 说明样本、控制变量、固定效应和聚类层级
3. 只解释能在日志或表格中找到的数字
4. 标出可能的识别威胁
5. 给出 robustness、heterogeneity、mechanism 的下一步清单
6. 生成 results_memos/ 下的结果解释 memo
```

**结果不稳定时的诊断 prompt：**

```text
当前结果不稳定。
请使用 story-diagnostics 判断：
1. 是理论故事不成立
2. 是测量或变量构造问题
3. 是样本或识别策略问题
4. 还是当前数据不足

请给出 STORY_READY、CREDIBLE_NULL、ITERATE_WITH_CURRENT_DATA 或 NEW_DATA_REQUIRED 的判断。
```

---

### 阶段六：论文写作与 QA

当表格和日志稳定后再进入写作。

**写作 prompt：**

```text
请使用 paper-writing workflow。
根据 output/tables/、output/figures/ 和 results_memos/，帮我起草 Main Results 小节。

要求：
1. 每个数值结论都引用对应表格或图形
2. 不夸大机制解释
3. 区分主效应、稳健性、异质性和机制
4. 标出还不能写死的地方
```

**投稿前 QA prompt：**

```text
请使用 qa-paper workflow 对当前论文草稿做投稿前检查。

重点检查：
1. 研究问题是否清楚
2. 识别策略是否自洽
3. 正文数字是否和表格一致
4. 图表标题和注释是否完整
5. 数据与代码可复现说明是否足够
6. 哪些问题会导致 hard gate failure
```

**R&R 回复 prompt：**

```text
请使用 review-response workflow。
我会提供审稿意见和修改后的结果。

请帮我生成：
1. comment-to-change map
2. response letter 初稿
3. 每条回复对应的修改位置
4. 还没有真正完成、不能承诺的地方
```

---

## 仓库目录

```
./
├── AGENTS.md                       ← Codex 主规则文件
├── CLAUDE.md                       ← Claude Code 兼容说明
├── MEMORY.md                       ← 仓库级记忆与上下文
├── config.codex-econ.example.toml  ← Codex 配置示例
│
├── agents/                         ← 专用 Agent 定义
│   ├── data-analyst/
│   ├── literature-reviewer/
│   ├── theory-auditor/
│   ├── paper-miner/
│   ├── paper-critic/
│   ├── paper-fixer/
│   ├── rebuttal-writer/
│   ├── response-critic/
│   ├── response-fixer/
│   └── artifact-verifier/
│
├── skills/                         ← 可复用技能包
│   ├── good-question/
│   ├── research-ideation/
│   ├── results-analysis/
│   ├── story-diagnostics/
│   ├── paper-writing/
│   ├── paper-self-review/
│   ├── qa-paper/
│   ├── review-response/
│   ├── qa-response/
│   ├── citation-verification/
│   └── post-acceptance/
│
├── templates/                      ← 模板文件
│   ├── master-do-template.do
│   ├── did-analysis-template.do
│   ├── ddml-analysis-template.do
│   ├── good-question-card.md
│   ├── requirements-spec.md
│   ├── response-to-referees.md
│   ├── ...
│   └── private-study-skeleton/
│
├── scripts/                        ← 运行、检查与项目创建脚本
│   ├── new_private_study.ps1
│   ├── run_pipeline.sh
│   ├── run_stata.sh
│   ├── check_data_safety.py
│   └── quality_score.py
│
├── dofiles/                        ← Stata 流水线模板
│   ├── 00_master.do                ← 主入口
│   └── README.md
│
├── quality_reports/                ← 质量报告模板与参考
│   ├── good_questions/
│   ├── specs/
│   ├── decisions/
│   └── passports/
│
├── reports/                        ← Quarto 报告模板
├── results_memos/                  ← 结果解释 memo 模板
└── master_supporting_docs/         ← 支持文档与图像
```

---

## 常用命令

### 项目创建

```powershell
powershell -ExecutionPolicy Bypass -File scripts/new_private_study.ps1 -Keyword "关键词" -InitGit
```

### Stata 执行

```bash
# 运行单个 do-file
bash scripts/run_stata.sh dofiles/03_analysis/main_regression.do

# 运行完整流水线
bash scripts/run_pipeline.sh
```

### 报告渲染

```bash
quarto render reports/analysis_report.qmd
```

### 质量检查

```bash
# 数据安全检查
python scripts/check_data_safety.py --staged $(git diff --cached --name-only)

# 制品质量评分
python scripts/quality_score.py dofiles/03_analysis/main_regression.do
python scripts/quality_score.py reports/analysis_report.qmd
```

---

## Stata 约定

- do-file 顶部写明 `version`
- 使用 `set more off`
- 使用 `set varabbrev off`
- 使用相对路径
- 可运行 do-file 必须写日志
- 随机过程设置统一 seed
- 回归结果进入表格前使用 `estimates store` 或 `est store`
- 图形同时导出 `.pdf` 和 `.png`
- 表格优先输出 `.tex` 和 `.csv`
- 新增或修改的 Stata 注释默认使用中文
- 聚类标准误放在最有经济学和研究设计依据的层级，并在表注或 memo 中说明

---

## Workspace 内可用资源

本仓库的 Codex 组件按经济学实证研究的完整流程组织，分为 Skills 和 Agents 两层，各自覆盖研究生命周期的不同阶段。

### 流程全景

```
研究构思 ──→ 数据分析 ──→ 结果解释 ──→ 论文写作 ──→ QA评审 ──→ 审稿回复 ──→ 录用后续
    │            │            │            │           │           │            │
    ▼            ▼            ▼            ▼           ▼           ▼            ▼
 ideation    data-analyst  results      paper-      qa-paper   review-     post-
 good-       (agent)       analysis     writing     qa-        response    acceptance
 question                  story-       paper-      response   rebuttal-
 lit-                      diagnostics  self-                  writer
 reviewer                               review                 response-
 (agent)                                                       critic/fixer
                                                               artifact-
                                                               verifier
                                              citation-verification (贯穿全程)
```

### Skills（技能包）

Skills 按研究流程阶段组织，Codex 会在对话中根据任务自动加载对应 Skill：

| 阶段               | Skill                     | 详细说明                                                                                                                                                    |
| ------------------ | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **研究构思** | `research-ideation`     | 问题框架 → 文献地图 → 识别策略 → 数据可行性。产出 `literature-review.md` 和 `identification-map.md`，在写代码之前先建立研究设计的全局视图            |
|                    | `good-question`         | 将模糊想法转化为可证伪的科学问题。生成 Good Question Card，检查重要性、竞争性解释、可证伪性和两周 pilot，区分"值得做"和"能做"的问题                         |
| **数据分析** | `results-analysis`      | Stata 优先的完整分析流程：原始数据审计 → 清洗合并 → 样本构造 → 变量定义 → 主回归 → 稳健性 → 异质性/机制 → 理论审计 → 图表输出 → 复现检查           |
|                    | `story-diagnostics`     | 当实证结果不稳定或不支持预期故事时使用。诊断是理论问题、测量问题、样本问题还是数据不足，给出 STORY_READY / CREDIBLE_NULL / ITERATE / NEW_DATA_REQUIRED 判断 |
| **论文写作** | `paper-writing`         | 按经济学实证论文标准结构起草：引言 → 制度背景 → 数据 → 实证策略 → 主要结果 → 机制/异质性。确保每个数值结论对应具体表格或图形                           |
|                    | `paper-self-review`     | 投稿前或导师审阅前的自检门禁。检查研究问题与识别策略匹配、样本选择可追溯、变量定义一致性、固定效应和聚类标准误选择的合理性                                  |
| **QA 评审**  | `qa-paper`              | 严格的论文 QA 循环：critic → fixer → verifier。检查识别可信度、表格数字一致性、引用保真度和复现准备。适用于投稿前 go/no-go 决策                           |
|                    | `qa-response`           | 审稿回复信的 QA 循环。检查评论覆盖率、修改可追溯性、语气规范性，确保每条审稿意见都有对应处理                                                                |
| **审稿回复** | `review-response`       | 完整 R&R 流程：解析审稿意见并分类（识别、稳健性、机制、外部有效性、文献定位等），起草回复信，映射每条意见到论文修改或合理的不修改理由                       |
| **录用后续** | `post-acceptance`       | 论文接受后的收尾工作：复现包清理、附录定稿、数据与代码可用性声明、期刊级图表清单、研讨会幻灯片、政策简报                                                    |
| **贯穿全程** | `citation-verification` | 引文核实：区分工作论文与已发表版本、检查期刊元数据和 DOI、防止虚构引用。信源优先级：出版社页面 > 顶级期刊网站 > NBER/RePEc/SSRN > Google Scholar            |

### Agents（专用代理）

Agents 按角色组织，通过 `Task` 工具以子代理方式调用，适合需要独立上下文和重复迭代的任务：

| 阶段               | Agent                   | 角色与职责                                                                                                                                                    |
| ------------------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **研究构思** | `literature-reviewer` | 文献综述专家。按研究问题、识别策略、数据来源和主要发现对论文分组，识别分歧、可信度差距和开放实证机会。默认使用 Zotero 作为引文骨架                            |
| **数据分析** | `data-analyst`        | Stata 优先的实证分析专家。将实证设计转化为可执行分析计划，构建回归规格矩阵、稳健性计划和表格框架。触发或推荐 `theory-auditor`                               |
| **结果解释** | `theory-auditor`      | 理论面向的解读审计者。测试当前解读是否符合经济学理论，竞争性机制是否仍然存活。产出结构化 memo：结果摘要 → 理论拟合 → 竞争机制 → 解读风险 → 下一步实证动作 |
| **论文写作** | `paper-miner`         | 写作模式挖掘者。从已发表论文和审稿材料中提取可复用模式（引言框架、制度背景、数据描述、实证策略写法），更新写作技能使用的参考文件                              |
| **QA 评审**  | `paper-critic`        | 只读批评者，对论文进行对抗性评审。审查维度：论证结构、识别可信度、计量规格、文献定位、写作规范、复现准备。未通过硬门禁前假设手稿未达到提交标准                |
|                    | `paper-fixer`         | 执行者，按 CRITICAL → MAJOR → MINOR 顺序修复 `paper-critic` 发现的问题，不扩大修改范围                                                                    |
|                    | `artifact-verifier`   | 最终验证者，检查硬门禁，按评分标准打分，宣布 APPROVED 或 CONTINUE。仅在硬门禁通过且分数 ≥ 90 时批准                                                          |
| **审稿回复** | `rebuttal-writer`     | 期刊修改专家。解析审稿意见并分类，选择合适回复立场，起草专业回复信，维护评论-修改-回复的可追溯性                                                              |
|                    | `response-critic`     | 只读批评者，对回复信进行对抗性评审。检查评论覆盖率、立场质量、修改可追溯性、证据充分性和语气规范                                                              |
|                    | `response-fixer`      | 执行者，按 CRITICAL → MAJOR → MINOR 顺序修复 `response-critic` 发现的问题，保持可追溯性                                                                   |

### Templates（模板）

`templates/` 目录提供开箱即用的骨架文件：

- **Stata do-file 模板**：`master-do-template.do`（含标准头部、日志、阶段组织）、`did-analysis-template.do`（TWFE DID / Callaway-Sant'Anna）、`ddml-analysis-template.do`（DDML 双重机器学习）
- **Memo 模板**：`good-question-card.md`、`requirements-spec.md`、`decision-record.md`、`session-log.md`、`passport-template.yaml`
- **论文模板**：`response-to-referees.md`（审稿回复）、`preregistration-template.md`
- **私有项目骨架**：`private-study-skeleton/`（包含完整目录结构和 `AGENTS.project.md` 模板）

---

## 数据与隐私规则

### 公开 workflow 仓库默认不提交

```
data/raw/**        data/derived/**        logs/**
*.log              *.smcl                 *.gph
*.dta              *.sav                  *.parquet
*.csv              *.json                 *.xls
*.xlsx
```

### 私有研究仓库注意事项

- 排除密钥和 token
- 排除个人账户配置
- 排除临时缓存
- 排除不允许上传 GitHub 的受限数据
- 大型数据建议使用 Git LFS 或 DVC，并在 `data/README.md` 中记录重建方式

---

## 本地环境

本仓库当前规则文件记录的本地环境：

```
Python: D:\ProgramFiles\anaconda3\python.exe
Conda:  D:\ProgramFiles\anaconda3\Scripts\conda.exe
Stata:  D:\Program Files\Stata18\StataMP-64.exe
```

如果你的机器路径不同，应在本地配置或项目说明中更新，但 do-file 仍应使用相对路径。

---

## 致谢

本仓库的流程搭建参考了以下优秀项目：

- [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) — Claude Code 工作流管理与项目组织范式
- [maxwell2732/codex-stata-for-economists](https://github.com/maxwell2732/codex-stata-for-economists) — 面向经管专业的 Stata 可复现研究 Codex 工作流
- [Rimagination/good-question](https://github.com/Rimagination/good-question) — Good Question Card 研究问题打磨方法论

并逐步整合了 Codex 优先、Claude Code 兼容、经济学论文 QA、研究问题打磨和私有研究工作区管理等实践。

---

## 许可证

MIT
