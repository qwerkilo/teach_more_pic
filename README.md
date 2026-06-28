# teach_more_pic — 视觉增强课程制作

配合 [base `teach` skill](https://github.com/mattpocock/skills/tree/main/teach) 使用的视觉增强技能，为每节课程注入 PPT 级的视觉品质。

> 需要先安装 base `teach` skill——本项目是它的视觉增强插件，两者缺一不可。

## 安装

### 前提

本技能需要 [opencode](https://opencode.ai) 环境。已安装了以下 base skill：
- [teach](https://github.com/mattpocock/skills/tree/main/teach) — 基础课程制作技能（必装）
- [grill-me](https://github.com/mattpocock/skills/tree/main/grill-me) — 需求拷问技能（**必备**，制课前对用户进行需求澄清）
- [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) — SVG 流程图创建（**必备**，所有 SVG 流程图依赖此 skill）
- [knowledge-graph-map](https://github.com/AragornZJF/knowledge-graph-map) — 知识图谱可视化（**必备**，课程完成后创建知识点图谱）

### 发给 agent 安装（推荐）

将以下内容发送给 OpenCode / Claude / Cursor 等 AI 助手一次安装所有前置技能：

```
帮我安装以下技能：
1. teach — https://github.com/mattpocock/skills/tree/main/teach
2. grill-me — https://github.com/mattpocock/skills/tree/main/grill-me
3. fireworks-tech-graph — https://github.com/yizhiyanhua-ai/fireworks-tech-graph
4. knowledge-graph-map — https://github.com/AragornZJF/knowledge-graph-map
5. teach_more_pic — https://github.com/qwerkilo/teach_more_pic
都克隆到 ~/.agents/skills/ 目录下。
```

### 手动安装

```bash
# 克隆到 opencode 的 skills 目录
cd ~/.agents/skills
git clone https://github.com/qwerkilo/teach_more_pic
git clone https://github.com/AragornZJF/knowledge-graph-map
git clone https://github.com/yizhiyanhua-ai/fireworks-tech-graph

# 同时安装 mattpocock 的 base skills（位于同一仓库中）
git clone https://github.com/mattpocock/skills
# 然后复制或链接 skills/teach 和 skills/grill-me 到 .agents/skills/ 下
```

### 通过 AGENTS.md 配置

在项目根目录的 `AGENTS.md` 中引用这些 skill：

```
Skills: teach, grill-me, teach_more_pic, fireworks-tech-graph, knowledge-graph-map
```

## 能力

**27 个视觉组件**（完整索引见 SKILL.md）：

- **#1-7 核心**：SVG 流程图 / 角色卡片 / CSS 时间线 / CSS 条形图 / 对比表 / SVG 容器 / PPT 质感（主题切换 + 语言切换 + 滚动动画 + 键盘导航 + 目录）
- **#8-14 交互式**：折叠分步详解 / Tab 切换面板 / 图片对比滑块 / 交互式时间线 / 数据卡片网格 / 引文卡片 / 标注式图片
- **#15-27 数据与辅助**：状态链 / 数值滚动动画 / 标签徽章组 / 告警条 / 热力图 / 步骤指示器 / 信息面板 / 对比表增强版 / 灯箱 / **ECharts 交互式图表**（柱状/饼/折线/堆叠，需 `libs/echarts.min.js`） / **Three.js 3D**（3D 可视化，需 `libs/three.min.js`，含 Sprite 文字标签） / **D3.js 自定义图表**（力导向图/旭日图/桑基图，需 `libs/d3.min.js` + `d3-sankey.min.js`） / 现代浏览器 API（原生折叠/模态/幻灯片/Popover）
- **19 品牌主题** — 22 个 CSS 变量，`var(--accent/border/surface/...)` 自动跟随
- **主题切换动画** — 0.35s 平滑过渡，`prefers-reduced-motion` 自动禁用

## 使用方法

在 opencode 中同时激活两个 skill：

```
Skills: teach, teach_more_pic
```

base `teach` 负责课程结构、mission、learning records；`teach_more_pic` 负责视觉组件。

```bash
# 验证课程 HTML
python scripts/validate-lesson.py lessons/NNNN-slug.html

# 批量验证所有示例
powershell -ExecutionPolicy Bypass -File scripts/run-tests.ps1

# 运行验证脚本单元测试
python scripts/test_validate.py

# JS 语法检查
node -e "new Function(require('fs').readFileSync('file','r',encoding='utf-8').match(/<script>([\\s\\S]*?)<\\/script>/)[1])"

# SVG XML 检查
python -c "import xml.etree.ElementTree as ET; ET.parse('path.svg')"
```

## 课程制作流程

0. **使用 `grill-me` skill 拷问需求** — 澄清主题/受众/叙事矛盾/数据/风格偏好/双语需求，确认后再继续
1. 复制 `templates/lesson-starter.html` 作为新课程骨架 → 确认三幕大纲
2. 从 SKILL.md 组件索引表选 4-7 个组件（每幕 1-3 个），使用决策指南匹配 → 确认组件清单
3. 打开对应 `components/NN-name.md`，复制 ````html`/```css`/```js` 合并到模板中
4. SVG 保存为 `lessons/svg/NNNN-slug.svg`（磁盘文件）**并**内联到 HTML 中 `<figure class="svg-fig">` 包裹
5. **`libs/` 依赖**：先完整复制本 skill 的 `libs/` 下所有文件到目标项目的 `libs/`（echarts.min.js、three.min.js、d3.min.js、d3-sankey.min.js），确保离线包版本一致
6. 运行 `python scripts/validate-lesson.py lessons/NNNN-slug.html` 验证
7. SPA 集成：从 `templates/index-spa.html` 复制为 `index.html`，追加 `<section class="lesson-view" id="lesson-NNN">`
7. 知识图谱：新项目从 `templates/kg-starter.html` 复制到项目根目录为 `kg-项目名.html`（双语 `nameZh`/`nameEn` + L 键切换）；已有项目在已有 `kg-*.html` 中追加节点和关系

## 项目结构

```
├── SKILL.md               ← 唯一入口文档，所有规则在此
├── components/             各组件独立文件（27 个 .md），含 HTML/CSS/JS/降级说明
├── scripts/
│   ├── validate-lesson.py  课程验证脚本（18 项检查，含双语 + SPA + KG）
│   ├── test_validate.py    验证脚本单元测试（78 项，覆盖全部 18 项检查）
│   └── run-tests.ps1       批量验证所有示例
├── examples/               组件用法示例（24 个 .html，含 1 个 ECharts/D3/Three 混合）
├── libs/                   外部库（echarts.min.js、three.min.js、d3.min.js、d3-sankey.min.js、magicui-effects.css）
├── references/             参考附件（决策指南、页面类型模板）
├── templates/              7 个模板（4 SVG 骨架 + 1 课程起始 HTML + 1 知识图谱骨架 + 1 SPA 入口）
├── theme/19 个品牌 DESIGN.md  各品牌设计语言参考
├── test-prompts.json       测试提示词（12 个场景）
└── results.tsv             darwin-skill 优化记录
```

### Magic UI 装饰效果

课程模板和所有示例通过 `libs/magicui-effects.css` 共享 6 种 CSS 装饰效果：

| 效果 | CSS 类 | 说明 |
|---|---|---|
| 光泽扫光 | `.shiny-text` | 文本渐变扫光动画（封面 badge / 标题） |
| 噪点纹理 | `.noise-overlay` | SVG feTurbulence 噪点叠加层（封面/工具栏背景） |
| 圆点网格 | `.dot-bg` | CSS radial-gradient 圆点背景 |
| 直线网格 | `.grid-bg` | CSS linear-gradient 双线网格背景 |
| 流星雨 | `.meteors-container` + `.meteor` | 封面装饰流星动画 |
| 边框发光 | `.border-glow` | conic-gradient 旋转边框 |
| 辉光悬停 | `.glare-hover` | 背景渐变过渡，鼠标悬停触发 |
| 渐变文字 | `.gradient-text` | 多色渐变流动动画 |
| 模糊淡入 | `data-anim="blur"` | 滚动 → 模糊消除入场动画 |

所有效果适配 CSS 变量（`var(--accent)`、`var(--surface)` 等），自动跟随主题切换。

## 前置依赖

- [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) skill（**必备**，所有 SVG 流程图依赖此 skill）
- `cairosvg`（`pip install cairosvg`，SVG → PNG 导出）
