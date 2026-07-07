# 内嵌设计

## 调查结果

| 依赖 | 本地存在 | 文件大小 | 复杂度 |
|---|---|---|---|
| `grill-me` | ✅ 7 行 | 极小，只是 `grilling` 的路由器 |
| `grilling` | ✅ 已安装 | grilling 技能本体（需一并内嵌） |
| `fireworks-tech-graph` | ✅ 599 行 + scripts/ | 大规模 skill |
| `teach` (base) | ✅ 140 行 | 中等，提供学习记录框架 |
| `knowledge-graph-map` | ❌ 未安装 | 需新建（已有模板 kg-starter.html） |
| `cairosvg` | pip 包 | 可选，替换为 Python 原生方案 |

## 内嵌策略

每个外部 skill 复制关键指令到 `.opencode/skills/{name}/SKILL.md`，保持 frontmatter + 核心指令完整。`teach` 的 EPUB 构建部分标记为可选示意步骤。

## 路径映射

```
.opencode/skills/
  grill-me/SKILL.md          ← grilling 路由
  grilling/SKILL.md          ← 拷问技能（grill-me 的 backend）
  fireworks-tech-graph/SKILL.md  ← SVG 流程图
  teach/SKILL.md             ← 学习记录框架
  knowledge-graph/SKILL.md   ← 新增：从 kg-starter.html 模板提取
```

## 引用更新

- `SKILL.md`：前置条件 → 引用 `.opencode/skills/` 路径
- `README.md`：安装步骤 → 移除外链安装，说明已内置
- `components/01-SVG 流程图.md`：移除外部 skill 依赖说明
