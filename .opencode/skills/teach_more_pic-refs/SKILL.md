---
name: teach_more_pic-refs
description: 可选页面类型、文件速查、失败模式和故障排除。
---

# 可选页面类型

完整 HTML/CSS 代码（中英双语版）见 `references/page-types.md`。

| 类型 | 必选？ | 视觉亮点 |
|---|---|---|
| 封面页 | ✅ 每课必须 | shiny-text 光泽标题、药丸 badge |
| 章节分隔页 | ✅ 三幕必须 | 圆形编号 + 顶部装饰线 |
| 总结卡片 | ✅ 每课必须 | SVG 矢量图标、hover 微上浮 |
| 全宽引文页 | 可选 | 左侧 accent 竖线、40vh 高度 |
| 关键数字页 | 可选 | 3rem 超大数字 + accent 色 |
| 信息面板侧边栏 | 可选 | 右浮动、窄屏自动降级 |

# 文件资源速查

| 路径 | 用途 | 对应步骤 |
|---|---|---|
| `templates/lesson-starter.html` | 课程骨架模板（15+ 组件示范） | Step 3 |
| `templates/index-spa.html` | SPA 课程集线器 | Step 6 |
| `templates/kg-starter.html` | 知识图谱模板（双语） | Step 7 |
| `templates/start-server.ps1` / `.sh` | 本地 HTTP 服务器 | Step 8 |
| `templates/flowchart-vertical.svg` | 垂直流程图模板 | Step 2/5 |
| `templates/cycle-diagram.svg` | 循环图模板 | Step 2/5 |
| `templates/comparison-side-by-side.svg` | 左右对比 SVG | Step 2/5 |
| `templates/timeline-horizontal.svg` | 水平时间线 | Step 2/5 |
| `examples/*.html` | 28+ 组件独立示例 | Step 2 |
| `components/NN-name.md` | 组件代码 + 降级说明（28 个） | Step 2/3 |
| `references/decision-guide.md` | 组件选择矩阵 + 组合示例 | Step 2 |
| `references/page-types.md` | 6 种页面类型完整代码 | 可选页面类型 |
| `scripts/validate-lesson.py` | 课程验证脚本（18 项检查） | Step 4 |
| `tests/test_validate.py` | 验证脚本 pytest 测试（99 项） | 开发 |
| `libs/magicui-effects.css` | Magic UI 装饰效果（13 种） | 模板自动加载 |
| `libs/` | 离线包（echarts/three/d3） | Step 6 |

# 失败模式与异常处理

| 触发条件 | 一线修复 | 兜底 |
|---|---|---|
| SVG 空白 | 检查 XML + viewBox 比例 | 降级 `<img>` 外部引用 |
| SVG 中文不渲染 | font-family 加中文字体 | 内联 font-family |
| 条形图溢出 | 检查 `bar-fill` width ≤ 100% | `text-overflow: ellipsis` |
| Quiz data-correct 写反 | `grep 'data-correct="true"'` | 手动核验 |
| IntersectionObserver 不触发 | 移除该元素 `data-anim` | 首屏不加 data-anim |
| 主题切换后颜色不变 | 用 `var(--accent)` 而非固定色 | boder-bottom-color: var(--accent) |
| Panel 点击外部不关闭 | click 委托到 document | 排除 toolbar/panel |
| 折叠动画不平滑 | 先 scrollHeight 再设 px | 过渡结束恢复 auto |
| ECharts/Three/D3 空白 | 对应 lib 未加载 | 复制 `libs/` 或 CDN |
| Three.js WebGPU 空白 | importmap 路径错误 | 降级 UMD 回退 |
| Three.js TSL 失效 | 版本不匹配 | 降级固定色材质 |
| libs 版本过旧 | 本地与 CDN 同步 | 重新下载覆盖 |
| 多图表性能 < 30fps | 延迟非首屏图表 | 减少动画复杂度 |
| SPA id 冲突 | 两个 id 相同 | 用 `lesson-NNN` 格式 |
| JS 括号顺序错误 | 检查 `});` vs `}})` 顺序 | — |
| 浏览器缓存旧 JS | Ctrl+F5 强制刷新 | 注销缓存 |
| 语言切换错位 | data-lang 成对数不一致 | 确保两版本段落数相同 |
| 组件特定问题 | 见 `components/NN-name.md` | — |
