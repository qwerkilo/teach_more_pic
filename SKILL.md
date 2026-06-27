---
name: teach_more_pic
description: >
  Teach a concept with visual-heavy HTML lessons: SVG flowcharts (via fireworks-tech-graph),
  CSS timelines, bar charts, role cards, data grids, comparison tables, interactive timelines,
  charts (bar/pie/line/stacked), foldable steps, tab panels, heatmaps, lightbox modals.
  Use when creating new lessons or redesigning existing ones for visual variety.
  Complements the base `teach` skill — run both.
  Triggers: "visual lesson", "redesign lesson", "add diagrams", "图表", "流程图",
  "SVG", "diagram", "timeline", "infographic", "可视化", "图示", "数据可视化", "图表",
  "流程图", "时间线", "交互式", "数据卡片", "热力图", "对比表".
disable-model-invocation: true
argument-hint: "What lesson to create or redesign?"
---

# teach_more_pic — 视觉增强课程制作

Use alongside the base `teach` skill. The base `teach` handles workspace structure, mission, and learning records; this skill handles **visual components** inside each lesson.

## 前置条件

- `fireworks-tech-graph` skill available (for SVG diagram creation)
- ECharts 5.x: download to `libs/echarts.min.js` for offline chart support (#26)
- `cairosvg` installed (`pip install cairosvg`) — for SVG → PNG export if needed

## 课程叙事框架

每课采用三幕叙事结构，避免"知识点串联"的枯燥感：

```
第一幕：设置矛盾  →  某个问题或制度设计的先天缺陷
第二幕：危机爆发  →  具体事件链，谁是推手，谁是受害者
第三幕：转折与遗产  →  解决方案、制度创新、与其它课程的联系
```

每幕结束时插入一个**视觉停顿**（SVG 流程图、时间线、对比表），让读者从文本中喘口气。

## 视觉组件工具箱

25 个组件，每个组件的 HTML/CSS/JS 代码和用法规则在 `components/NN-name.md` 中。此处只列索引。

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

### 数据与辅助组件（#15-25）

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
| 24 | ECharts 交互式图表集 | `components/26-ECharts 交互式图表集.md` | 柱状图/饼图/折线图/堆叠图，ECharts 引擎，交互式 |
| 25 | 现代浏览器 API | `components/25-现代浏览器API组件.md` | 原生折叠/原生模态/CSS 幻灯片/Popover |

### 使用规则

- 每课按内容自然选用合适的组件，每个 h2 章节至少 1 个视觉组件；可用 4-7 个组件，但不超过 8 个
- 新增组件：先在 `components/` 下创建文件，再更新此索引表
- 颜色语义全局统一：蓝=正常，橙=触发，红=崩溃，绿=救助

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

### 组件选择决策指南

按内容类型选择最合适的组件。每课可从多个象限选取，形成丰富的视觉节奏。

#### 象限一：解释与拆解（复杂概念 → 分步/多视角）

| 内容场景 | 推荐组件 | 备选 | 适合的一幕 |
|---|---|---|---|
| 复杂概念分步拆解 | 折叠式分步详解 (#8) | 原生折叠 (#25a) / 信息面板 (#21) | 第一/三幕 |
| 多视角/多方案对比 | Tab 切换面板 (#9) | 对比表 (#22) | 第二幕 |
| 资金/逻辑流向 | SVG 流程图 (#1) | 标注式图片 (#14) | 第一幕 |
| 复杂图表/地图详解 | 标注式图片 (#14) | SVG 流程图 (#1) | 第二幕 |
| 零 JS 的折叠/展开 | 原生折叠 (#25a) | 折叠分步 (#8) | 各幕 |

#### 象限二：数据与统计（数字 → 可视化）

**数据格式速查**：使用 #26 图表前先确认数据格式
| 图表类型 | 输入数据格式 | 示例 |
|---------|------------|------|
| 柱状图 (#26a) | 分类 → 数值（最多 8 个柱子） | `["2020":30, "2021":45, "2022":38]` |
| 饼图 (#26b) | 分类 → 百分比（总和 100%，≤6 块） | `["A":30%, "B":25%, "C":20%]` |
| 折线图 (#26c) | 时间 → 数值（≥3 个数据点） | `["2020":30, "2021":45, "2022":55]` |
| 堆叠图 (#26d) | 分类 → [子类1, 子类2, …]（≤4 子类） | `["2020":[20,10], "2021":[25,20]]` |

| 内容场景 | 推荐组件 | 备选 | 适合的一幕 |
|---|---|---|---|
| 关键统计数据 | 数据卡片网格 (#12) + 数值滚动动画 (#16) | CSS 条形图 (#4) | 第二/三幕 |
| 分类数值对比 | 纵向柱状图 (#26a) | CSS 条形图 (#4) | 第二幕 |
| 单组数据对比 | CSS 条形图 (#4) | 纵向柱状图 (#26a) | 第二幕 |
| 占比/比例展示 | 饼图 (#26b) | 堆叠图 (#26d) | 第二幕 |
| 趋势变化（时间序列） | 折线图 (#26c) | 交互式时间线 (#11) | 第二幕 |
| 构成对比（多行堆叠） | 堆叠图 (#26d) | 饼图 (#26b) | 第二幕 |
| 多方案多维度对比 | 对比表增强版 (#22) | Tab 面板 (#9) | 第三幕 |
| 二维数据密度矩阵 | 热力图 (#19) | 堆叠图 (#24d) | 第二幕 |

#### 象限三：时间与过程（时序 → 可视化）

| 内容场景 | 推荐组件 | 备选 | 适合的一幕 |
|---|---|---|---|
| 事件时间序列（≤4） | CSS 时间线 (#3) | 编号列表 | 第一幕 |
| 事件时间序列（5+） | 交互式时间线 (#11) | 状态链 (#15) | 第二幕 |
| 流程阶段/进度 | 状态链 (#15) | 步骤指示器 (#20) | 第三幕 |
| 步骤引导 | 步骤指示器 (#20) | 状态链 (#15) | 第一幕 |

#### 象限四：引用与强调（观点 → 高亮）

| 内容场景 | 推荐组件 | 备选 | 适合的一幕 |
|---|---|---|---|
| 人物引言/文献引用 | 引用/引文卡片 (#13) | 提示框 (#18) | 第二/三幕 |
| 重要提示/警告信息 | 提示框/告警条 (#18) | 引用卡片 (#13) | 第二幕 |
| 关键词/分类展示 | 标签/徽章组 (#17) | — | 封面/结尾 |
| 扩展阅读/术语详解 | 信息面板 (#21) | 折叠分步 (#8) / Popover 提示 (#25d) | 第三幕 |
| 术语即时弹出解释 | Popover 提示 (#25d) | 信息面板 (#21) | 各幕 |

#### 象限五：视觉对比（图 → 交互式查看）

| 内容场景 | 推荐组件 | 备选 | 适合的一幕 |
|---|---|---|---|
| 前后效果对比（图） | 图片对比滑块 (#10) | 标注式图片 (#14) | 第三幕 |
| 参与者介绍 | 角色卡片 (#2) | 数据卡片 (#12) | 第一幕 |
| 全屏放大查看 | 全屏模态/灯箱 (#23) | 原生模态 (#25b) | 第二幕 |
| 图片多张轮播 | CSS 幻灯片 (#25c) | 全屏模态 (#23) | 第二幕 |
| 词条/术语弹出解释 | Popover 提示 (#25d) | 信息面板 (#21) | 各幕 |

#### 象限六：零 JS 轻量方案（无需 JS 的场景）

| 内容场景 | 推荐组件 | 适合的一幕 |
|---|---|---|
| 无 JS 的折叠内容 | 原生折叠 (#25a) | 各幕 |
| 无 JS 的模态框 | 原生模态 (#25b) | 第二幕 |
| 无 JS 的卡片轮播 | CSS 幻灯片 (#25c) | 第二幕 |
| 无 JS 的弹出提示 | Popover 提示 (#25d) | 各幕 |

#### 三幕选型组合示例

| 课的类型 | 第一幕（背景） | 第二幕（核心） | 第三幕（收束） |
|---|---|---|---|
| 金融危机课 | SVG 流程图 (#1) + 折线图 (#26c) | 交互式时间线 (#11) + 数据卡片 (#12) + 引文卡片 (#13) | 对比表 (#22) + 信息面板 (#21) |
| 政策分析课 | 状态链 (#15) + 柱状图 (#26a) | Tab 面板 (#9) + 热力图 (#19) + 告警条 (#18) | 饼图 (#26b) + 对比表增强版 (#22) |
| 人物/事件课 | 角色卡片 (#2) | 交互式时间线 (#11) + 标注图片 (#14) + 引文卡片 (#13) | CSS 时间线 (#3) + 提示框 (#18) |
| 概念讲解课 | 折叠分步 (#8) + SVG 流程图 (#1) | Tab 面板 (#9) + 数据卡片 (#12) + 数值动画 (#16) | 信息面板 (#21) + 标签组 (#17) |
| 技术/产品课 | 原生折叠 (#25a) + 幻灯片 (#25c) | 标注图片 (#14) + 柱状图 (#26a) + Popover (#25d) | 原生模态 (#25b) + 对比表 (#22) |
| 网络攻防课 | SVG 流程图 (#1) + 告警条 (#18) | 交互式时间线 (#11) + 热力图 (#19) + 数据卡片 (#12) + 数值动画 (#16) | 折叠分步 (#8) + 对比表 (#22) + 标签组 (#17) |
| 商业案例课 | 角色卡片 (#2) + 柱状图 (#26a) | 对比表 (#22) + 饼图 (#26b) + 引文卡片 (#13) | 信息面板 (#21) + 状态链 (#15) + 标签组 (#17) |
| 文学/历史课 | 交互式时间线 (#11) + 角色卡片 (#2) | 标注图片 (#14) + 引文卡片 (#13) + 原生折叠 (#25a) | CSS 时间线 (#3) + 提示框 (#18) + 标签组 (#17) |
| 社会议题课 | SVG 流程图 (#1) + 数据卡片 (#12) + 数值动画 (#16) | Tab 面板 (#9) + 折线图 (#26c) + 告警条 (#18) + 引文卡片 (#13) | 对比表 (#22) + 信息面板 (#21) + 标签组 (#17) |
| 自然/医学课 | SVG 流程图 (#1) + 折叠分步 (#8) | 热力图 (#19) + 柱状图 (#26a) + 堆叠图 (#26d) + 标注图片 (#14) | Popover (#25d) + 幻灯片 (#25c) + 标签组 (#17) |

## 可选页面类型（来自 html-ppt 的布局概念）

在纵向滚读课程中，以下特殊页可以打破单调的"标题→段落→图→标题"节奏：

### 封面页（Cover）

课程开始时，在 `<p class="lesson-meta">` 之前插入：

```html
<div class="cover-page">
  <div class="cover-badge">第 N 课</div>
  <h1 style="margin-top:0.5em;">主标题</h1>
  <p class="cover-subtitle">一句话副标题——本课的核心问题或结论</p>
  <p class="cover-hook">一个吸引人的引子，2-3 句话</p>
</div>
```

```css
.cover-page { text-align: center; padding: 4rem 1rem; margin-bottom: 2rem; border-bottom: 2px solid var(--accent); }
.cover-badge { display: inline-block; padding: 0.2em 1em; background: var(--accent); color: #fff; border-radius: 3px; font-size: 0.85rem; letter-spacing: 0.05em; margin-bottom: 1em; }
.cover-subtitle { font-size: 1.1rem; color: #888; margin-top: 0.5em; }
.cover-hook { font-size: 0.95rem; color: #666; margin-top: 1em; font-style: italic; }
```

### 章节分隔页（Section Divider）

在三幕叙事之间插入，标记叙事阶段的切换：

```html
<div class="section-divider">
  <span class="divider-num">第一幕</span>
  <h2>设置矛盾</h2>
  <p>这一部分将讨论……</p>
</div>
```

```css
.section-divider { text-align: center; padding: 3rem 1rem; margin: 3rem 0; background: var(--bg); border-top: 1px solid #e0ddd8; border-bottom: 1px solid #e0ddd8; }
.divider-num { display: inline-block; padding: 0.1em 0.8em; background: var(--accent); color: #fff; border-radius: 3px; font-size: 0.8rem; letter-spacing: 0.05em; margin-bottom: 0.5em; }
.section-divider h2 { border-bottom: none; margin-top: 0.3em; }
```

### 总结页（Summary Cards）

课程结束时、测验前插入，用卡片形式总结关键洞察：

```html
<div class="summary-cards">
  <div class="summary-card"><span class="summary-icon">💡</span><strong>核心洞察 1</strong><p>一句话</p></div>
  <div class="summary-card"><span class="summary-icon">🔗</span><strong>与上一课的联系</strong><p>一句话</p></div>
  <div class="summary-card"><span class="summary-icon">❓</span><strong>开放问题</strong><p>一句话</p></div>
</div>
```

```css
.summary-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 2rem 0; }
.summary-card { background: #fff; border: 1px solid #e0ddd8; border-radius: 8px; padding: 1.2rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
.summary-icon { font-size: 1.5rem; display: block; margin-bottom: 0.3em; }
```

使用规则：
- **封面页**：每课必须使用（替换当前课程开头的 info-box 开场）
- **章节分隔页**：三幕叙事时使用，放在第一幕和第二幕之间、第二幕和第三幕之间
- **总结页**：长篇课程（>3000 字）使用，短课可跳过

## 课程制作工作流

```
Step 0: 需求拷问
  - 使用 `grill-me` skill 对用户进行需求拷问，澄清：
    · 课程主题与目标受众（谁学、为什么学）
    · 核心叙事矛盾（三幕中"冲突"是什么）
    · 预期数据/数字（有哪些可量化的内容可可视化）
    · 参考与风格偏好（是否有品牌色/参考课程/审美方向）
  - 🔴 未经过 grill-me 拷问不得开始 Step 1。拷问后输出一行 "设计读法" 确认方向
  - 🛑 STOP：等待用户确认设计读法后再进入 Step 1

Step 1: 确定叙事框架（三幕）
  - 第一幕：矛盾/背景（1-2段）
  - 第二幕：事件/危机（核心内容）
  - 第三幕：转折/遗产（收束+跨课连接）
  - 🔴 输出：三段式大纲（每幕 2-3 句话），展示给用户确认
  - 🛑 STOP：用户确认大纲后再进入 Step 2

Step 2: 设计视觉组件
  - 从上方索引表按内容脉络选择组件：第一幕 1-2 个、第二幕 2-3 个、第三幕 1-2 个，总量建议 4-7 个
  - 打开对应的 components/NN-name.md 读取完整 HTML/CSS/JS
  - 🔴 输出：组件选择清单（组件名+编号+所属幕），展示给用户确认
  - 🛑 STOP：用户确认组件清单后再进入 Step 3
  - 🔴 每个 SVG 创建后立即验证：`python -c "import xml.etree.ElementTree as ET; ET.parse('path.svg')"`
  - **SVG 需同时保存为磁盘文件和内联到 HTML**：`lessons/svg/NNNN-slug.svg` 保留为独立文件，同时将 SVG 内容复制到 HTML 中用 `<figure class="svg-fig">` 包裹内联

Step 3: 写 HTML
  - 复制 `templates/lesson-starter.html` 作为新课程骨架，填入标题/内容
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
  - 各组件 JS 代码合并到课程末尾 `<script>` 块中（放在 PPT 增强 JS 之前或之后均可）
  - 每幕之间的"视觉停顿"法则：每 2-3 段文本后插入一个视觉元素
  - 阅读节奏：核心内容用交互式组件（Tab/折叠/时间线），数据用卡片/条形图/热力图，引用用引文卡片，提示用告警条
  - **课程间互相链接使用相对路径**：如 `<a href="NNNN-slug.html">`，不要加前导 `/` 或完整 URL

Step 4: 验证
  - 浏览器打开 .html 检查渲染
  - SVG 验证：python -c "import xml.etree.ElementTree as ET; ET.parse('path.svg')"
  - 交叉链接检查（glossary 路径、课程链接）——确认所有跨课链接为相对路径
  - 测验 5 题，每题 3 个选项
  - 🔴 任一验证失败 → 定位问题 → 修复后重跑验证 → 全部通过后再继续

Step 5: 配套产出
  - 调用 base `teach` skill 的 learning-record 模板，生成课程学习记录（含课程名、日期、关键概念列表）
  - EPUB 重建：如本课程隶属于某个系列（已有 `.epub` 文件），用 `teach` skill 的 EPUB 工具重新打包
  - 🔴 课程间链接验证：打开所有 `<a href="NNNN-slug.html">` 确认目标文件存在
  - 🛑 STOP：用户确认配套产出无误后再进入 SPA 集成

Step 6: SPA 集成
  - 将生成的 `lessons/NNN-slug.html` 内容内联到 `index.html`：
    · 在 `index.html` 的 `</body>` 前插入 `<section class="lesson-view" id="lesson-NNN">...</section>`
    · 确保每课一个独立的 `<section>`，用 `id="lesson-NNN"` 索引
  - 🔴 验证：`id="lesson-NNN"` 在 `index.html` 中不与其他课程冲突
  - SPA 切换 JS 已存在于 `index.html` 中，通过 `id` 控制显示/隐藏
  - 保留 `lessons/NNN-slug.html` 独立文件，供非 SPA 场景直接打开

Step 7: 知识图谱更新
  - 在 `kg-yuecai.html` 的 `graphData.nodes[]` 和 `links[]` 中追加新课程节点
  - 提取课程中的关键概念/术语作为节点，课程间的链接作为边
  - 🔴 验证：新节点 id 不与已有节点重复
```

## 失败模式与异常处理

| 触发条件 | 一线修复 | 仍失败兜底 |
|---|---|---|
| SVG 无法正确显示（浏览器空白） | 检查 SVG XML 语法；检查 viewBox 与 width/height 比例一致 | 降级为纯 CSS 流程图或外部链接 |
| SVG 内联到 HTML 后排版错乱 | 检查 `<figure class="svg-fig">` 容器：`svg { max-width: 100%; height: auto; }` | 降级为 `<img src="NNNN-slug.svg">` 外部引用 |
| 条形图 width 导致数据溢出容器 | 检查所有 `bar-fill` 的 width 值 ≤ 100% | 改用 `text-overflow: ellipsis` |
| CSS 时间线在窄屏上跑偏 | 确保 `.tl-dot` 使用 `position: absolute` + `left` 固定 | 转为水平折叠式 |
| 角色卡片中文显示乱码 | 确认 SVG 中 font-family 包含中文字体 | 用内联 font-family |
| 测验 `<button>` 的 `data-correct` 属性写反 | 用 `grep 'data-correct="true"'` 确认每题恰好 1 个 | 手动核验 |
| fireworks-tech-graph 不可用时 | 手动编写 SVG 或修改已有模板 | 用 CSS 伪元素制作简化版 |
| SVG 中文字体不渲染 | 确认 `<style>` 内 font-family 包含中文字体 | 在 `<style>` 内层加 text font-family |
| IntersectionObserver 不触发动画 | 元素可能在首屏内 | 首屏前 2 个视觉元素不加 `data-anim` |
| 主题切换后 h2 下划线颜色不变 | CSS 中使用固定色而非 `var(--accent)` | 确保使用 `border-bottom-color: var(--accent)` |
| SVG viewBox 比例不匹配 width/height | 图片被不等比例拉伸 | 确保 viewBox 宽高比 = width/height 比 |
| 折叠组件 `height` 从 `auto` 过渡 | CSS transition 无效 | JS 中先测量 scrollHeight 再设 px，恢复 auto |
| SPA 中课程 `id` 冲突 | 两个 `<section>` 用了相同 `id` | 使用 `id="lesson-NNN"` 格式，NNN 为课程编号 |
| `index.html` 中课程区块未显示 | `<section>` 插在了 `<body>` 外部 | 确认在 `</body>` 前插入，不是 `</html>` 之后 |
| 组件特定的其他问题 | 见对应 `components/NN-name.md` 中的降级说明 | — |

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
| 1 | 课程中同时使用超过 8 种组件 | 视觉密度过高，读者疲劳 | 每课控制在 4-7 个，精选与内容匹配的 |
| 2 | SVG 流程图用纯红色表示所有环节 | 失去颜色语义 | 蓝=正常，橙=触发，红=崩溃，绿=救助 |
| 3 | 条形图 width 用绝对数值 | 超出容器 | 归一化后按百分比 |
| 4 | 角色卡片中放超过 4 行文本 | 视觉重量失衡 | 最多 3 行，单行 ≤25 字 |
| 5 | CSS 时间轴 < 5 个事件 | 视觉空洞 | 事件 < 5 用列表 |
| 6 | 混用 ASCII 图和 SVG 图 | 风格不统一 | 全部 SVG 或全部 ASCII |
| 7 | SVG 浅色盒用白字 | 不可读 | 深色背景用白字，浅色背景用深字 |
| 8 | 课程没有主题切换和键盘导航 | 缺少 PPT 质感 | 每个课程均加入 T 键和 ← → 键 |
| 9 | 连续超过 4 段文本无视觉停顿 | 读者疲劳 | 每 1-2 段间插入一个视觉组件 |
| 10 | 饼图展示时间序列、折线图展示静态分类 | 图表类型与数据性质错位 | 时间序列→折线图，静态比例→饼图，对比→柱状图 |
| 11 | 编造不存在的统计数据或引文来源 | 损害课程可信度 | 无可靠数据时用模拟数据并标注 `mock-data` 类 |
| 12 | 硬编码颜色覆盖 theme CSS 变量 | 主题切换后颜色不变 | 颜色值统一使用 `var(--accent)`、`var(--border)` 等 CSS 变量 |
| 13 | 使用 emoji 作为结构图标（导航、工具栏、目录） | 风格不统一，窄屏错位 | 使用对应的 SVG 图标组件 |

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

验证自动化：`python scripts/validate-lesson.py lessons/NNNN-slug.html` — 自动检查 SVG 路径/XML 有效性/颜色对比度、quiz 正确数/完整度、h1 数量、data-anim 语法、容器宽度、相对路径、PPT JS（主题+导航）存在性。
