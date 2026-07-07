# teach_more_pic — 视觉增强课程制作

**全技能内嵌，零外部依赖。** 本体已包含 `teach`、`grill-me`、`fireworks-tech-graph`、`knowledge-graph` 四个前置 skill。

## Recent Fixes

- **2026-07-07** 数值滚动动画 (#16) 修复 IntersectionObserverEntry 误用 `.dataset` 而非 `entry.target.dataset` 的 bug，涉及 `components/16-数值滚动动画.md` + `templates/lesson-starter.html`
- **2026-07-07** CDN 优先 + 离线降级策略：第三方库使用 jsDelivr CDN，`libs/` 为离线 fallback

## 能力

**33 个视觉组件**（完整索引见 SKILL.md）：

- **#1-7 核心**：SVG 流程图 / 角色卡片 / CSS 时间线 / CSS 条形图 / 对比表 / SVG 容器 / PPT 质感（主题切换 + 语言切换 + 滚动动画 + 键盘导航 + 目录）
- **#8-14 交互式**：折叠分步详解 / Tab 切换面板 / 图片对比滑块 / 交互式时间线 / 数据卡片网格 / 引文卡片 / 标注式图片
- **#15-28 数据与辅助**：状态链 / 数值滚动动画 / 标签徽章组 / 告警条 / 热力图 / 步骤指示器 / 信息面板 / 对比表增强版 / 灯箱 / ECharts / Three.js 3D / D3.js / ECharts GL / 现代浏览器 API
- **#29-33 微交互**：走马灯轮播 / 打字机效果 / 视差滚动 / 浮动提醒 / 计数器徽章
- **20 品牌主题** — 22 个 CSS 变量，`var(--accent/border/surface/...)` 自动跟随
- **自适应节奏** — 回复"直接干"即可跳过中间确认步骤直达验证

## 使用方法

```bash
Skills: teach_more_pic  # 单一 skill，无需安装外部依赖
```

```bash
python scripts/validate-lesson.py lessons/NNNN-slug.html
python -m pytest tests/ -v
powershell -ExecutionPolicy Bypass -File scripts/run-tests.ps1
```

## 课程制作流程

1. 运行 `grill-me` skill 澄清需求（主题/受众/数据/风格）
2. 从 `templates/lesson-starter.html` 复制骨架
3. 从组件索引表选最少 6 个组件（含标签组 #17）
4. 从 `components/NN-name.md` 复制代码合并到模板
5. 运行 `python scripts/validate-lesson.py` 验证
6. SPA 集成：`templates/index-spa.html` → `index.html`
7. 知识图谱：`templates/kg-starter.html` → `kg-项目名.html`

## 项目结构

```
├── SKILL.md                          ← 入口 + 工作流
├── .opencode/skills/                 ← 内嵌子 skill
│   ├── teach_more_pic-core/          ← 核心工作流
│   ├── teach_more_pic-components/    ← 33 组件索引
│   ├── teach_more_pic-design/        ← 视觉纪律
│   ├── teach_more_pic-refs/          ← 页面类型 + 失败模式
│   ├── grill-me/ + grilling/         ← 需求拷问
│   ├── fireworks-tech-graph/         ← SVG 流程图
│   ├── teach/                        ← 学习记录
│   └── knowledge-graph/              ← 知识图谱
├── components/                       28→33 个组件文档
├── examples/                         31 个组件示例
├── templates/                        9 个模板
├── scripts/                          验证器（21 项检查）
├── tests/                            pytest（109 项）
├── libs/                             离线包（echarts/three/d3）
├── references/                       决策指南 + 页面类型
└── theme/                            19 品牌 DESIGN.md
```

## 验证

| 指标 | 值 |
|---|---|
| 组件数 | 33（21 检查 + 5 微交互） |
| 验证检查 | 21 项（含 meta/封面/总结卡片） |
| pytest | 109 项，99+% 通过 |
| 示例文件 | 31 个，全部通过验证 |
| 外部依赖 | 0（全部内嵌） |
