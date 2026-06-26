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

### 5. 对比表（增强版）

当需要对比多个选项/方案的多个维度时，使用增强版 HTML 表格。支持固定表头（滚动时保持可见）、斑马纹交替行、鼠标悬停高亮、点击列头排序（数字和文本均支持）。

详见增强版说明（### 22. 对比表 增强版）。

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

### 8. 折叠式分步详解（替换平铺的长篇分步文本）

当需要拆解一个复杂概念（3-5 步）时，用折叠组件替代平铺的长段落。每步默认折叠，读者按需展开，避免一下子看到太多文字压力。

颜色语义：
- 每步的圆形数字徽章使用 `var(--accent)`，与课程主色一致
- 分隔线和边框用 `#e2e8f0` 浅灰，不抢眼

HTML 结构：
```html
<div class="step-detail">
  <div class="sd-item" data-expanded="true">
    <button class="sd-trigger" aria-expanded="true">
      <span class="sd-num">1</span>
      <span class="sd-title">步骤标题</span>
      <span class="sd-icon">+</span>
    </button>
    <div class="sd-content">
      <div class="sd-inner"><p>展开的内容...</p></div>
    </div>
  </div>
  <div class="sd-item" data-expanded="false">
    <button class="sd-trigger" aria-expanded="false">
      <span class="sd-num">2</span>
      <span class="sd-title">步骤标题</span>
      <span class="sd-icon">+</span>
    </button>
    <div class="sd-content">
      <div class="sd-inner"><p>折叠的内容...</p></div>
    </div>
  </div>
</div>
```

使用规则：
- 每组分步 3-5 步，超过 5 步拆成两组
- 默认第一项展开（`data-expanded="true"`），其余折叠
- 每步内容控制在 1-3 段，不宜过长

CSS：
```css
.step-detail {
  border: 1px solid #e2e8f0; border-radius: var(--radius, 8px);
  overflow: hidden; margin: 1.5rem 0; background: var(--bg);
}
.sd-item + .sd-item { border-top: 1px solid #e2e8f0; }
.sd-trigger {
  display: flex; align-items: center; width: 100%; padding: 0.8em 1em;
  background: transparent; border: none; cursor: pointer; text-align: left;
  font-size: 0.95rem; color: var(--text);
  transition: background var(--anim-dur, 0.3s) ease;
}
.sd-trigger:hover { background: rgba(0,0,0,0.03); }
.sd-trigger:focus-visible { outline: 2px solid var(--accent); outline-offset: -2px; }
.sd-num {
  display: inline-flex; align-items: center; justify-content: center;
  width: 26px; height: 26px; border-radius: 50%;
  background: var(--accent); color: #fff; font-size: 0.8rem; font-weight: 700;
  margin-right: 0.7em; flex-shrink: 0;
}
.sd-title { flex: 1; font-weight: 500; }
.sd-icon {
  font-size: 1.2rem; color: var(--accent); font-weight: 300;
  transition: transform var(--anim-dur, 0.3s) ease;
}
.sd-item[data-expanded="true"] .sd-icon { transform: rotate(45deg); }
.sd-content { overflow: hidden; transition: height var(--anim-dur, 0.3s) ease; }
.sd-item[data-expanded="false"] .sd-content { height: 0; }
.sd-item[data-expanded="true"] .sd-content { height: auto; }
.sd-inner { padding: 0 1.2em 1.2em 3.4em; }
```

JS（与其他 PPT 增强 JS 一起放在课程末尾 `<script>` 中）：
```html
<script>
// 折叠式分步详解
(function(){document.querySelectorAll('.sd-trigger').forEach(function(b){b.addEventListener('click',function(){
var i=this.closest('.sd-item'),c=i.querySelector('.sd-content'),o=i.dataset.expanded==='true';
if(o){c.style.height=c.scrollHeight+'px';requestAnimationFrame(function(){c.style.height='0px';});
i.dataset.expanded='false';this.setAttribute('aria-expanded','false');}else{
c.style.height='0px';requestAnimationFrame(function(){var h=c.scrollHeight;
c.style.height=h+'px';});i.dataset.expanded='true';this.setAttribute('aria-expanded','true');
c.addEventListener('transitionend',function h(){c.removeEventListener('transitionend',h);
c.style.height='auto';});}});});})();
</script>
```

降级说明：
- **不支持 CSS transition 的旧浏览器**：`height: auto` 和 `height: 0` 直接生效，组件仍可正常开关（只是无动画）
- **JS 未加载**：默认状态下第一项展开可见，其余项折叠（`height: 0`），内容完整但不可交互——降级后读者只能看到首步内容
- **键盘导航**：`<button>` 元素原生支持 Tab 聚焦和 Enter/Space 触发，无额外依赖

### 9. Tab 切换面板（替换平铺的多视角罗列）

当需要呈现同一主题的多个视角/维度时，用 Tab 面板替代一次性全部罗列。读者点击左侧 Tab 切换内容，每次只看一个视角。

布局：左侧纵向药丸 Tab + 右侧内容区。窄屏（<600px）自动折叠为顶部横向 Tab。

颜色语义：
- 选中 Tab 使用 `var(--accent)` 填充 + 白色文字
- 未选中 Tab 灰色边框 + 正文色文字
- 悬停时浅灰背景

HTML 结构：
```html
<div class="tab-panel">
  <div class="tab-nav">
    <button class="tab-btn" data-tab="1" aria-selected="true">视角一</button>
    <button class="tab-btn" data-tab="2" aria-selected="false">视角二</button>
    <button class="tab-btn" data-tab="3" aria-selected="false">视角三</button>
  </div>
  <div class="tab-content">
    <div class="tab-pane active" data-tab="1" role="tabpanel">
      <p>视角一的内容...</p>
    </div>
    <div class="tab-pane" data-tab="2" role="tabpanel">
      <p>视角二的内容...</p>
    </div>
    <div class="tab-pane" data-tab="3" role="tabpanel">
      <p>视角三的内容...</p>
    </div>
  </div>
</div>
```

使用规则：
- Tab 数量 2-4 个，超过 4 个考虑改用其他组件
- 每个 Tab 的内容控制在 1-3 段，不宜过长
- 默认第一个 Tab 选中（`aria-selected="true"` + `class="active"`）

CSS：
```css
.tab-panel { display: flex; gap: 0; margin: 1.5rem 0; border: 1px solid #e2e8f0; border-radius: var(--radius, 8px); overflow: hidden; }
.tab-nav { display: flex; flex-direction: column; gap: 4px; padding: 0.8em; background: var(--bg); border-right: 1px solid #e2e8f0; min-width: 100px; }
.tab-btn {
  display: block; width: 100%; padding: 0.55em 1em; border: 1px solid #e2e8f0; border-radius: 6px;
  background: transparent; color: var(--text); cursor: pointer; text-align: left;
  font-size: 0.88rem; font-weight: 500; transition: all var(--anim-dur, 0.2s) ease;
}
.tab-btn:hover { background: rgba(0,0,0,0.03); }
.tab-btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.tab-btn[aria-selected="true"] { background: var(--accent); color: #fff; border-color: var(--accent); }
.tab-content { flex: 1; padding: 1em 1.2em; background: var(--bg); }
.tab-pane { display: none; }
.tab-pane.active { display: block; animation: tabFadeIn var(--anim-dur, 0.3s) ease; }
@keyframes tabFadeIn { from { opacity: 0; } to { opacity: 1; } }

@media (max-width: 600px) {
  .tab-panel { flex-direction: column; }
  .tab-nav { flex-direction: row; overflow-x: auto; border-right: none; border-bottom: 1px solid #e2e8f0; padding: 0.5em; }
  .tab-btn { white-space: nowrap; flex-shrink: 0; }
}
```

