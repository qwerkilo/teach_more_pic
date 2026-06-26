---
name: teach_more_pic
description: >
  Teach a concept with visual-heavy HTML lessons: SVG flowcharts (via fireworks-tech-graph),
  CSS timelines, bar charts, role cards. Use when creating new lessons or redesigning
  existing ones for visual variety. Complements the base `teach` skill — run both.
  Triggers: "visual lesson", "redesign lesson", "add diagrams", "图表", "流程图",
  "SVG", "diagram", "timeline", "infographic", "可视化", "图示".
disable-model-invocation: true
argument-hint: "What lesson to create or redesign?"
---

# teach_more_pic — 视觉增强课程制作

Use alongside the base `teach` skill. The base `teach` handles workspace structure, mission, and learning records; this skill handles **visual components** inside each lesson.

## 前置条件

- `fireworks-tech-graph` skill available (for SVG diagram creation)
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

从以下组件中按需选用，**不要每课全用**——视觉密度要和叙事节奏匹配。

### 1. SVG 流程图（替换 ASCII 图）

用 `fireworks-tech-graph` 的 flat-icon style（Style 1）创建彩色流程图。

```
流程：
1. 加载样式参考: references/style-1-flat-icon.md
2. 设计的流程图，viewBox 约 700×N（按节点数量）
3. 颜色语义：
   - 蓝色 (#2563eb / #eff6ff): 资金流、正常经济活动
   - 橙色 (#d97706 / #fff7ed): 触发因素、转折点
   - 红色 (#dc2626 / #fef2f2): 崩溃、负面循环
   - 绿色 (#16a34a / #f0fdf4): 救助、恢复
4. 保存为 lessons/NNNN-slug.svg
5. 验证: python -c "import xml.etree.ElementTree as ET; ET.parse('lessons/NNNN-slug.svg')"
6. HTML 中引用: <img src="NNNN-slug.svg" alt="..." class="svg-fig">
```

