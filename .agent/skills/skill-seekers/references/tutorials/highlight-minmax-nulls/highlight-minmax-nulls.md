# How To: Highlight Minmax Nulls

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test highlight minmax nulls

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`

**Setup Required:**
```python
# Fixtures: f, axis
```

## Step-by-Step Guide

### Step 1: Assign expected = value

```python
expected = {(1, 0): [('background-color', 'yellow')], (1, 1): [('background-color', 'yellow')]}
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = value

```python
result = getattr(df.style, f)(axis=axis)._compute().ctx
```

**Verification:**
```python
assert result == expected
```

### Step 3: Call expected.update()

```python
expected.update({(2, 1): [('background-color', 'yellow')]})
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [NA, 1, None], 'b': [np.nan, 1, -1]})
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [NA, -1, None], 'b': [np.nan, -1, 1]})
```


## Complete Example

```python
# Setup
# Fixtures: f, axis

# Workflow
expected = {(1, 0): [('background-color', 'yellow')], (1, 1): [('background-color', 'yellow')]}
if axis == 1:
    expected.update({(2, 1): [('background-color', 'yellow')]})
if f == 'highlight_max':
    df = DataFrame({'a': [NA, 1, None], 'b': [np.nan, 1, -1]})
else:
    df = DataFrame({'a': [NA, -1, None], 'b': [np.nan, -1, 1]})
result = getattr(df.style, f)(axis=axis)._compute().ctx
assert result == expected
```

## Next Steps


---

*Source: test_highlight.py:84 | Complexity: Intermediate | Last updated: 2026-06-02*