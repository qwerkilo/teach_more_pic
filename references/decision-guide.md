# 组件选择决策指南

> 本文档是 `SKILL.md` 的参考附件。主工作流在 SKILL.md 中，此处只列选择矩阵。

**组件编号说明**：SKILL.md 组件索引表的编号（#1-33）是规范编号。磁盘文件编号（01-33）因历史重排与规范编号有偏移（#24 对应 `24-ECharts 交互式图表集.md`，跳转入口见 `components/24-ECharts-index.md`），引用时以组件索引表为准。

## 核心策略

```
内容 → 有可量化数据？→ Yes → ECharts/D3/Three 主视觉锚点 → 搭配 2-4 个轻量组件
                       → No  → 流程?→ SVG 流程 #1 / 折叠 #8
                               → 时序?→ 时间线 #3 #11 / 状态链 #15
                               → 对比?→ 对比表 #5 #22 / Tab #9
```

**铁律**：每课至少 1 个 ECharts/Three.js/D3.js 作为主视觉锚点 + 2-4 个轻量组件（卡片/折叠/告警条等）+ 零或多个 Magic UI 装饰效果。

**参考起点**：`examples/` 下 30 个独立示例可直接打开预览，`templates/` 下 4 个有效 SVG 模板（流程图/循环图/对比图/时间线）可作为 SVG 创作基底。

## 象限一：解释与拆解

