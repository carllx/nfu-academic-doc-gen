# How To: Sticky Levels

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test sticky levels

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`

**Setup Required:**
```python
# Fixtures: styler_mi, index, columns, levels
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
styler_mi.index.names, styler_mi.columns.names = (['zero', 'one'], ['zero', 'one'])
```

**Verification:**
```python
assert '#T_ thead tr th:nth-child(1)' not in res
```

### Step 2: Assign left_css = '#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n  left: {1}px;\n  min-width: 75px;\n  max-width: 75px;\n  z-index: {2};\n}}'

```python
left_css = '#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n  left: {1}px;\n  min-width: 75px;\n  max-width: 75px;\n  z-index: {2};\n}}'
```

**Verification:**
```python
assert '#T_ tbody tr th.level0' not in res
```

### Step 3: Assign top_css = '#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n  top: {1}px;\n  height: 25px;\n  z-index: {2};\n}}'

```python
top_css = '#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n  top: {1}px;\n  height: 25px;\n  z-index: {2};\n}}'
```

**Verification:**
```python
assert '#T_ thead tr:nth-child(1) th' not in res
```

### Step 4: Assign res = styler_mi.set_uuid.to_html(...)

```python
res = styler_mi.set_uuid('').to_html()
```

**Verification:**
```python
assert (left_css.format('thead tr th:nth-child(2)', '0', '3 !important') in res) is index
```

### Step 5: Call styler_mi.set_sticky()

```python
styler_mi.set_sticky(axis=0, levels=levels)
```

**Verification:**
```python
assert (left_css.format('tbody tr th.level1', '0', '1') in res) is index
```

### Step 6: Call styler_mi.set_sticky()

```python
styler_mi.set_sticky(axis=1, levels=levels)
```

**Verification:**
```python
assert (top_css.format('thead tr:nth-child(2) th', '0', '2') in res) is columns
```


## Complete Example

```python
# Setup
# Fixtures: styler_mi, index, columns, levels

# Workflow
styler_mi.index.names, styler_mi.columns.names = (['zero', 'one'], ['zero', 'one'])
if index:
    styler_mi.set_sticky(axis=0, levels=levels)
if columns:
    styler_mi.set_sticky(axis=1, levels=levels)
left_css = '#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n  left: {1}px;\n  min-width: 75px;\n  max-width: 75px;\n  z-index: {2};\n}}'
top_css = '#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n  top: {1}px;\n  height: 25px;\n  z-index: {2};\n}}'
res = styler_mi.set_uuid('').to_html()
assert '#T_ thead tr th:nth-child(1)' not in res
assert '#T_ tbody tr th.level0' not in res
assert '#T_ thead tr:nth-child(1) th' not in res
assert (left_css.format('thead tr th:nth-child(2)', '0', '3 !important') in res) is index
assert (left_css.format('tbody tr th.level1', '0', '1') in res) is index
assert (top_css.format('thead tr:nth-child(2) th', '0', '2') in res) is columns
```

## Next Steps


---

*Source: test_html.py:374 | Complexity: Intermediate | Last updated: 2026-06-02*