JS（与其他 PPT 增强 JS 一起放在课程末尾 `<script>` 中）：
```html
<script>
// Tab 切换面板
(function(){document.querySelectorAll('.tab-panel').forEach(function(p){var btns=p.querySelectorAll('.tab-btn');
btns.forEach(function(b){b.addEventListener('click',function(){var t=this.dataset.tab;
btns.forEach(function(x){x.setAttribute('aria-selected','false');});
this.setAttribute('aria-selected','true');
p.querySelectorAll('.tab-pane').forEach(function(x){x.classList.remove('active');});
var a=p.querySelector('.tab-pane[data-tab="'+t+'"]');if(a)a.classList.add('active');});});});})();
</script>
```

降级说明：
- **JS 未加载**：第一个 `tab-pane.active` 可见，其余隐藏（`display: none`），读者能看到首视角内容
- **不支持 CSS animation**：内容直接显示，无淡入效果但不影响可读性
- **键盘导航**：Tab 键在按钮间切换，Enter/Space 激活

### 10. 图片前后对比滑块（替换静态对比图）

当需要展示 before/after 效果对比（如政策实施前后、修复前后、周期对比）时，用可拖拽的滑块替代两张静态图片。读者拖拽中间手柄查看变化。

布局：两张图片叠放，默认各占 50%。用户左右拖拽手柄调整分割线位置。支持鼠标拖拽和触摸拖拽。

HTML 结构：
```html
<div class="compare-slider">
  <div class="compare-images">
    <img src="after-image.png" alt="之后" class="compare-after">
    <div class="compare-before-wrap" style="width: 50%;">
      <img src="before-image.png" alt="之前" class="compare-before">
    </div>
    <div class="compare-handle" style="left: 50%;">
      <span class="cmp-arrow">&#8592;</span>
      <span class="cmp-arrow">&#8594;</span>
    </div>
  </div>
  <div class="compare-labels">
    <span class="cmp-label-before">之前</span>
    <span class="cmp-label-after">之后</span>
  </div>
</div>
```

使用规则：
- 两张图片宽高比必须一致（推荐使用同一张图片的不同版本）
- 图片建议宽度 600-800px，过小则对比效果不明显
- 默认分割线在 50% 位置

CSS：
```css
.compare-slider { position: relative; margin: 1.5rem 0; overflow: hidden; }
.compare-images { position: relative; width: 100%; cursor: col-resize; user-select: none; -webkit-user-select: none; }
.compare-after, .compare-before { display: block; width: 100%; height: auto; pointer-events: none; }
.compare-before-wrap { position: absolute; top: 0; left: 0; height: 100%; overflow: hidden; }
.compare-handle {
  position: absolute; top: 0; bottom: 0; width: 3px; background: #fff;
  cursor: col-resize; box-shadow: -1px 0 4px rgba(0,0,0,0.15), 1px 0 4px rgba(0,0,0,0.15);
  transform: translateX(-1px); z-index: 2;
}
.compare-handle::before {
  content: ''; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
  width: 36px; height: 36px; border-radius: 50%; background: #fff;
  box-shadow: 0 1px 4px rgba(0,0,0,0.25); z-index: 1;
}
.cmp-arrow { position: absolute; top: 50%; z-index: 3; font-size: 14px; color: #333; transform: translateY(-50%); }
.cmp-arrow:first-child { left: 3px; }
.cmp-arrow:last-child { right: 3px; }
.compare-labels { position: absolute; bottom: 8px; left: 0; right: 0; display: flex; justify-content: space-between; pointer-events: none; padding: 0 8px; z-index: 2; }
.cmp-label-before, .cmp-label-after {
  background: rgba(0,0,0,0.55); color: #fff; padding: 0.2em 0.7em;
  border-radius: 4px; font-size: 0.78rem; font-weight: 600;
}
```

JS（与其他 PPT 增强 JS 一起放在课程末尾 `<script>` 中）：
```html
<script>
// 图片前后对比滑块
(function(){document.querySelectorAll('.compare-slider').forEach(function(s){
var c=s.querySelector('.compare-images'),b=s.querySelector('.compare-before-wrap'),h=s.querySelector('.compare-handle'),d=false;
function p(x){var r=c.getBoundingClientRect(),pct=Math.max(0,Math.min(100,((x-r.left)/r.width)*100));
b.style.width=pct+'%';h.style.left=pct+'%';}
function ms(e){d=true;e.preventDefault();}
function me(){d=false;}
function mv(e){if(!d)return;e.preventDefault();p(e.touches?e.touches[0].clientX:e.clientX);}
h.addEventListener('mousedown',ms);
document.addEventListener('mousemove',mv);document.addEventListener('mouseup',me);
h.addEventListener('touchstart',ms,{passive:false});
document.addEventListener('touchmove',mv,{passive:false});document.addEventListener('touchend',me);
});})();
</script>
```

降级说明：
- **JS 未加载**：两张图片各占 50%，读者看到的是"半之前半之后"的静态画面，可读但不交互
- **不支持 touch**：鼠标拖拽仍正常工作
- **图片加载慢**：先加载 after 图（底层），before 图在上层覆盖，不影响视觉

### 11. 交互式时间线（替换静态时间线 / 事件表格）

当事件数量较多（5-10 个）且每个事件有详细说明时，用交互式时间线替代一次性全部展示。默认只显示日期和标题，点击圆点/标题展开详情，保持时间线概览的整洁。

布局：继承现有 CSS 时间线的竖线 + 圆点视觉风格，增加点击展开/收起的交互能力。

视觉规则：
- 左侧竖线 + 彩色圆点（`var(--accent)`）
- 日期使用强调色加粗，标题居左
- 展开图标 `+` 在展开时旋转 45° 变为 `×`

HTML 结构：
```html
<div class="tl-interactive">
  <div class="tli-item" data-expanded="false">
    <button class="tli-dot" aria-expanded="false">
      <span class="tli-date">2008</span>
      <span class="tli-title">事件标题</span>
      <span class="tli-icon">+</span>
    </button>
    <div class="tli-content">
      <div class="tli-inner"><p>事件详情...</p></div>
    </div>
  </div>
  <div class="tli-item" data-expanded="false">
    <button class="tli-dot" aria-expanded="false">
      <span class="tli-date">2010</span>
      <span class="tli-title">事件标题</span>
      <span class="tli-icon">+</span>
    </button>
    <div class="tli-content">
      <div class="tli-inner"><p>事件详情...</p></div>
    </div>
  </div>
</div>
```

使用规则：
- 适合 5-10 个事件，少于 5 个用静态时间线或列表
- 默认全部折叠，读者按需展开
- 每个事件详情控制在 1-3 段

