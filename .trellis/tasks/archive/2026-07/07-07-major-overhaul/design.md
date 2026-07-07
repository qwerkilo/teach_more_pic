# 整体设计

## 结构变化

```
teach_more_pic/
├── SKILL.md                          ← 编排入口，精简为工作流 + 路由
├── .opencode/skills/
│   ├── teach_more_pic-core/SKILL.md  ← 工作流 Step 0-8（含内嵌的 grill 指令）
│   ├── teach_more_pic-components/SKILL.md  ← 28+ 组件索引 + 决策指南 + 使用规则
│   ├── teach_more_pic-design/SKILL.md      ← 视觉纪律 + 反模式 + 写作风格 + 主题
│   ├── teach_more_pic-refs/SKILL.md        ← 页面类型 + 失败模式 + 文件速查
│   ├── fireworks-tech-graph/SKILL.md       ← 内嵌（SVG 流程图）
│   ├── grill-me/SKILL.md                   ← 内嵌（需求拷问）
│   └── knowledge-graph/SKILL.md            ← 内嵌（知识图谱）
├── components/                      ← 28+ 组件文件（不变）
├── templates/                       ← 模板文件（不变）
├── references/                      ← 决策指南 + 页面类型（不变）
├── libs/                            ← 离线包（不变）
└── scripts/                         ← 验证器（不变）
```

## 自适应节奏

新增 Step 0 末尾信号检测：用户回复含"直接干/少问/快速/fast/go"等关键字 → 标记 fast_pace=true，跳过 Step 1/2/5/6/7 的 STOP。
