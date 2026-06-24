# How To: Has Infs Floats

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test has infs floats

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: request, arr, correct, astype, disable_bottleneck
```

## Step-by-Step Guide

### Step 1: Assign val = request.getfixturevalue(...)

```python
val = request.getfixturevalue(arr)
```

**Verification:**
```python
assert res0
```

### Step 2: Assign val = val.astype(...)

```python
val = val.astype(astype)
```

**Verification:**
```python
assert not res0
```

### Step 3: Assign res0 = nanops._has_infs(...)

```python
res0 = nanops._has_infs(val)
```

### Step 4: Assign val = np.take(...)

```python
val = np.take(val, 0, axis=-1)
```

**Verification:**
```python
assert res0
```


## Complete Example

```python
# Setup
# Fixtures: request, arr, correct, astype, disable_bottleneck

# Workflow
val = request.getfixturevalue(arr)
if astype is not None:
    val = val.astype(astype)
while getattr(val, 'ndim', True):
    res0 = nanops._has_infs(val)
    if correct:
        assert res0
    else:
        assert not res0
    if not hasattr(val, 'ndim'):
        break
    val = np.take(val, 0, axis=-1)
```

## Next Steps


---

*Source: test_nanops.py:789 | Complexity: Intermediate | Last updated: 2026-06-02*