CSS：
```css
.tl-interactive { position: relative; margin: 1.5rem 0; }
.tl-interactive::before {
  content: ''; position: absolute; left: 18px; top: 8px; bottom: 8px;
  width: 2px; background: #d0d0d0;
}
.tli-item { position: relative; }
.tli-dot {
  display: flex; align-items: center; gap: 0.6em; width: 100%;
  padding: 0.6em 0 0.6em 3em; border: none; background: none; text-align: left;
  cursor: pointer; color: var(--text); font-family: inherit; font-size: inherit;
}
.tli-dot::before {
  content: ''; position: absolute; left: 10px; top: 0.6em;
  width: 18px; height: 18px; border-radius: 50%;
  background: var(--accent); border: 3px solid var(--bg); z-index: 1;
  transition: box-shadow var(--anim-dur, 0.2s) ease;
}
.tli-dot:hover::before { box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent) 25%, transparent); }
.tli-dot:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 4px; }
.tli-date { font-size: 0.8rem; font-weight: 700; color: var(--accent); white-space: nowrap; min-width: 3.5em; }
.tli-title { flex: 1; font-size: 0.92rem; font-weight: 500; }
.tli-icon {
  font-size: 1.1rem; color: var(--accent); font-weight: 300; margin-right: 0.3em;
  transition: transform var(--anim-dur, 0.3s) ease;
}
.tli-item[data-expanded="true"] .tli-icon { transform: rotate(45deg); }
.tli-content { overflow: hidden; transition: height var(--anim-dur, 0.3s) ease; }
.tli-item[data-expanded="false"] .tli-content { height: 0; }
.tli-item[data-expanded="true"] .tli-content { height: auto; }
.tli-inner { padding: 0.2em 0 1em 3em; font-size: 0.92rem; }
```

JS（与折叠分步组件模式一致，可复用同一逻辑结构）：
```html
<script>
// 交互式时间线
(function(){document.querySelectorAll('.tli-dot').forEach(function(b){b.addEventListener('click',function(){
var i=this.closest('.tli-item'),c=i.querySelector('.tli-content'),o=i.dataset.expanded==='true';
if(o){c.style.height=c.scrollHeight+'px';requestAnimationFrame(function(){c.style.height='0px';});
i.dataset.expanded='false';this.setAttribute('aria-expanded','false');}else{
c.style.height='0px';requestAnimationFrame(function(){c.style.height=c.scrollHeight+'px';});
i.dataset.expanded='true';this.setAttribute('aria-expanded','true');
c.addEventListener('transitionend',function h(){c.removeEventListener('transitionend',h);c.style.height='auto';});}});});})();
</script>
```

降级说明：
- **JS 未加载**：所有事件标题可见（圆点+日期+标题），详情不可展开——读者至少能看到完整事件列表
- **不支持 CSS transition**：展开/收起瞬间切换，无动画但不影响功能

### 12. 数据卡片网格（替换文本数据段）

当需要展示一组关键统计数据时，用卡片网格替代散落在段落中的数字。每张卡片包含图标 + 大号数值 + 标签 + 简短说明，让核心数据一目了然。

布局：CSS Grid 自适应列宽（最小 180px），窄屏自动折叠为 2 列 → 1 列。

颜色语义：
- 数值使用 `var(--accent)` 强调色加粗
- 标签用 `#64748b` 灰色弱化，制造视觉层次

HTML 结构：
```html
<div class="data-grid">
  <div class="dg-card" data-anim="fade-up">
    <div class="dg-icon">📉</div>
    <div class="dg-value">8.8</div>
    <div class="dg-unit">万亿美元</div>
    <div class="dg-label">全球财富蒸发</div>
  </div>
  <div class="dg-card" data-anim="fade-up">
    <div class="dg-icon">🏦</div>
    <div class="dg-value">127</div>
    <div class="dg-unit">家</div>
    <div class="dg-label">倒闭银行数</div>
  </div>
  <div class="dg-card" data-anim="fade-up">
    <div class="dg-icon">🌍</div>
    <div class="dg-value">0.1</div>
    <div class="dg-unit">%</div>
    <div class="dg-label">全球 GDP 萎缩</div>
  </div>
</div>
```

使用规则：
- 适合 3-8 张卡片，超过 8 张考虑拆分
- `dg-icon` 使用 emoji 或短标签，不要用图片
- 每张卡片内容精炼：数值一般不超过 5 位数字，标签不超过 10 字

CSS：
```css
.data-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 1rem; margin: 1.5rem 0;
}
.dg-card {
  background: var(--bg); border: 1px solid #e2e8f0; border-radius: var(--radius, 8px);
  padding: 1.2em 0.8em; text-align: center;
  transition: box-shadow var(--anim-dur, 0.2s) ease;
}
.dg-card:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
.dg-icon { font-size: 2rem; margin-bottom: 0.25em; line-height: 1; }
.dg-value { font-size: 1.8rem; font-weight: 800; color: var(--accent); line-height: 1.1; }
.dg-unit { font-size: 0.8rem; color: var(--accent); font-weight: 500; margin-bottom: 0.5em; }
.dg-label { font-size: 0.85rem; color: #64748b; line-height: 1.3; }
```

JS：不需要，入场动画复用现有 IntersectionObserver（`data-anim="fade-up"`）。

降级说明：
- **不支持 CSS Grid**（IE11）：卡片退化为全宽堆叠显示，不影响阅读
- **不支持 IntersectionObserver**：卡片直接可见，无动画但不影响内容

### 13. 引用/引文卡片（替换普通 `<blockquote>`）

当需要突出人物引言或重要文献引用时，用引文卡片替代普通的 `<blockquote>` 标签。左侧强调色竖条 + 装饰性引号 + 署名信息，视觉上比默认引用更突出。

布局：flex 行，左侧 4px 强调色竖条 + 右侧引文主体。主体内为引文文本 + 底部署名。

HTML 结构：
```html
<div class="quote-card" data-anim="fade-up">
  <div class="qc-bar"></div>
  <div class="qc-body">
    <p class="qc-text">这不仅仅是一场金融危机，更是一次全球经济的结构性转型。旧有的增长模式已经走到了尽头，未来的繁荣需要建立在全新的基础之上。</p>
    <div class="qc-source">
      <span class="qc-name">约瑟夫·斯蒂格利茨</span>
      <span class="qc-title">《全球化及其不满》，2002</span>
    </div>
  </div>
</div>
```

使用规则：
- 每段引文控制在 30-80 字，不宜过长
- 署名行包含人名 + 来源（书籍/演讲/年份）
- 引文应当是对课程核心观点的精炼概括

