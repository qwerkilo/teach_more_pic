### 27. Three.js 3D 组件

使用 Three.js 在课程中渲染 3D 场景，适合展示地理/贸易网络、三维数据可视化、结构/架构图。

#### 前置依赖

```bash
# PowerShell（Windows）
Invoke-WebRequest -Uri "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" -OutFile "libs/three.min.js"

# macOS / Linux
curl -Lo libs/three.min.js https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js
```

```html
<!-- 本地离线加载 -->
<script src="libs/three.min.js"></script>
```

#### 使用规则

- Three.js 默认接管鼠标事件，与课程 `← →` 键盘导航冲突时需在场景容器上加 `tabindex` 隔离
- 每个场景唯一 `id`，`height` 建议 300-450px
- Three.js 渲染异步，用 `window.requestAnimationFrame` 循环
- 销毁：课程切换时需 `renderer.dispose()` 释放 GPU 资源

#### 示例：3D 柱状图（数据可视化）

```html
<div id="three-bar" style="width:100%;height:400px;margin:1rem 0;"></div>
```

```css
#three-bar { background: var(--surface); border-radius: var(--radius); }
```

```js
(function(){
  var container = document.getElementById('three-bar');
  if(!container || typeof THREE === 'undefined') return;

  var scene = new THREE.Scene();
  scene.background = new THREE.Color(0xf5f0eb);

  var camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 100);
  camera.position.set(5, 4, 8);
  camera.lookAt(0, 0, 0);

  var renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(container.clientWidth, container.clientHeight);
  container.appendChild(renderer.domElement);

  // 数据柱
  var data = [3.2, 5.1, 2.8, 4.5, 3.9];
  var colors = [0xc0392b, 0xe67e22, 0x2ecc71, 0x3498db, 0x9b59b6];
  var barW = 0.6;
  for(var i = 0; i < data.length; i++){
    var geo = new THREE.BoxGeometry(barW, data[i], barW);
    var mat = new THREE.MeshLambertMaterial({ color: colors[i] });
    var bar = new THREE.Mesh(geo, mat);
    bar.position.x = (i - 2) * 1.2;
    bar.position.y = data[i] / 2;
    scene.add(bar);
  }

  // 地面
  var floor = new THREE.Mesh(
    new THREE.PlaneGeometry(8, 3),
    new THREE.MeshLambertMaterial({ color: 0xddd8d0, side: THREE.DoubleSide })
  );
  floor.rotation.x = -Math.PI / 2;
  floor.position.y = -0.05;
  scene.add(floor);

  // 光照
  var light = new THREE.DirectionalLight(0xffffff, 1);
  light.position.set(5, 10, 7);
  scene.add(light);
  scene.add(new THREE.AmbientLight(0xffffff, 0.4));

  // 动画
  function animate(){ requestAnimationFrame(animate); renderer.render(scene, camera); }
  animate();

  // 响应式
  window.addEventListener('resize', function(){
    camera.aspect = container.clientWidth / container.clientHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(container.clientWidth, container.clientHeight);
  });
})();
```

#### 降级说明

- **WebGL 不支持**：显示 `<div class="no-js-fallback"><p>3D 场景需要 WebGL 支持</p></div>`
- **Three.js 未加载**：用 `typeof THREE === 'undefined'` 保护
- **键盘导航冲突**：在 Three.js 容器上设置 `onkeydown="e.stopPropagation()"`
- **性能**：移动端降低 `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))`
