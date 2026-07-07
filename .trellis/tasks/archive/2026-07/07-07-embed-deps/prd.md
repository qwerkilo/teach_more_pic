# PRD: 全量内嵌前置依赖

## 目标

将 4 个外部 skill 依赖 + cairosvg 替代方案内嵌到本项目中，零外部 skill 依赖。

## 范围

| 外部依赖 | 当前用途 | 内嵌方案 |
|---|---|---|
| `fireworks-tech-graph` | SVG 流程图创建 (flat-icon style) | `.opencode/skills/fireworks-tech-graph/SKILL.md` 完整复制其指令 |
| `teach` (base) | 学习记录模板 + EPUB 构建 | 学习记录模板本地化；EPUB 指示转为可选步骤 |
| `grill-me` | Step 0 需求拷问 | `.opencode/skills/grill-me/SKILL.md` 完整复制其指令 |
| `knowledge-graph-map` | KG 知识图谱渲染 | `.opencode/skills/knowledge-graph/SKILL.md` 完整复制其指令 |
| `cairosvg` | SVG→PNG (可选) | 替换为 Python Pillow 方案或移除说明 |

## 验收

- [ ] 4 个子 skill 目录创建，含完整 SKILL.md
- [ ] README.md 前置依赖列表移除所有外部 skill 引用，改为"本技能已内置"
- [ ] SKILL.md 中所有外部 skill 引用改为本地 `.opencode/skills/` 路径
- [ ] cairosvg 依赖移除或替换
- [ ] 原有工作流仍可通过本地 skill 执行
