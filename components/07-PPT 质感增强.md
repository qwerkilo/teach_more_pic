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
