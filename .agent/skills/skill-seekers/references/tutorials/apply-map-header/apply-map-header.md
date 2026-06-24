# How To: Apply Map Header

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test apply map header

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
# Fixtures: method, axis
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [0, 0], 'B': [1, 1]}, index=['C', 'D'])
```

**Verification:**
```python
assert len(result._todo) == 1
```

### Step 2: Assign func = value

```python
func = {'apply': lambda s: ['attr: val' if 'A' in v or 'C' in v else '' for v in s], 'map': lambda v: 'attr: val' if 'A' in v or 'C' in v else ''}
```

**Verification:**
```python
assert len(getattr(result, f'ctx_{axis}')) == 0
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(df.style, f'{method}_index')(func[method], axis=axis)
```

**Verification:**
```python
assert getattr(result, f'ctx_{axis}') == expected
```

### Step 4: Call result._compute()

```python
result._compute()
```

### Step 5: Assign expected = value

```python
expected = {(0, 0): [('attr', 'val')]}
```

**Verification:**
```python
assert getattr(result, f'ctx_{axis}') == expected
```


## Complete Example

```python
# Setup
# Fixtures: method, axis

# Workflow
df = DataFrame({'A': [0, 0], 'B': [1, 1]}, index=['C', 'D'])
func = {'apply': lambda s: ['attr: val' if 'A' in v or 'C' in v else '' for v in s], 'map': lambda v: 'attr: val' if 'A' in v or 'C' in v else ''}
result = getattr(df.style, f'{method}_index')(func[method], axis=axis)
assert len(result._todo) == 1
assert len(getattr(result, f'ctx_{axis}')) == 0
result._compute()
expected = {(0, 0): [('attr', 'val')]}
assert getattr(result, f'ctx_{axis}') == expected
```

## Next Steps


---

*Source: test_style.py:433 | Complexity: Intermediate | Last updated: 2026-06-02*