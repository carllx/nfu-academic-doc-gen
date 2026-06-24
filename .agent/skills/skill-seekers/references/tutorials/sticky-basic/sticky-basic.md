# How To: Sticky Basic

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test sticky basic

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
# Fixtures: styler, index, columns, index_name
```

## Step-by-Step Guide

### Step 1: Assign left_css = '#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n  left: 0px;\n  z-index: {1};\n}}'

```python
left_css = '#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n  left: 0px;\n  z-index: {1};\n}}'
```

**Verification:**
```python
assert (left_css.format('thead tr th:nth-child(1)', '3 !important') in res) is index
```

### Step 2: Assign top_css = '#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n  top: {1}px;\n  z-index: {2};\n{3}}}'

```python
top_css = '#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n  top: {1}px;\n  z-index: {2};\n{3}}}'
```

**Verification:**
```python
assert (left_css.format('tbody tr th:nth-child(1)', '1') in res) is index
```

### Step 3: Assign res = styler.set_uuid.to_html(...)

```python
res = styler.set_uuid('').to_html()
```

**Verification:**
```python
assert (top_css.format('thead tr:nth-child(1) th', '0', '2', '  height: 25px;\n') in res) is (columns and index_name)
```

### Step 4: Assign styler.index.name = 'some text'

```python
styler.index.name = 'some text'
```

**Verification:**
```python
assert (top_css.format('thead tr:nth-child(2) th', '25', '2', '  height: 25px;\n') in res) is (columns and index_name)
```

### Step 5: Call styler.set_sticky()

```python
styler.set_sticky(axis=0)
```

**Verification:**
```python
assert (top_css.format('thead tr:nth-child(1) th', '0', '2', '') in res) is (columns and (not index_name))
```

### Step 6: Call styler.set_sticky()

```python
styler.set_sticky(axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: styler, index, columns, index_name

# Workflow
if index_name:
    styler.index.name = 'some text'
if index:
    styler.set_sticky(axis=0)
if columns:
    styler.set_sticky(axis=1)
left_css = '#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n  left: 0px;\n  z-index: {1};\n}}'
top_css = '#T_ {0} {{\n  position: sticky;\n  background-color: inherit;\n  top: {1}px;\n  z-index: {2};\n{3}}}'
res = styler.set_uuid('').to_html()
assert (left_css.format('thead tr th:nth-child(1)', '3 !important') in res) is index
assert (left_css.format('tbody tr th:nth-child(1)', '1') in res) is index
assert (top_css.format('thead tr:nth-child(1) th', '0', '2', '  height: 25px;\n') in res) is (columns and index_name)
assert (top_css.format('thead tr:nth-child(2) th', '25', '2', '  height: 25px;\n') in res) is (columns and index_name)
assert (top_css.format('thead tr:nth-child(1) th', '0', '2', '') in res) is (columns and (not index_name))
```

## Next Steps


---

*Source: test_html.py:301 | Complexity: Intermediate | Last updated: 2026-06-02*