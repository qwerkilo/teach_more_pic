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
