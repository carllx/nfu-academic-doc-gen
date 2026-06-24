# How To: Transpose Get View Dt64Tzget View

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transpose get view dt64tzget view

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=6, tz='US/Pacific')
```

**Verification:**
```python
assert df._mgr.nblocks == 1
```

### Step 2: Assign arr = dti._data.reshape(...)

```python
arr = dti._data.reshape(3, 2)
```

**Verification:**
```python
assert result._mgr.nblocks == 1
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(arr)
```

**Verification:**
```python
assert np.shares_memory(df._mgr.blocks[0].values._ndarray, rtrip._ndarray)
```

### Step 4: Assign result = value

```python
result = df.T
```

**Verification:**
```python
assert np.shares_memory(arr._ndarray, rtrip._ndarray)
```

### Step 5: Assign rtrip = value

```python
rtrip = result._mgr.blocks[0].values
```

**Verification:**
```python
assert np.shares_memory(df._mgr.blocks[0].values._ndarray, rtrip._ndarray)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
dti = date_range('2016-01-01', periods=6, tz='US/Pacific')
arr = dti._data.reshape(3, 2)
df = DataFrame(arr)
assert df._mgr.nblocks == 1
result = df.T
assert result._mgr.nblocks == 1
rtrip = result._mgr.blocks[0].values
if using_copy_on_write:
    assert np.shares_memory(df._mgr.blocks[0].values._ndarray, rtrip._ndarray)
else:
    assert np.shares_memory(arr._ndarray, rtrip._ndarray)
```

## Next Steps


---

*Source: test_transpose.py:141 | Complexity: Intermediate | Last updated: 2026-06-02*