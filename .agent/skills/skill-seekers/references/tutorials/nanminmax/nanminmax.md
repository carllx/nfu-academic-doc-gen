# How To: Nanminmax

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nanminmax

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays.string_arrow`

**Setup Required:**
```python
# Fixtures: opname, dtype, val, index_or_series
```

## Step-by-Step Guide

### Step 1: Assign klass = index_or_series

```python
klass = index_or_series
```

**Verification:**
```python
assert check_missing(getattr(obj, opname)())
```

### Step 2: Assign obj = klass(...)

```python
obj = klass([None], dtype=dtype)
```

**Verification:**
```python
assert check_missing(getattr(obj, opname)(skipna=False))
```

### Step 3: Assign obj = klass(...)

```python
obj = klass([], dtype=dtype)
```

**Verification:**
```python
assert check_missing(getattr(obj, opname)())
```

### Step 4: Assign obj = klass(...)

```python
obj = klass([None, val], dtype=dtype)
```

**Verification:**
```python
assert check_missing(getattr(obj, opname)(skipna=False))
```

### Step 5: Assign obj = klass(...)

```python
obj = klass([None, val, None], dtype=dtype)
```

**Verification:**
```python
assert getattr(obj, opname)() == val
```


## Complete Example

```python
# Setup
# Fixtures: opname, dtype, val, index_or_series

# Workflow
klass = index_or_series

def check_missing(res):
    if dtype == 'datetime64[ns]':
        return res is NaT
    elif dtype in ['Int64', 'boolean']:
        return res is pd.NA
    else:
        return isna(res)
obj = klass([None], dtype=dtype)
assert check_missing(getattr(obj, opname)())
assert check_missing(getattr(obj, opname)(skipna=False))
obj = klass([], dtype=dtype)
assert check_missing(getattr(obj, opname)())
assert check_missing(getattr(obj, opname)(skipna=False))
if dtype == 'object':
    return
obj = klass([None, val], dtype=dtype)
assert getattr(obj, opname)() == val
assert check_missing(getattr(obj, opname)(skipna=False))
obj = klass([None, val, None], dtype=dtype)
assert getattr(obj, opname)() == val
assert check_missing(getattr(obj, opname)(skipna=False))
```

## Next Steps


---

*Source: test_reductions.py:90 | Complexity: Intermediate | Last updated: 2026-06-02*