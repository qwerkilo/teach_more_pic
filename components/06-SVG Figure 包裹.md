### 6. SVG Figure 包裹（标准容器）

用于包裹内联 SVG。相比 `<img src="...">`，内联 SVG 支持 CSS 变量继承、响应式缩放、可被 `<use>` 引用。

```html
<figure class="svg-fig">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 900">
    <!-- SVG 内容 -->
  </svg>
</figure>
```

```css
.svg-fig { margin: 1.5rem auto; text-align: center; }
.svg-fig svg { max-width: 100%; height: auto; border-radius: 8px; }
```
