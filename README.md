# teach_more_pic — 视觉增强课程制作

配合 [base `teach` skill](https://github.com/mattpocock/skills/tree/main/teach) 使用的视觉增强技能，为每节课程注入 PPT 级的视觉品质。

> 需要先安装 base `teach` skill——本项目是它的视觉增强插件，两者缺一不可。

## 安装

### 前提

本技能需要 [opencode](https://opencode.ai) 环境。已安装了以下 base skill：
- [teach](https://github.com/mattpocock/skills/tree/main/teach) — 基础课程制作技能（必装）
- [grill-me](https://github.com/mattpocock/skills/tree/main/grill-me) — 需求拷问技能（**必备**，制课前对用户进行需求澄清）
- [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) — SVG 流程图创建（**必备**，所有 SVG 流程图依赖此 skill）

### 手动安装

```bash
# 克隆到 opencode 的 skills 目录
cd ~/.agents/skills
git clone https://github.com/qwerkilo/teach_more_pic

# 同时安装 base teach skill（位于 mattpocock/skills 仓库中）
git clone https://github.com/mattpocock/skills
# 然后复制或链接 skills/teach 和 skills/grill-me 到 .agents/skills/ 下
```

### 通过 AGENTS.md 配置

在项目根目录的 `AGENTS.md` 中引用这些 skill：

```
Skills: teach, grill-me, teach_more_pic, fireworks-tech-graph
```

## 能力

**核心视觉组件（#1-7）：**
- **SVG 流程图** — 四色语义（蓝/橙/红/绿）的彩色流程图
- **角色卡片** — 网格化角色介绍卡片
- **CSS 时间线** — 垂直时间轴组件
- **CSS 条形图** — 水平数据条
- **对比表（增强版）** — 粘性表头、斑马纹、点击排序（#22）
- **PPT 质感** — 右下角工具栏（SVG 调色盘图标主题面板 + SVG 目录）+ T 键快捷切换、滚动动画、键盘导航
- **19 品牌主题** — 从各品牌 DESIGN.md 自动提取 CSS 变量，组件使用 `var(--border/surface/accent)` 自动跟随
- **主题切换动画** — 切换时 bg/text/border/shadow 0.35s 平滑过渡，`prefers-reduced-motion` 时自动禁用
- **深度主题系统** — 每个主题从 DESIGN.md 提取 22 个 CSS 变量（含 `--surface-raised`、`--muted`、`--h2-size`、`--body-size`、`--small-size`），字体和行高精确匹配品牌设计语言

**交互式组件（#8-14）：**
- **折叠式分步详解** — 复杂概念分步折叠点击展开
- **Tab 切换面板** — 垂直 Tab 切换多视角
- **图片对比滑块** — 拖拽对比 before/after
- **交互式时间线** — 点击时间点展开详情
- **数据卡片网格** — 图标 + 数值 + 标签卡片
- **引用/引文卡片** — 左侧竖条 + 引文 + 署名
- **标注式图片** — 图片标注点弹出说明

**数据与辅助组件（#15-22）：**
- **状态链** — 水平里程碑 done/current/pending
- **数值滚动动画** — 进入视口 0→N 滚动
- **标签/徽章组** — 5 色药丸标签
- **提示框/告警条** — 4 类型彩色提示框
- **热力图/密度图** — 绿→黄→红 5 级矩阵
- **步骤指示器** — 水平编号步骤条
- **信息面板** — 右侧滑入抽屉
- **对比表增强版** — 粘性表头 + 斑马纹 + 排序
- **全屏模态/灯箱** — 点击放大全屏展示大图/详情
- **数据图表集** — 柱状图/饼图/折线图/堆叠图，纯 CSS + SVG，无 JS 依赖
- **现代浏览器 API** — 原生 `<details>` 折叠 / `<dialog>` 模态框 / CSS 幻灯片 / Popover 提示，零 JS

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

## 项目结构

```
├── SKILL.md               ← 唯一入口文档，所有规则在此
├── components/             各组件独立文件（25 个 .md），含 HTML/CSS/JS/降级说明
├── scripts/
│   ├── validate-lesson.py  课程验证脚本（11 项检查）
│   ├── test_validate.py    验证脚本单元测试（29 项）（Popover/dialog 一致性检查）
│   └── run-tests.ps1       批量验证所有示例
├── examples/               组件用法示例（21 个 .html）
├── templates/              5 个模板（4 SVG 骨架 + 1 课程起始 HTML）
├── theme/19 个品牌 DESIGN.md  各品牌设计语言参考
├── test-prompts.json       测试提示词（12 个场景）
└── results.tsv             darwin-skill 优化记录
```

## 前置依赖

- [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) skill（**必备**，所有 SVG 流程图依赖此 skill）
- `cairosvg`（`pip install cairosvg`，SVG → PNG 导出）