CSS：
```css
.quote-card {
  display: flex; gap: 1em; margin: 1.5rem 0;
  background: var(--bg); border-radius: var(--radius, 8px);
  padding: 1.2em;
}
.qc-bar { width: 4px; flex-shrink: 0; background: var(--accent); border-radius: 2px; }
.qc-body { flex: 1; }
.qc-text {
  font-size: 1rem; font-style: italic; line-height: 1.7;
  color: var(--text); margin: 0;
}
.qc-text::before { content: '\201C'; font-size: 1.5em; line-height: 0; vertical-align: -0.3em; color: var(--accent); font-style: normal; padding-right: 0.1em; }
.qc-text::after { content: '\201D'; font-size: 1.5em; line-height: 0; vertical-align: -0.15em; color: var(--accent); font-style: normal; padding-left: 0.1em; }
.qc-source { margin-top: 0.8em; display: flex; flex-direction: column; }
.qc-name { font-weight: 600; font-size: 0.9rem; color: var(--text); font-style: normal; }
.qc-title { font-size: 0.8rem; color: #64748b; font-style: normal; }
```

JS：不需要，入场动画复用现有 IntersectionObserver（`data-anim="fade-up"`）。

降级说明：
- **不支持 `::before`/`::after`**（极旧浏览器）：引文缺少装饰引号，其余内容正常显示

### 14. 标注式图片（替换纯文本图注说明）

当需要详解一张复杂图表/示意图/地图时，在图片上叠加数字标注点，点击标注点在图片下方显示对应的说明面板。避免把大量图注文字挤在图片周围或写成长段说明。

布局：图片容器 `position: relative`，标注点用百分比坐标 `left`/`top` 绝对定位（随图片缩放自适应）。点击后下方动态显示说明面板。

HTML 结构：
```html
<div class="annotated-img" data-anim="fade-up">
  <div class="ai-wrapper">
    <img src="diagram.png" alt="图表说明" class="ai-img">
    <button class="ai-dot" style="left: 25%; top: 30%;" data-point="1" aria-expanded="false">
      <span class="ai-num">1</span>
    </button>
    <button class="ai-dot" style="left: 60%; top: 55%;" data-point="2" aria-expanded="false">
      <span class="ai-num">2</span>
    </button>
    <button class="ai-dot" style="left: 80%; top: 20%;" data-point="3" aria-expanded="false">
      <span class="ai-num">3</span>
    </button>
  </div>
  <div class="ai-panels">
    <div class="ai-panel" data-point="1">
      <strong>节点 1：</strong>说明文字...
    </div>
    <div class="ai-panel" data-point="2">
      <strong>节点 2：</strong>说明文字...
    </div>
    <div class="ai-panel" data-point="3">
      <strong>节点 3：</strong>说明文字...
    </div>
  </div>
</div>
```

使用规则：
- 标注点 3-6 个为宜，超过 6 个则图片过于拥挤
- 标注点坐标用百分比（`left`/`top`）而非像素，确保响应式缩放
- 每个说明面板控制在 1-2 段

CSS：
```css
.annotated-img { margin: 1.5rem 0; }
.ai-wrapper { position: relative; display: inline-block; max-width: 100%; }
.ai-img { display: block; max-width: 100%; height: auto; border-radius: var(--radius, 8px); }
.ai-dot {
  position: absolute; width: 32px; height: 32px; border-radius: 50%; border: 2px solid #fff;
  background: rgba(0,0,0,0.45); cursor: pointer; padding: 0; transform: translate(-50%, -50%);
  transition: background var(--anim-dur, 0.2s) ease, transform var(--anim-dur, 0.2s) ease;
  z-index: 2;
}
.ai-dot:hover { background: rgba(0,0,0,0.65); transform: translate(-50%, -50%) scale(1.15); }
.ai-dot.active { background: var(--accent); transform: translate(-50%, -50%) scale(1.15); }
.ai-num {
  font-size: 0.85rem; font-weight: 700; color: #fff;
  position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
}
.ai-panels { margin-top: 1em; display: flex; flex-direction: column; gap: 0.5em; }
.ai-panel { display: none; background: var(--bg); border: 1px solid #e2e8f0; border-radius: var(--radius, 8px); padding: 0.8em 1em; font-size: 0.9rem; }
.ai-panel.active { display: block; }
```

JS：
```html
<script>
// 标注式图片
(function(){document.querySelectorAll('.annotated-img').forEach(function(c){
var dots=c.querySelectorAll('.ai-dot'),ps=c.querySelectorAll('.ai-panel');
dots.forEach(function(d){d.addEventListener('click',function(){
var p=this.dataset.point,a=this.classList.contains('active');
dots.forEach(function(x){x.classList.remove('active');x.setAttribute('aria-expanded','false');});
ps.forEach(function(x){x.classList.remove('active');});
if(!a){this.classList.add('active');this.setAttribute('aria-expanded','true');
var tp=c.querySelector('.ai-panel[data-point="'+p+'"]');if(tp)tp.classList.add('active');}});});})();
</script>
```

降级说明：
- **JS 未加载**：标注点可见但不可点击，下方面板全隐藏——读者看到的是纯图片，标注点作为视觉标记
- **不支持 touch**：鼠标点击正常工作

### 15. 状态链/进度里程碑（替换纯文本阶段列表）

当需要展示一个过程的多个阶段及各阶段状态（如危机演变阶段、政策实施步骤）时，用水平连接线 + 圆点里程碑替代编号列表。三种状态（完成/进行中/待办）用不同颜色区分。

布局：水平 flex 行，每个阶段等宽。连接线在圆点后方贯通。窄屏自动换行或横向滚动。

颜色语义：
- `done`（已完成）：实心强调色圆点
- `current`（进行中）：强调色描边 + 加粗阴影环
- `pending`（待办）：灰色描边

HTML 结构：
```html
<div class="status-chain" data-anim="fade-up">
  <div class="sc-step done">
    <div class="sc-dot"></div>
    <div class="sc-label">需求分析</div>
    <div class="sc-status">已完成</div>
  </div>
  <div class="sc-step current">
    <div class="sc-dot"></div>
    <div class="sc-label">系统设计</div>
    <div class="sc-status">进行中</div>
  </div>
  <div class="sc-step pending">
    <div class="sc-dot"></div>
    <div class="sc-label">开发实施</div>
    <div class="sc-status">待开始</div>
  </div>
  <div class="sc-step pending">
    <div class="sc-dot"></div>
    <div class="sc-label">测试部署</div>
    <div class="sc-status">待开始</div>
  </div>
</div>
```

使用规则：
- 每链 3-5 步，超过 5 步拆成两条或使用交互式时间线
- 至少有一个 `done` 或 `current`，全部 `pending` 无意义
- `sc-label` 控制在 4 字以内，过长则窄屏溢出

CSS：
```css
.status-chain { display: flex; justify-content: space-between; margin: 1.5rem 0; position: relative; padding: 0.5em 0; }
.status-chain::before {
  content: ''; position: absolute; top: 22px; left: 15%; right: 15%;
  height: 2px; background: #d0d0d0; z-index: 0;
}
.sc-step { display: flex; flex-direction: column; align-items: center; position: relative; z-index: 1; flex: 1; text-align: center; min-width: 0; }
.sc-dot { width: 28px; height: 28px; border-radius: 50%; margin-bottom: 0.4em; position: relative; background: #fff; transition: all var(--anim-dur, 0.2s) ease; }
.sc-step.done .sc-dot { background: var(--accent); border: 3px solid var(--accent); }
.sc-step.current .sc-dot { background: #fff; border: 3px solid var(--accent); box-shadow: 0 0 0 4px rgba(192,57,43,0.15); }
.sc-step.pending .sc-dot { background: #fff; border: 3px solid #d0d0d0; }
.sc-label { font-size: 0.85rem; font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 100%; padding: 0 0.3em; }
.sc-status { font-size: 0.72rem; color: #94a3b8; margin-top: 0.15em; }

@media (max-width: 500px) {
  .status-chain { gap: 0.5em; overflow-x: auto; justify-content: flex-start; }
  .status-chain::before { display: none; }
  .sc-step { flex: 0 0 auto; min-width: 70px; }
}
```

