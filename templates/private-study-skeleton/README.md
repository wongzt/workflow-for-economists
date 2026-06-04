# {{PROJECT_NAME}}

这是一个私有研究工作区，用于保存单个真实研究项目的输入、代码、日志、输出、memo 和论文材料。

本项目默认复用公开 workflow 仓库：

```text
{{WORKFLOW_REPO_PATH}}
```

## 目录结构

```text
.
├── AGENTS.project.md
├── README.md
├── data/
│   ├── raw/
│   └── derived/
├── dofiles/
│   ├── 01_clean/
│   ├── 02_construct/
│   ├── 03_analysis/
│   └── 04_output/
├── logs/
├── output/
│   ├── tables/
│   └── figures/
├── reports/
├── quality_reports/
│   ├── good_questions/
│   ├── specs/
│   ├── decisions/
│   ├── checkpoints/
│   └── passports/
├── results_memos/
│   ├── theory_audits/
│   └── story_diagnostics/
└── workflow/
```

## 使用原则

- 真实研究内容保存在本私有仓库中。
- 公开 workflow 仓库只保存流程、模板、脚本、skills、agents 和教学示例。
- 数值结论必须能追溯到 `logs/` 或 `output/tables/`。
- 如果数据受到使用协议、隐私或机构限制，不要仅依赖 GitHub private；应改用加密存储、Git LFS、DVC 或机构服务器，并在 `data/README.md` 说明访问方式。

## 第一次会话 Prompt

```text
请把当前目录当成一个私有经济学实证研究项目。
公开 workflow 仓库在：
{{WORKFLOW_REPO_PATH}}

请先阅读本项目的 AGENTS.project.md，以及 workflow 仓库中的 AGENTS.md。
我的研究问题是：[question]
我的数据放在：[data path]

请先完成：
1. 如问题还不够清楚，生成 Good Question Card。
2. 如任务边界还不清楚，生成 requirements spec。
3. 检查数据结构、变量、样本和缺失。
4. 制定 analysis-plan.md 和 regression-spec-matrix.md。
5. 编写 Stata do-file，并把日志、表格、图形输出到本项目规范目录。
6. 只在有日志或输出表格支撑后解释数值结果。
```
