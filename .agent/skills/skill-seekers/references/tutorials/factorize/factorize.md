# How To: Factorize

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test factorize

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = TimedeltaIndex(...)

```python
idx1 = TimedeltaIndex(['1 day', '1 day', '2 day', '2 day', '3 day', '3 day'])
```

**Verification:**
```python
assert idx.freq == exp_idx.freq
```

### Step 2: Assign exp_arr = np.array(...)

```python
exp_arr = np.array([0, 0, 1, 1, 2, 2], dtype=np.intp)
```

**Verification:**
```python
assert idx.freq == exp_idx.freq
```

### Step 3: Assign exp_idx = TimedeltaIndex(...)

```python
exp_idx = TimedeltaIndex(['1 day', '2 day', '3 day'])
```

### Step 4: Assign unknown = idx1.factorize(...)

```python
arr, idx = idx1.factorize()
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, exp_arr)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, exp_idx)
```

**Verification:**
```python
assert idx.freq == exp_idx.freq
```

### Step 7: Assign unknown = idx1.factorize(...)

```python
arr, idx = idx1.factorize(sort=True)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, exp_arr)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, exp_idx)
```

**Verification:**
```python
assert idx.freq == exp_idx.freq
```


## Complete Example

```python
# Workflow
idx1 = TimedeltaIndex(['1 day', '1 day', '2 day', '2 day', '3 day', '3 day'])
exp_arr = np.array([0, 0, 1, 1, 2, 2], dtype=np.intp)
exp_idx = TimedeltaIndex(['1 day', '2 day', '3 day'])
arr, idx = idx1.factorize()
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
assert idx.freq == exp_idx.freq
arr, idx = idx1.factorize(sort=True)
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
assert idx.freq == exp_idx.freq
```

## Next Steps


---

*Source: test_factorize.py:12 | Complexity: Advanced | Last updated: 2026-06-02*