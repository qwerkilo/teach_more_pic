# teach_more_pic — 视觉增强课程制作

配合 [base `teach` skill](https://github.com/mattpocock/skills/tree/main/teach) 使用的视觉增强技能，为每节课程注入 PPT 级的视觉品质。

> 需要先安装 base `teach` skill——本项目是它的视觉增强插件，两者缺一不可。

## 安装

### 前提

本技能需要 [opencode](https://opencode.ai) 环境。已安装了以下 base skill：
- [teach](https://github.com/mattpocock/skills/tree/main/teach) — 基础课程制作技能（必装）
- [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) — SVG 流程图创建（**必备**，本技能所有 SVG 流程图依赖此 skill）

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

在项目根目录的 `AGENTS.md` 中引用这些 skill：

```
Skills: teach, teach_more_pic, fireworks-tech-graph
```

## 能力

**核心视觉组件：**
- **SVG 流程图** — 四色语义（蓝/橙/红/绿）的彩色流程图，替换传统 ASCII 图
- **CSS 时间线** — 垂直时间轴组件，替代事件表格
- **CSS 条形图** — 水平数据条，让统计数字"可见"
- **角色卡片** — 网格化角色介绍卡片，替代文本列表
- **对比表（增强版）** — 粘性表头、斑马纹、点击排序

**交互式组件：**
- **折叠式分步详解** — 复杂概念分步折叠，点击展开
- **Tab 切换面板** — 垂直 Tab 切换多视角内容
- **图片对比滑块** — 拖拽滑块对比 before/after 图片
- **交互式时间线** — 点击时间点展开事件详情
- **标注式图片** — 图片上数字标注点，点击弹出说明
- **信息面板/侧边栏** — 右侧滑入抽屉展示扩展内容

**数据展示组件：**
- **数据卡片网格** — 关键数据卡片（图标 + 数值 + 标签）
- **数值滚动动画** — 数字从 0 滚动到目标值，进入视口触发
- **热力图/密度图** — 5 级绿→黄→红信号灯彩色矩阵
- **状态链** — 水平连接线里程碑（done/current/pending）
- **步骤指示器** — 水平编号步骤条（已完成/当前/待办）

**辅助组件：**
- **标签/徽章组** — 5 色药丸标签分类展示
- **提示框/告警条** — 4 类型彩色提示框（信息/警告/错误/成功）
- **引用/引文卡片** — 左侧强调色竖条 + 引文 + 署名

**PPT 质感：**
- 主题切换（T 键循环 4 主题）、滚动入场动画、键盘章节导航（← →）
- **三幕叙事** — 设置矛盾 → 危机爆发 → 转折与遗产
- 可选的封面页、章节分隔页、总结页

## 使用方法

在 opencode 中同时激活两个 skill：

```
Skills: teach, teach_more_pic
```

base `teach` 负责课程结构、mission、learning records；`teach_more_pic` 负责视觉组件。

```bash
# 验证课程 HTML
python scripts/validate-lesson.py lessons/NNNN-slug.html
```

## 项目结构

```
├── SKILL.md                        # 技能定义与完整文档（入口）
├── AGENTS.md                       # 快捷指令（gitignored）
├── scripts/
│   └── validate-lesson.py          # 课程验证脚本（9 项检查）
├── templates/                      # SVG 骨架模板（4 个 .svg）
├── examples/                       # 视觉组件示例文件（15 个 .html）
├── theme/
│   ├── apple/                      # Apple 主题设计参考
│   ├── minimax/                    # Minimax 主题设计参考
│   └── nvidia/                     # NVIDIA 主题设计参考
├── test-prompts.json               # 测试提示词
└── README.md
```

## 前置依赖

- [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) skill（**必备**，所有 SVG 流程图依赖此 skill）
- `cairosvg`（`pip install cairosvg`，SVG → PNG 导出）