JS：不需要，纯 CSS 组件。

降级说明：
- **窄屏（<500px）**：连接线隐藏，步骤变为横向可滚动卡片
- **不支持 `::before`**：连接线消失，各阶段圆点独立展示

### 16. 数值滚动动画（替换静态数字）

当页面中的关键数字（在数据卡片或其他位置）需要吸引注意时，使用数值滚动动画：数字从 0 开始滚动到目标值，进入视口时触发，2 秒内完成（ease-out 缓动）。

核心用法：在 `.dg-value` 或任意 `<span>` 上添加 `data-countup` 属性，JS 自动处理动画。

HTML 结构（数据卡片中的用法）：
```html
<div class="dg-card" data-anim="fade-up">
  <div class="dg-icon">📉</div>
  <div class="dg-value" data-countup="8848">0</div>
  <div class="dg-unit">亿美元</div>
  <div class="dg-label">全球财富蒸发</div>
</div>
```

独立用法：
```html
<div class="countup" data-countup="127" style="text-align:center;">
  <span class="cu-value">0</span>
  <span class="cu-unit">家</span>
  <div class="cu-label">倒闭银行数</div>
</div>
```

使用规则：
- 配合数据卡片（#12）使用时，将 `.dg-value` 的文本数字替换为 `data-countup` 属性
- 数值不超过 999999，超过用万/亿等单位缩写
- 一个页面中动画数字不超过 8 个，过多分散注意力

CSS：
```css
.countup { margin: 0.5em 0; }
.cu-value { font-size: 1.8rem; font-weight: 800; color: var(--accent); line-height: 1.1; }
.cu-unit { font-size: 0.8rem; color: var(--accent); font-weight: 500; margin-left: 0.2em; }
.cu-label { font-size: 0.85rem; color: #64748b; margin-top: 0.2em; }
```

JS（与其他 PPT 增强 JS 一起放在课程末尾 `<script>` 中）：
```html
<script>
// 数值滚动动画
(function(){if(!window.IntersectionObserver)return;
document.querySelectorAll('[data-countup]').forEach(function(el){var v=parseFloat(el.dataset.countup)||0,d=2000;
function a(t){var r;return function(n){if(!r)r=n;var p=Math.min((n-r)/d,1),e=1-Math.pow(1-p,3);
el.textContent=Math.round(e*v).toLocaleString();if(p<1)requestAnimationFrame(a);}}();
var o=new IntersectionObserver(function(e){
if(e[0].isIntersecting){requestAnimationFrame(a);o.unobserve(el);}},{threshold:0.5});o.observe(el);});})();
</script>
```

降级说明：
- **不支持 IntersectionObserver**：数字直接显示目标值，无动画
- **JS 未加载**：`data-countup` 元素显示 `0`（初始值）——确保 `data-countup` 元素的初始文本对应一个合理回退值

### 17. 标签/徽章组（替换纯文本关键词列表）

当需要展示一组关键词、分类标签或技术栈时，用彩色药丸标签替代逗号分隔的文本列表。5 种预定义颜色对应不同类别。

颜色语义：
- `tag-blue`（蓝）：经济/宏观主题
- `tag-red`（红）：危机/事件
- `tag-green`（绿）：政策/救助/恢复
- `tag-orange`（橙）：监管/改革
- `tag-purple`（紫）：理论/概念/全球化

HTML 结构：
```html
<div class="tag-group" data-anim="fade-up">
  <span class="tag tag-blue"># 宏观经济</span>
  <span class="tag tag-red"># 金融危机</span>
  <span class="tag tag-green"># 政策应对</span>
  <span class="tag tag-orange"># 监管改革</span>
  <span class="tag tag-purple"># 全球化</span>
</div>
```

使用规则：
- 每组 3-8 个标签，超过 8 个则精选去掉最不重要的
- 每个标签控制在 6 字以内
- 颜色按内容语义选择，不要随机分配

CSS：
```css
.tag-group { display: flex; flex-wrap: wrap; gap: 0.5em; margin: 1.5rem 0; }
.tag { display: inline-block; padding: 0.25em 0.7em; border-radius: 999px; font-size: 0.8rem; font-weight: 500; white-space: nowrap; }
.tag-blue { background: #dbeafe; color: #1e40af; }
.tag-red { background: #fee2e2; color: #b91c1c; }
.tag-green { background: #dcfce7; color: #166534; }
.tag-orange { background: #ffedd5; color: #9a3412; }
.tag-purple { background: #f3e8ff; color: #6d28d9; }
```

JS：不需要，纯 CSS 组件。

降级说明：
- **不支持 `flex-wrap`**（IE11）：标签不换行，溢出截断——一般在标签数量不大时不明显

### 18. 提示框/告警条（替换普通强调段落）

当需要突出提示、警告、错误或成功信息时，用彩色提示框替代普通段落或 `<blockquote>`。左侧 4px 强调色竖条 + 浅色背景 + emoji 图标，4 种类型按语义选用。

颜色语义：
- `callout-info`（蓝 `#2563eb`）：一般信息/背景说明
- `callout-warning`（橙 `#d97706`）：注意/潜在风险
- `callout-error`（红 `#dc2626`）：重大错误/崩溃
- `callout-success`（绿 `#16a34a`）：成功/救助/好消息

HTML 结构：
```html
<div class="callout callout-info" data-anim="fade-up">
  <div class="callout-icon">💡</div>
  <div class="callout-body">
    <p>一般提示信息，补充课程背景。</p>
  </div>
</div>

<div class="callout callout-warning" data-anim="fade-up">
  <div class="callout-icon">⚠️</div>
  <div class="callout-body">
    <p>需要注意的风险或陷阱。</p>
  </div>
</div>

<div class="callout callout-error" data-anim="fade-up">
  <div class="callout-icon">❌</div>
  <div class="callout-body">
    <p>错误信息或负面结果。</p>
  </div>
</div>

<div class="callout callout-success" data-anim="fade-up">
  <div class="callout-icon">✅</div>
  <div class="callout-body">
    <p>成功结果或正面发展。</p>
  </div>
</div>
```

使用规则：
- 每课每种类型最多用 1 次，过量使用降低冲击力
- 提示框之间至少隔 1 段正文（不要在失败模式表中连续使用）
- 内容控制在 1-2 段

