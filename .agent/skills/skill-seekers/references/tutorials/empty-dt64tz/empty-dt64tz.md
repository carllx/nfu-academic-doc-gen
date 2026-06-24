# How To: Empty Dt64Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty dt64tz

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=2, tz='Asia/Tokyo')
```

**Verification:**
```python
assert result.dtype == dtype
```

### Step 2: Assign dtype = value

```python
dtype = dti.dtype
```

**Verification:**
```python
assert isinstance(result, DatetimeArray)
```

### Step 3: Assign shape = value

```python
shape = (0,)
```

**Verification:**
```python
assert result.shape == shape
```

### Step 4: Assign result = DatetimeArray._empty(...)

```python
result = DatetimeArray._empty(shape, dtype=dtype)
```

**Verification:**
```python
assert result.dtype == dtype
```


## Complete Example

```python
# Workflow
dti = date_range('2016-01-01', periods=2, tz='Asia/Tokyo')
dtype = dti.dtype
shape = (0,)
result = DatetimeArray._empty(shape, dtype=dtype)
assert result.dtype == dtype
assert isinstance(result, DatetimeArray)
assert result.shape == shape
```

## Next Steps


---

*Source: test_ndarray_backed.py:45 | Complexity: Intermediate | Last updated: 2026-06-02*