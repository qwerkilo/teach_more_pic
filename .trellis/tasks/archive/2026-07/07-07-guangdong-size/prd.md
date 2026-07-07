# PRD: libs/ 文件清理

## 问题

- `guangdong.json` (188KB) 是原始 GeoJSON，未被任何文件引用——`guangdong.js` (205KB) 是它的 JS 封装版
- 删除未使用的 `guangdong.json`

## 验收

- [ ] `libs/guangdong.json` 已删除
- [ ] ECharts GL 地图 demo 仍正常工作（依赖 `guangdong.js`）
