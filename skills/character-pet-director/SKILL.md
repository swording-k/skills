---
name: character-pet-director
description: Direct the creation of character-accurate Codex desktop pets before using hatch-pet: define a character identity card, map canon/personality traits to the 9 Codex pet states, enforce row-specific action logic, and QA generated contact sheets for identity, prop, outfit, and motion consistency. Use when making anime, game, movie, mascot, celebrity-inspired, or other recognizable character pets.
metadata:
  short-description: Plan and QA character-accurate Codex pets
---

# Character Pet Director

Use this skill before and alongside `hatch-pet` when the user wants a Codex desktop pet based on a specific character, mascot, fandom, brand avatar, or recognizable persona.

This skill is the "director" layer. It does not replace `hatch-pet`; it makes `hatch-pet` better by forcing character intent, state logic, and visual QA before generating the final atlas.

## Core Rule

Do not start image generation immediately. First write a compact character direction brief with:

1. **Identity locks**: features that must survive every row.
2. **Avoidances**: details that should not appear because they break clarity, licensing posture, extraction, or pet readability.
3. **State action map**: what each of the 9 Codex rows should do.
4. **QA checklist**: row-specific failure conditions.

Then use `hatch-pet` to generate and package the sprite atlas.

## Codex Pet States

Every character must map naturally to the Codex 9-row state contract:

| Row | State | Director question |
| --- | --- | --- |
| 0 | `idle` | What does this character do while calmly present? |
| 1 | `running-right` | How do they move right without losing their silhouette? |
| 2 | `running-left` | How do they move left without identity drift? |
| 3 | `waving` | How do they greet or acknowledge the user? |
| 4 | `jumping` | What should hover/jump feel like for this character? |
| 5 | `failed` | What is their natural failure/error reaction? |
| 6 | `waiting` | How do they wait for permission, help, or input? |
| 7 | `running` | What is their active-task/work loop, not locomotion? |
| 8 | `review` | How do they inspect, think, review, or focus? |

## Character Direction Brief

Before generation, write a brief like this:

```text
Character: <name>
Pet id: <id>
Identity locks:
- <must-have visual trait>
- <must-have outfit/prop/marking>
- <must-have personality cue>

Avoid:
- text, logos, symbols, scenery, detached effects
- prop switching across frames
- outfit drift or body-proportion drift

State action map:
0 idle: <calm loop>
1 running-right: <directional movement>
2 running-left: <directional movement>
3 waving: <greeting>
4 jumping: <hover/jump>
5 failed: <failure reaction>
6 waiting: <waiting for user>
7 running: <active task loop>
8 review: <review/focus loop>

Special QA:
- <row-specific checks>
```

Keep the brief short enough to paste into image prompts and README notes.

## Prompting Rules

- Keep each row prompt state-specific. Do not ask for all personality traits in every row if it makes the prompt bloated.
- Preserve identity locks in every row: face, hair/headgear, outfit, signature prop, body proportions, and palette.
- Avoid detached effects by default: no speed lines, dust, glow, floating punctuation, floating symbols, cast shadows, or scenery.
- Use props only when they are part of the character identity or state logic.
- If a prop appears in a row, it must remain consistent across every frame of that row.
- If a state should not use a prop, explicitly say "no new props."
- For copyrighted/fandom characters, avoid readable logos, flags, text, and unnecessary marks unless the user explicitly requests them. Favor recognizable character features and actions over exact printed symbols.

## Row QA

After `hatch-pet` creates `qa/contact-sheet.png`, inspect it before accepting.

Reject or repair rows with:

- body size/proportion drift across frames
- outfit, hair, hat, weapon, or prop changes across frames
- prop switching, such as dumbbells becoming a barbell
- missing prop in the middle of an action
- wrong state logic, such as a failed action ending in success
- running-left/right that does not face the correct direction
- hover/jump action that feels unnatural when triggered by mouse hover
- detached effects, shadows, dust, symbols, text, or scenery
- identity drift where the character becomes a generic mascot

Repair the smallest failing row. Do not regenerate a complete pet when one row is bad.

## Character Series Workflow

When making many characters from one series:

1. Create a roster with priority order.
2. For each character, write the direction brief.
3. Generate, QA, and package one character at a time.
4. Install locally under `${CODEX_HOME:-$HOME/.codex}/pets/<pet-id>`.
5. Add the pet to the collection repository under `pets/<series>/<pet-id>/`.
6. Update the series README and root README.
7. Commit and push after each completed, QA-passing character.

## Handoff To hatch-pet

After the direction brief is accepted or obvious from the task, invoke `hatch-pet`:

- Use the character name as `--pet-name`.
- Put identity locks and key avoidances in `--pet-notes`.
- Put style/readability constraints in `--style-notes`.
- Use the direction brief to shape base and row prompts.
- Keep the final contact sheet as the acceptance source of truth.

## Repository Packaging

For shareable pet collections, use:

```text
pets/<series>/<pet-id>/
  pet.json
  spritesheet.webp
  contact-sheet.png
```

Provide an installer that copies `pet.json` and `spritesheet.webp` to:

```text
~/.codex/pets/<pet-id>/
```

README files should explain:

- install all pets
- install one series
- install one character
- restart Codex after installation

