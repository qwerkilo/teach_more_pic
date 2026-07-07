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

Use alongside the `teach` skill (已内嵌见 `.opencode/skills/teach/`)。The base `teach` handles workspace structure, mission, and learning records; this skill handles **visual components** inside each lesson.

## 前置条件

- 已内嵌：`fireworks-tech-graph`、`grill-me`、`teach`、`knowledge-graph` 四个 skill（见 `.opencode/skills/`）
- 离线包：本 skill 的 `libs/` 下已包含 echarts.min.js、echarts-gl.min.js、three.min.js（UMD 回退）、three.module.js（ESM 主入口）、d3.min.js、d3-sankey.min.js、magicui-effects.css（13 种零依赖装饰效果），课程创建时完整复制到目标项目即可
- Three.js WebGPU/TSL 需通过 `<script type="importmap">` 导入，详见 `25-Three.js 3D组件.md`

- `cairosvg` (可选, `pip install cairosvg`) — for SVG → PNG export
- Magic UI CSS 效果：`libs/magicui-effects.css` 共享 13 种零依赖装饰效果（shiny-text/noise/dot/grid/meteors/border-glow/glare-hover/gradient-text/blur/neon-card/spotlight-card/interactive-btn/typing-cursor），所有模板和示例均已引用

## 🔴 重要纪律（必须遵守）

- **所有课程必须从 `templates/lesson-starter.html` 复制作为基础**。禁止从零生成 HTML 结构。
- 保留模板的完整 CSS 变量系统（`:root` + 20 个 `[data-theme]`）、工具栏（主题/语言/目录）、键盘快捷键（T/L/←→）。
- 只修改以下部分：封面页标题/描述、三幕正文内容、组件 CSS/HTML/JS 插入标记处、测验内容。
- 视觉组件（折叠分步、时间线、图表等）在模板预留的 `<!-- INSERT: 组件 HTML/CSS/JS -->` 注释处追加，不删除任何已有功能。
- 违反此纪律的课程视为不合格，需重做。

## 页面类型

| 类型 | 必选？ | 视觉亮点 |
|---|---|---|
| 封面页 | ✅ 每课必须 | shiny-text 光泽标题、药丸 badge |
| 章节分隔页 | ✅ 三幕必须 | 圆形编号 + 顶部装饰线 |
| 总结卡片 | ✅ 每课必须 | SVG 矢量图标、hover 微上浮 |
| 全宽引文页 | 可选 | 左侧 accent 竖线、40vh 高度 |
| 关键数字页 | 可选 | 3rem 超大数字 + accent 色 |
| 信息面板侧边栏 | 可选 | 右浮动、窄屏自动降级 |

完整代码见 `references/page-types.md`。

## 课程制作工作流

