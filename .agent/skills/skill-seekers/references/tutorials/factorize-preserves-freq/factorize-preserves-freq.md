# How To: Factorize Preserves Freq

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test factorize preserves freq

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx3 = timedelta_range(...)

```python
idx3 = timedelta_range('1 day', periods=4, freq='s')
```

**Verification:**
```python
assert idx.freq == idx3.freq
```

### Step 2: Assign exp_arr = np.array(...)

```python
exp_arr = np.array([0, 1, 2, 3], dtype=np.intp)
```

**Verification:**
```python
assert idx.freq == idx3.freq
```

### Step 3: Assign unknown = idx3.factorize(...)

```python
arr, idx = idx3.factorize()
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, exp_arr)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, idx3)
```

**Verification:**
```python
assert idx.freq == idx3.freq
```

### Step 6: Assign unknown = factorize(...)

```python
arr, idx = factorize(idx3)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, exp_arr)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, idx3)
```

**Verification:**
```python
assert idx.freq == idx3.freq
```


## Complete Example

```python
# Workflow
idx3 = timedelta_range('1 day', periods=4, freq='s')
exp_arr = np.array([0, 1, 2, 3], dtype=np.intp)
arr, idx = idx3.factorize()
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, idx3)
assert idx.freq == idx3.freq
arr, idx = factorize(idx3)
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, idx3)
assert idx.freq == idx3.freq
```

## Next Steps


---

*Source: test_factorize.py:28 | Complexity: Advanced | Last updated: 2026-06-02*