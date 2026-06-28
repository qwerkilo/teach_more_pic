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

**26 个视觉组件**（完整索引见 SKILL.md）：

- **#1-7 核心**：SVG 流程图 / 角色卡片 / CSS 时间线 / CSS 条形图 / 对比表 / SVG 容器 / PPT 质感（主题切换 + 滚动动画 + 键盘导航）
- **#8-14 交互式**：折叠分步详解 / Tab 切换面板 / 图片对比滑块 / 交互式时间线 / 数据卡片网格 / 引文卡片 / 标注式图片
- **#15-26 数据与辅助**：状态链 / 数值滚动动画 / 标签徽章组 / 告警条 / 热力图 / 步骤指示器 / 信息面板 / 对比表增强版 / 灯箱 / **ECharts 交互式图表**（柱状/饼/折线/堆叠，需下载 `libs/echarts.min.js`） / **Three.js 3D**（3D 数据可视化，需下载 `libs/three.min.js`） / 现代浏览器 API（原生折叠/模态/幻灯片/Popover）
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
```

## 课程制作流程

0. **使用 `grill-me` skill 拷问需求** — 澄清主题/受众/叙事矛盾/数据/风格偏好，确认后再继续
1. 复制 `templates/lesson-starter.html` 作为新课程骨架 → 确认三幕大纲
2. 从 SKILL.md 组件索引表选 4-7 个组件（每幕 1-3 个），使用决策指南匹配 → 确认组件清单
3. 打开对应 `components/NN-name.md`，复制 ````html`/```css`/```js` 合并到模板中
4. SVG 保存为 `lessons/svg/NNNN-slug.svg`（磁盘文件）**并**内联到 HTML 中 `<figure class="svg-fig">` 包裹
5. 运行 `python scripts/validate-lesson.py lessons/NNNN-slug.html` 验证
6. 知识图谱：新项目从 `templates/kg-starter.html` 复制骨架，填入节点和关系数据；已有项目在 `kg-yuecai.html` 中追加

## 项目结构

```
├── SKILL.md               ← 唯一入口文档，所有规则在此
├── components/             各组件独立文件（25 个 .md），含 HTML/CSS/JS/降级说明
├── scripts/
│   ├── validate-lesson.py  课程验证脚本（11 项检查）
│   ├── test_validate.py    验证脚本单元测试（29 项）（Popover/dialog 一致性检查）
│   └── run-tests.ps1       批量验证所有示例
├── examples/               组件用法示例（21 个 .html）
├── templates/              6 个模板（4 SVG 骨架 + 1 课程起始 HTML + 1 知识图谱骨架）
├── theme/19 个品牌 DESIGN.md  各品牌设计语言参考
├── test-prompts.json       测试提示词（12 个场景）
└── results.tsv             darwin-skill 优化记录
```

## 前置依赖

- [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) skill（**必备**，所有 SVG 流程图依赖此 skill）
- `cairosvg`（`pip install cairosvg`，SVG → PNG 导出）
