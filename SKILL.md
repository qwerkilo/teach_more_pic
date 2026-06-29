---
name: teach_more_pic
description: >
  SVG + CSS + ECharts + D3.js + Three.js visual-heavy HTML lessons.
  Use when creating new lessons or redesigning existing ones for visual variety.
  Complements the base `teach` skill — run both.
  Does NOT: generate text content, write quiz questions, manage learning records, or build EPUB files.
  Triggers: "visual lesson", "redesign lesson", "add diagrams", "图表", "流程图",
  "SVG", "diagram", "timeline", "infographic", "可视化", "图示", "数据可视化",
  "流程图", "时间线", "交互式", "数据卡片", "热力图", "对比表", "力导向图", "桑基图",
  "3D 场景", "Three.js", "ECharts", "D3.js",
  "中英双语", "language switch", "语言切换", "bilingual".
disable-model-invocation: true
argument-hint: "What lesson to create or redesign?"
---

# teach_more_pic — 视觉增强课程制作

Use alongside the base `teach` skill. The base `teach` handles workspace structure, mission, and learning records; this skill handles **visual components** inside each lesson.

## 前置条件

- `fireworks-tech-graph` skill available (for SVG diagram creation)
- 离线包：本 skill 的 `libs/` 下已包含 echarts.min.js、three.min.js（UMD 回退）、three.module.js（ESM 主入口，r185 WebGPU）、d3.min.js、d3-sankey.min.js、magicui-effects.css，课程创建时完整复制到目标项目即可
- Three.js WebGPU/TSL 需通过 `<script type="importmap">` 导入，详见 `27-Three.js 3D组件.md`
- Anime.js 4.5+ 内置 Three.js Adapter，动画优先使用 Anime.js（`animate(mesh, { x, rotateY, ... })`）而非手写 rAF
- `cairosvg` installed (`pip install cairosvg`) — for SVG → PNG export if needed
- Magic UI CSS 效果：`libs/magicui-effects.css` 共享 13 种零依赖装饰效果（shiny-text/noise/dot/grid/meteors/border-glow/glare-hover/gradient-text/blur/neon-card/spotlight-card/interactive-btn/typing-cursor），所有模板和示例均已引用

## 核心约定

- **无构建系统**：纯 HTML/CSS/JS，无 package.json、无 npm 命令。修改后直接浏览器打开。
- **中英双语**：课程内容、UI 标签、SVG 文本须同时包含中文和英文版本，通过语言切换按钮切换。默认显示中文。
- SVG 中文字体需显式指定 font-family（含中文字体名）。
- 课程文件命名：`lessons/NNNN-slug.html`（4 位编号 + 英文短名），SVG 同名同目录。
- 跨课链接：`<a href="NNNN-slug.html">`（无前导 `/`，无完整 URL）。

## 课程叙事框架

每课采用三幕叙事结构，避免"知识点串联"的枯燥感：

```
第一幕：设置矛盾  →  某个问题或制度设计的先天缺陷
第二幕：危机爆发  →  具体事件链，谁是推手，谁是受害者
第三幕：转折与遗产  →  解决方案、制度创新、与其它课程的联系
```

每幕结束时插入一个**视觉停顿**（SVG 流程图、时间线、对比表），让读者从文本中喘口气。

## 视觉组件工具箱

27 个组件，每个组件的 HTML/CSS/JS 代码和用法规则在 `components/NN-name.md` 中。此处只列索引。

### 核心组件（#1-7）

| # | 组件 | 文件 | 说明 |
|---|---|---|---|
| 1 | SVG 流程图 | `components/01-SVG 流程图.md` | 四色语义流程图，依赖 fireworks-tech-graph |
| 2 | 角色卡片 | `components/02-角色卡片.md` | 网格化角色介绍卡片 emoji + 名称 + 描述 |
| 3 | CSS 时间线 | `components/03-CSS 时间线.md` | 垂直时间轴，5+ 事件使用 |
| 4 | CSS 条形图 | `components/04-CSS 条形图.md` | 水平数据条，归一化百分比 |
| 5 | 对比表 | `components/05-对比表.md` | 多维度 flex 对比（指向增强版 #22） |
| 6 | SVG Figure | `components/06-SVG Figure 包裹.md` | 标准图片容器 |
| 7 | PPT 质感增强 | `components/07-PPT 质感增强.md` | T 键主题切换 + 滚动动画 + 键盘导航 + JS 模板 |

