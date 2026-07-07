# teach_more_pic — 视觉增强课程制作

**全技能内嵌，零外部依赖。** 本体已包含 `teach`、`grill-me`、`fireworks-tech-graph`、`knowledge-graph` 四个前置 skill（见 `.opencode/skills/`）。

## 能力

**33 个视觉组件**（完整索引见 SKILL.md）：

- **#1-7 核心**：SVG 流程图 / 角色卡片 / CSS 时间线 / CSS 条形图 / 对比表 / SVG 容器 / PPT 质感（主题切换 + 语言切换 + 滚动动画 + 键盘导航 + 目录）
- **#8-14 交互式**：折叠分步详解 / Tab 切换面板 / 图片对比滑块 / 交互式时间线 / 数据卡片网格 / 引文卡片 / 标注式图片
- **#15-28 数据与辅助**：状态链 / 数值滚动动画 / **标签徽章组**（每课必须，带 `#` 前缀） / 告警条 / 热力图 / 步骤指示器 / 信息面板 / 对比表增强版 / 灯箱 / **ECharts 交互式图表**（柱状/饼/折线/堆叠，需 `libs/echarts.min.js`） / **Three.js 3D**（3D 可视化，需 `libs/three.min.js`，含 Sprite 文字标签） / **D3.js 自定义图表**（力导向图/旭日图/桑基图，需 `libs/d3.min.js` + `d3-sankey.min.js`） / **ECharts GL 3D**（3D 柱状/散点/地球，需 `libs/echarts-gl.min.js`） / 现代浏览器 API（原生折叠/模态/幻灯片/Popover）
- **20 品牌主题** — 22 个 CSS 变量，`var(--accent/border/surface/...)` 自动跟随
- **主题切换动画** — 0.35s 平滑过渡，`prefers-reduced-motion` 自动禁用

## 最近更新

**质量改进**（23 项 bug 修复，覆盖 P0-P2）：

- **P0 必修**：测验错答高亮按语言过滤 / KG tooltip/legend XSS 风险消除 / `<html lang>` 随 L 键切换同步 / KG 嵌套大括号解析 (``\{(.+?)\}`` 正则改 `_extract_brace_blocks` brace-counting)
- **P1 应修**：验证脚本 `check_inline_svg` 混合场景漏检、`check_container_width` 死代码、popover 检测无效 三处盲点全部修复 / `data-anim="blur"` 降级残影 / 模板标题占位符 / SD/tab 缺 `aria-*` 属性 / `dir()` 变量存在检查改 `locals().get()` / `is_kg` 与 `has_graphdata` 检测条件对齐
- **P2 可选**：spotlight mousemove 改 RAF 节流 / `buildTOC` 跨 try 块作用域 / 重复 `--h1-size` 与 body 声明清理 / meta + og + favicon + 打印样式 / SPA 卡片改事件委托 / inline SVG XML 语法校验 / 109 pytest 测试覆盖

详见 git history。`python -m pytest tests/ -q` 109 PASS，3 个核心模板验证零回归。

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

# 运行验证脚本单元测试（pytest）
python -m pytest tests/ -v

# JS 语法检查
node -e "new Function(require('fs').readFileSync('file','r',encoding='utf-8').match(/<script>([\\s\\S]*?)<\\/script>/)[1])"