CSS：
```css
.callout {
  display: flex; gap: 0.8em; padding: 0.8em 1em;
  border-radius: var(--radius, 8px); border-left: 4px solid; margin: 1.5rem 0;
}
.callout-info { background: #eff6ff; border-left-color: #2563eb; }
.callout-warning { background: #fff7ed; border-left-color: #d97706; }
.callout-error { background: #fef2f2; border-left-color: #dc2626; }
.callout-success { background: #f0fdf4; border-left-color: #16a34a; }
.callout-icon { font-size: 1.2rem; line-height: 1.5; flex-shrink: 0; }
.callout-body { flex: 1; }
.callout-body p { margin: 0; }
.callout-body p + p { margin-top: 0.5em; }
```

JS：不需要，纯 CSS 组件。

降级说明：
- **不支持 flex**（IE11）：图标和文字垂直堆叠，可读性略降但不影响信息传递

### 19. 热力图/密度图（替换纯数字表格）

当需要展示二维数据的分布密度或强度时，用彩色矩阵替代枯燥的数字表格。单元格颜色按数值从低到高渐变（绿→黄→红），数值保留在单元格内。

布局：CSS Grid 表格。每行第一个单元格为行标签（灰色背景），其余为数据单元格。5 级强度（`data-l="0"~"4"`）。

颜色语义（绿→黄→红信号灯）：
- `data-l="0"`（极低）：浅绿
- `data-l="1"`（低）：绿
- `data-l="2"`（中）：黄
- `data-l="3"`（高）：橙
- `data-l="4"`（极高）：红

HTML 结构：
```html
<div class="heatmap" data-anim="fade-up">
  <div class="hm-row">
    <div class="hm-label"></div>
    <div class="hm-hdr">2007</div>
    <div class="hm-hdr">2008</div>
    <div class="hm-hdr">2009</div>
  </div>
  <div class="hm-row">
    <div class="hm-label">美国</div>
    <div class="hm-cell" data-l="1">低</div>
    <div class="hm-cell" data-l="4">极高</div>
    <div class="hm-cell" data-l="2">中</div>
  </div>
  <div class="hm-row">
    <div class="hm-label">欧洲</div>
    <div class="hm-cell" data-l="0">极低</div>
    <div class="hm-cell" data-l="3">高</div>
    <div class="hm-cell" data-l="3">高</div>
  </div>
  <div class="hm-row">
    <div class="hm-label">亚洲</div>
    <div class="hm-cell" data-l="0">极低</div>
    <div class="hm-cell" data-l="1">低</div>
    <div class="hm-cell" data-l="2">中</div>
  </div>
</div>
```

使用规则：
- 行数 3-8，列数 3-6（不含标签列和表头行）
- 数据级 0-4，避免全是 0 或全是 4（那样无对比意义）
- 行标签控制在 4 字以内

CSS：
```css
.heatmap { display: grid; margin: 1.5rem 0; border: 1px solid #e2e8f0; border-radius: var(--radius, 8px); overflow: hidden; }
.hm-row { display: contents; }
.hm-label, .hm-hdr, .hm-cell { padding: 0.5em 0.7em; text-align: center; font-size: 0.85rem; font-weight: 500; border-bottom: 1px solid #e2e8f0; }
.hm-row:last-child .hm-label,
.hm-row:last-child .hm-cell { border-bottom: none; }
.hm-label { background: #f8fafc; font-weight: 600; color: var(--text); text-align: left; }
.hm-hdr { background: #f8fafc; font-weight: 700; color: var(--text); font-size: 0.82rem; border-bottom: 2px solid #e2e8f0; }
.hm-cell[data-l="0"] { background: #f0fdf4; color: #166534; }
.hm-cell[data-l="1"] { background: #dcfce7; color: #166534; }
.hm-cell[data-l="2"] { background: #fef9c3; color: #854d0e; }
.hm-cell[data-l="3"] { background: #fed7aa; color: #9a3412; }
.hm-cell[data-l="4"] { background: #fca5a5; color: #b91c1c; }
```

JS：不需要，纯 CSS 组件。

降级说明：
- **不支持 CSS Grid**（IE11）：退化为普通表格布局，颜色属性仍在

### 20. 步骤指示器（替换"第 X 步"文字）

当需要在课程中引导读者了解流程进度时，用水平步骤条替代"第一步/第二步/第三步"的文字表述。已完成步骤用强调色实心圆，当前步骤用描边高亮，待办步骤灰色。

布局：水平 flex，圆点 + 底部标签。步骤之间用灰色连接线贯通。

状态语义：
- `done`（已完成）：强调色实心圆 + 白色数字
- `current`（进行中）：白色描边圆 + 强调色数字 + 外围光晕
- 无 class（待办）：灰色描边圆 + 灰色数字

HTML 结构：
```html
<div class="step-indicator" data-anim="fade-up">
  <div class="si-step done">
    <div class="si-num">1</div>
    <div class="si-label">需求分析</div>
  </div>
  <div class="si-step done">
    <div class="si-num">2</div>
    <div class="si-label">系统设计</div>
  </div>
  <div class="si-step current">
    <div class="si-num">3</div>
    <div class="si-label">开发实施</div>
  </div>
  <div class="si-step">
    <div class="si-num">4</div>
    <div class="si-label">测试验收</div>
  </div>
  <div class="si-step">
    <div class="si-num">5</div>
    <div class="si-label">部署上线</div>
  </div>
</div>
```

使用规则：
- 每链 3-6 步，超过 6 步拆分为多个
- 标签控制在 4 字以内
- 至少有一个 `done` 或 `current`，全部待办无意义

CSS：
```css
.step-indicator { display: flex; align-items: center; justify-content: space-between; margin: 1.5rem 0; position: relative; }
.step-indicator::before {
  content: ''; position: absolute; left: 10%; right: 10%; top: 16px;
  height: 2px; background: #d0d0d0; z-index: 0;
}
.si-step { display: flex; flex-direction: column; align-items: center; position: relative; z-index: 1; }
.si-num {
  width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
  font-size: 0.85rem; font-weight: 700; margin-bottom: 0.3em; border: 2px solid #e2e8f0;
  background: #fff; color: #94a3b8;
}
.si-step.done .si-num { background: var(--accent); color: #fff; border-color: var(--accent); }
.si-step.current .si-num { background: #fff; color: var(--accent); border-color: var(--accent); box-shadow: 0 0 0 4px rgba(192,57,43,0.12); }
.si-label { font-size: 0.78rem; color: #94a3b8; font-weight: 500; }
.si-step.done .si-label, .si-step.current .si-label { color: var(--text); }

@media (max-width: 500px) {
  .step-indicator { gap: 0.3em; overflow-x: auto; justify-content: flex-start; }
  .step-indicator::before { display: none; }
  .si-step { flex: 0 0 auto; min-width: 60px; }
}
```

JS：不需要，纯 CSS 组件。

降级说明：
- **窄屏（<500px）**：连接线隐藏，步骤变为横向可滚动
- **不支持 `::before`**：连接线消失，各步骤独立展示

### 21. 信息面板/侧边栏（替换脚注/附录）

当正文中需要提供扩展阅读、人物简介、术语详解等补充信息时，用从右侧滑入的面板替代脚注或附录跳转。读者点击按钮打开面板，阅读完毕关闭后回到原位，不丢失阅读进度。

布局：固定定位右侧抽屉（380px）。打开时左侧有半透明遮罩层。支持 ESC 关闭。

