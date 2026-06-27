# 可选页面类型

> 本文档是 `SKILL.md` 的参考附件。主工作流在 SKILL.md 中，此处只列布局模板。

在纵向滚读课程中，以下特殊页可以打破单调的"标题→段落→图→标题"节奏。

## 封面页（Cover）

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
.cover-badge { display: inline-block; padding: 0.2em 1em; background: var(--accent); color: var(--accent-text); border-radius: 3px; font-size: 0.85rem; letter-spacing: 0.05em; margin-bottom: 1em; }
.cover-subtitle { font-size: 1.1rem; color: var(--muted); margin-top: 0.5em; }
.cover-hook { font-size: 0.95rem; color: var(--muted); margin-top: 1em; font-style: italic; }
```

## 章节分隔页（Section Divider）

在三幕叙事之间插入，标记叙事阶段的切换：

```html
<div class="section-divider">
  <span class="divider-num">第一幕</span>
  <h2>设置矛盾</h2>
  <p>这一部分将讨论……</p>
</div>
```

```css
.section-divider { text-align: center; padding: 3rem 1rem; margin: 3rem 0; background: var(--bg); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }
.divider-num { display: inline-block; padding: 0.1em 0.8em; background: var(--accent); color: var(--accent-text); border-radius: 3px; font-size: 0.8rem; letter-spacing: 0.05em; margin-bottom: 0.5em; }
.section-divider h2 { border-bottom: none; margin-top: 0.3em; }
```

## 总结页（Summary Cards）

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
.summary-card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.2rem; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
.summary-icon { font-size: 1.5rem; display: block; margin-bottom: 0.3em; }
```

## 使用规则

- **封面页**：每课必须使用（替换当前课程开头的 info-box 开场）
- **章节分隔页**：三幕叙事时使用，放在第一幕和第二幕之间、第二幕和第三幕之间
- **总结页**：长篇课程（>3000 字）使用，短课可跳过
