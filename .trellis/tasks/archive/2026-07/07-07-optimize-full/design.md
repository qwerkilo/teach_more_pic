# Design: 全面优化方案

## B. 组件 #17 CSS 变量方案

**现状**：5 色硬编码，不随主题切换。
**方案 A**（推荐）：用 `color-mix()` 基于 `var(--accent)` 派生 5 种语义色，配合 `var(--bg)` 调底色。
```css
.tag-blue   { background: color-mix(in srgb, var(--accent) 15%, var(--bg)); color: var(--accent); }
.tag-red    { background: color-mix(in srgb, var(--error) 15%, var(--bg)); color: var(--error); }
.tag-green  { background: color-mix(in srgb, var(--success) 15%, var(--bg)); color: var(--success); }
.tag-orange { background: color-mix(in srgb, var(--warning) 15%, var(--bg)); color: var(--warning); }
.tag-purple { background: color-mix(in srgb, var(--accent) 20%, var(--bg)); color: color-mix(in srgb, var(--accent) 80%, var(--text)); }
```
**优势**：零 JS、主题自适应、保持 5 色语义。
**风险**：`color-mix()` 是 CSS Color 5 特性，现代浏览器支持 (>95%)。旧浏览器回退：tags 仍可见但无色差，功能不损失。

## C/D. 模板去重 + 同步机制

**去重策略**：
1. `lesson-starter.html` 中只保留 7 个代表性 TP items（warm/apple/spotify/nvidia/notion/x.ai/binance），其余 13 个由 PPT JS 动态注入 DOM
2. PPT JS 中删除 `t` 硬编码数组，改为 `document.querySelectorAll('.tp-item')` 收集
3. `index-spa.html` 同理

**JS 动态生成逻辑**（注入 PPT JS IIFE 内）：
```js
// 完整 20 主题列表作为数据（只在这一处）
var themes=[{id:'warm',color:'#c0392b',label:'暖色'},...];
// 检测 .tp-grid 中已有 item 数，不足则追加
```

**权衡**：主题数据仍在一处硬编码但只有 JS 中一份数据源，模板 HTML 只保留静态示例。

## E. 验证器新增检查

每项检查按 `check_xxx()` 函数实现，在 `run_all()` 中注册。保持已有 `[PASS]/[FAIL]` 输出格式。

## F. 品牌主题一致性

直接修改 `lesson-starter.html` 中 3 个主题块的 CSS 变量值。

## G. 组件编号

简单创建跳转文件 + 更新 decision-guide.md 措辞。
