# Authentic Course Lab Skill / 真实课程实验 Skill

## 中文

这是一个适用于任意大学课程实验的 Codex Skill。它要求智能体严格按照实验指导书，真实完成实验、操作指定软件或设备、逐步截图、根据实际证据编写报告，并为教师现场检查准备可直接照着操作的演示说明。

适用场景包括编程、数据库、电子电路、MATLAB/Simulink、操作系统、虚拟机、网络、数据分析、机器学习、物理化学仿真、机械设计和控制工程等课程实验。

### 推荐运行环境

这个 Skill 在 **Codex 桌面客户端（部分用户也称 Code X）** 中通常能发挥更完整的效果，因为 Codex 可以在获得授权后读取本地实验文件、运行代码、操作电脑中的 GUI 软件并获取真实截图。

其他支持 Skills 的 Agent 也可以使用本 Skill，但实际效果取决于 Agent 是否具备以下能力：

- 读取实验指导书和本地文件；
- 运行代码、命令和测试；
- 操作指定桌面软件、网页或虚拟机；
- 获取真实界面截图；
- 创建或编辑实验报告。

如果 Agent 没有电脑操作或截图能力，它仍可帮助解析指导书、检查代码和编写报告框架，但不能声称已经完成真实 GUI 操作或提供真实操作截图。

### 核心原则

- 完整阅读指导书后再开始实验。
- 逐条映射“要求、执行步骤、实际结果、证据”。
- 真实实现和运行，不用固定打印结果冒充功能。
- 真实操作指导书指定的软件、GUI 或设备。
- 每个关键步骤完成后立即保存原生截图和结果文件。
- 禁止生成、重绘、拼接或伪造实验截图与数据。
- 报告只能描述已经真实执行并有证据支持的内容。
- 为用户写明现场演示时打开什么、输入什么、点击什么以及预期结果。

### 安装方式一：使用 Git 克隆（推荐）

```bash
git clone https://github.com/swording-k/authentic-course-lab-skill.git
mkdir -p ~/.codex/skills
cp -R authentic-course-lab-skill/skill/authentic-course-lab ~/.codex/skills/
```

重新打开 Codex 后即可使用。

更新到最新版：

```bash
cd authentic-course-lab-skill
git pull
rm -rf ~/.codex/skills/authentic-course-lab
cp -R skill/authentic-course-lab ~/.codex/skills/
```

### 安装方式二：下载 ZIP

1. 在 GitHub 仓库页面点击 `Code`，选择 `Download ZIP`。
2. 解压下载的文件。
3. 找到 `skill/authentic-course-lab` 文件夹。
4. 将整个 `authentic-course-lab` 文件夹复制到公共 Skill 目录 `~/.codex/skills/`。
5. 最终应存在文件 `~/.codex/skills/authentic-course-lab/SKILL.md`。
6. 重新打开 Codex。

macOS 或 Linux 可以在解压后的仓库目录运行：

```bash
mkdir -p ~/.codex/skills
cp -R skill/authentic-course-lab ~/.codex/skills/
```

### 安装方式三：让 Agent 自动安装

可以把本仓库链接发送给具备联网和本地文件操作能力的 Agent，并明确告诉它：

```text
请从这个 GitHub 仓库下载 authentic-course-lab Skill：
https://github.com/swording-k/authentic-course-lab-skill

将仓库中的 skill/authentic-course-lab 整个文件夹安装到公共 Skill 目录
~/.codex/skills/authentic-course-lab，并验证其中存在 SKILL.md。
不要只复制 SKILL.md，references、scripts 和 agents 目录也必须保留。
```

若使用的 Agent 有专门的 Skill 安装器，也可以直接要求它从仓库链接安装 `authentic-course-lab`。

### 验证安装

确认以下文件存在：

```bash
test -f ~/.codex/skills/authentic-course-lab/SKILL.md && echo "Skill installed"
```

然后在新对话中明确调用 `$authentic-course-lab`。若 Agent 没有自动识别，重新启动客户端或重新加载 Skills。

### 使用示例

```text
使用 $authentic-course-lab，严格按照这份实验指导书真实完成实验，
逐步操作指定软件并截图，根据实际证据写实验报告，
最后告诉我教师现场检查时每一步如何演示。
```

### 交付物审计

Skill 包含一个通用审计脚本，用于清点源码、工程、数据、截图、报告和其他实验证据，并提示常见真实性风险：

