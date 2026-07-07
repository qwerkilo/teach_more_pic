# PRD: 全面优化 teach_more_pic 项目

## 需求概述

对 teach_more_pic 技能项目进行 7 项系统性优化，消除文档数值漂移、样式不一致、模板冗余和验证盲区。

## 子项清单

### A. 数值一致性修正（6 处）
| 文件 | 位置 | 当前文本 | 修正值 |
|---|---|---|---|
| `SKILL.md:25` | 前言 | 未提及 `magicui-effects.css` | 补上 magicui-effects.css |
| `teach_more_pic-refs/SKILL.md:35` | 文件速查表 | "验证脚本 18 项检查" | 21 |
| `teach_more_pic-refs/SKILL.md:36` | 文件速查表 | "pytest 测试 99 项" | 实际函数数 |
| `AGENTS.md:53` | 验证命令 | "109 tests" | 实际函数数 |
| `teach_more_pic-core/SKILL.md:33` | 资源速查 | "28 个组件" | 33 |
| `SKILL.md:25` | libs 声明 | `three.module.js（ESM 主入口，r185 WebGPU）` | 确认版本号或软化 |

### B. 组件 #17 标签组从硬编码色改为 CSS 变量
`components/17-标签徽章组.md` 使用 `#dbeafe` 等固定色，违反设计纪律"全部用 var(--accent)"。改为 CSS 变量方案使标签色随主题切换。

**验收**：标签组在 5 个主题切换后颜色自动适配，而非固定 Tailwind 色票。

### C. 模板 HTML 深层去重
`lesson-starter.html` 中 20 个 `tp-item` 手动枚举 + PPT JS 中 `t` 数组重复，占 ~60 行。

**验收**：模板从 832 行降至 ≤600 行，功能不变（20 主题可用），无视觉回归。

### D. SPA/KG 模板同步机制
当前主题列表在 3 处硬编码（`lesson-starter.html` TP items, PPT JS `t` 数组, `index-spa.html`），修改需 3 处同步。

**验收**：PPT JS 自动从 HTML 收集主题，消除 `t` 硬编码数组，在 `lesson-starter.html` 和 `index-spa.html` 中同时生效。

### E. 验证器新增 5 项检查
`validate-lesson.py` 新增：
1. 缺失 `<meta name="description">` 检测
2. 标签组 #17 存在性检测
3. 测验选项严格 3 个/语言检测
4. `@media print` 样式表存在性
5. ECharts GL GeoJSON `.js` 加载兼容性检测

**验收**：`pytest tests/ -v` 全部通过；对已有课程运行 0 误报。

### F. 品牌主题一致性修正
- `bmw-m`：`--bg: #000000` → off-black `#1a1a1a`
- `dell-1996`：`--text: #000000` → `#1a1a1a`
- `spotify`：`--surface-raised` 与 `--surface` 差过小 → 加大对比

**验收**：违反"禁止纯黑"纪律的 2 个主题修正，深色主题对比度可接受。

### G. 组件文件编号漂移
`references/decision-guide.md:5` 声明文件编号与规范编号不一致。创建 `components/24-ECharts-index.md` 作为跳转入口，更新 decision-guide 文档。

**验收**：`components/` 目录无断裂感，`components/24-ECharts-index.md` 指向 `24-ECharts 交互式图表集.md`。

## 约束与边界
- 不破坏已有课程兼容性
- 不改变 PPT JS 的 IIFE + try/catch 结构
- 不引入外部依赖
- 每个子项可独立验收，不阻塞其他子项
