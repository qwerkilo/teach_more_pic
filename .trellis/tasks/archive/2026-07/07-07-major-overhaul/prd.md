# PRD: 大刀阔斧改进 teach_more_pic

## 决策记录（grill session）

- 主轴顺序：abcde（流程→组件→架构→质量→门槛）
- a（流程）：自适应节奏，Step 0 末尾判断快/慢模式，快模式跳过所有中间 STOP 直到 Step 4
- b（组件）：先做微交互象限，5 个：轮播 / 打字机 / 视差滚动 / 浮动提醒 / 计数器徽章
- c（架构）：纵向拆分子 skill（core / components / design / refs），主 skill 自动路由
- d（质量）：测试覆盖 + 验证规则扩充
- e（门槛）：全量内嵌 4 个前置依赖 + cairosvg 替代

## parent-child 结构

```
parent: major-overhaul
  ├─ child 1: 全量内嵌前置依赖（fireworks-tech-graph / teach / grill-me / knowledge-graph-map）
  ├─ child 2: SKILL.md 纵向拆分子 skill
  ├─ child 3: 自适应节奏工作流
  ├─ child 4: 微交互组件 × 5（轮播/打字机/视差/浮动提醒/计数器徽章）
  └─ child 5: 测试覆盖 + 验证规则扩充
```

## 跨 child 依赖

- child 1 ← child 2（新 skill 结构依赖内嵌后的边界）
- child 2 ← child 3（工作流修改依赖新 skill 结构）
- child 4、child 5 独立于前 3 个，可并行
