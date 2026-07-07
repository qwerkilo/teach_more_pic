---
name: teach_more_pic-core
description: 课程制作核心工作流 — 从需求拷问到完整 HTML 课程的全流程编排。
---

# 课程制作工作流

## 核心约定（所有课程必须遵守）

- **无构建系统**：纯 HTML/CSS/JS，无 package.json、无 npm 命令
- **中英双语**：内容/UI/SVG 文本须同时包含中英版本，通过语言切换按钮切换，默认中文
- SVG 中文字体需显式指定 font-family（含中文字体名）
- 课程文件：`lessons/NNNN-slug.html`（4 位编号 + 英文短名），SVG 同名同目录
- 跨课链接：`<a href="NNNN-slug.html">`（无前导 `/`，无完整 URL）

## 课程叙事框架

每课采用三幕叙事：

```
第一幕：设置矛盾  →  某个问题或制度设计的先天缺陷
第二幕：危机爆发  →  具体事件链，谁是推手，谁是受害者
第三幕：转折与遗产  →  解决方案、制度创新、与其它课程的联系
```

每幕结束时插入一个**视觉停顿**（SVG 流程图、时间线、对比表）。

## 🔴 重要纪律

- **所有课程必须从 `templates/lesson-starter.html` 复制作为基础**
- 保留模板的完整 CSS 变量系统（`:root` + 20 个 `[data-theme]`）、工具栏、键盘快捷键
- 只修改：封面标题/描述、正文内容、组件 HTML/CSS/JS、测验内容
- 组件在 `<!-- INSERT: 组件 HTML/CSS/JS -->` 注释处追加

## Step 0: 需求拷问

使用 `grill-me` skill 对用户进行需求拷问，澄清：
- 课程主题与目标受众
- 核心叙事矛盾
- 预期数据/数字
- 参考与风格偏好
- **是否希望大量使用 3D 类型组件**（Three.js #25 / ECharts GL #28 / D3.js #27）

🛑 STOP：等待用户确认后再进入 Step 1。

## Step 1: 确定叙事框架（三幕）

输出三段式大纲（每幕 2-3 句话），展示给用户确认。
🛑 STOP：用户确认后进入 Step 2。

## Step 2: 设计视觉组件

- 从组件索引表选择组件：第一幕 2+ 个、第二幕 2+ 个、第三幕 2+ 个，**最少 6 个**（含标签组 #17）
- 打开 `components/NN-name.md` 读取完整代码
- 每个 SVG 创建后立即验证：`python -c "import xml.etree.ElementTree as ET; ET.parse('path.svg')"`
- SVG 需同时保存为 `lessons/svg/NNNN-slug.svg` + 内联到 HTML

🛑 STOP：用户确认后进入 Step 3。

## Step 3: 写 HTML

从 `templates/lesson-starter.html` 复制。最终结构：

```
lessons/NNNN-slug.html
├── <html lang="zh-CN" data-theme="warm">
│   ├── <head>
│   │   ├── <style>  ← 模板 CSS + 组件 CSS
│   │   └── </head>
│   ├── <body>
│   │   ├── <article class="cover-page">
│   │   ├── <section class="section-divider">  ← 第一幕
│   │   ├── <figure class="svg-fig"><svg>...
│   │   ├── <!-- INSERT: 组件 HTML -->
│   │   ├── <section class="section-divider">  ← 第二幕
│   │   ├── ... 组件 + 正文 ...
│   │   ├── <section class="section-divider">  ← 第三幕
│   │   ├── <aside class="summary-cards">  ← 3 张总结卡片
│   │   ├── <div class="quiz-section">  ← 5 题双语测验
│   │   ├── <div class="ui-toolbar">
│   │   ├── <!-- Quiz JS -->
│   │   ├── <!-- PPT 质感增强 JS -->
│   │   └── <!-- 组件 JS -->
│   └── </body>
```

组件 CSS 合并到 `<style>` 中按前缀分组。组件 JS 放在 PPT 增强 JS 下方。

## Step 4: 验证

- 浏览器打开检查渲染
- `python -c "import xml.etree.ElementTree as ET; ET.parse('path.svg')"`
- 交叉链接检查（确认相对路径）
- 测验 5 题，每题 3 个选项
- 🔴 失败 → 修复 → 重跑 → 全过再继续

🛑 STOP：全部通过后进入 Step 5。

## Step 5: 配套产出

- 调用 `teach` skill 的 learning-record 模板生成学习记录
- EPUB 重建（如适用）
- 课程间链接验证

🛑 STOP：用户确认后进入 Step 6。

## Step 6: SPA 集成

从 `templates/index-spa.html` 复制骨架。每课一个 `<section class="lesson-view" id="lesson-NNN">`。
保留 `lessons/NNN-slug.html` 独立文件。

🛑 STOP：预览正常后进入 Step 7。

## Step 7: 知识图谱更新

从 `templates/kg-starter.html` 创建 `kg-项目名.html`。节点 `nameZh`/`nameEn` 双语。

🛑 STOP：图谱显示正确后再提交。

## Step 8: 本地 HTTP 服务器（可选）

从 `templates/start-server.ps1` 或 `.sh` 复制到项目根，运行即起。
按 Q 键停止。Python 内置 `http.server`。
🛑 STOP：全部完整性检查通过。

## 错误检查清单

- [ ] SVG XML 验证通过
- [ ] SVG 中文渲染正常（font-family 含中文字体）
- [ ] Quiz data-correct 正确（每题 1 个 true）
- [ ] 跨课链接使用相对路径
- [ ] 中英文成对 `data-lang="zh/en"`
- [ ] L 键 + 语言切换按钮存在