```bash
python3 ~/.codex/skills/authentic-course-lab/scripts/lab_evidence_audit.py <实验交付目录>
```

自动审计不能代替人工检查。仍需目视确认截图来自真实操作，并重新运行实验验证结果会随输入或参数变化。

### 目录结构

```text
skill/authentic-course-lab/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── completion-audit.md
│   ├── evidence-standard.md
│   ├── live-demo-guide.md
│   ├── report-guide.md
│   └── step-record-template.md
└── scripts/lab_evidence_audit.py
```

## English

This repository contains a Codex Skill for authentic university course labs. It instructs the agent to follow the lab guide strictly, genuinely perform the experiment, operate the required software or equipment, capture native screenshots step by step, write the report from real evidence, and prepare an actionable live demonstration guide for the instructor.

It is designed for programming, databases, electronics and EDA, MATLAB/Simulink, operating systems, virtual machines, networking, data analysis, machine learning, scientific simulation, mechanical design, control engineering, and other university lab courses.

### Recommended Environment

This Skill usually provides its most complete experience in the **Codex desktop app** because Codex can, with permission, inspect local lab files, run code, operate GUI applications, and capture authentic screenshots.

Other Skill-compatible agents can also use it. Results depend on whether the agent can read local files, execute code, operate the required software or virtual machine, capture real screenshots, and create reports. An agent without computer-control or screenshot capabilities must not claim that it completed real GUI operations.

### Core Principles

- Read the complete lab guide before starting.
- Map every requirement to an action, actual result, and authoritative evidence.
- Implement and run real functionality; never substitute hard-coded output.
- Operate the software, GUI, or equipment explicitly required by the guide.
- Save native screenshots and result files immediately after each key step.
- Never generate, redraw, composite, or fabricate screenshots or experimental data.
- Write only claims supported by actions that were actually performed.
- Provide exact live-demo instructions: what to open, enter, click, and expect.

### Installation Option 1: Git Clone (Recommended)

```bash
git clone https://github.com/swording-k/authentic-course-lab-skill.git
mkdir -p ~/.codex/skills
cp -R authentic-course-lab-skill/skill/authentic-course-lab ~/.codex/skills/
```

Restart Codex, then invoke the skill in your request.

To update:

```bash
cd authentic-course-lab-skill
git pull
rm -rf ~/.codex/skills/authentic-course-lab
cp -R skill/authentic-course-lab ~/.codex/skills/
```

### Installation Option 2: Download ZIP

1. On GitHub, select `Code` and then `Download ZIP`.
2. Extract the archive.
3. Locate `skill/authentic-course-lab`.
4. Copy the entire folder into the shared Skill directory `~/.codex/skills/`.
5. Confirm that `~/.codex/skills/authentic-course-lab/SKILL.md` exists.
6. Restart Codex.

### Installation Option 3: Ask an Agent to Install It

Send the repository URL to an agent with internet and local-file access:

```text
Download the authentic-course-lab Skill from this GitHub repository:
https://github.com/swording-k/authentic-course-lab-skill

Install the entire skill/authentic-course-lab folder into
~/.codex/skills/authentic-course-lab and verify that SKILL.md exists.
Preserve the references, scripts, and agents directories.
```

If the agent provides a dedicated Skill installer, ask it to install `authentic-course-lab` directly from the repository URL.

### Verify Installation

```bash
test -f ~/.codex/skills/authentic-course-lab/SKILL.md && echo "Skill installed"
```

Invoke `$authentic-course-lab` in a new conversation. Restart the client or reload Skills if it is not detected immediately.

### Example

```text
Use $authentic-course-lab to follow this lab guide strictly, perform every
required operation in the specified software, capture native screenshots for
each key step, write the report from real evidence, and prepare my live demo.
```

### Evidence Audit

The included generic audit script inventories source files, projects, data, screenshots, reports, and other evidence while flagging common authenticity risks:

```bash
python3 ~/.codex/skills/authentic-course-lab/scripts/lab_evidence_audit.py <lab-delivery-directory>
```

Automated inventory does not replace manual verification. Screenshots must still be visually checked, and the experiment should be rerun with changed inputs or parameters to prove genuine behavior.

### Contributing

Keep the installed Skill focused on instructions and reusable resources. Put repository-facing documentation in this root README, preserve the authenticity rules, and validate changes with the official Skill validator before sharing.
