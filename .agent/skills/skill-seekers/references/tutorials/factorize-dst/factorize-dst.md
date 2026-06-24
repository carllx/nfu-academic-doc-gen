# How To: Factorize Dst

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test factorize dst

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index_or_series
```

## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('2016-11-06', freq='h', periods=12, tz='US/Eastern')
```

**Verification:**
```python
assert res.freq == idx.freq
```

### Step 2: Assign obj = index_or_series(...)

```python
obj = index_or_series(idx)
```

**Verification:**
```python
assert res.freq == idx.freq
```

### Step 3: Assign unknown = obj.factorize(...)

```python
arr, res = obj.factorize()
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, np.arange(12, dtype=np.intp))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, idx)
```

### Step 6: Assign idx = date_range(...)

```python
idx = date_range('2016-06-13', freq='h', periods=12, tz='US/Eastern')
```

### Step 7: Assign obj = index_or_series(...)

```python
obj = index_or_series(idx)
```

### Step 8: Assign unknown = obj.factorize(...)

```python
arr, res = obj.factorize()
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, np.arange(12, dtype=np.intp))
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, idx)
```

**Verification:**
```python
assert res.freq == idx.freq
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series

# Workflow
idx = date_range('2016-11-06', freq='h', periods=12, tz='US/Eastern')
obj = index_or_series(idx)
arr, res = obj.factorize()
tm.assert_numpy_array_equal(arr, np.arange(12, dtype=np.intp))
tm.assert_index_equal(res, idx)
if index_or_series is Index:
    assert res.freq == idx.freq
idx = date_range('2016-06-13', freq='h', periods=12, tz='US/Eastern')
obj = index_or_series(idx)
arr, res = obj.factorize()
tm.assert_numpy_array_equal(arr, np.arange(12, dtype=np.intp))
tm.assert_index_equal(res, idx)
if index_or_series is Index:
    assert res.freq == idx.freq
```

## Next Steps


---

*Source: test_factorize.py:90 | Complexity: Advanced | Last updated: 2026-06-02*