# 可选页面类型

> 本文档是 `SKILL.md` 的参考附件。主工作流在 SKILL.md 中，此处只列布局模板。

在纵向滚读课程中，以下特殊页可以打破单调的"标题→段落→图→标题"节奏。

## 封面页（Cover Page）

每课必须使用，展示课程编号、标题、副标题、引子。中英双语版使用 `data-lang` 成对包裹：

```html
<div class="cover-page" data-lang="zh">
  <div class="cover-badge">第 5 课</div>
  <h1><span class="shiny-text">MMT 现代货币理论</span></h1>
  <p class="cover-subtitle">政府债务真的是未来的负担吗？</p>
  <p class="cover-hook">当一个国家可以无限制发行自己的货币，它的支出真的需要税收来"买单"吗？</p>
</div>
<div class="cover-page" data-lang="en" style="display:none;">
  <div class="cover-badge">Lesson 5</div>
  <h1><span class="shiny-text">Modern Monetary Theory</span></h1>
  <p class="cover-subtitle">Is government debt really a burden on the future?</p>
  <p class="cover-hook">When a nation can issue its own currency without limit, does it really need taxes to "pay for" its spending?</p>
</div>
```

```css
.cover-page { text-align: center; padding: 4rem 1rem 2rem; margin-bottom: 2rem; }
.cover-badge { display: inline-block; padding: 0.2em 1.2em; background: var(--accent); color: var(--accent-text); border-radius: 20px; font-size: 0.8rem; font-weight: 600; letter-spacing: 0.05em; }
.cover-subtitle { font-size: 1.15rem; color: var(--muted); margin-top: 0.6em; max-width: 600px; margin-left: auto; margin-right: auto; }
.cover-hook { font-size: 0.95rem; color: var(--muted); margin-top: 1em; font-style: italic; max-width: 500px; margin-left: auto; margin-right: auto; line-height: 1.6; }
```

**效果**：badge 药丸形、shiny-text 光泽扫光动画（已内置在模板 CSS 中）、副标题居中约束宽度。

## 章节分隔页（Section Divider）

在三幕叙事之间插入，标记叙事阶段的切换。含装饰性顶部强调线 + 圆形编号：

```html
<div class="section-divider" data-lang="zh">
  <div class="divider-line"></div>
  <span class="divider-num">第一幕</span>
  <h2>矛盾：MMT 的承诺与疑点</h2>
  <p class="divider-desc">在深入 MMT 之前，先理解它试图解决什么根本问题。</p>
</div>
<div class="section-divider" data-lang="en" style="display:none;">
  <div class="divider-line"></div>
  <span class="divider-num">Act I</span>
  <h2>The Contradiction</h2>
  <p class="divider-desc">Before diving into MMT, understand the fundamental problem it tries to solve.</p>
</div>
```

```css
.section-divider { text-align: center; padding: 2.5rem 1rem; margin: 3rem 0; }
.divider-line { width: 60px; height: 3px; background: var(--accent); border-radius: 2px; margin: 0 auto 1rem; }
.divider-num { display: inline-block; width: 44px; height: 44px; line-height: 44px; background: var(--accent); color: var(--accent-text); border-radius: 50%; font-size: 0.8rem; font-weight: 600; letter-spacing: 0.05em; margin-bottom: 0.5em; }
.section-divider h2 { border-bottom: none; margin-top: 0.3em; font-size: var(--h2-size, 1.5rem); }
.divider-desc { color: var(--muted); font-size: 0.95rem; max-width: 500px; margin: 0.5em auto 0; }
```

**效果**：顶部短强调线、圆形编号（非药丸）、居中约束描述文字。

## 总结卡片（Summary Cards）

课程结束时、测验前插入。使用 SVG 图标替代 emoji，保证各主题下渲染一致：

```html
<div class="summary-cards" data-lang="zh">
  <div class="summary-card">
    <svg class="summary-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>
    <strong>核心洞察</strong>
    <p>MMT 认为主权货币发行国不会"破产"——但这个权力有通胀这个天然上限。</p>
  </div>
  <div class="summary-card">
    <svg class="summary-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"/></svg>
    <strong>与后续课程的联系</strong>
    <p>第 7 课将展示 MMT 在日本的实践——一个主权货币国家如何管理巨额债务。</p>
  </div>
  <div class="summary-card">
    <svg class="summary-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
    <strong>开放问题</strong>
    <p>如果 MMT 的理论正确，为什么大部分国家仍然坚持财政紧缩？是政治约束还是理论缺陷？</p>
  </div>
</div>
<div class="summary-cards" data-lang="en" style="display:none;">
  <div class="summary-card">
    <svg class="summary-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>
    <strong>Key Insight</strong>
    <p>MMT argues sovereign currency issuers cannot go bankrupt — but this power has inflation as its natural ceiling.</p>
  </div>
  <div class="summary-card">
    <svg class="summary-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"/></svg>
    <strong>Next Lesson</strong>
    <p>Lesson 7 will show MMT in practice in Japan — how a sovereign currency nation manages massive debt.</p>
  </div>
  <div class="summary-card">
    <svg class="summary-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
    <strong>Open Question</strong>
    <p>If MMT is correct, why do most countries still practice fiscal austerity? Political constraints or theoretical flaws?</p>
  </div>
</div>
```