SVG 模板结构：
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 900">
  <defs>
    <marker id="arrow-{color}" .../>
    <filter id="shadow"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.1"/></filter>
  </defs>
  <style>
    text { font-family: "Noto Sans CJK SC", "PingFang SC", "Microsoft YaHei", sans-serif; }
    .node-label { font-size: 14px; font-weight: 500; fill: #1e293b; }
    .sub-label { font-size: 12px; font-weight: 400; fill: #64748b; }
  </style>
  <rect width="700" height="900" fill="#ffffff" rx="12"/>
  <!-- ... nodes, arrows, legend ... -->
</svg>
```

关键样式：每个节点是一个 `g` 包裹的圆角 `rect` + 图标 + 标题 + 副标题。每个节点加 drop-shadow。

可复用的 SVG 骨架模板（在 `templates/` 目录下）：
- `templates/flowchart-vertical.svg` — 纵向流程图，填充 {TITLE} {HEIGHT} {LABEL} {DESC}
- `templates/timeline-horizontal.svg` — 横向时间线，适合 4-8 个时间节点
- `templates/cycle-diagram.svg` — 环形循环图，中心+周围 3-6 个节点
- `templates/comparison-side-by-side.svg` — 左右对比图，适合 A vs B 场景

使用方式：复制模板文件，用编辑替换占位符（{TITLE}、{LABEL} 等），按节点数调整 HEIGHT 和间距。

SVG 文字颜色规则（重要）：
- 深色填充盒（`#dc2626`、`#2563eb`、`#16a34a`、`#d97706` 等饱和色）→ 文字用白色 `#fff`
- 浅色填充盒（`#fef2f2`、`#f0fdf4`、`#eff6ff`、`#fff7ed` 等淡色调）→ 文字用深色 `#1e293b` 或 `#7f1d1d`（红色盒）/ `#1e40af`（蓝色盒）/ `#166534`（绿色盒）
- 禁止白色文字（`fill="#fff"`）出现在浅色背景（`#fef2f2` 等）上 → 完全不可读

### 2. 角色卡片（替换文本列表）

当需要介绍多个参与者或对比多方观点时，用 SVG 卡片网格。

参考 `0001-roles.svg`：
- 3×2 网格，每张卡片 210×100
- 卡片顶栏 30px 高，颜色区分角色类型
- 圆角 8px，带阴影
- 每个卡片包含 emoji 图标 + 角色名称 + 2-3 行描述

```xml
<g filter="url(#shadow)">
  <rect x="18" y="50" width="210" height="100" rx="8" fill="#fff" stroke="#e2e8f0"/>
  <rect x="18" y="50" width="210" height="30" rx="8" fill="#2563eb"/>
  <rect x="18" y="72" width="210" height="8" fill="#2563eb"/>
  <text x="123" y="70" text-anchor="middle" fill="#fff" font-size="14" font-weight="600">🏛️ 角色名</text>
  <text x="28" y="98" fill="#475569" font-size="12">描述第一行</text>
  <text x="28" y="116" fill="#475569" font-size="12">描述第二行</text>
</g>
```

### 3. CSS 时间线（替换事件表格）

用纯 CSS 竖直时间轴替代 HTML 表格中的事件列表：

```css
.timeline { position: relative; padding: 1em 0; margin: 1.5rem 0; }
.timeline::before {
  content: ''; position: absolute; left: 18px; top: 0; bottom: 0;
  width: 2px; background: #d0d0d0;
}
.tl-item { position: relative; padding: 0.6em 0 0.6em 3em; }
.tl-dot {
  position: absolute; left: 10px; width: 18px; height: 18px; border-radius: 50%;
  background: #c0392b; border: 3px solid #faf9f7; z-index: 1;
}
.tl-dot.major { width: 22px; height: 22px; left: 8px; } /* 关键事件的强调圆点 */
.tl-date { font-size: 0.8rem; font-weight: 700; color: #c0392b; }
.tl-desc { font-size: 0.9rem; margin-top: 0.1em; }
```

HTML 结构：
```html
<div class="timeline">
  <div class="tl-item">
    <div class="tl-dot"></div>
    <div class="tl-date">2006 年中</div>
    <div class="tl-desc">事件描述</div>
  </div>
  ...
</div>
```

### 4. CSS 条形图（替换纯文本统计）

当需要展示数据对比时，用水平条形图让数字"可见"：

```css
.bar-chart { margin: 1.2rem 0; }
.bar-item { display: flex; align-items: center; margin: 0.5em 0; }
.bar-label { width: 100px; flex-shrink: 0; font-size: 0.85rem; text-align: right; padding-right: 0.8em; color: #555; }
.bar-track { flex: 1; height: 1.6em; background: #eee; border-radius: 3px; overflow: hidden; }
.bar-fill {
  height: 100%; border-radius: 3px; display: flex; align-items: center;
  padding: 0 0.5em; font-size: 0.8rem; color: #fff; font-weight: 600;
  min-width: 2.5em; justify-content: flex-end;
}
```

HTML 结构（width 反映比例，颜色区分类别）：
```html
<div class="bar-item">
  <div class="bar-label">标签</div>
  <div class="bar-track"><div class="bar-fill" style="width:75%; background:#c0392b;">数值</div></div>
</div>
```

### 5. 对比表（保留现有样式）

复用 `comp-table` flex 组件。仅当对比维度 ≥ 3 且对比内容较为复杂时使用。

### 6. SVG Figure 包裹（标准容器）

```css
.svg-figure { margin: 1.5rem auto; text-align: center; }
.svg-figure img { max-width: 100%; height: auto; border-radius: 8px; }
```

### 7. PPT 质感增强（纵向滚读 + 动画 + 主题切换）

在保持纵向滚读结构的基础上，添加 PPT 级的视觉品质。以下三个能力需要添加到每个课程的 `<head>` 中（CSS + JS）。

#### 7.1 主题切换（T 键）

键盘按 `T` 键循环切换主题。CSS 层使用 `[data-theme="..."]` 选择器覆盖。

默认包含 4 个主题，每个主题控制 12 个 CSS 变量：

```css
:root {
  --bg: #faf9f7; --text: #1a1a1a; --accent: #c0392b;
  --font: "Noto Serif CJK SC", Georgia, "Times New Roman", serif;
  --font-h: "Noto Serif CJK SC", Georgia, "Times New Roman", serif;
  --lh: 1.8; --radius: 8px; --anim-dur: 0.6s; --anim-y: 24px;
  --h2-border: 1px solid #ddd; --h1-size: 2rem;
}
[data-theme="apple"] {
  --bg: #ffffff; --text: #1d1d1f; --accent: #0066cc;
  --font: -apple-system, "SF Pro Text", "Helvetica Neue", sans-serif;
  --font-h: -apple-system, "SF Pro Display", "Helvetica Neue", sans-serif;
  --lh: 1.9; --radius: 12px; --anim-dur: 0.8s; --anim-y: 20px;
  --h2-border: 1px solid #f0f0f0; --h1-size: 2.1rem;
}
[data-theme="minimax"] {
  --bg: #ffffff; --text: #0a0a0a; --accent: #ff5530;
  --font: "DM Sans", "Inter", "Helvetica Neue", Arial, sans-serif;
  --font-h: "DM Sans", "Inter", "Helvetica Neue", Arial, sans-serif;
  --lh: 1.7; --radius: 8px; --anim-dur: 0.35s; --anim-y: 30px;
  --h2-border: none; --h1-size: 2.4rem;
}
[data-theme="nvidia"] {
  --bg: #ffffff; --text: #1a1a1a; --accent: #76b900;
  --font: "Inter", Arial, "Helvetica Neue", sans-serif;
  --font-h: "Inter", Arial, "Helvetica Neue", sans-serif;
  --lh: 1.6; --radius: 2px; --anim-dur: 0s; --anim-y: 0px;
  --h2-border: 2px solid var(--accent); --h1-size: 1.9rem;
}
```

| 变量 | 作用 | warm | apple | minimax | nvidia |
|------|------|------|-------|---------|--------|
| `--font` | 正文字体 | Noto Serif | SF Pro Text | DM Sans | Inter |
| `--font-h` | 标题字体 | Noto Serif | SF Pro Display | DM Sans | Inter |
| `--lh` | 行高 | 1.8 | 1.9 | 1.7 | 1.6 |
| `--h1-size` | 大标题 | 2rem | 2.1rem | 2.4rem | 1.9rem |
| `--h2-border` | h2 下划线 | 1px 灰 | 1px 浅灰 | 无边框 | 2px 强调色粗线 |
| `--radius` | 组件圆角 | 8px | 12px | 8px | 2px |
| `--anim-dur` | 动画时长 | 0.6s | 0.8s | 0.35s | 0s（无动画） |
| `--anim-y` | 动画位移 | 24px | 20px | 30px | 0px |

主题详情参考 `theme/{apple|minimax|nvidia}/DESIGN.md`。

主题详情参考 `theme/{apple|minimax|nvidia}/DESIGN.md`。

JS 处理 T 键：

```js
const themes = ['warm', 'apple', 'minimax', 'nvidia'];
let ti = 0;
document.addEventListener('keydown', e => {
  if (e.key === 't' && !e.ctrlKey && !e.metaKey) {
    ti = (ti + 1) % themes.length;
    document.documentElement.dataset.theme = themes[ti];
  }
});
```

#### 7.2 入场动画（滚动触发）

使用 IntersectionObserver 实现元素进入视口时播放动画。

```css
[data-anim] { opacity: 0; transform: translateY(24px); transition: opacity 0.6s ease, transform 0.6s ease; }
[data-anim].in-view { opacity: 1; transform: translateY(0); }
[data-anim="fade"] { transform: none; }
[data-anim="slide-left"] { transform: translateX(-24px); }
[data-anim="slide-left"].in-view { transform: translateX(0); }
```

需要动画的元素加 `data-anim="fade-up"`。JS：

```js
const obs = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) e.target.classList.add('in-view');
}));
document.querySelectorAll('[data-anim]').forEach(el => obs.observe(el));
```

使用规则：
- **h2 标题**：总是加 `data-anim="fade-up"`（进入视口时从下方滑入）
- **SVG 图 / 时间线 / 条形图**：总是加 `data-anim="fade-up"`
- **对比表**：加 `data-anim="fade"`
- **段落文本**：不加（太多段落同时动画反而眼花）
- 前 2 个视觉元素不用动画（首屏元素已在视口内）

#### 7.3 键盘章节导航（← → 键）

按 ← → 键跳转到上一个/下一个 h2 标题。

```js
document.addEventListener('keydown', e => {
  if ((e.key === 'ArrowRight' || e.key === 'ArrowLeft') && !e.ctrlKey && !e.metaKey) {
    e.preventDefault();
    const sections = document.querySelectorAll('h2');
    const current = [...sections].findIndex(h2 => {
      const rect = h2.getBoundingClientRect();
      return rect.top >= 0 && rect.top < window.innerHeight / 2;
    });
    const next = e.key === 'ArrowRight' ? Math.min(current + 1, sections.length - 1) : Math.max(current - 1, 0);
    if (next >= 0 && sections[next]) sections[next].scrollIntoView({ behavior: 'smooth' });
  }
});
```

#### 7.4 内容密度规范（区别于纯 PPT）

纵向滚读的课程每屏要有"视觉呼吸"：
- 每两个 h2 之间至少插入 1 个视觉组件（SVG / 时间线 / 条形图 / 对比表）
- 连续文本不超过 4 段
- 段落中不使用过多的引用或信息框——每个 `.info-box` / `.warning-box` 之间至少隔 1 段
- 一个标准的 h2 章节体量："1-2 段引出 → 视觉组件 → 1-2 段深化"

#### 7.5 JS 运行时模板

课程末尾的 `<script>` 块（在 quiz JS 之后）追加：

```html
<script>
// PPT 质感增强 — 含降级处理
(function(){var t=['warm','apple','minimax','nvidia'],i=0,d=document.documentElement;
try{document.addEventListener('keydown',function(e){if(e.key==='t'&&!e.ctrlKey&&!e.metaKey){i=(i+1)%t.length;d.dataset.theme=t[i];}});
}catch(e){} // 主题切换降级：静默失败，不影响课程阅读
try{var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)e.target.classList.add('in-view');});});
document.querySelectorAll('[data-anim]').forEach(function(el){o.observe(el);});
}catch(e){document.querySelectorAll('[data-anim]').forEach(function(el){el.style.opacity='1';el.style.transform='none';});
} // IntersectionObserver 降级：直接显示所有元素
try{var s=document.querySelectorAll('h2');
document.addEventListener('keydown',function(e){if((e.key==='ArrowRight'||e.key==='ArrowLeft')&&!e.ctrlKey&&!e.metaKey){e.preventDefault();
var c=Array.from(s).findIndex(function(h){var r=h.getBoundingClientRect();return r.top>=0&&r.top<window.innerHeight/2;});
var n=e.key==='ArrowRight'?Math.min(c+1,s.length-1):Math.max(c-1,0);if(n>=0&&s[n])s[n].scrollIntoView({behavior:'smooth'});
}});}catch(e){} // 键盘导航降级：静默失败
})();
</script>
```

降级说明：
- **IntersectionObserver 不支持的浏览器**（IE11、旧 Safari）：catch 块将所有 `[data-anim]` 元素的 opacity 设为 1、transform 取消，用户看到的是静态完整页面
- **smooth scroll 不支持**：浏览器自动降级为 instant scroll
- **T 键切主题不支持**：静默失败，用户停留在默认主题
- 降级设计的核心原则：**JS 增强不影响基本可用性**——所有降级情况下，课程内容仍然是完整可读的

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
Step 1: 确定叙事框架（三幕）
  - 第一幕：矛盾/背景（1-2段）
  - 第二幕：事件/危机（核心内容）
  - 第三幕：转折/遗产（收束+跨课连接）
  - 🔴 输出：三段式大纲（每幕 2-3 句话），展示给用户确认

Step 2: 设计视觉组件
  - 流程图：确定节点数和流向 → 用 fireworks-tech-graph 创建 SVG → 验证
  - 时间线：提取关键日期 → 写 timeline HTML
  - 条形图：提取数据 → 写 bar-chart HTML
  - 角色卡：确定参与者 → 写 cards SVG
  - 对比表：确定对比维度 → 写 comp-table HTML
  - 🔴 每个 SVG 创建后立即验证：`python -c "import xml.etree.ElementTree as ET; ET.parse('path.svg')"`，验证失败则回到上一步修改坐标/标签后重试

Step 3: 写 HTML
  - 从已有课程复制 CSS（保持一致性）
  - 只引入本课需要的视觉组件 CSS（不需要 timeline 就不用加）
  - 每幕之间的"视觉停顿"法则：每 2-3 段文本后插入一个视觉元素
  - **课程间互相链接使用相对路径**：如 `<a href="NNNN-slug.html">`，不要加前导 `/` 或完整 URL，确保 GitHub 仓库内跳转正常

Step 4: 验证
  - 浏览器打开 .html 检查渲染
  - SVG 验证：python -c "import xml.etree.ElementTree as ET; ET.parse('path.svg')"
  - 交叉链接检查（glossary 路径、课程链接）——确认所有跨课链接为相对路径（不以 `/` 或 `http` 开头）
  - 测验 5 题，每题 3 个选项
  - 🔴 任一验证失败 → 定位问题（SVG 坐标偏移/HTML 标签闭合/路径有误）→ 修复后重跑验证 → 全部通过后再继续

Step 5: 配套产出
  - learning-record
  - EPUB 重建（如果有）
```

## 失败模式与异常处理

| 触发条件 | 一线修复 | 仍失败兜底 |
|---|---|---|
| SVG 无法正确显示（浏览器空白） | 检查 SVG XML 语法：`python -c "import xml.etree.ElementTree as ET; ET.parse('path.svg')"`；检查 viewBox 与 width/height 比例一致 | 回到 fireworks-tech-graph 流程重新生成，或降级为纯 CSS 流程图（用 div+border 拼箭头） |
| HTML 嵌入 SVG 后排版错乱 | 加 `.svg-figure { max-width: 100%; overflow-x: auto; }` 防止溢出 | 改为 `<a href="NNNN-slug.svg" target="_blank">点击查看大图</a>` 外部链接 |
| 条形图 width 导致数据溢出容器 | 检查所有 `bar-fill` 的 width 值 ≤ 100%；保持值的比例一致（如全部除以最大值归一化） | 改用 `inline-block` 加 `text-overflow: ellipsis` 在数值过长时截断 |
| 时间线在窄屏（移动端）上跑偏 | 确保 `.tl-dot` 使用 `position: absolute` + `left` 固定，不受父容器 padding 影响 | 转为水平折叠式：窄屏时每个 `.tl-item` 变成水平块，时间竖排 |
| 角色卡片中文显示乱码 | 确认 SVG 中的 font-family 包含中文字体（如 "Noto Sans CJK SC"），且在 `<style>` 而非内联 | 用 `<text font-family="..." />` 替代 CSS 样式内的 font-family 声明 |
| 测验 `<button>` 的 `data-correct` 属性写反 | 用 `grep 'data-correct="true"'` 确认每题恰好 1 个正确答案 | 手动核一遍 5 题，在浏览器中点每个选项验证反馈 |
| fireworks-tech-graph 不可用时 | 手动编写 SVG 或使用 fireworks-tech-graph 的 template 模板直接修改 | 用 CSS 盒子模型 + `::before/::after` 伪元素制作简化版流程图 |
| 新增课程后 EPUB 构建失败 | 运行 `python build_epub.py` 查看错误输出 | 删除 `_epub_build/` 后重试；若仍失败检查 `lessons/` 下是否有不合法的 HTML 文件 |
| SVG 中文字体不渲染（浏览器显示为方格） | 确认 `<style>` 内的 font-family 包含中文字体（"Noto Sans CJK SC"），且在 `<style>` 块内而非内联 `<text>` 属性 | 在 `<style>` 内层加入 `text { font-family: "Noto Sans CJK SC", "PingFang SC", sans-serif; }` |
| IntersectionObserver 不触发动画 | 元素可能在页面加载时已在视口内（首屏元素） | 首屏前 2 个视觉元素不加 `data-anim`；或者用 `rootMargin: '100px'` 提前触发 |
| 主题切换后 h2 的下划线颜色不变 | CSS 中 h2 border-bottom-color 使用了固定色而非 `var(--accent)` | 确保 h2 样式使用 `border-bottom-color: var(--accent)` 而非 `#c0392b` |
| SVG viewBox 比例不匹配 width/height | 导致图片在 `<img>` 内被不等比例拉伸 | viewBox 的宽高比必须与 width/height 的宽高比一致（如 viewBox="0 0 700 480" 对应 width="700" height="480"） |
| `<button>` 文字在 CSS 中设置了 `text-transform` | 导致选择题选项文字被大写，破坏可读性 | 不要在课程样式中全局设置 `text-transform`，如需设则用 `.quiz-btn { text-transform: none; }` 覆盖 |

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
| 1 | 课程中同时使用所有 6 种视觉组件 | 视觉密度过高，读者"喘不过气" | 每课选 2-3 个组件，和叙事节奏匹配 |
| 2 | SVG 流程图用纯红色表示所有环节 | 失去颜色语义，读者无法从颜色快速判断"这是好事还是坏事" | 严格遵守颜色语义：蓝=正常，橙=触发，红=崩溃，绿=救助 |
| 3 | 条形图的 `width` 直接用绝对数值（如 `width:9000000`） | 超出容器宽度，数据失真 | 先归一化到最大值，按百分比设 width |
| 4 | 角色卡片中放超过 4 行文本 | 卡片视觉重量失衡，字号被迫缩小 | 每张卡片最多 3 行描述，单行不超过 25 字 |
| 5 | CSS 时间轴占满整屏高度却只有 3 个事件 | 视觉空洞，不如用表格或编号列表 | 事件 < 5 个时不使用时间轴组件 |
| 6 | 直接用 ASCII 流程图不改 SVG | 样式不统一，和 SVG 图的精细质感对比强烈 | 一节课内不要混用 ASCII 图和 SVG 图——要么全部 SVG，要么全部 ASCII |
| 7 | SVG 中浅色盒用白字 | 白字在浅红/浅蓝/浅绿色背景上完全不可读，是 SVG 常见的可读性问题 | 深色饱和背景用白字，浅色淡背景用深字；红色调盒字用 `#7f1d1d`，蓝色调用 `#1e40af`，绿色调用 `#166534` |
| 8 | 课程没有主题切换和键盘导航 | 缺少 PPT 质感，读者只能被动滚读 | 每个课程均加入 T 键主题切换和 ← → 章节导航 |
| 9 | 连续超过 4 段文本无视觉停顿 | 读者疲劳，失去阅读节奏 | 每 1-2 段间插入一个视觉组件（SVG/时间线/条形图/对比表） |

## 错误检查清单

- [ ] SVG 文件通过了 XML 验证
- [ ] 所有 SVG 文字颜色与背景有足够对比度：白字（`#fff`）不放在浅色背景（`#fef2f2`、`#f0fdf4`、`#fff7ed` 等）上
- [ ] SVG 中的中文渲染正常（font-family 包含中文字体）
- [ ] SVG 的 viewBox 匹配 width/height 比例
- [ ] 条形图的 width 百分比<100%（不会溢出）
- [ ] 时间线的最后一个事件不会超出容器（padding 足够）
- [ ] 对比表在窄屏（<600px）下折叠为堆叠布局
- [ ] Quiz 数据属性正确（`data-correct="true"` v.s. `"false"`）
- [ ] 外部链接的 SVG src 路径正确
- [ ] 课程间链接使用相对路径（不以 `/` 或 `http` 开头），兼容 GitHub 仓库内跳转

验证自动化：`python scripts/validate-lesson.py lessons/NNNN-slug.html` — 自动检查 SVG 路径、XML 有效性、quiz 正确数、h1 数量、data-anim 语法、容器宽度。
