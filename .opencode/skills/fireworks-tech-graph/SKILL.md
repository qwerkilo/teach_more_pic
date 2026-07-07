---
name: fireworks-tech-graph
description: >-
  Use when the user wants to create any technical diagram - architecture, data
  flow, flowchart, sequence, agent/memory, or concept map - and export as
  SVG+PNG.
---

# Fireworks Tech Graph

Generate production-quality SVG technical diagrams exported as PNG via `cairosvg` (recommended), `rsvg-convert`, or `puppeteer`.

## SVG Generation Strategy

Generate SVG directly using the Python List Method:

```python
python3 << 'EOF'
lines = []
lines.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 700">')
# ... each line separately
lines.append('</svg>')
with open('/path/to/output.svg', 'w') as f:
    f.write('\n'.join(lines))
EOF
```

## Diagram Types & Layout Rules

### Architecture Diagram
Nodes = services/components. Group into **horizontal layers** (top→bottom or left→right).
- Typical layers: Client → Gateway/LB → Services → Data/Storage
- Use `<rect>` dashed containers to group related services in the same layer
- Arrow direction follows data/request flow
- ViewBox: `0 0 960 600` standard, `0 0 960 800` for tall stacks

### Data Flow Diagram
Emphasizes **what data moves where**. Focus on data transformation.
- Label every arrow with the data type
- Use wider arrows (`stroke-width: 2.5`) for primary data paths
- Dashed arrows for control/trigger flows

### Flowchart / Process Flow
Sequential decision/process steps.
- Top-to-bottom preferred; left-to-right for wide flows
- Diamond shapes for decisions, rounded rects for processes, parallelograms for I/O
- Keep node labels short (≤3 words); put detail in sub-labels
- Align nodes on a grid: x positions snap to 120px intervals, y to 80px

### Agent Architecture Diagram
Shows how an AI agent reasons, uses tools, and manages memory.
- **Input layer**: User, query, trigger
- **Agent core**: LLM, reasoning loop, planner
- **Memory layer**: Short-term (context window), Long-term (vector/graph DB), Episodic
- **Tool layer**: Tool calls, APIs, search, code execution
- **Output layer**: Response, action, side-effects

### Memory Architecture Diagram (Mem0, MemGPT-style)
- Show memory **write path** and **read path** separately (different arrow colors)
- Memory tiers: Working Memory → Short-term → Long-term → External Store
- Label memory operations: `store()`, `retrieve()`, `forget()`, `consolidate()`

### Sequence Diagram
Time-ordered message exchanges between participants.
- Participants as vertical **lifelines** (top labels + vertical dashed lines)
- Messages as horizontal arrows between lifelines, top-to-bottom time order
- Activation boxes (thin filled rects on lifeline) show active processing
- Group with `<rect>` loop/alt frames with label in top-left corner
- ViewBox height = 80 + (num_messages × 50)

### Comparison / Feature Matrix
Side-by-side comparison of approaches, systems, or components.
- Column headers = systems, row headers = attributes
- Row height: 40px; column width: min 120px; header row height: 50px
- Checked cell: tinted background (e.g. `#dcfce7`) + `✓` checkmark; unsupported: `#f9fafb` fill
- Alternating row fills (`#f9fafb` / `#ffffff`) for readability
- Max readable columns: 5; beyond that, split into two diagrams

### Timeline / Gantt
Horizontal time axis showing durations, phases, and milestones.
- X-axis = time (weeks/months/quarters); Y-axis = items/tasks/phases
- Bars: rounded rects, colored by category, labeled inside or beside
- Milestone markers: diamond or filled circle at specific x position with label above

### Mind Map / Concept Map
Radial layout from central concept.
- Central node at `cx=480, cy=280`
- First-level branches: evenly distributed around center (360/N degrees)
- Second-level branches: branch off first-level at 30-45° offset
- Use curved `<path>` with cubic bezier for branches, not straight lines

### Class Diagram (UML)
- **Class box**: 3-compartment rect (name / attributes / methods), min width 160px
- **Relationships**: Inheritance (solid + hollow triangle), Implementation (dashed + hollow triangle), Association (solid + open arrowhead), Aggregation (solid + hollow diamond), Composition (solid + filled diamond), Dependency (dashed + open arrowhead)
- **Interface**: `<<interface>>` stereotype above name
- Layout: parent classes top, children below; interfaces to left/right of implementors

### Use Case Diagram (UML)
- **Actor**: stick figure (circle head + body line)
- **Use case**: ellipse with label centered inside, min 140×60px
- **System boundary**: large rect with dashed border + system name in top-left
- **Relationships**: Include (`<<include>>`), Extend (`<<extend>>`), Generalization (solid + hollow triangle)

