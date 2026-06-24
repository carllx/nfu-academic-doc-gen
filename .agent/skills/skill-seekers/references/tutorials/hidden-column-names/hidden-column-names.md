# How To: Hidden Column Names

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hidden column names

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `copy`
- `re`
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.style`
- `pandas.io.formats.style_render`

**Setup Required:**
```python
# Fixtures: mi_df
```

## Step-by-Step Guide

### Step 1: Assign mi_df.columns.names = value

```python
mi_df.columns.names = ['Lev0', 'Lev1']
```

**Verification:**
```python
assert ctx['head'][0][1]['display_value'] == 'Lev0'
```

### Step 2: Assign mi_styler = value

```python
mi_styler = mi_df.style
```

**Verification:**
```python
assert ctx['head'][1][1]['display_value'] == 'Lev1'
```

### Step 3: Assign ctx = mi_styler._translate(...)

```python
ctx = mi_styler._translate(True, True)
```

**Verification:**
```python
assert ctx['head'][0][1]['display_value'] == '&nbsp;'
```

### Step 4: Call mi_styler.hide()

```python
mi_styler.hide(names=True, axis='columns')
```

**Verification:**
```python
assert ctx['head'][1][1]['display_value'] == '&nbsp;'
```

### Step 5: Assign ctx = mi_styler._translate(...)

```python
ctx = mi_styler._translate(True, True)
```

**Verification:**
```python
assert len(ctx['head']) == 1
```

### Step 6: Call mi_styler.hide()

```python
mi_styler.hide(level=0, axis='columns')
```

**Verification:**
```python
assert ctx['head'][0][1]['display_value'] == '&nbsp;'
```

### Step 7: Assign ctx = mi_styler._translate(...)

```python
ctx = mi_styler._translate(True, True)
```

**Verification:**
```python
assert len(ctx['head']) == 1
```


## Complete Example

```python
# Setup
# Fixtures: mi_df

# Workflow
mi_df.columns.names = ['Lev0', 'Lev1']
mi_styler = mi_df.style
ctx = mi_styler._translate(True, True)
assert ctx['head'][0][1]['display_value'] == 'Lev0'
assert ctx['head'][1][1]['display_value'] == 'Lev1'
mi_styler.hide(names=True, axis='columns')
ctx = mi_styler._translate(True, True)
assert ctx['head'][0][1]['display_value'] == '&nbsp;'
assert ctx['head'][1][1]['display_value'] == '&nbsp;'
mi_styler.hide(level=0, axis='columns')
ctx = mi_styler._translate(True, True)
assert len(ctx['head']) == 1
assert ctx['head'][0][1]['display_value'] == '&nbsp;'
```

## Next Steps


---

*Source: test_style.py:1461 | Complexity: Intermediate | Last updated: 2026-06-02*