# teach_more_pic Skill 架构指南

## 项目结构

```
SKILL.md                              ← 入口点：前置条件 + 工作流 + 路由表
.opencode/skills/
  teach_more_pic-core/                ← 核心工作流（Step 0-8）
  teach_more_pic-components/          ← 33 组件索引 + 决策指南
  teach_more_pic-design/              ← 视觉纪律 + 反模式
  teach_more_pic-refs/                ← 页面类型 + 失败模式 + 文件速查
  grill-me/                           ← 内嵌的拷问路由
  grilling/                           ← 内嵌的拷问流程
  fireworks-tech-graph/               ← 内嵌的 SVG 流程图指令
  teach/                              ← 内嵌的学习记录框架
  knowledge-graph/                    ← 内嵌的知识图谱指令
components/NN-name.md                 ← 组件文档（含 HTML/CSS/JS）
examples/name-demo.html               ← 组件独立示例
templates/lesson-starter.html         ← 课程骨架模板（必须从此复制）
scripts/validate-lesson.py            ← 验证器（21 项检查）
tests/test_validate.py                ← pytest 测试（109 项）
```

## 关键约定

### 自适应节奏
Step 0 grill 拷问后检测用户回复含 `直接干/少问/快速/fast/go` → 标记 `fast_pace=true`，跳过 Step 1/2/5/6/7 的 STOP，直抵 Step 4 验证。

### 子 Skill 路由
主 SKILL.md 末尾的"深入阅读"表列出了子 skill 路径。Agent 在需要深入某个领域（如组件选择、设计纪律、失败排查）时按需 load 对应子 skill。

### 组件编号
- 前缀与 SKILL.md 索引编号一致（24-28 对齐后，新组件续 29-33）
- 新组件加在 `components/` 下后，需同时更新 `teach_more_pic-components/SKILL.md` 的索引表
- 组件类名前缀：`cr-`（轮播）、`tw-`（打字机）、`px-`（视差）、`tt-`（Toast）、`cb-`（徽章）

### 验证规则
新增验证函数需两步：
1. 在 `scripts/validate-lesson.py` 中添加 `check_*` 函数
2. 在 `run_all()` 中注册
3. 在 `tests/test_validate.py` 中添加 pytest 测试（`test_*_pass` + `test_*_fails`）

### 内嵌依赖
所有前置 skill 已内嵌到 `.opencode/skills/`，无需外部安装。新增外部依赖时同样采用内嵌方式。
