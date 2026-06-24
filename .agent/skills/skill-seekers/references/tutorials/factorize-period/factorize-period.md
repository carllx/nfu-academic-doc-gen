# How To: Factorize Period

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test factorize period

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = PeriodIndex(...)

```python
idx1 = PeriodIndex(['2014-01', '2014-01', '2014-02', '2014-02', '2014-03', '2014-03'], freq='M')
```

### Step 2: Assign exp_arr = np.array(...)

```python
exp_arr = np.array([0, 0, 1, 1, 2, 2], dtype=np.intp)
```

### Step 3: Assign exp_idx = PeriodIndex(...)

```python
exp_idx = PeriodIndex(['2014-01', '2014-02', '2014-03'], freq='M')
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


## Complete Example

```python
# Workflow
idx1 = PeriodIndex(['2014-01', '2014-01', '2014-02', '2014-02', '2014-03', '2014-03'], freq='M')
exp_arr = np.array([0, 0, 1, 1, 2, 2], dtype=np.intp)
exp_idx = PeriodIndex(['2014-01', '2014-02', '2014-03'], freq='M')
arr, idx = idx1.factorize()
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
arr, idx = idx1.factorize(sort=True)
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
```

## Next Steps


---

*Source: test_factorize.py:8 | Complexity: Advanced | Last updated: 2026-06-02*