| 场景 | 首选 | 备选 | 推荐幕 |
|------|------|------|--------|
| 复杂概念分步拆解 | 折叠分步 (#8) | 信息面板 (#21) | 一/三 |
| 多视角/多方案对比 | Tab 面板 (#9) | 对比表 (#22) | 二 |
| 资金/逻辑流向 | SVG 流程图 (#1) | 标注图片 (#14) | 一 |
| 零 JS 折叠/展开 | 原生折叠 (#26a) | — | 各幕 |

> 参考示例：`examples/flowchart-demo.html`、`examples/step-detail-demo.html`、`examples/tab-demo.html`

## 象限二：数据与统计

ECharts 4 子类型是数据可视化的首选引擎，D3.js 适合复杂自定义图表：

| 场景 | 首选 | 备选 | 推荐幕 |
|------|------|------|--------|
| 关键统计数据 | 数据卡片 (#12) + 数值动画 (#16) | CSS 条形图 (#4) | 二/三 |
| 分类数值对比 | **ECharts 柱状图 (#24a)** | CSS 条形图 (#4) | 二 |
| 占比/比例展示 | **ECharts 饼图 (#24b)** | 堆叠图 (#24d) | 二 |
| 趋势变化 | **ECharts 折线图 (#24c)** | 时间线 (#11) | 二 |
| 多维度构成 | **ECharts 堆叠图 (#24d)** | 对比表 (#22) | 二 |
| 二维密度矩阵 | 热力图 (#19) | 堆叠图 (#24d) | 二 |
| 关系网络/知识图谱 | **D3 力导向图 (#27a)** | SVG 流程图 (#1) | 一/二 |
| 多层层次占比 | **D3 旭日图 (#27b)** | 饼图 (#24b) | 二 |
| 流量/转化路径 | **D3 桑基图 (#27c)** | 状态链 (#15) | 二 |
| 三维空间分布 | **ECharts GL 3D 散点 (#28b)** | 热力图 (#19) | 二/三 |
| 三维分簇对比 | **ECharts GL 3D 柱状 (#28a)** | 堆叠图 (#24d) | 二 |
| 地理数据全球分布 | **ECharts GL 地球 (#28c)** | 无 | 二 |
| 单组数据对比 | CSS 条形图 (#4) | 柱状图 (#24a) | 二 |
| 多方案多维度对比 | 对比表增强版 (#22) | Tab 面板 (#9) | 三 |

> 参考示例：`examples/bar-chart-demo.html`、`examples/echarts-demo.html`、`examples/d3-demo.html`、`examples/heatmap-demo.html`、`examples/cmp-table-basic-demo.html`、`examples/cmp-table-demo.html`

## 象限三：时间与过程

| 场景 | 首选 | 备选 | 推荐幕 |
|------|------|------|--------|
| 事件序列（≤4 个） | CSS 时间线 (#3) | 编号列表 | 一 |
| 事件序列（5+ 个） | 交互式时间线 (#11) | 状态链 (#15) | 二 |
| 流程阶段/进度 | 状态链 (#15) | 步骤指示器 (#20) | 三 |
| 步骤引导 | 步骤指示器 (#20) | 状态链 (#15) | 一 |

> 参考示例：`examples/timeline-css-demo.html`、`examples/timeline-demo.html`、`examples/status-chain-demo.html`、`examples/step-indicator-demo.html`

## 象限四：引用与强调

| 场景 | 首选 | 备选 | 推荐幕 |
|------|------|------|--------|
| 人物引言/文献引用 | 引文卡片 (#13) | 提示框 (#18) | 二/三 |
| 警告/提示 | 告警条 (#18) | 引文卡片 (#13) | 二 |
| 关键词/分类展示 | 标签组 (#17) | — | 封面/结尾 |
| 术语详解 | 信息面板 (#21) | 折叠分步 (#8) | 三 |
| 即时术语弹出 | Popover (#26d) | 信息面板 (#21) | 各幕 |

## 象限五：视觉对比

| 场景 | 首选 | 备选 | 推荐幕 |
|------|------|------|--------|
| 前后效果对比 | 图片对比滑块 (#10) | 标注图片 (#14) | 三 |
| 参与者介绍 | 角色卡片 (#2) | 数据卡片 (#12) | 一 |
| 全屏放大查看 | 灯箱 (#23) | 原生模态 (#26b) | 二 |
| 图片轮播 | CSS 幻灯片 (#26c) | 灯箱 (#23) | 二 |
| 3D 数据可视化 | **Three.js (#25)** / **ECharts GL (#28)** | 柱状图 (#24a) | 二 |

## 象限六：零 JS 轻量

| 场景 | 组件 |
|------|------|
| 无 JS 折叠 | 原生折叠 (#26a) |
| 无 JS 模态 | 原生模态 (#26b) |
| 无 JS 轮播 | CSS 幻灯片 (#26c) |
| 无 JS 弹出 | Popover (#26d) |

## 象限七：Magic UI 装饰

`libs/magicui-effects.css` 提供零依赖纯 CSS 装饰。用法：在目标元素上加 class 名即可，无需额外 JS：

| 效果 | CSS 类 | 用法 | 适合位置 |
|------|--------|------|---------|
| 光泽扫光 | `.shiny-text` | `<h1 class="shiny-text">标题</h1>` | 封面标题、badge |
| 噪点纹理 | `.noise-overlay` | `<div class="noise-overlay">` | 封面、工具栏背景 |
| 圆点网格 | `.dot-bg` | `<div class="dot-bg">` | 章节分隔背景 |
| 直线网格 | `.grid-bg` | `<div class="grid-bg">` | 图表背景区 |
| 流星雨 | `.meteors-container` + JS | 模板已内置（15 个 meteor div） | 封面动态装饰 |
| 边框发光 | `.border-glow` | `<div class="border-glow">卡片</div>` | 数据卡片、图例 |
| 辉光悬停 | `.glare-hover` | `<div class="glare-hover">卡片</div>` | 任意卡片 hover |
| 渐变文字 | `.gradient-text` | `<span class="gradient-text">文字</span>` | 标题强调 |
| 模糊淡入 | `data-anim="blur"` | `<p data-anim="blur">文本</p>` | 正文段落动画 |
| 霓虹卡片 | `.neon-card` | `<div class="neon-card">卡片</div>` | 强调数据卡片 |
| 聚光灯追踪 | `.spotlight-card` | `<div class="spotlight-card">` + JS | 首屏焦点卡片 |
| 点击波纹 | `.interactive-btn` | `<button class="interactive-btn">` | 按钮、选项 |
| 打字光标 | `.typing-cursor` | `<span class="typing-cursor">文字</span>` | 引文、关键句 |

**组合技巧**：多个效果可以叠加——`<h1 class="shiny-text gradient-text">` 同时有扫光 + 渐变。

## 跨库组合策略

ECharts、D3.js、Three.js 不互斥，可按需组合发挥各自优势：

| 模式 | 数据层 | 渲染层 | 典型场景 |
|------|--------|--------|---------|
| D3 布局 → Three 渲染 | D3 计算力导向/层次/地理投影 | Three.js 渲染 3D 场景 | 3D 力导向网络、3D 旭日图 |
| D3 数据 → ECharts | D3 聚合/筛选/排序 | ECharts 渲染标准图表 | 大数据量降采样后喂 ECharts |
| Three + ECharts 同屏 | ECharts 2D 趋势 | Three.js 3D 空间分布 | 金融仪表盘 = 折线图 + 3D 网络 |
| D3 纯数据处理 | D3 做格式转换、比例尺映射 | CSS/HTML 消费数据 | d3-scale 生成色阶 → CSS 热力图 |

**典型组合**：金融课中 D3 计算相关性矩阵 → Three 渲染 3D 网络；同时 ECharts 折线图展示历史走势。

### 跨库示例索引

| 文件 | 组合方式 | 说明 |
|------|---------|------|
| `examples/echarts-gl-demo.html` | ECharts GL 3D 柱状 + 3D 散点 | file:// 兼容，autoRotate + cluster 颜色编码 |
| `examples/echarts-gl-map-demo.html` | ECharts GL 3D 广东地图 + scatter3D 标注 | GeoJSON DataV + 21 地市 GDP 数据，visualMap 颜色编码 |
| `examples/d3-three-demo.html` | D3 力导向布局 → Three.js 3D 渲染 | 11 节点金融网络，鼠标 hover 高亮 + Canvas Sprite 文字标签 |
| `examples/hybrid-d3-three-echarts.html` | D3→Three + D3→ECharts + Three+ECharts | 3 个独立示例同页展示所有组合模式 |
| `examples/three-demo.html` | Three.js r185 WebGPU + importmap CDN | WebGPU 优先/WEBGL 降级，Sprite 标签 + hover tooltip |

## 三幕选型速查

| 课类型 | 第一幕（背景） | 第二幕（核心） | 第三幕（收束） |
|--------|--------------|--------------|--------------|
| 金融危机 | SVG 流程 #1 + 时间线 #3 | **折线图 #24c** + 时间线 #11 + 数据卡片 #12 | 对比表 #22 + 面板 #21 |
| 政策分析 | 状态链 #15 + **柱状图 #24a** | Tab #9 + 热力图 #19 + 告警条 #18 | **饼图 #24b** + 对比表 #22 |
| 人物/事件 | 角色卡片 #2 | 时间线 #11 + 标注 #14 + 引文 #13 | CSS 时间线 #3 + **Three #25** |
| 概念讲解 | 折叠 #8 + SVG 流程 #1 | Tab #9 + 数据卡片 #12 + 数值动画 #16 | 面板 #21 + 标签 #17 |
| 商业案例 | 角色卡片 #2 + 数据卡片 #12 | 对比表 #22 + **堆叠图 #24d** + 引文 #13 | 面板 #21 + 标签 #17 |
| 社会议题 | SVG 流程 #1 + **柱状图 #24a** + 数值动画 #16 | Tab #9 + 告警条 #18 + 引文 #13 | **Three #25** + 面板 #21 + 标签 #17 |
| 自然/医学 | SVG 流程 #1 + 折叠 #8 | 热力图 #19 + **Three #25** + 幻灯片 #26c | Popover #26d + **饼图 #24b** |