HTML 结构（触发按钮 + 面板）：
```html
<p>正文内容……<button class="ip-btn" data-panel="glossary-mmt">📖 MMT 详解</button></p>

<div class="info-panel" id="panel-glossary-mmt">
  <div class="ip-overlay"></div>
  <div class="ip-drawer">
    <div class="ip-header">
      <h4>现代货币理论（MMT）</h4>
      <button class="ip-close">✕</button>
    </div>
    <div class="ip-body">
      <p>详细说明内容……</p>
    </div>
  </div>
</div>
```

使用规则：
- 一课最多 3 个信息面板，过多则读者频繁开关影响流畅度
- 面板内内容控制在屏幕 70% 高度以内（超出可滚动）
- 面板标题简明，触发按钮文字控制在 10 字以内

CSS：
```css
.ip-btn {
  display: inline; padding: 0.1em 0.4em; border: 1px dashed var(--accent); border-radius: 4px;
  background: transparent; color: var(--accent); cursor: pointer; font-size: inherit; font-family: inherit;
  transition: background var(--anim-dur, 0.2s) ease;
}
.ip-btn:hover { background: color-mix(in srgb, var(--accent) 10%, transparent); }

.info-panel { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 1000; visibility: hidden; }
.info-panel.open { visibility: visible; }
.ip-overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.3); opacity: 0; transition: opacity 0.3s ease; }
.info-panel.open .ip-overlay { opacity: 1; }
.ip-drawer {
  position: absolute; top: 0; right: 0; width: 380px; max-width: 90vw; height: 100%;
  background: var(--bg); box-shadow: -4px 0 20px rgba(0,0,0,0.1);
  transform: translateX(100%); transition: transform 0.3s ease; overflow-y: auto;
}
.info-panel.open .ip-drawer { transform: translateX(0); }
.ip-header { display: flex; align-items: center; justify-content: space-between; padding: 1em 1.2em; border-bottom: 1px solid #e2e8f0; position: sticky; top: 0; background: var(--bg); z-index: 1; }
.ip-header h4 { margin: 0; font-size: 1rem; }
.ip-close { background: none; border: none; font-size: 1.3rem; cursor: pointer; color: #94a3b8; padding: 0.2em; line-height: 1; }
.ip-close:hover { color: var(--text); }
.ip-body { padding: 1.2em; }
```

JS：
```html
<script>
// 信息面板
(function(){document.querySelectorAll('.ip-btn').forEach(function(b){b.addEventListener('click',function(){
var p=document.getElementById('panel-'+this.dataset.panel);if(p){p.classList.add('open');document.body.style.overflow='hidden';}});});
document.querySelectorAll('.ip-close,.ip-overlay').forEach(function(e){e.addEventListener('click',function(){
var p=this.closest('.info-panel');p.classList.remove('open');document.body.style.overflow='';});});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){document.querySelectorAll('.info-panel.open').forEach(function(p){p.classList.remove('open');document.body.style.overflow='';});}});})();
</script>
```

降级说明：
- **JS 未加载**：面板不可用，触发按钮显示但无交互——补充信息完全不可见，需确保面板内容不是理解正文的必要前提
- **不支持 `position: fixed`**（极旧浏览器）：面板退化为页面底部块级显示
- **窄屏（<480px）**：面板宽度自动设为 90vw

### 22. 对比表 增强版（替换普通 HTML 表格）

当需要多维度对比多个方案/选项时，用增强表格替代普通 `<table>`。支持粘性表头（滚动不消失）、斑马纹交替行、鼠标悬停高亮、点击列头排序（智能识别数值 vs 文本）。

布局：普通 `<table>` 结构，外层 `overflow-x: auto` 容器。`data-sortable` 属性启用排序。

HTML 结构：
```html
<div class="cmp-wrap" data-anim="fade-up">
  <table class="cmp-table" data-sortable>
    <thead>
      <tr>
        <th data-sort>维度 <span class="cmp-arrow">↕</span></th>
        <th data-sort>方案 A <span class="cmp-arrow">↕</span></th>
        <th data-sort>方案 B <span class="cmp-arrow">↕</span></th>
        <th data-sort>方案 C <span class="cmp-arrow">↕</span></th>
      </tr>
    </thead>
    <tbody>
      <tr><td>实施成本</td><td>高</td><td>中</td><td>低</td></tr>
      <tr><td>覆盖范围</td><td>全国</td><td>区域</td><td>城市</td></tr>
      <tr><td>见效速度</td><td>快</td><td>中</td><td>慢</td></tr>
      <tr><td>可持续性</td><td>强</td><td>中</td><td>弱</td></tr>
    </tbody>
  </table>
</div>
```

使用规则：
- 行数 3-10，列数 3-6（含首列标签）
- 首列是维度标签，左对齐加粗
- 数据单元格文字控制在 10 字以内

CSS：
```css
.cmp-wrap { overflow-x: auto; margin: 1.5rem 0; border: 1px solid #e2e8f0; border-radius: var(--radius, 8px); }
.cmp-table { width: 100%; border-collapse: collapse; font-size: 0.88rem; }
.cmp-table th {
  position: sticky; top: 0; z-index: 2; background: #f8fafc;
  padding: 0.6em 0.8em; text-align: left; font-weight: 600;
  border-bottom: 2px solid var(--accent); white-space: nowrap;
  cursor: pointer; user-select: none;
}
.cmp-table th:hover { background: #f1f5f9; }
.cmp-arrow { font-size: 0.75rem; opacity: 0.3; margin-left: 0.3em; }
.cmp-table th.sorted-asc .cmp-arrow, .cmp-table th.sorted-desc .cmp-arrow { opacity: 1; }
.cmp-table th.sorted-asc .cmp-arrow::after { content: ' \25B2'; }
.cmp-table th.sorted-desc .cmp-arrow::after { content: ' \25BC'; }
.cmp-table td { padding: 0.5em 0.8em; border-bottom: 1px solid #e2e8f0; }
.cmp-table tbody tr:nth-child(even) td { background: #f8fafc; }
.cmp-table tbody tr:hover td { background: #f1f5f9; }
.cmp-table tbody td:first-child { font-weight: 600; }
```

JS：
```html
<script>
// 对比表排序
(function(){document.querySelectorAll('[data-sortable] th[data-sort]').forEach(function(t){
t.addEventListener('click',function(){
var T=this.closest('table'),b=T.querySelector('tbody'),R=Array.from(b.querySelectorAll('tr'));
var i=Array.from(this.parentNode.children).indexOf(this),a=!this.classList.contains('sorted-asc');
T.querySelectorAll('th').forEach(function(h){h.classList.remove('sorted-asc','sorted-desc');});
this.classList.add(a?'sorted-asc':'sorted-desc');
R.sort(function(x,y){var u=x.children[i].textContent.trim(),v=y.children[i].textContent.trim();
var p=parseFloat(u),q=parseFloat(v);
if(!isNaN(p)&&!isNaN(q))return a?p-q:q-p;
return a?u.localeCompare(v,'zh-CN'):v.localeCompare(u,'zh-CN');});
R.forEach(function(r){b.appendChild(r);});});});})();
</script>
```