### 交互式组件（#8-14）

| # | 组件 | 文件 | 说明 |
|---|---|---|---|
| 8 | 折叠式分步详解 | `components/08-折叠式分步详解.md` | 复杂概念分步折叠，点击展开 |
| 9 | Tab 切换面板 | `components/09-Tab 切换面板.md` | 垂直 Tab 切换多视角内容 |
| 10 | 图片对比滑块 | `components/10-图片对比滑块.md` | 拖拽滑块对比 before/after |
| 11 | 交互式时间线 | `components/11-交互式时间线.md` | 点击时间点展开事件详情 |
| 12 | 数据卡片网格 | `components/12-数据卡片网格.md` | 图标 + 数值 + 标签卡片 |
| 13 | 引用/引文卡片 | `components/13-引用引文卡片.md` | 左侧竖条 + 引文 + 署名 |
| 14 | 标注式图片 | `components/14-标注式图片.md` | 图片上数字标注点弹出说明 |

### 数据与辅助组件（#15-27）

| # | 组件 | 文件 | 说明 |
|---|---|---|---|
| 15 | 状态链 | `components/15-状态链.md` | 水平里程碑 done/current/pending |
| 16 | 数值滚动动画 | `components/16-数值滚动动画.md` | 进入视口时 0→N 滚动 |
| 17 | 标签/徽章组 | `components/17-标签徽章组.md` | 5 色药丸标签 |
| 18 | 提示框/告警条 | `components/18-提示框告警条.md` | 4 类型 info/warning/error/success |
| 19 | 热力图/密度图 | `components/19-热力图密度图.md` | 绿→黄→红 5 级矩阵 |
| 20 | 步骤指示器 | `components/20-步骤指示器.md` | 水平编号步骤条 |
| 21 | 信息面板 | `components/21-信息面板.md` | 右侧滑入抽屉 |
| 22 | 对比表增强版 | `components/22-对比表增强版.md` | 粘性表头 + 斑马纹 + 排序 |
| 23 | 全屏模态/灯箱 | `components/23-全屏模态灯箱.md` | 点击放大全屏展示 |
| 24 | ECharts 交互式图表集 | `components/26-ECharts 交互式图表集.md` | 柱状图/饼图/折线图/堆叠图，ECharts 引擎，交互式 (CDN: cdn.jsdelivr.net/npm/echarts) |
| 25 | Three.js 3D 组件 | `components/27-Three.js 3D组件.md` | 3D 场景/柱状图/地理可视化，Three.js r185。**WebGPU 优先**（`WebGPURenderer`），不支持则回退 WebGL。**TSL 优先**（着色器节点），无法实现再降级 WGSL |
| 26 | 现代浏览器 API | `components/25-现代浏览器API组件.md` | 原生折叠/原生模态/CSS 幻灯片/Popover |
| 27 | D3.js 数据可视化 | `components/28-D3.js 数据可视化.md` | 力导向图/旭日图/桑基图，D3.js 引擎 (CDN: d3js.org/d3.v7.min.js，桑基图需额外 d3-sankey) |

### 使用规则

