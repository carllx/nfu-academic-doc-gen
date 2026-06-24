# How To: Drop Metadata

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop metadata

## Prerequisites

**Required Modules:**
- `io`
- `pytest`
- `numpy`
- `numpy.lib._utils_impl`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign dt = np.dtype(...)

```python
dt = np.dtype([('l1', [('l2', np.dtype('S8', metadata={'msg': 'toto'}))])], metadata={'msg': 'titi'})
```

**Verification:**
```python
assert _compare_dtypes(dt, dt_m) is True
```

### Step 2: Assign dt_m = _utils_impl.drop_metadata(...)

```python
dt_m = _utils_impl.drop_metadata(dt)
```

**Verification:**
```python
assert dt_m.metadata is None
```

### Step 3: Assign dt = np.dtype(...)

```python
dt = np.dtype([('x', '<f8'), ('y', '<i4')], align=True, metadata={'msg': 'toto'})
```

**Verification:**
```python
assert dt_m['l1'].metadata is None
```

### Step 4: Assign dt_m = _utils_impl.drop_metadata(...)

```python
dt_m = _utils_impl.drop_metadata(dt)
```

**Verification:**
```python
assert dt_m['l1']['l2'].metadata is None
```

### Step 5: Assign dt = np.dtype(...)

```python
dt = np.dtype('8f', metadata={'msg': 'toto'})
```

**Verification:**
```python
assert _compare_dtypes(dt, dt_m) is True
```

### Step 6: Assign dt_m = _utils_impl.drop_metadata(...)

```python
dt_m = _utils_impl.drop_metadata(dt)
```

**Verification:**
```python
assert dt_m.metadata is None
```

### Step 7: Assign dt = np.dtype(...)

```python
dt = np.dtype('uint32', metadata={'msg': 'toto'})
```

**Verification:**
```python
assert _compare_dtypes(dt, dt_m) is True
```

### Step 8: Assign dt_m = _utils_impl.drop_metadata(...)

```python
dt_m = _utils_impl.drop_metadata(dt)
```

**Verification:**
```python
assert dt_m.metadata is None
```


## Complete Example

```python
# Workflow
def _compare_dtypes(dt1, dt2):
    return np.can_cast(dt1, dt2, casting='no')
dt = np.dtype([('l1', [('l2', np.dtype('S8', metadata={'msg': 'toto'}))])], metadata={'msg': 'titi'})
dt_m = _utils_impl.drop_metadata(dt)
assert _compare_dtypes(dt, dt_m) is True
assert dt_m.metadata is None
assert dt_m['l1'].metadata is None
assert dt_m['l1']['l2'].metadata is None
dt = np.dtype([('x', '<f8'), ('y', '<i4')], align=True, metadata={'msg': 'toto'})
dt_m = _utils_impl.drop_metadata(dt)
assert _compare_dtypes(dt, dt_m) is True
assert dt_m.metadata is None
dt = np.dtype('8f', metadata={'msg': 'toto'})
dt_m = _utils_impl.drop_metadata(dt)
assert _compare_dtypes(dt, dt_m) is True
assert dt_m.metadata is None
dt = np.dtype('uint32', metadata={'msg': 'toto'})
dt_m = _utils_impl.drop_metadata(dt)
assert _compare_dtypes(dt, dt_m) is True
assert dt_m.metadata is None
```

## Next Steps


---

*Source: test_utils.py:34 | Complexity: Advanced | Last updated: 2026-06-02*