```
Step 0: 需求拷问
  - 使用 `grill-me` skill（已内嵌 `.opencode/skills/grill-me/`）对用户进行需求拷问，澄清：
     · 课程主题与目标受众（谁学、为什么学）
     · 核心叙事矛盾（三幕中"冲突"是什么）
     · 预期数据/数字（有哪些可量化的内容可可视化）
     · 参考与风格偏好（是否有品牌色/参考课程/审美方向）
     · **是否希望大量使用 3D 类型组件**（Three.js #25 / ECharts GL #28 / D3.js 3D #27）——若回答"是"，三幕中尽可能多地使用 3D 组件
   - 🔴 未经过 grill-me 拷问不得开始 Step 1。拷问后输出一串 "设计读法" 确认方向，格式：`主题 → NNNN-slug.html · 三幕：矛盾/危机/转折 · 组件数 最少 6`
   - 🎯 **自适应节奏**：如果用户回复含"直接干/少问/快速/fast/go"等关键字，标记 `fast_pace=true`，跳过 Step 1/2/5/6/7 的所有 STOP，直接全量输出至 Step 4 验证。
  - 🛑 STOP（默认）：等待用户回复 "确认" 或 "可以，继续" 后再进入 Step 1。用户未明确确认不得推进。

Step 1: 确定叙事框架（三幕）
  - 第一幕：矛盾/背景（1-2段）
  - 第二幕：事件/危机（核心内容）
  - 第三幕：转折/遗产（收束+跨课连接）
  - 🔴 输出：三段式大纲（每幕 2-3 句话），展示给用户确认
  - 🛑 STOP（默认）：用户回复 "确认" 或 "可以" 后再进入 Step 2。用户若提出修改意见 → 修改后再次展示 → 重复直到确认。若 `fast_pace=true` 则跳过。

Step 2: 设计视觉组件
  - 从上方索引表按内容脉络选择组件：第一幕 2+ 个、第二幕 2+ 个、第三幕 2+ 个，**总量最少 6 个**（含标签组 #17）
  - 打开对应的 components/NN-name.md 读取完整 HTML/CSS/JS
  - 🔴 输出：组件选择清单（组件名+编号+所属幕），展示给用户确认
  - 🛑 STOP（默认）：用户回复 "确认" 后再进入 Step 3。用户想增减组件 → 调整清单 → 再次展示确认。若 `fast_pace=true` 则跳过。
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
  - 调用 `teach` skill（已内嵌 `.opencode/skills/teach/`）的 learning-record 模板，生成课程学习记录（含课程名、日期、关键概念列表）
  - EPUB 重建：如本课程隶属于某个系列（已有 `.epub` 文件），用 `teach` skill 的 EPUB 工具重新打包
  - 🔴 课程间链接验证：打开所有 `<a href="NNNN-slug.html">` 确认目标文件存在
  - 🛑 STOP（默认）：用户确认配套产出无误后再进入 SPA 集成。若 `fast_pace=true` 则跳过。

Step 6: SPA 集成
  - 从 `templates/index-spa.html` 复制骨架作为 `index.html`，插入各课的
    `<section class="lesson-view" id="lesson-NNN">...</section>` 到注释标记处
  - 已有 SPA 则直接追加新 `<section class="lesson-view">` 到 `</body>` 前
  - 确保每课一个独立的 `<section>`，用 `id="lesson-NNN"` 索引
  - 🔴 验证：`id="lesson-NNN"` 在 `index.html` 中不与其他课程冲突
  - SPA 切换 JS 已存在于 `index.html` 中，通过 `id` 控制显示/隐藏
  - 保留 `lessons/NNN-slug.html` 独立文件，供非 SPA 场景直接打开
  - 🔴 将本 skill 的 `libs/` 下所有文件（echarts.min.js、echarts-gl.min.js、three.min.js、three.module.js、d3.min.js、d3-sankey.min.js）完整复制到目标项目的 `libs/` 目录，确保课程始终使用固定版本离线包
  - 🛑 STOP（默认）：确认 SPA 预览正常后再进入 Step 7。若 `fast_pace=true` 则跳过。

Step 7: 知识图谱更新
  - 新项目从 `templates/kg-starter.html` 复制到项目根目录为 `kg-项目名.html`；已有项目在已有 `kg-*.html` 中追加
  - 提取课程中的关键概念/术语作为节点，课程间的链接作为边
  - 节点名使用 `nameZh`/`nameEn` 双字段，图谱通过 L 键切换语言
  - 🔴 验证：新节点 id 不与已有节点重复
  - 🛑 STOP（默认）：确认图谱显示正确后再提交最终成果。若 `fast_pace=true` 则跳过。

Step 8: 本地 HTTP 服务器（可选）
  - 从 `templates/start-server.ps1` 复制到项目根目录
  - 运行 `powershell -ExecutionPolicy Bypass -File start-server.ps1`
  - 自动打开浏览器到 `index.html`（有 SPA 时）或第一课
  - 按 Q 键停止服务器
  - Python 内置 `http.server`，无需额外依赖
  - Linux/macOS：复制 `templates/start-server.sh`，运行 `bash start-server.sh`，后台静默运行（nohup），PID 写入 `.server.pid`；停止 `kill $(cat .server.pid) && rm .server.pid`
  - 🛑 STOP：全部完成后做最终完整性检查——课程可双击打开（file://）、SPA 路由正常、KG 图谱双语言切换正常、服务器一键启停正常
```

## 深入阅读

以下子 skill 可按需加载以获取详细参考：

| 子 skill | 路径 | 涵盖内容 |
|---|---|---|
| teach_more_pic-core | `.opencode/skills/teach_more_pic-core/` | 核心约定、叙事框架、完整工作流 |
| teach_more_pic-components | `.opencode/skills/teach_more_pic-components/` | 33 组件索引（含 5 个微交互）、使用规则、决策指南、折叠 JS 模式 |
| teach_more_pic-design | `.opencode/skills/teach_more_pic-design/` | 视觉纪律、写作风格、反模式、PPT JS 注意事项 |
| teach_more_pic-refs | `.opencode/skills/teach_more_pic-refs/` | 页面类型、文件速查、失败模式表 |

## 验证命令

```bash
python scripts/validate-lesson.py lessons/NNNN-slug.html
python -m pytest tests/ -v
python -c "import xml.etree.ElementTree as ET; ET.parse('path.svg')"
```
