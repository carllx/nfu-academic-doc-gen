# How To: Hidden Index Names

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hidden index names

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

### Step 1: Assign mi_df.index.names = value

```python
mi_df.index.names = ['Lev0', 'Lev1']
```

**Verification:**
```python
assert len(ctx['head']) == 3
```

### Step 2: Assign mi_styler = value

```python
mi_styler = mi_df.style
```

**Verification:**
```python
assert len(ctx['head']) == 2
```

### Step 3: Assign ctx = mi_styler._translate(...)

```python
ctx = mi_styler._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][0][i]['is_visible']
```

### Step 4: Call mi_styler.hide()

```python
mi_styler.hide(axis='index', names=True)
```

**Verification:**
```python
assert len(ctx['head']) == 2
```

### Step 5: Assign ctx = mi_styler._translate(...)

```python
ctx = mi_styler._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][0][0]['is_visible'] is True
```

### Step 6: Call mi_styler.hide()

```python
mi_styler.hide(axis='index', level=1)
```

**Verification:**
```python
assert ctx['body'][0][1]['is_visible'] is False
```

### Step 7: Assign ctx = mi_styler._translate(...)

```python
ctx = mi_styler._translate(True, True)
```

**Verification:**
```python
assert len(ctx['head']) == 2
```


## Complete Example

```python
# Setup
# Fixtures: mi_df

# Workflow
mi_df.index.names = ['Lev0', 'Lev1']
mi_styler = mi_df.style
ctx = mi_styler._translate(True, True)
assert len(ctx['head']) == 3
mi_styler.hide(axis='index', names=True)
ctx = mi_styler._translate(True, True)
assert len(ctx['head']) == 2
for i in range(4):
    assert ctx['body'][0][i]['is_visible']
mi_styler.hide(axis='index', level=1)
ctx = mi_styler._translate(True, True)
assert len(ctx['head']) == 2
assert ctx['body'][0][0]['is_visible'] is True
assert ctx['body'][0][1]['is_visible'] is False
```

## Next Steps


---

*Source: test_style.py:1442 | Complexity: Intermediate | Last updated: 2026-06-02*