# SVG XML 检查
python -c "import xml.etree.ElementTree as ET; ET.parse('path.svg')"
```

## 课程制作流程

0. **使用 `grill-me` skill 拷问需求** — 必问"是否使用 3D 组件" + 澄清主题/受众/叙事矛盾/数据/风格偏好/双语需求，确认后再继续
1. 复制 `templates/lesson-starter.html` 作为新课程骨架 → 确认三幕大纲
2. 从 SKILL.md 组件索引表选最少 6 个组件（含标签组 #17），使用决策指南匹配 → 确认组件清单
3. 打开对应 `components/NN-name.md`，复制 ````html`/```css`/```js` 合并到模板中
4. SVG 保存为 `lessons/svg/NNNN-slug.svg`（磁盘文件）**并**内联到 HTML 中 `<figure class="svg-fig">` 包裹
5. **`libs/` 依赖**：先完整复制本 skill 的 `libs/` 下所有文件到目标项目的 `libs/`，确保离线包版本一致
6. 运行 `python scripts/validate-lesson.py lessons/NNNN-slug.html` 验证
7. SPA 集成：从 `templates/index-spa.html` 复制为 `index.html`，追加 `<section class="lesson-view" id="lesson-NNN">`
8. 知识图谱：新项目从 `templates/kg-starter.html` 复制到项目根目录为 `kg-项目名.html`（双语 `nameZh`/`nameEn` + L 键切换）；已有项目在已有 `kg-*.html` 中追加节点和关系
9. 本地 HTTP 服务器：从 `templates/start-server.ps1`（Windows）或 `start-server.sh`（Linux/macOS）复制到项目根目录，运行后自动打开浏览器

## 项目结构

```
├── SKILL.md               ← 唯一入口文档，所有规则在此
├── components/             各组件独立文件（28 个 .md），含 HTML/CSS/JS/降级说明
├── scripts/
│   ├── validate-lesson.py  课程验证脚本（18 项检查，含双语 + SPA + KG）
│   ├── test_validate.py    验证脚本单元测试（85 项旧测试，向后兼容）
│   └── run-tests.ps1       批量验证所有示例
├── examples/               组件用法示例（30 个 .html，含 D3→Three 专用示例、ECharts GL 示例、跨库混合）
├── libs/                   外部库（echarts.min.js、echarts-gl.min.js、three.min.js、three.module.js、d3.min.js、d3-sankey.min.js、guangdong.js、magicui-effects.css）
├── tests/                  pytest 单元测试（test_validate.py，99 项，推荐）
├── references/             参考附件（决策指南、页面类型模板）
├── templates/              9 个模板（4 有效 SVG 图例 + 课程支架 + SPA + KG + 2 启动脚本）
├── theme/20 品牌 DESIGN.md  各品牌设计语言参考
├── test-prompts.json       测试提示词（3 个场景）
```

### Magic UI 装饰效果

课程模板和所有示例通过 `libs/magicui-effects.css` 共享 13 种 CSS 装饰效果，已内置到课程模板和所有示例：

| 效果 | CSS 类 | 说明 |
|---|---|---|
| 光泽扫光 | `.shiny-text` | 封面/标题光泽扫光动画 |
| 噪点纹理 | `.noise-overlay` | SVG feTurbulence 噪点叠加层 |
| 圆点网格 | `.dot-bg` | CSS radial-gradient 圆点背景 |
| 直线网格 | `.grid-bg` | CSS linear-gradient 双线网格背景 |
| 流星雨 | `.meteors-container` + `.meteor` | 封面装饰流星动画 |
| 边框发光 | `.border-glow` | conic-gradient 旋转边框 |
| 辉光悬停 | `.glare-hover` | 背景渐变过渡，鼠标悬停触发 |
| 渐变文字 | `.gradient-text` | 多色渐变流动动画 |
| 模糊淡入 | `data-anim="blur"` | 滚动模糊淡入（filter blur + opacity） |
| 霓虹卡片 | `.neon-card` | 霓虹渐变色边框 |
| 聚光灯卡片 | `.spotlight-card` | 鼠标追踪聚光灯效果 |
| 交互按钮 | `.interactive-btn` | 点击波纹扩散按钮 |
| 打字光标 | `.typing-cursor` | 闪烁打字光标 |

所有效果适配 CSS 变量（`var(--accent)`、`var(--surface)` 等），自动跟随主题切换。新增效果应先加到 `libs/magicui-effects.css` 再更新所有模板。

## 前置依赖

- `fireworks-tech-graph` skill（已内嵌 `.opencode/skills/fireworks-tech-graph/`）
- `cairosvg`（可选，`pip install cairosvg`，SVG → PNG 导出）
