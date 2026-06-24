# How To: Display Format Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test display format index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`
- `pandas.io.formats.style_render`

**Setup Required:**
```python
# Fixtures: styler, index, columns
```

## Step-by-Step Guide

### Step 1: Assign exp_index = value

```python
exp_index = ['x', 'y']
```

**Verification:**
```python
assert row[0]['display_value'] == exp_index[r]
```

### Step 2: Assign exp_columns = value

```python
exp_columns = ['A', 'B']
```

**Verification:**
```python
assert col['display_value'] == exp_columns[c]
```

### Step 3: Assign ctx = styler._translate(...)

```python
ctx = styler._translate(True, True)
```

### Step 4: Call styler.format_index()

```python
styler.format_index(lambda v: v.upper(), axis=0)
```

### Step 5: Assign exp_index = value

```python
exp_index = ['X', 'Y']
```

### Step 6: Call styler.format_index()

```python
styler.format_index('*{}*', axis=1)
```

### Step 7: Assign exp_columns = value

```python
exp_columns = ['*A*', '*B*']
```

**Verification:**
```python
assert row[0]['display_value'] == exp_index[r]
```


## Complete Example

```python
# Setup
# Fixtures: styler, index, columns

# Workflow
exp_index = ['x', 'y']
if index:
    styler.format_index(lambda v: v.upper(), axis=0)
    exp_index = ['X', 'Y']
exp_columns = ['A', 'B']
if columns:
    styler.format_index('*{}*', axis=1)
    exp_columns = ['*A*', '*B*']
ctx = styler._translate(True, True)
for r, row in enumerate(ctx['body']):
    assert row[0]['display_value'] == exp_index[r]
for c, col in enumerate(ctx['head'][1:]):
    assert col['display_value'] == exp_columns[c]
```

## Next Steps


---

*Source: test_format.py:56 | Complexity: Intermediate | Last updated: 2026-06-02*