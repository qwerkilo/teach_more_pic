<!-- TRELLIS:START -->
# Trellis Instructions

These instructions are for AI assistants working in this project.

This project is managed by Trellis. The working knowledge you need lives under `.trellis/`:

- `.trellis/workflow.md` — development phases, when to create tasks, skill routing
- `.trellis/spec/` — package- and layer-scoped coding guidelines (read before writing code in a given layer)
- `.trellis/workspace/` — per-developer journals and session traces
- `.trellis/tasks/` — active and archived tasks (PRDs, research, jsonl context)

If a Trellis command is available on your platform (e.g. `/trellis:finish-work`, `/trellis:continue`), prefer it over manual steps. Not every platform exposes every command.

If you're using Codex or another agent-capable tool, additional project-scoped helpers may live in:
- `.agents/skills/` — reusable Trellis skills
- `.codex/agents/` — optional custom subagents

Managed by Trellis. Edits outside this block are preserved; edits inside may be overwritten by a future `trellis update`.

<!-- TRELLIS:END -->

# teach_more_pic — Agent Guide

This repo defines an OpenCode **skill** (`teach_more_pic`) for creating bilingual (zh/en) visual HTML lessons. It is self-contained — zero external skill dependencies.

## Entry Points

| File | Purpose |
|---|---|
| `SKILL.md` | Main entry — frontmatter + workflow + routing to sub-skills |
| `.opencode/skills/teach_more_pic-core/` | Step 0-8 workflow (adaptive pace included) |
| `.opencode/skills/teach_more_pic-components/` | 33 component index + decision guide |
| `.opencode/skills/teach_more_pic-design/` | Visual rules + anti-patterns |
| `.opencode/skills/teach_more_pic-refs/` | Page types + failure modes + file map |
| `components/NN-name.md` | Per-component HTML/CSS/JS code |
| `templates/lesson-starter.html` | **Must** copy from this for every lesson |

## Key Facts

- **No build system.** Pure HTML/CSS/JS — open in browser directly.
- **Bilingual by default.** All content has `data-lang="zh"` + `data-lang="en"` pairs. L key toggles.
- **Adaptive pace.** If user says "直接干"/"快速"/"fast"/"go" at Step 0, skip all intermediate STOPs to Step 4.
- **33 components.** Minimum 6 per lesson (including tag group #17).
- **Every SVG must be both** a disk file (`lessons/svg/NNNN-slug.svg`) and inline in HTML.
- **Blacklist:** no external GitHub skill dependencies; everything in `.opencode/skills/`.

## Validation Commands

```bash
python scripts/validate-lesson.py lessons/NNNN-slug.html   # 21 checks
python -m pytest tests/ -v                                   # 109 tests
python scripts/run-tests.ps1                                 # batch all examples
python -c "import xml.etree.ElementTree as ET; ET.parse('path.svg')"
```

## Project Structure

```
.opencode/skills/     ← All skills embedded locally (no external installs)
components/           ← 33 component .md files
templates/            ← 9 templates (lesson, SPA, KG, SVG, server scripts)
libs/                 ← Offline packages (echarts, three, d3, magicui)
scripts/              ← Validator (validate-lesson.py)
tests/                ← pytest (109 tests)
references/           ← Decision guide + page types
theme/                ← 19 brand DESIGN.md files
```

## Conventions

- Component file prefix = SKILL.md index number (24-28 aligned, 29+ sequential)
- Component CSS classes use unique prefixes: `cr-` (carousel), `tw-` (typewriter), `px-` (parallax), `tt-` (toast), `cb-` (counter badge)
- New checks go in `validate-lesson.py` + register in `run_all()` + add pytest tests
- New components go in `components/` + update `teach_more_pic-components/SKILL.md` index
