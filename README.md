# swording-k/skills

我的 Claude / Codex **Skills 集合**。每个 skill 都在 `skills/<skill-name>/` 子目录下，有自己独立的 README、配置说明和使用方式。

## 📦 Skills 列表

| Skill | 简介 | 标签 |
|---|---|---|
| [authentic-course-lab](./skills/authentic-course-lab) | 大学课程实验助手：中英双语、可执行、可截屏 | `codex`, `claude`, `lab`, `course` |
| [character-pet-director](./skills/character-pet-director) | 角色桌宠导演：先设计角色身份卡、9 行状态动作和 QA 规则，再配合 hatch-pet 生成 Codex 桌宠 | `codex`, `pet`, `character`, `hatch-pet` |

## 🚀 如何使用某个 skill

### 方式 1：GitHub 子目录直链（最简单）

点击上面列表里的 skill 链接 → 进入子目录 → 点 `Code` → `Download ZIP` → 解压后取对应子目录。

直接子目录 URL 格式：
```
https://github.com/swording-k/skills/tree/main/skills/<skill-name>
```

### 方式 2：git sparse-checkout（只拉一个 skill，零浪费）

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/swording-k/skills.git
cd skills
git sparse-checkout set skills/authentic-course-lab
# 或：
git sparse-checkout set skills/character-pet-director
```

### 方式 3：git clone + cp

```bash
git clone https://github.com/swording-k/skills.git
cp -r skills/authentic-course-lab ~/.claude/skills/   # 或 ~/.codex/skills/
cp -r skills/character-pet-director ~/.codex/skills/
```

## 📝 配置方式

**每个 skill 子目录的 README 里都写明了具体配置步骤和安装方式**，点进 skill 链接查看。

## 🤝 添加新 skill

1. 在 `skills/<new-skill-name>/` 下创建子目录
2. 按 `skill-creator` 或 `anthropics/skills` 的标准结构填充（`SKILL.md` / `scripts/` / `README.md`）
3. 在本 README 的"Skills 列表"加一行
4. 提 PR

## 📜 License

每个 skill 各自的 license 以子目录为准。