### State Machine Diagram (UML)
- **State**: rounded rect with state name, min 120×50px
- **Initial state**: filled black circle (r=8), one outgoing arrow
- **Final state**: filled circle (r=8) inside hollow circle (r=12)
- **Choice**: small hollow diamond, guard labels on outgoing arrows `[condition]`
- Layout: initial state top-left, final state bottom-right, flow top-to-bottom

### ER Diagram (Entity-Relationship)
- **Entity**: rect with entity name in header (bold), attributes below
- **Relationship**: diamond shape on connecting line
- **Weak entity**: double-bordered rect with double diamond relationship
- Layout: entities in 2-3 rows, relationships between related entities

### Network Topology
- **Devices**: icon-like rects or rounded rects
- **Subnets/Zones**: dashed rect containers with zone label (DMZ, Internal, External)
- Layout: tiered top-to-bottom (Internet → Edge → Core → Access → Endpoints)

## Shape Vocabulary

| Concept | Shape | Notes |
|---------|-------|-------|
| User / Human | Circle + body path | Stick figure or avatar |
| LLM / Model | Rounded rect with brain/spark icon or gradient fill | Use accent color |
| Agent / Orchestrator | Hexagon or rounded rect with double border | Signals "active controller" |
| Memory (short-term) | Rounded rect, dashed border | Ephemeral = dashed |
| Memory (long-term) | Cylinder (database shape) | Persistent = solid cylinder |
| Vector Store | Cylinder with grid lines inside | Add 3 horizontal lines |
| Graph DB | Circle cluster (3 overlapping circles) | |
| Tool / Function | Gear-like rect or rect with wrench icon | |
| API / Gateway | Hexagon (single border) | |
| Queue / Stream | Horizontal tube (pipe shape) | |
| File / Document | Folded-corner rect | |
| Browser / UI | Rect with 3-dot titlebar | |
| Decision | Diamond | Flowcharts only |
| Process / Step | Rounded rect | Standard box |
| External Service | Rect with cloud icon or dashed border | |
| Data / Artifact | Parallelogram | I/O in flowcharts |

## Arrow Semantics

| Flow Type | Color | Stroke | Meaning |
|-----------|-------|--------|---------|
| Primary data flow | blue `#2563eb` | 2px solid | Main request/response path |
| Control / trigger | orange `#ea580c` | 1.5px solid | One system triggering another |
| Memory read | green `#059669` | 1.5px solid | Retrieval from store |
| Memory write | green `#059669` | 1.5px dashed `5,3` | Write/store operation |
| Async / event | gray `#6b7280` | 1.5px dashed `4,2` | Non-blocking, event-driven |
| Embedding / transform | purple `#7c3aed` | 1px solid | Data transformation |
| Feedback / loop | purple `#7c3aed` | 1.5px curved | Iterative reasoning loop |

Always include a **legend** when 2+ arrow types are used.

## Layout Rules

**Spacing**: Same-layer nodes: 80px horizontal, 120px vertical between layers. Canvas margins: 40px minimum, 60px between node edges. Snap to 8px grid.

**Arrow Labels**: Offset-first (6-8px above horizontal arrows, 8px left/right of vertical arrows). Background `<rect>` fallback only when offset crosses another element. Max 3 words, stagger by 15-20px when multiple arrows converge.

**Arrow Routing**: Prefer orthogonal (L-shaped) paths. Anchor arrows on component edges. Route around dense node clusters. Jump-over arcs (5px radius) for crossings.

**Line Overlap Prevention**: When two arrows must cross, use jump-over arcs (radius 5px, fill none) that "jumps over" the other line.

## SVG Technical Rules

- ViewBox: `0 0 960 600` default; `0 0 960 800` tall; `0 0 1200 600` wide
- Fonts: embed via `<style>font-family: ...</style>` — no external `@import`
- `<defs>`: arrow markers, gradients, filters, clip paths
- Text: minimum 12px, prefer 13-14px labels, 11px sub-labels, 16-18px titles
- Z-order (painter's model): ① background ② containers ③ arrows ④ nodes ⑤ text ⑥ legends
- Keep filtered elements at least 30px from viewBox edges

## Validation

```bash
python3 -c "import xml.etree.ElementTree as ET; ET.parse('file.svg')"
```

## SVG → PNG Conversion

```bash
# cairosvg (recommended)
python3 -c "import cairosvg; cairosvg.svg2png(url='input.svg', write_to='output.png', scale=2)"

# rsvg-convert (fallback)
rsvg-convert -w 1920 file.svg -o file.png
```

## Color Palette (Style 1: Flat Icon)

| Role | Fill | Stroke |
|------|------|--------|
| Primary/Active | `#e8f4fd` | `#2196f3` |
| Success/Ready | `#e8f5e9` | `#4caf50` |
| Warning/Pending | `#fff3e0` | `#ff9800` |
| Error/Critical | `#ffebee` | `#f44336` |
| Neutral/Default | `#f5f5f5` | `#9e9e9e` |
| Background | `#ffffff` | — |
