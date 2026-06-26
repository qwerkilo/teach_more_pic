# teach_more_pic — 视觉增强课程制作

配合 base `teach` skill 使用的视觉增强技能，为每节课程注入 PPT 级的视觉品质。

## 能力

- **SVG 流程图** — 四色语义（蓝/橙/红/绿）的彩色流程图，替换传统 ASCII 图
- **CSS 时间线** — 垂直时间轴组件，替代事件表格
- **CSS 条形图** — 水平数据条，让统计数字"可见"
- **角色卡片** — 网格化角色介绍卡片，替代文本列表
- **对比表** — 多维度 flex 对比布局
- **PPT 质感** — 主题切换（T 键）、滚动入场动画、键盘章节导航（← →）
- **三幕叙事** — 设置矛盾 → 危机爆发 → 转折与遗产

## 使用方法

```bash
# 验证课程 HTML
python scripts/validate-lesson.py lessons/NNNN-slug.html
```

## 项目结构

```
├── SKILL.md                        # 技能定义与完整文档
├── scripts/
│   └── validate-lesson.py          # 课程验证脚本
├── templates/
│   ├── flowchart-vertical.svg      # 纵向流程图骨架
│   ├── timeline-horizontal.svg     # 横向时间线骨架
│   ├── cycle-diagram.svg           # 环形循环图骨架
│   └── comparison-side-by-side.svg # 左右对比图骨架
├── theme/
│   ├── apple/                      # Apple 主题定义
│   ├── minimax/                    # Minimax 主题定义
│   └── nvidia/                     # NVIDIA 主题定义
├── test-prompts.json               # 测试提示词
└── README.md
```

## 前置依赖

- `fireworks-tech-graph` skill（SVG 流程图创建）
- `cairosvg`（`pip install cairosvg`，SVG → PNG 导出）
