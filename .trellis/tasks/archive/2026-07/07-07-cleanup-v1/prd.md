# PRD: 项目清理

## 范围

轻量级清理任务，不涉及功能变更。

## 清单

1. 删除 `examples/` 下冲突残留文件
2. 清理 `.gitignore` 中被同步污染的冲突条目
3. 移除旧测试 `scripts/test_validate.py`，统一使用 `tests/test_validate.py`（pytest）
4. 更新 `scripts/run-tests.ps1` 不再引用 scripts/ 下的旧测试
5. 删除 `libs/.gitkeep`（多余）

## 验收标准

- [ ] `examples/` 下无 `(Conflicted copy*` 文件
- [ ] `.gitignore` 无冲突残留行（第 11-14 行已清除）
- [ ] `scripts/test_validate.py` 已移除
- [ ] `run-tests.ps1` 运行正常（仅 pytest）
- [ ] `libs/.gitkeep` 已删除
