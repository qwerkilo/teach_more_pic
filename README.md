# teach_more_pic — 视觉增强课程制作

配合 [base `teach` skill](https://github.com/mattpocock/skills/tree/main/teach) 使用的视觉增强技能，为每节课程注入 PPT 级的视觉品质。

> 需要先安装 base `teach` skill——本项目是它的视觉增强插件，两者缺一不可。

## 安装

### 前提

本技能需要 [opencode](https://opencode.ai) 环境。已安装了以下 base skill：
- [teach](https://github.com/mattpocock/skills/tree/main/teach) — 基础课程制作技能（必装）
- `fireworks-tech-graph` — SVG 流程图创建（可选，用于自动生成流程图）

### 手动安装

```bash
# 克隆到 opencode 的 skills 目录
cd ~/.agents/skills
git clone https://github.com/qwerkilo/teach_more_pic

# 同时安装 base teach skill（位于 mattpocock/skills 仓库中）
git clone https://github.com/mattpocock/skills
# 然后复制或链接 skills/teach 到 .agents/skills/teach
```

### 通过 AGENTS.md 配置

在项目根目录的 `AGENTS.md` 中引用这两个 skill：

```
Skills: teach, teach_more_pic
```

## 能力

- **SVG 流程图** — 四色语义（蓝/橙/红/绿）的彩色流程图，替换传统 ASCII 图
- **CSS 时间线** — 垂直时间轴组件，替代事件表格
- **CSS 条形图** — 水平数据条，让统计数字"可见"
- **角色卡片** — 网格化角色介绍卡片，替代文本列表
- **对比表** — 多维度 flex 对比布局
- **PPT 质感** — 主题切换（T 键）、滚动入场动画、键盘章节导航（← →）
- **三幕叙事** — 设置矛盾 → 危机爆发 → 转折与遗产

## 使用方法

在 opencode 中同时激活两个 skill：

```
Skills: teach, teach_more_pic
```

base `teach` 负责课程结构、mission、learning records；`teach_more_pic` 负责视觉组件（流程图、时间线、条形图等）。

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
