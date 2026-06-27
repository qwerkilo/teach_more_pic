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

#### 7.5 主题选择器按钮（UI 方式切换，替代纯键盘）

在页面右下角添加一个浮动的主题选择器，方便不熟悉 T 键的用户切换主题。包含 4 个彩色圆点按钮，当前主题高亮。

HTML（放在 `<body>` 末尾，JS 之前）——使用组合工具栏（主题选择器 + 浮动目录）：
```html
<div class="ui-toolbar">
  <div class="theme-picker" role="toolbar" aria-label="切换主题">
    <button class="tp-btn active" data-theme="warm" style="--tp-color:#c0392b;" title="暖色"></button>
    <button class="tp-btn" data-theme="apple" style="--tp-color:#0066cc;" title="Apple"></button>
    <button class="tp-btn" data-theme="minimax" style="--tp-color:#ff5530;" title="Minimax"></button>
    <button class="tp-btn" data-theme="nvidia" style="--tp-color:#76b900;" title="NVIDIA"></button>
  </div>
  <button class="toc-btn" aria-label="目录" title="目录">📑</button>
</div>
<nav class="toc-panel"><ul class="toc-list"></ul></nav>
```

CSS（放在课程 `<style>` 中）——主题选择器 + TOC 共用样式：
```css
.ui-toolbar { position: fixed; bottom: 20px; right: 20px; z-index: 999; display: flex; align-items: center; gap: 8px; padding: 6px 12px; background: rgba(255,255,255,0.85); backdrop-filter: blur(6px); border-radius: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
.theme-picker { display: flex; gap: 6px; }
.tp-btn { width: 18px; height: 18px; border-radius: 50%; border: 2px solid transparent; background: var(--tp-color); cursor: pointer; padding: 0; transition: transform 0.2s ease, border-color 0.2s ease; }
.tp-btn:hover { transform: scale(1.2); }
.tp-btn.active { border-color: var(--text); transform: scale(1.15); }
.toc-btn { background: none; border: none; font-size: 1.1rem; cursor: pointer; padding: 0 2px; line-height: 1; opacity: 0.6; transition: opacity 0.2s ease; color: var(--text); }
.toc-btn:hover { opacity: 1; }
.toc-panel { position: fixed; bottom: 70px; right: 20px; z-index: 998; background: var(--bg); border: 1px solid #e2e8f0; border-radius: var(--radius, 8px); padding: 0.6em 0; box-shadow: 0 4px 12px rgba(0,0,0,0.08); max-height: 50vh; overflow-y: auto; display: none; min-width: 160px; }
.toc-panel.open { display: block; }
.toc-list { list-style: none; margin: 0; padding: 0; }
.toc-item { padding: 0.4em 1em; font-size: 0.82rem; cursor: pointer; color: #64748b; transition: color 0.15s ease, background 0.15s ease; }
.toc-item:hover { background: rgba(0,0,0,0.03); color: var(--text); }
.toc-item.active { color: var(--accent); font-weight: 600; background: rgba(0,0,0,0.02); }
```

JS（在 PPT 运行时模板中整合）——主题选择器 + TOC 处理：
```js
try{document.querySelectorAll('.tp-btn').forEach(function(b){b.addEventListener('click',function(){
var th=this.dataset.theme;d.dataset.theme=th;i=t.indexOf(th);
document.querySelectorAll('.tp-btn').forEach(function(x){x.classList.toggle('active',x.dataset.theme===th);});});});
}catch(e){}
try{var tl=document.querySelector('.toc-list');if(tl){var h2s=document.querySelectorAll('h2');
h2s.forEach(function(h,i){var li=document.createElement('li');li.className='toc-item';li.textContent=h.textContent;
li.addEventListener('click',function(){h.scrollIntoView({behavior:'smooth'});
document.querySelector('.toc-panel').classList.remove('open');});tl.appendChild(li);});
document.querySelector('.toc-btn').addEventListener('click',function(){
document.querySelector('.toc-panel').classList.toggle('open');});
var to=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){
var idx=Array.from(h2s).indexOf(e.target);
document.querySelectorAll('.toc-item').forEach(function(x,i){x.classList.toggle('active',i===idx);});}});},
{rootMargin:'-80px 0px -60% 0px'});h2s.forEach(function(h){to.observe(h);});
document.addEventListener('click',function(e){if(!e.target.closest('.ui-toolbar')&&!e.target.closest('.toc-panel')){
document.querySelector('.toc-panel').classList.remove('open');}});}
}catch(e){}

#### 7.6 JS 运行时模板

课程末尾的 `<script>` 块（在 quiz JS 之后）追加：

```html
<script>
// PPT 质感增强 — 含降级处理
(function(){var t=['warm','apple','minimax','nvidia'],i=t.indexOf(document.documentElement.dataset.theme)||0,d=document.documentElement;
try{document.querySelectorAll('.tp-btn').forEach(function(b){b.addEventListener('click',function(){
var th=this.dataset.theme;d.dataset.theme=th;i=t.indexOf(th);
document.querySelectorAll('.tp-btn').forEach(function(x){x.classList.toggle('active',x.dataset.theme===th);});});});
}catch(e){}
try{document.addEventListener('keydown',function(e){if(e.key==='t'&&!e.ctrlKey&&!e.metaKey){i=(i+1)%t.length;d.dataset.theme=t[i];
document.querySelectorAll('.tp-btn').forEach(function(x){x.classList.toggle('active',x.dataset.theme===t[i]);});}});
}catch(e){} // 主题切换降级：静默失败
try{var tl=document.querySelector('.toc-list');if(tl){var h2s=document.querySelectorAll('h2');
h2s.forEach(function(h,i){var li=document.createElement('li');li.className='toc-item';li.textContent=h.textContent;
li.addEventListener('click',function(){h.scrollIntoView({behavior:'smooth'});
document.querySelector('.toc-panel').classList.remove('open');});tl.appendChild(li);});
document.querySelector('.toc-btn').addEventListener('click',function(){
document.querySelector('.toc-panel').classList.toggle('open');});
var to=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){
var idx=Array.from(h2s).indexOf(e.target);
document.querySelectorAll('.toc-item').forEach(function(x,i){x.classList.toggle('active',i===idx);});}});},
{rootMargin:'-80px 0px -60% 0px'});h2s.forEach(function(h){to.observe(h);});
document.addEventListener('click',function(e){if(!e.target.closest('.ui-toolbar')&&!e.target.closest('.toc-panel')){
document.querySelector('.toc-panel').classList.remove('open');}});}
}catch(e){} // 浮动目录降级：静默失败
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
