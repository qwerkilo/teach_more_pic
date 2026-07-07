---
name: knowledge-graph
description: Create interactive knowledge graph visualizations with bilingual (zh/en) nodes. Uses ECharts force-directed graph.
---

# Knowledge Graph

Create an interactive knowledge graph HTML file from lesson concepts.

## Template

Copy `templates/kg-starter.html` from the project root as `kg-{project-name}.html`.

## Data Format

Nodes use bilingual names and categories:

```js
nodes: [
  { id: 'mmt', nameZh: '现代货币理论', nameEn: 'Modern Monetary Theory', category: 0, weight: 10 },
]
links: [
  { source: 'mmt', target: 'deficit', weight: 5 },
]
```

Categories define node colors:

```js
categories: [
  { name: '概念' },
  { name: '制度' },
  { name: '事件' },
]
```

## Language Switch

The template includes L-key language switching that toggles `nameZh`/`nameEn`.

## Acceptance

- [ ] Node IDs are unique across all nodes
- [ ] Links only reference existing node IDs
- [ ] At least 2 categories defined
- [ ] Bilingual: every node has both `nameZh` and `nameEn`
