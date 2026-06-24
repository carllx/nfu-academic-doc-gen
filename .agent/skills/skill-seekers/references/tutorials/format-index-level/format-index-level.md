# How To: Format Index Level

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test format index level

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
# Fixtures: axis, level, expected
```

## Step-by-Step Guide

### Step 1: Assign midx = MultiIndex.from_arrays(...)

```python
midx = MultiIndex.from_arrays([['_', '_'], ['_', '_']], names=['zero', 'one'])
```

**Verification:**
```python
assert expected == result
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2], [3, 4]])
```

### Step 3: Assign styler = df.style.format_index(...)

```python
styler = df.style.format_index(lambda v: 'X', level=level, axis=axis)
```

### Step 4: Assign ctx = styler._translate(...)

```python
ctx = styler._translate(True, True)
```

**Verification:**
```python
assert expected == result
```

### Step 5: Assign df.index = midx

```python
df.index = midx
```

### Step 6: Assign df.columns = midx

```python
df.columns = midx
```

### Step 7: Assign result = value

```python
result = [ctx['body'][s][0]['display_value'] for s in range(2)]
```

### Step 8: Assign result = value

```python
result = [ctx['head'][0][s + 1]['display_value'] for s in range(2)]
```


## Complete Example

```python
# Setup
# Fixtures: axis, level, expected

# Workflow
midx = MultiIndex.from_arrays([['_', '_'], ['_', '_']], names=['zero', 'one'])
df = DataFrame([[1, 2], [3, 4]])
if axis == 0:
    df.index = midx
else:
    df.columns = midx
styler = df.style.format_index(lambda v: 'X', level=level, axis=axis)
ctx = styler._translate(True, True)
if axis == 0:
    result = [ctx['body'][s][0]['display_value'] for s in range(2)]
    result += [ctx['body'][s][1]['display_value'] for s in range(2)]
else:
    result = [ctx['head'][0][s + 1]['display_value'] for s in range(2)]
    result += [ctx['head'][1][s + 1]['display_value'] for s in range(2)]
assert expected == result
```

## Next Steps


---

*Source: test_format.py:313 | Complexity: Advanced | Last updated: 2026-06-02*