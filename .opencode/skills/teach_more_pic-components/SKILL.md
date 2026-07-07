---
name: teach_more_pic-components
description: 33 个视觉组件的完整索引、使用规则和选择决策指南。
---

# 视觉组件工具箱

33 个组件（核心 #1-7 / 交互 #8-14 / 数据辅助 #15-28 / 微交互 #29-33），代码和用法在 `components/NN-name.md` 中。

## 核心组件（#1-7）

| # | 组件 | 文件 | 说明 |
|---|---|---|---|
| 1 | SVG 流程图 | `components/01-SVG 流程图.md` | 四色语义流程图 |
| 2 | 角色卡片 | `components/02-角色卡片.md` | 网格化角色介绍卡片 |
| 3 | CSS 时间线 | `components/03-CSS 时间线.md` | 垂直时间轴 |
| 4 | CSS 条形图 | `components/04-CSS 条形图.md` | 水平数据条 |
| 5 | 对比表 | `components/05-对比表.md` | 多维度 flex 对比 |
| 6 | SVG Figure | `components/06-SVG Figure 包裹.md` | 标准图片容器 |
| 7 | PPT 质感增强 | `components/07-PPT 质感增强.md` | T 键主题/语言/目录/导航 |

## 交互式组件（#8-14）

| # | 组件 | 文件 | 说明 |
|---|---|---|---|
| 8 | 折叠式分步详解 | `components/08-折叠式分步详解.md` | 复杂概念分步折叠 |
| 9 | Tab 切换面板 | `components/09-Tab 切换面板.md` | 垂直 Tab 多视角 |
| 10 | 图片前后对比滑块 | `components/10-图片前后对比滑块.md` | 拖拽滑块对比 |
| 11 | 交互式时间线 | `components/11-交互式时间线.md` | 点击展开事件详情 |
| 12 | 数据卡片网格 | `components/12-数据卡片网格.md` | 图标 + 数值 + 标签 |
| 13 | 引用/引文卡片 | `components/13-引用引文卡片.md` | 左侧竖条 + 引文 |
| 14 | 标注式图片 | `components/14-标注式图片.md` | 数字标注点弹出说明 |

## 数据与辅助组件（#15-28）

| # | 组件 | 文件 | 说明 |
|---|---|---|---|
| 15 | 状态链 | `components/15-状态链.md` | 水平里程碑 |
| 16 | 数值滚动动画 | `components/16-数值滚动动画.md` | 0→N 滚动 |
| 17 | 标签/徽章组 | `components/17-标签徽章组.md` | 5 色药丸标签 |
| 18 | 提示框/告警条 | `components/18-提示框告警条.md` | info/warning/error/success |
| 19 | 热力图/密度图 | `components/19-热力图密度图.md` | 绿→黄→红 5 级矩阵 |
| 20 | 步骤指示器 | `components/20-步骤指示器.md` | 水平编号步骤条 |
| 21 | 信息面板 | `components/21-信息面板.md` | 右侧滑入抽屉 |
| 22 | 对比表增强版 | `components/22-对比表增强版.md` | 粘性表头 + 排序 |
| 23 | 全屏模态/灯箱 | `components/23-全屏模态灯箱.md` | 点击放大全屏 |
| 24 | ECharts 图表集 | `components/24-ECharts 交互式图表集.md` | 柱状/饼/折线/堆叠图 |
| 25 | Three.js 3D | `components/25-Three.js 3D组件.md` | 3D 场景/柱状/地理可视化 |
| 26 | 现代浏览器 API | `components/26-现代浏览器API组件.md` | 原生折叠/模态/Popover |
| 27 | D3.js 可视化 | `components/27-D3.js 数据可视化.md` | 力导向/旭日/桑基图 |
| 28 | ECharts GL 3D | `components/28-ECharts GL 3D可视化.md` | 3D柱状/散点/地球 |
| 29 | 走马灯/轮播 | `components/29-走马灯轮播.md` | 图片/卡片自动轮播 |
| 30 | 打字机效果 | `components/30-打字机效果.md` | 文本逐字输出 |
| 31 | 视差滚动 | `components/31-视差滚动.md` | 背景视差滚动 |
| 32 | 浮动提醒/Toast | `components/32-浮动提醒.md` | 临时提示条 |
| 33 | 计数器徽章 | `components/33-计数器徽章.md` | 数字角标 + 等宽计数 |

## 使用规则

- 每课最少 6 个组件（含标签组 #17），不设上限
- 每课必须包含标签组 #17，放在课程结尾、测验之前，使用 `#` 前缀
- 颜色语义：蓝=正常，橙=触发，红=崩溃，绿=救助
- ECharts/Three.js/D3.js 可组合使用：D3 算布局→Three 渲染，或 D3 预处理→ECharts 呈现
- ECharts GL：`<script>` 加载 GeoJSON（转为 `.js` + `window.__gdGeoJSON`），`file://` 兼容

## 共享模式：折叠展开 JS

折叠分步详解（#08）和交互式时间线（#11）共用 JS 模式：

```js
var i=this.closest('.XX-item'),c=i.querySelector('.XX-content'),o=i.dataset.expanded==='true';
if(o){c.style.height=c.scrollHeight+'px';requestAnimationFrame(function(){c.style.height='0px';});
i.dataset.expanded='false';this.setAttribute('aria-expanded','false');}else{
c.style.height='0px';requestAnimationFrame(function(){c.style.height=c.scrollHeight+'px';});
i.dataset.expanded='true';this.setAttribute('aria-expanded','true');
c.addEventListener('transitionend',function h(){c.removeEventListener('transitionend',h);c.style.height='auto';});}
```

替换 `XX` 为组件前缀（`sd`、`tli`）即可复用。

## 组件选择决策指南

| 象限 | 适用场景 | 核心组件 |
|---|---|---|
| 解释与拆解 | 复杂概念分步拆解 | 折叠 (#8)、Tab (#9)、SVG (#1) |
| 数据与统计 | 数值对比、趋势 | ECharts (#24)、D3 (#27)、条形图 (#4) |
| 时间与过程 | 事件序列 | CSS 时间线 (#3)、交互时间线 (#11)、状态链 (#15) |
| 引用与强调 | 名言、警告 | 引文 (#13)、告警条 (#18)、信息面板 (#21) |
| 视觉对比 | 图对比、3D | 对比滑块 (#10)、Three (#25)、灯箱 (#23) |
| 零 JS 方案 | 降级场景 | 原生折叠/模态/Popover (#26) |
| Magic UI 装饰 | 纯 CSS 效果 | shiny-text / neon-card / 网格背景 |

完整选择矩阵见 `references/decision-guide.md`。
