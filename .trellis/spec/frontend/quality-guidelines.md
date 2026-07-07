# Quality Guidelines

> Code quality standards for frontend development.

---

## Overview

<!--
Document your project's quality standards here.

Questions to answer:
- What patterns are forbidden?
- What linting rules do you enforce?
- What are your testing requirements?
- What code review standards apply?
-->

(To be filled by the team)

---

## Forbidden Patterns

<!-- Patterns that should never be used and why -->

(To be filled by the team)

---

## Required Patterns

<!-- Patterns that must always be used -->

### Theme Template Pattern (Single Data Source)

Theme picker must use a unified `themes` array in PPT JS block — no separate `t` array:

```js
var themes=[{id:'warm',color:'#c0392b',label:'暖色'},...];
```

- Both `lesson-starter.html` and `index-spa.html` carry the same array
- HTML keeps only 7 static `.tp-item` buttons; JS auto-injects missing ones
- T key cycles via `themes[(ci + 1) % themes.length].id`
- Adding a theme = one array entry in both templates

### Tag Color System (CSS Variables)

Tag colors use `color-mix()` to stay adaptive across themes:

```css
.tag-blue   { background: color-mix(in srgb, var(--accent) 15%, var(--bg)); color: var(--accent); }
.tag-red    { background: color-mix(in srgb, var(--error) 15%, var(--bg)); color: var(--error); }
```

No hardcoded Tailwind-style hex colors allowed in component CSS.

---

## Testing Requirements

<!-- What level of testing is expected -->

(To be filled by the team)

---

## Code Review Checklist

<!-- What reviewers should check -->

(To be filled by the team)