- 每课按内容自然选用合适的组件，每个 h2 章节至少 1 个视觉组件；可用 4-7 个组件，但不超过 8 个
- 新增组件：先在 `components/` 下创建文件，再更新此索引表
- 颜色语义全局统一：蓝=正常，橙=触发，红=崩溃，绿=救助
- **ECharts (#24)、Three.js (#25)、D3.js (#27) 可组合使用**：例如 D3.js 计算力导向布局后由 Three.js 渲染 3D 场景；或 D3.js 数据预处理后交给 ECharts 图表呈现。组合时只需确认各库的 CDN/本地文件均已加载即可。
- **Anime.js 4.5+ → Three.js 动画**：Three.js 对象动画优先使用 Anime.js Three.js Adapter（`import 'animejs/adapters/three'`），一句 `animate(mesh, { x, rotateY, color })` 完成多属性动画，参见 `examples/anime-three-demo.html`

### 视觉设计纪律

- **最多 1 个强调色**，饱和度 < 80%。禁止 AI 默认的紫/蓝渐变
- **禁止热暖系蜡笔色默认**（#f5f1ea 等米白背景、#b08947 等黄铜强调色）。避免所有课程看起来像同一个模板
- **禁止纯黑 `#000000`**，用 off-black（zinc-950、`#1a1a1a`）；**禁止纯白 `#ffffff`**，用 off-white
- 渐变文本只用于极小标题，禁止大标题全渐变
- 卡片只在真的需要层次感时使用，否则用 `border-top` 或间距分组
- **一页只用一个字体族**，不要混搭衬线+无衬线做强调（用同字体的 bold/italic）

### 共享模式：折叠展开 JS

折叠分步详解（#08）和交互式时间线（#11）共用同一套 JS 模式：点击触发器（`.XX-trigger` / `.XX-dot`）→ 测量内容高度（`scrollHeight`）→ CSS transition 动画。核心逻辑：

```js
var i=this.closest('.XX-item'),c=i.querySelector('.XX-content'),o=i.dataset.expanded==='true';
if(o){c.style.height=c.scrollHeight+'px';requestAnimationFrame(function(){c.style.height='0px';});
i.dataset.expanded='false';this.setAttribute('aria-expanded','false');}else{
c.style.height='0px';requestAnimationFrame(function(){c.style.height=c.scrollHeight+'px';});
i.dataset.expanded='true';this.setAttribute('aria-expanded','true');
c.addEventListener('transitionend',function h(){c.removeEventListener('transitionend',h);c.style.height='auto';});}
```

替换其中的 `XX` 为对应组件的前缀（`sd`、`tli`）即可复用。两个组件文件中的 JS 代码均基于此模板。新增类似折叠组件时直接复制此模式。**注意**：`transitionend` 事件确保动画完成后将 `height` 恢复为 `auto`，防止内容变化（如字体渲染）后高度穿帮。

### PPT 增强 JS 注意事项

- 所有 JS 在课程 HTML 末尾 `<script>` 内，单个 IIFE 包裹，每个功能块包在 `try{}catch(e){}` 内
- 主题切换使用 `localStorage`（主题名存储为 `theme` key）
- 闭包体结尾 `})();` 之前不能有多余字符
- 修改 toolbar 按钮或添加新功能时需同步 3 个文件（模板、SPA、KG）
- 语言切换使用 L 键或右下工具栏语言按钮，切换中日英（`zh`/`en`），通过 `data-lang` 属性控制显示/隐藏，`localStorage`（key: `lang`）持久化

### 组件选择决策指南

按内容类型选择最合适的组件。七个象限和完整决策表见 `references/decision-guide.md`。

快速摘要：

| 象限 | 适用场景 | 核心组件 |
|------|---------|---------|
| 一：解释与拆解 | 复杂概念分步拆解、多视角对比 | 折叠分步 (#8)、Tab 面板 (#9)、SVG 流程图 (#1) |
| 二：数据与统计 | 数值对比、趋势、占比 | ECharts (#24)、D3.js (#27)、CSS 条形图 (#4) |
| 三：时间与过程 | 事件序列、进度阶段 | CSS 时间线 (#3)、交互式时间线 (#11)、状态链 (#15) |
| 四：引用与强调 | 名言、警告、术语 | 引文卡片 (#13)、告警条 (#18)、信息面板 (#21) |
| 五：视觉对比 | 图对比、3D、全屏 | 对比滑块 (#10)、Three.js (#25)、灯箱 (#23) |
| 六：零 JS 方案 | 需要降级的场景 | 原生折叠/模态/幻灯片/Popover (#26) |
| 七：Magic UI 装饰 | 锦上添花的纯 CSS 效果 | shiny-text / globe / neon-card / 边框发光 / 网格背景 |

→ 完整选择矩阵 + 7 组三幕组合示例见 `references/decision-guide.md`

## 可选页面类型

在纵向滚读课程中，以下特殊页可以打破单调的"标题→段落→图→标题"节奏。完整 HTML/CSS 代码（含中英双语版）见 `references/page-types.md`。

| 类型 | 必选？ | 用法 | 视觉亮点 |
|------|--------|------|---------|
| **封面页** | ✅ 每课必须 | 课程开头，展示编号 + 标题 + 引子 | shiny-text 光泽标题、药丸 badge |
| **章节分隔页** | ✅ 三幕必须 | 幕与幕之间，标记叙事切换 | 圆形编号 + 顶部装饰线 |
| **总结卡片** | ✅ 每课必须 | 测验前，3 张卡片总结核心洞察 | SVG 矢量图标、hover 微上浮 |
| **全宽引文页** | 可选 | 关键论断单独占据视区 | 左侧 accent 竖线、40vh 高度 |
| **关键数字页** | 可选 | 数据密集型课程强调关键数字 | 3rem 超大数字 + accent 色 |
| **信息面板侧边栏** | 可选 | 术语解释、背景补充 | 右浮动、窄屏自动降级 |

## 🔴 重要纪律（必须遵守）

- **所有课程必须从 `templates/lesson-starter.html` 复制作为基础**。禁止从零生成 HTML 结构。
- 保留模板的完整 CSS 变量系统（`:root` + 20 个 `[data-theme]`）、工具栏（主题/语言/目录）、键盘快捷键（T/L/←→）。
- 只修改以下部分：封面页标题/描述、三幕正文内容、组件 CSS/HTML/JS 插入标记处、测验内容。
- 视觉组件（折叠分步、时间线、图表等）在模板预留的 `<!-- INSERT: 组件 HTML/CSS/JS -->` 注释处追加，不删除任何已有功能。
- 违反此纪律的课程视为不合格，需重做。

## 课程制作工作流

```
Step 0: 需求拷问
  - 使用 `grill-me` skill 对用户进行需求拷问，澄清：
    · 课程主题与目标受众（谁学、为什么学）
    · 核心叙事矛盾（三幕中"冲突"是什么）
    · 预期数据/数字（有哪些可量化的内容可可视化）
    · 参考与风格偏好（是否有品牌色/参考课程/审美方向）
  - 🔴 未经过 grill-me 拷问不得开始 Step 1。拷问后输出一串 "设计读法" 确认方向，格式：`主题 → NNNN-slug.html · 三幕：矛盾/危机/转折 · 组件数 4-7`
  - 🛑 STOP：等待用户回复 "确认" 或 "可以，继续" 后再进入 Step 1。用户未明确确认不得推进。

Step 1: 确定叙事框架（三幕）
  - 第一幕：矛盾/背景（1-2段）
  - 第二幕：事件/危机（核心内容）
  - 第三幕：转折/遗产（收束+跨课连接）
  - 🔴 输出：三段式大纲（每幕 2-3 句话），展示给用户确认
  - 🛑 STOP：用户回复 "确认" 或 "可以" 后再进入 Step 2。用户若提出修改意见 → 修改后再次展示 → 重复直到确认

Step 2: 设计视觉组件
  - 从上方索引表按内容脉络选择组件：第一幕 1-2 个、第二幕 2-3 个、第三幕 1-2 个，总量 4-7 个（上限 8 个）
  - 打开对应的 components/NN-name.md 读取完整 HTML/CSS/JS
  - 🔴 输出：组件选择清单（组件名+编号+所属幕），展示给用户确认
  - 🛑 STOP：用户回复 "确认" 后再进入 Step 3。用户想增减组件 → 调整清单 → 再次展示确认
  - 🔴 每个 SVG 创建后立即验证：`python -c "import xml.etree.ElementTree as ET; ET.parse('path.svg')"`
  - **SVG 需同时保存为磁盘文件和内联到 HTML**：`lessons/svg/NNNN-slug.svg` 保留为独立文件，同时将 SVG 内容复制到 HTML 中用 `<figure class="svg-fig">` 包裹内联

Step 3: 写 HTML
  - 复制 `templates/lesson-starter.html` 作为新课程骨架，填入标题/内容
  - 文件命名：`lessons/NNNN-slug.html`（NNNN=4 位编号，slug=英文短名）
  - 从 `components/NN-name.md` 复制所选组件的结构 HTML + CSS + JS 合并到模板中：
    · 结构 HTML：复制文件中 ````html` 代码块（不含上述说明文字）
    · 组件 CSS：复制文件中 ````css` 代码块→合并到课程 `<style>` 中
    · 组件 JS：复制文件中 ````js` 代码块→合并到课程 `<script>` 中
  - **合并组件 CSS**：合并规则：
    1. 所有组件 CSS 放同一个 `<style>` 块中，按前缀分组（如 /* data-grid */ / /* countup */）
    2. 组件类名使用唯一前缀（`dg-`、`sd-`、`tab-`、`ai-` 等），不会相互冲突
    3. 重复的 `:root` 变量声明只需保留一份
    4. `@media` 查询放各组件的 CSS 块末尾
  - 将各组件 HTML 结构分散到课程正文对应位置——流程图放第一幕、数据卡片和引文放第二幕、对比表放第三幕等
  - 各组件 JS 代码合并到课程末尾 `<script>` 块中：**组件 JS 放在 `<!-- ===== 组件 JS 从此处插入（可选） ===== -->` 注释之后**（在 PPT 增强 JS 下方），确保 PPT 增强 JS 始终最先加载
  - CSS 放在 `/* ===== 组件 CSS 从此处插入（按前缀分组） ===== */` 注释之上，与模板 CSS 在同一 `<style>` 块内
  - 每幕之间的"视觉停顿"法则：每 2-3 段文本后插入一个视觉元素
  - 阅读节奏：核心内容用交互式组件（Tab/折叠/时间线），数据用卡片/条形图/热力图，引用用引文卡片，提示用告警条
  - **课程间互相链接使用相对路径**：如 `<a href="NNNN-slug.html">`，不要加前导 `/` 或完整 URL
  - **最终 HTML 文件结构（必须遵守）**：
```
lessons/NNNN-slug.html
├── <html lang="zh-CN" data-theme="warm">
│   ├── <head>
│   │   ├── <style>  ← 模板 CSS 变量 + 20 主题 + 正文排版 + 组件 CSS（按前缀分组）
│   │   └── </head>
│   ├── <body>
│   │   ├── <article class="cover-page">  ← 中英双语封面 badge/h1/subtitle/hook
│   │   ├── <section class="section-divider">  ← 第一幕分隔（divider-num + h2）
│   │   ├── <p>  ← 中英双语正文段落
│   │   ├── <figure class="svg-fig"><svg>...  ← SVG 流程图（磁盘 + 内联）
│   │   ├── <!-- INSERT: 组件 HTML（拆散到各幕） -->
│   │   ├── <section class="section-divider">  ← 第二幕分隔
│   │   ├── ... 组件 + 正文 ...
│   │   ├── <section class="section-divider">  ← 第三幕分隔
│   │   ├── <aside class="summary-cards">  ← 3 张总结卡片（SVG 图标）
│   │   ├── <div class="quiz-section">  ← 5 题双语测验
│   │   ├── <div class="ui-toolbar">  ← T 键 + L 键 + 目录按钮
│   │   ├── <!-- Quiz JS -->
│   │   ├── <!-- PPT 质感增强 JS（主题/语言/TOC/动画/导航） -->
│   │   └── <!-- 组件 JS -->
│   └── </body>
```
  - 这个结构是必须遵守的骨架。所有课程内容以此为基底，仅填充 `<body>` 内的内容区。

Step 4: 验证
  - 浏览器打开 .html 检查渲染
  - SVG 验证：python -c "import xml.etree.ElementTree as ET; ET.parse('path.svg')"
  - 交叉链接检查（glossary 路径、课程链接）——确认所有跨课链接为相对路径
  - 测验 5 题，每题 3 个选项
  - 🔴 任一验证失败 → 定位问题 → 修复后重跑验证 → 全部通过后再继续
  - 🛑 STOP：全部验证通过后再进入 Step 5

Step 5: 配套产出
  - 调用 base `teach` skill 的 learning-record 模板，生成课程学习记录（含课程名、日期、关键概念列表）
  - EPUB 重建：如本课程隶属于某个系列（已有 `.epub` 文件），用 `teach` skill 的 EPUB 工具重新打包
  - 🔴 课程间链接验证：打开所有 `<a href="NNNN-slug.html">` 确认目标文件存在
  - 🛑 STOP：用户确认配套产出无误后再进入 SPA 集成

Step 6: SPA 集成
  - 从 `templates/index-spa.html` 复制骨架作为 `index.html`，插入各课的
    `<section class="lesson-view" id="lesson-NNN">...</section>` 到注释标记处
  - 已有 SPA 则直接追加新 `<section class="lesson-view">` 到 `</body>` 前
  - 确保每课一个独立的 `<section>`，用 `id="lesson-NNN"` 索引
  - 🔴 验证：`id="lesson-NNN"` 在 `index.html` 中不与其他课程冲突
  - SPA 切换 JS 已存在于 `index.html` 中，通过 `id` 控制显示/隐藏
  - 保留 `lessons/NNN-slug.html` 独立文件，供非 SPA 场景直接打开
  - 🔴 将本 skill 的 `libs/` 下所有文件（echarts.min.js、three.min.js、three.module.js、three/ 目录、d3.min.js、d3-sankey.min.js）完整复制到目标项目的 `libs/` 目录，确保课程始终使用固定版本离线包
  - 🛑 STOP：确认 SPA 预览正常后再进入 Step 7

Step 7: 知识图谱更新
  - 新项目从 `templates/kg-starter.html` 复制到项目根目录为 `kg-项目名.html`；已有项目在已有 `kg-*.html` 中追加
  - 提取课程中的关键概念/术语作为节点，课程间的链接作为边
  - 节点名使用 `nameZh`/`nameEn` 双字段，图谱通过 L 键切换语言
  - 🔴 验证：新节点 id 不与已有节点重复
  - 🛑 STOP：确认图谱显示正确后再提交最终成果

Step 8: 本地 HTTP 服务器（可选）
  - 从 `templates/start-server.ps1` 复制到项目根目录
  - 运行 `powershell -ExecutionPolicy Bypass -File start-server.ps1`
  - 自动打开浏览器到 `index.html`（有 SPA 时）或第一课
  - 按 Q 键停止服务器
  - Python 内置 `http.server`，无需额外依赖
  - Linux/macOS：复制 `templates/start-server.sh`，运行 `bash start-server.sh`，后台静默运行（nohup），PID 写入 `.server.pid`；停止 `kill $(cat .server.pid) && rm .server.pid`
```

## 文件资源速查

| 路径 | 用途 | 工作流中引用处 |
|---|---|---|---|
| `templates/lesson-starter.html` | 课程骨架模板（所有课程的起点，内含 15 个组件 CSS/HTML/JS） | Step 3 |
| `templates/index-spa.html` | SPA 课程集线器模板（hash 路由 + 主题/语言切换） | Step 6 |
| `templates/kg-starter.html` | 知识图谱模板（双语 nameZh/nameEn，L 键切换） | Step 7 |
| `templates/start-server.ps1` / `.sh` | 本地 HTTP 服务器启动脚本（Windows PS / Linux bash） | Step 8 |
| `templates/flowchart-vertical.svg` | 垂直流程图模板（完整有效 SVG，四色语义） | Step 2/5 |
| `templates/cycle-diagram.svg` | 循环图模板（中心+周边节点） | Step 2/5 |
| `templates/comparison-side-by-side.svg` | 左右对比 SVG 模板（双列对比） | Step 2/5 |
| `templates/timeline-horizontal.svg` | 水平时间线 SVG 模板（单线事件序列） | Step 2/5 |
| `examples/*.html` | 29 个组件的独立用法示例（含 Anime.js+Three、D3→Three 专用示例，D3/Three/ECharts/Anime 四合一混合） | Step 2 参考 |
| `components/NN-name.md` | 组件代码 + 降级说明（27 个） | Step 2/3 |
| `references/decision-guide.md` | 组件选择决策矩阵 + 7 组三幕组合示例 | Step 2 |
| `references/page-types.md` | 6 种可选页面类型的完整 HTML/CSS（中英双语） | 可选页面类型 |
| `scripts/validate-lesson.py` | 课程验证脚本（18 项检查，含双语+SPA+KG） | Step 4 |
| `scripts/test_validate.py` | 验证脚本单元测试（85 项） | 开发 |
| `libs/magicui-effects.css` | Magic UI 装饰效果共享 CSS（13 种零依赖纯 CSS） | 模板自动加载 |
| `libs/` | 离线包（echarts/three UMD/three.module.js/three addons/d3/d3-sankey） | Step 6 |

## 失败模式与异常处理

| 触发条件 | 超时判定 | 一线修复 | 仍失败兜底 |
|---|---|---|---|
| SVG 空白/排版错乱 | 5s 内无渲染 | 检查 XML 语法、viewBox 与 width/height 比例 | 降级为 `<img>` 外部引用 |
| SVG 中文不渲染 | 页面加载后立即可见 | font-family 加中文字体 | 内联 font-family |
| 条形图溢出容器 | 页面加载后立即可见 | 检查 `bar-fill` width ≤ 100% | `text-overflow: ellipsis` |
| 测验 `data-correct` 写反 | 点击后反馈文字错误 | `grep 'data-correct="true"'` 确认每题 1 个 | 手动核验 |
| IntersectionObserver 不触发 | 滚动 2s 后无动画 | 移除该元素 `data-anim` | 首屏元素不加 `data-anim` |
| 主题切换后颜色不变 | 按下 T 键后立即可见 | 用 `var(--accent)` 而非固定色 | `border-bottom-color: var(--accent)` |
| Panel 点击外部不关闭 | 点击外部 1s 后面板未关 | click 事件未委托到 document | 排除 toolbar/panel 区域 |
| 折叠动画不平滑 | 点击时过渡不平滑 | 先 `scrollHeight` 再设 px | 过渡结束恢复 `auto` |
| ECharts/Three/D3/D3-sankey 空白 | 页面加载 3s 后空白 | 对应 lib 未加载 | 复制 `libs/` 下文件，或 CDN 加载 |
| Three.js WebGPU 空白（THREE 未定义） | 页面加载 3s 后空白 | importmap 路径错误或 r185 CDN 不可达 | 降级为 `libs/three.min.js` UMD 回退 |
| Three.js TSL 失效 | 着色器效果不显示 | TSL 节点语法错误或版本不匹配 | 降级为固定色常规材质 |
| libs 版本过旧 | API 报错（如 `setOption is not a function`） | 检查版本号，本地与 CDN 同步 | 重新下载 libs 覆盖 |
| 多图表库性能问题 | 帧率 < 30fps 持续 5s | 延迟非首屏图表 | 减少动画复杂度 |
| SPA 课程 id 冲突 | 路由跳转显示错误课程 | 两个 `id` 相同 | 用 `id="lesson-NNN"` 格式 |
| JS 括号顺序错误 | 控制台 `})` unexpected | function body `}` + if body `}` + `)` 闭调用 | 检查 `});` vs `}})` 顺序 |
| 浏览器缓存旧 JS | 修改后刷新无变化 | Ctrl+F5 强制刷新 | 注销浏览器缓存 |
| 语言切换错位 | L 键后有中文残余 | 中英文段落数不一致或未成对 `data-lang` | 确保两版本段落数相同 |
| 组件特定问题 | — | 见 `components/NN-name.md` | — |

## 写作风格

- 三幕叙事，避免"知识点串联"
- 每课一个贯穿性隐喻或核心问题
- 删除不必要的过渡词（"值得注意的是"、"需要指出的是" → 直接说）
- 数据和引用的数字用 `.num` 蓝色加粗标记
- 核心术语首次出现时用 `.key-term` 红色加粗
- 引用来源用脚注编号 `[1]`

## 反模式黑名单（不要做的事）

| # | 反模式 | 为什么 | 替代做法 |
|---|---|---|---|
| 1 | 超过 8 种组件 / 连续 4 段无视觉停顿 | 视觉密度过高，读者疲劳 | 每课 4-7 个组件，每 1-2 段插一个视觉元素 |
| 2 | 图标类型错位（饼图做时序、emoji 做结构） | 语义错误、风格不统一 | 时序→折线图，结构→SVG 图标 |
| 3 | SVG 颜色语义错误 / 浅底白字 / 纯红流程图 | 不可读、失去语义 | 蓝=正常，橙=触发，红=崩溃，绿=救助；深底白字浅底深字 |
| 4 | 条形图用绝对数值 / 角色卡片超 4 行 / 时间线 < 5 事件 | 溢出或视觉空洞 | 归一化百分比；最多 3 行；事件 < 5 用列表 |
| 5 | 硬编码颜色而非 CSS 变量 | 主题切换后颜色不变 | 全部用 `var(--accent)`、`var(--border)` 等 |
| 6 | 缺少 PPT 质感（无主题切换/键盘导航） | 交互体验差 | 每个课程加入 T 键 + ← → 键 |
| 7 | 编造数据/引文 | 损害可信度 | 模拟数据标注 `mock-data` 类 |
| 8 | 只写中文不写英文 / CDN 无离线降级 | 违反双语约定 / 离线空白 | 成对 `data-lang` + libs 离线包双保险 |
| 9 | 混用 ASCII 和 SVG 图 | 风格不统一 | 全部 SVG 或全部 ASCII |
| 10 | 图表库只加载部分依赖（D3+Three 但漏 Three） | 一种图表空白 | 用到几个库就加载几个 libs 文件 |

## 错误检查清单

- [ ] SVG 文件通过了 XML 验证
- [ ] 所有 SVG 文字颜色与背景有足够对比度
- [ ] SVG 中的中文渲染正常（font-family 包含中文字体）
- [ ] SVG 的 viewBox 匹配 width/height 比例
- [ ] 条形图的 width 百分比 < 100%
- [ ] 时间线的最后一个事件不会超出容器
- [ ] 对比表在窄屏（<600px）下折叠为堆叠布局
- [ ] Quiz 数据属性正确（`data-correct="true"` v.s. `"false"`）
- [ ] 外部链接的 SVG src 路径正确
- [ ] 课程间链接使用相对路径
- [ ] 中英文内容成对标记（`data-lang="zh"` + `data-lang="en"`）
- [ ] 语言切换按钮和 L 键快捷键存在

验证自动化：`python scripts/validate-lesson.py lessons/NNNN-slug.html` — 自动检查 SVG 路径/XML 有效性/颜色对比度、quiz 正确数/完整度、h1 数量、data-anim 语法、容器宽度、相对路径、PPT JS（主题+导航）存在性。

JS 语法检查：`node -e "new Function(require('fs').readFileSync('file','r',encoding='utf-8').match(/<script>([\\s\\S]*?)<\\/script>/)[1])"`
