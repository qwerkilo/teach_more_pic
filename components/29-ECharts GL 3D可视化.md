### 28. ECharts GL 3D 可视化

基于 ECharts GL 扩展库，在标准 ECharts 基础上增加 WebGL 3D 渲染能力。支持 3D 柱状图、3D 散点图、3D 地球/地图和 3D 曲面图。

#### 前置依赖

```html
<!-- ECharts 基础库（必须） -->
<script src="libs/echarts.min.js"></script>
<!-- ECharts GL 扩展（必须） -->
<script src="libs/echarts-gl.min.js"></script>
```

#### 使用规则

- 所有 3D 系列类型都加 `gl` 后缀：`type: 'bar3D'`、`type: 'scatter3D'`、`type: 'map3D'`、`type: 'surface'`
- 3D 图表需要 `grid3D` 组件（而非普通 `grid`）定义三维坐标系
- GL 扩展自动检测 WebGL 支持，不支持时显示降级提示
- 每个容器必须有明确的 `width` 和 `height`（百分比或 px 均可）

#### 子类型

| 子类型 | 系列 type | 适用场景 |
|--------|-----------|---------|
| 3D 柱状图 | `bar3D` | 三维数据对比，高度 + 颜色双维度编码 |
| 3D 散点图 | `scatter3D` | 三维空间分布，适合聚类/异常检测 |
| 3D 地球 | `map3D` | 地理数据全球分布，可飞线动画 |
| 3D 曲面 | `surface` | 函数曲面/地形/连续场数据 |

#### 示例：3D 柱状图

```js
var chart = echarts.init(document.getElementById('my-chart'));
chart.setOption({
  grid3D: {
    viewControl: { autoRotate: true, distance: 120 },
    boxWidth: 80, boxHeight: 80, boxDepth: 80,
  },
  xAxis3D: { type: 'category', data: ['A','B','C','D','E'] },
  yAxis3D: { type: 'category', data: ['X','Y','Z'] },
  zAxis3D: { type: 'value' },
  series: [{
    type: 'bar3D',
    data: [[0,0,10],[1,0,25],[2,0,15],[3,0,30],[4,0,20],
           [0,1,18],[1,1,12],[2,1,28],[3,1,8],[4,1,22]],
    shading: 'lambert',
    itemStyle: { opacity: 0.8 },
    label: { show: true }
  }]
});
```

#### 示例：3D 地球

```js
chart.setOption({
  globe: {
    baseTexture: 'world.topo.bathy.200401.jpg', // 或使用动态纹理
    viewControl: { autoRotate: true, distance: 150 },
    shading: 'realistic',
  },
  series: [{
    type: 'scatter3D',
    coordinateSystem: 'globe',
    data: [[116.4,39.9,100],[121.5,25.0,80],[139.7,35.7,120]],
    symbolSize: 8,
    itemStyle: { color: '#e74c3c', opacity: 0.9 },
    label: { show: true, formatter: '{b}' }
  }]
});
```

#### 示例：3D 广东省地图

```html
<div id="gd-map" style="width:100%;height:600px;"></div>
```
```js
// 本地 GeoJSON 优先 → CDN 降级
fetch('../libs/guangdong.json').catch(function(){
  return fetch('https://geo.datav.aliyun.com/areas_v3/bound/440000_full.json');
}).then(function(r){ return r.json(); }).then(function(geoJson){
  echarts.registerMap('guangdong', geoJson);
  var chart = echarts.init(document.getElementById('gd-map'));
  chart.setOption({
    series: [{
      type: 'map3D', map: 'guangdong',
      data: [{name:'深圳市',value:3.46},...],
      shading: 'lambert'
    }, {
      type: 'scatter3D',
      coordinateSystem: 'geo3D',
      data: [{name:'深圳',value:[114.07,22.55,34600]},...],
      symbolSize: function(v){ return 6 + Math.sqrt(v[2]/10000)*4; },
      label: { show: true }
    }]
  });
});
```
完整示例见 `examples/echarts-gl-map-demo.html`。

#### 降级说明

- **WebGL 不支持**：ECharts GL 自动降级为提示信息，不影响 ECharts 2D 部分
- **未加载 GL**：访问 `echarts` 对象时 GL 系列不存在，显示 `[ECharts] Unknown series bar3D` 警告但不崩溃
- **纹理缺失**：地球底图使用网络纹理，离线时可用纯色 `itemStyle.color` 替代
- **GeoJSON 离线**：省级/城市边界 GeoJSON 可下载到 `libs/` 目录，`fetch` 本地路径加载