降级说明：
- **JS 未加载**：表格正常显示，排序功能不可用——粘性表头、斑马纹、悬停效果仍正常工作
- **不支持 `position: sticky`**（旧浏览器）：表头随页面滚动，不固定

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
  - 折叠分步：拆解复杂概念为 3-5 步 → 写 step-detail HTML
  - Tab 切换：多视角对比 → 写 tab-panel HTML
  - 对比滑块：before/after 效果展示 → 写 compare-slider HTML
  - 交互时间线：5-10 事件列表 → 写 tl-interactive HTML
  - 数据卡片：关键统计数字展示 → 写 data-grid HTML
  - 引文卡片：人物引言/文献引用 → 写 quote-card HTML
  - 标注图片：复杂图表/地图标注 → 写 annotated-img HTML
  - 状态链：阶段/进度展示 → 写 status-chain HTML
  - 数值动画：关键数字滚动 → 为 dg-value 加 data-countup
  - 标签组：关键词/分类展示 → 写 tag-group HTML
  - 提示框：突出提示/警告 → 写 callout HTML
  - 热力图：二维数据密度展示 → 写 heatmap HTML
  - 步骤指示：流程进度引导 → 写 step-indicator HTML
  - 信息面板：扩展内容侧边抽屉 → 写 info-panel HTML
  - 对比表高级：多维度数据表格 → 写 cmp-table HTML
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
| 折叠分步的 `sd-trigger` 未设 `cursor: pointer` | 用户不知可点击，交互意图不明确 | 始终包含 `cursor: pointer` 和 `border: none`，消除默认按钮样式 |
| 折叠展开动画中 `height` 从 `auto` 直接过渡 | CSS transition 无法从 `auto` 过渡到固定值，动画失效 | JS 中先测量 `scrollHeight` 再设 px 值，过渡结束后恢复 `auto` |
| Tab 面板中多个 `tab-pane` 同时 `display: block` | 所有视角内容重叠显示，视觉混乱 | 确保 JS 切换时先移除所有 `active` 类，再给目标添加 |
| 窄屏时 Tab 导航溢出 | 横向 Tab 过多时溢出容器，部分 Tab 看不到 | 已设 `.tab-nav { overflow-x: auto; }`，检查未误删此属性 |
| 对比滑块的两张图片尺寸不一致 | 图片错位导致对比效果失真 | 确保 before 和 after 图片宽高完全一致（用同一张原图裁切/调色） |
| 滑块 touch 事件中调用了 `e.preventDefault()` 但未设 `{passive: false}` | 某些浏览器忽略 preventDefault 并报警告 | touch 事件监听已设 `{passive: false}`，需确保复制代码时保留此选项 |
| 交互时间线的圆点 `::before` 被父元素 `overflow: hidden` 裁剪 | 时间线竖线穿过了圆点但圆点不完整 | 不要在 `.tl-interactive` 或 `.tli-item` 上设 `overflow: hidden` |
| 交互时间线事件 < 5 个仍使用此组件 | 视觉空洞，竖线过长但事件过少 | 事件 < 5 个时使用静态 CSS 时间线或列表 |
| 数据卡片的 `dg-value` 数值位数过多（6+ 位） | 数字太长在卡片内折行或溢出 | 使用缩写（如 8.8 万亿而非 8800000000000）或增大 `minmax` 值 |
| 数据卡片 < 3 张仍使用网格布局 | 只有 1-2 张卡片在宽屏上拉得极宽，视觉失衡 | 少于 3 张卡片时使用内联 flex 或段落展示 |
| 引文卡片连续使用超过 2 个 | 多个引文卡片堆叠失去强调效果，读者疲劳 | 每课最多用 1-2 张引文卡片，选最关键的一两句 |
| 引文卡片 `qc-text` 过短（< 10 字） | 一句话太短，配不上卡片容器的视觉重量 | 引文至少 20 字，过短时融入正文或使用 `<blockquote>` |
| 标注图片的坐标使用 px 而非百分比 | 图片缩放后标注点错位 | 始终使用百分比坐标（`left: 25%`），勿用 px |
| 标注点数量超过 6 个 | 图片被标注点覆盖，难以看清 | 标注点控制在 3-6 个，必要时拆分多张图片 |
| 状态链的 `sc-label` 超过 6 字 | 窄屏下文字溢出或换行破坏对齐 | 标签控制在 2-4 字，过长则用缩写 |
| 状态链全部为 `pending` | 整条链全灰，读者看不出任何进展信息 | 至少标注一个 `done` 或 `current` 状态 |
| `data-countup` 数值超过 999999 | 数字过长，动画卡顿或显示异常 | 用万/亿等单位缩写（如 `data-countup="88"` 配合单位 "百万"） |
| 页面中 `[data-countup]` 元素超过 8 个 | 同时触发多个 IntersectionObserver + 动画，性能开销大 | 控制在 8 个以内，或错开放置在不同视口区域 |
| 标签组中标签超过 8 个 | 多行标签降低可读性 | 精选控制 3-8 个 |
| 标签文字超过 6 字 | 标签被撑得太宽，破坏整体节奏 | 控制在 6 字以内，过长用缩写 |
| 提示框在一课中使用超过 4 次 | 彩色区块堆叠失去视觉冲击力 | 精选关键信息，每课最多 4 个提示框 |
| 提示框连续排列无正文间隔 | 各色区块挤在一起，难以区分 | 提示框之间至少隔 1 段正文 |
| 热力图数据全部相同（全 0 或全 4） | 整张图只有一种颜色，失去对比意义 | 确保数据分布有梯度，至少包含 3 种级别 |
| 热力图行列标签超过 6 字 | 单元格被标签文字撑宽，比例失调 | 标签控制在 4 字以内 |
| 步骤指示器全部为待办（无 `done`/`current`） | 整条全灰，读者看不出进度 | 至少标注一个 `done` 或 `current` |
| 步骤指示器标签超过 4 字 | 窄屏下标签换行或溢出 | 控制在 4 字以内 |
| 一课中使用信息面板超过 3 次 | 读者频繁开关面板，影响阅读流畅度 | 控制在 3 个以内，精选真正需要扩展的内容 |
| 信息面板内容在触发时被 `overflow: hidden` 裁剪 | 面板内长内容无法完整查看 | 确保面板设 `overflow-y: auto` |
| 对比表单元格文字超过 10 字 | 列宽被撑得参差不齐 | 控制在 10 字以内或用缩写 |
| 对比表 `th` 未设 `position: sticky` | 长表格滚动时表头消失，读者迷失 | 确保 `th` 包含 `position: sticky; top: 0;` |

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
| 1 | 课程中同时使用所有视觉组件（7+ 种） | 视觉密度过高，读者"喘不过气" | 每课选 2-3 个组件，和叙事节奏匹配 |
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
- [ ] 折叠分步组件 JS 正常工作（展开/收起动画平滑，`aria-expanded` 同步更新）

验证自动化：`python scripts/validate-lesson.py lessons/NNNN-slug.html` — 自动检查 SVG 路径/XML 有效性/颜色对比度、quiz 正确数/完整度、h1 数量、data-anim 语法、容器宽度、相对路径、PPT JS（主题+导航）存在性。
