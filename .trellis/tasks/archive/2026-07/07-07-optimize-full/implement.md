# Implement: 全面优化执行计划

## 执行顺序

每个子项独立可验收，按复杂度递增排序。

### 1. A — 数值一致性修正（5min）
- [ ] 修改 6 处文件中的数值
- [ ] `python -m pytest tests/ -v` 保证测试通过
- [ ] **验收**：grep 确认所有 6 处已修正

### 2. F — 品牌主题一致性（5min）
- [ ] `bmw-m`：`--bg: #000000` → `#1a1a1a`
- [ ] `dell-1996`：`--text: #000000` → `#1a1a1a`
- [ ] `spotify`：`--surface-raised` 对比度增强
- [ ] **验收**：`lesson-starter.html` 中 grep 无 `#000000`

### 3. G — 组件编号跳转（5min）
- [ ] 创建 `components/24-ECharts-index.md` 跳转文件
- [ ] 更新 `references/decision-guide.md:5` 措辞
- [ ] **验收**：`components/` 无断裂感

### 4. B — 组件 #17 CSS 变量化（10min）
- [ ] 修改 `components/17-标签徽章组.md` CSS 块
- [ ] 同步修改 `templates/lesson-starter.html` 中 #17 CSS
- [ ] **验收**：`tag-group-demo.html` 页面主题切换后标签色变化

### 5. E — 验证器新增检查（20min）
- [ ] 在 `scripts/validate-lesson.py` 实现 5 个新 `check_*` 函数
- [ ] 在 `run_all()` 中注册
- [ ] 在 `tests/test_validate.py` 添加对应 pytest 用例
- [ ] `python -m pytest tests/ -v` 全部通过
- [ ] **验收**：109+ 项测试全部通过

### 6. C+D — 模板去重 + 同步机制（30min）
- [ ] 修改 `lesson-starter.html`：保留 7 个 TP items，其余由 JS 动态生成
- [ ] 修改 PPT JS：删除 `t` 硬编码数组，改为数据驱动
- [ ] 同步修改 `templates/index-spa.html`
- [ ] 浏览器打开 `lesson-starter.html` 验证 20 主题全部可用
- [ ] **验收**：模板 ≤600 行，20 主题功能完整

## 验证命令

```bash
python -m pytest tests/ -v
python scripts/validate-lesson.py templates/lesson-starter.html
```

## 回滚点

每完成一个子项即 `git add` + `git commit`（不成文——用户确认后提交），确保任意子项可单独回滚。
