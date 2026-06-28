# character-pet-director

角色桌宠导演 skill。它不是直接替代 `hatch-pet`，而是在生成桌宠前先帮助 Codex 理解“角色感觉”：

- 角色身份卡：外观、服装、道具、表情、性格
- 9 行 Codex pet 状态动作：idle、左右移动、waving、jumping、failed、waiting、running、review
- 逐行 QA：身材一致、道具一致、动作逻辑、角色识别点、状态语义
- 仓库打包：按系列/角色整理 `pet.json`、`spritesheet.webp`、`contact-sheet.png`

## 适用场景

当你要制作动漫、游戏、影视、品牌 mascot 或任何“必须像某个角色”的 Codex 桌宠时，先用这个 skill，再用 `hatch-pet`。

示例：

```text
请用 character-pet-director + hatch-pet 做一个索隆 Codex 桌宠。
先写角色身份卡和 9 行状态动作映射，再生成图集。
```

## 安装到 Codex

从仓库根目录复制：

```bash
mkdir -p ~/.codex/skills
cp -R skills/character-pet-director ~/.codex/skills/
```

或只拉这个子目录：

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/swording-k/skills.git
cd skills
git sparse-checkout set skills/character-pet-director
mkdir -p ~/.codex/skills
cp -R skills/character-pet-director ~/.codex/skills/
```

重启 Codex 后生效。

## 和 hatch-pet 的关系

`hatch-pet` 负责具体生成、切帧、验证和打包；`character-pet-director` 负责前置导演和后置 QA：

1. 写角色身份卡
2. 写 9 行动作表
3. 约束每行提示词
4. 检查 contact sheet
5. 发现问题只修坏行
6. 按仓库结构打包分享

