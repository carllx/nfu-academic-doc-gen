# How To: Astype Preserves Name

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test astype preserves name

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index, dtype
```

## Step-by-Step Guide

### Step 1: Assign warn = None

```python
warn = None
```

**Verification:**
```python
assert result.names == index.names
```

### Step 2: Assign is_pyarrow_str = value

```python
is_pyarrow_str = str(index.dtype) == 'string[pyarrow]' and dtype == 'category'
```

**Verification:**
```python
assert result.name == index.name
```

### Step 3: Assign index.names = value

```python
index.names = ['idx' + str(i) for i in range(index.nlevels)]
```

### Step 4: Assign index.name = 'idx'

```python
index.name = 'idx'
```

**Verification:**
```python
assert result.names == index.names
```

### Step 5: Assign warn = value

```python
warn = np.exceptions.ComplexWarning
```

### Step 6: Assign warn = value

```python
warn = np.ComplexWarning
```

### Step 7: Assign result = index.astype(...)

```python
result = index.astype(dtype)
```


## Complete Example

```python
# Setup
# Fixtures: index, dtype

# Workflow
if isinstance(index, MultiIndex):
    index.names = ['idx' + str(i) for i in range(index.nlevels)]
else:
    index.name = 'idx'
warn = None
if index.dtype.kind == 'c' and dtype in ['float64', 'int64', 'uint64']:
    if np_version_gte1p25:
        warn = np.exceptions.ComplexWarning
    else:
        warn = np.ComplexWarning
is_pyarrow_str = str(index.dtype) == 'string[pyarrow]' and dtype == 'category'
try:
    with tm.assert_produces_warning(warn, raise_on_extra_warnings=is_pyarrow_str, check_stacklevel=False):
        result = index.astype(dtype)
except (ValueError, TypeError, NotImplementedError, SystemError):
    return
if isinstance(index, MultiIndex):
    assert result.names == index.names
else:
    assert result.name == index.name
```

## Next Steps


---

*Source: test_common.py:386 | Complexity: Advanced | Last updated: 2026-06-02*