```css
.summary-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin: 2.5rem 0; }
.summary-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius, 8px); padding: 1.3rem; transition: box-shadow 0.2s, transform 0.2s; }
.summary-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.08); transform: translateY(-2px); }
.summary-icon { width: 28px; height: 28px; display: block; margin-bottom: 0.5rem; color: var(--accent); }
.summary-card strong { display: block; font-size: 0.95rem; margin-bottom: 0.3em; }
.summary-card p { font-size: 0.85rem; color: var(--muted); line-height: 1.5; margin: 0; }
```

**效果**：SVG 矢量图标（lightbulb/link/question）、hover 微上浮、等宽 28px 图标对齐。

## 全宽引文页（Full-Width Quote）

用于幕与幕之间或关键转折处，让某句核心论断单独占据一整个视区高度：

```html
<div class="quote-spread">
  <blockquote>
    <p>"主权货币发行国不会因为本币债务而破产——正如美元不会因为美国人欠美元而违约。"</p>
    <cite>— Stephanie Kelton, 《赤字神话》</cite>
  </blockquote>
</div>
```

```css
.quote-spread { display: flex; align-items: center; justify-content: center; min-height: 40vh; padding: 3rem 2rem; margin: 3rem 0; background: var(--surface); border-left: 4px solid var(--accent); border-radius: 0 var(--radius, 8px) var(--radius, 8px) 0; }
.quote-spread blockquote { max-width: 600px; }
.quote-spread blockquote p { font-size: 1.15rem; line-height: 1.7; font-style: italic; color: var(--text); }
.quote-spread cite { display: block; margin-top: 1em; font-size: 0.85rem; color: var(--muted); font-style: normal; }
```

**效果**：左侧 accent 竖线、最小 40vh 高度、居中约束宽度。

## 关键数字页（Number Spotlight）

在需要强调某个关键数据时使用——让一个数字占据视觉焦点：

```html
<div class="num-spotlight">
  <span class="num-value">$28<span class="num-unit">万亿</span></span>
  <p class="num-label">美国国债总额（2024）</p>
</div>
```

```css
.num-spotlight { text-align: center; padding: 3rem 1rem; margin: 2.5rem 0; background: var(--surface); border-radius: var(--radius, 8px); }
.num-value { font-size: 3rem; font-weight: 700; color: var(--accent); display: block; line-height: 1; }
.num-unit { font-size: 1.2rem; font-weight: 400; opacity: 0.7; margin-left: 0.15em; }
.num-label { font-size: 0.9rem; color: var(--muted); margin-top: 0.5em; max-width: 400px; margin-left: auto; margin-right: auto; }
```

**效果**：超大数字 + accent 色、单位小字、标签居中约束。

## 信息面板侧边栏（Info Sidebar）

用于术语解释、背景补充等次要内容，不打断正文流：

```html
<aside class="info-sidebar">
  <h4>💡 什么是"主权货币"？</h4>
  <p>主权货币是指由国家政府发行、不承诺兑换为任何特定数量黄金或其他货币的货币。美元、日元、人民币都是主权货币。</p>
</aside>
```

```css
.info-sidebar { float: right; width: 280px; margin: 0.5em 0 0.5em 1.5em; padding: 1rem; background: var(--surface); border-radius: var(--radius, 8px); border: 1px solid var(--border); font-size: 0.85rem; }
.info-sidebar h4 { font-size: 0.9rem; margin-bottom: 0.4em; }
.info-sidebar p { color: var(--muted); line-height: 1.5; }
@media (max-width: 600px) { .info-sidebar { float: none; width: 100%; margin: 1em 0; } }
```

**效果**：右浮动侧边栏、窄屏自动降级为行内块。

## 使用规则

- **封面页**：每课必须使用（替换当前课程开头的 info-box 开场）
- **章节分隔页**：三幕叙事时使用，放在第一幕和第二幕之间、第二幕和第三幕之间
- **总结卡片**：每课必须使用（测验前，3 张）
- **全宽引文页**：可选，用于关键论断强调
- **关键数字页**：可选，用于数据密集型课程
- **信息面板侧边栏**：可选，用于补充性背景知识
