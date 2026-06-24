# How To: Factorize Period Nonmonotonic

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test factorize period nonmonotonic

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx2 = PeriodIndex(...)

```python
idx2 = PeriodIndex(['2014-03', '2014-03', '2014-02', '2014-01', '2014-03', '2014-01'], freq='M')
```

### Step 2: Assign exp_idx = PeriodIndex(...)

```python
exp_idx = PeriodIndex(['2014-01', '2014-02', '2014-03'], freq='M')
```

### Step 3: Assign exp_arr = np.array(...)

```python
exp_arr = np.array([2, 2, 1, 0, 2, 0], dtype=np.intp)
```

### Step 4: Assign unknown = idx2.factorize(...)

```python
arr, idx = idx2.factorize(sort=True)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, exp_arr)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, exp_idx)
```

### Step 7: Assign exp_arr = np.array(...)

```python
exp_arr = np.array([0, 0, 1, 2, 0, 2], dtype=np.intp)
```

### Step 8: Assign exp_idx = PeriodIndex(...)

```python
exp_idx = PeriodIndex(['2014-03', '2014-02', '2014-01'], freq='M')
```

### Step 9: Assign unknown = idx2.factorize(...)

```python
arr, idx = idx2.factorize()
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, exp_arr)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, exp_idx)
```


## Complete Example

```python
# Workflow
idx2 = PeriodIndex(['2014-03', '2014-03', '2014-02', '2014-01', '2014-03', '2014-01'], freq='M')
exp_idx = PeriodIndex(['2014-01', '2014-02', '2014-03'], freq='M')
exp_arr = np.array([2, 2, 1, 0, 2, 0], dtype=np.intp)
arr, idx = idx2.factorize(sort=True)
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
exp_arr = np.array([0, 0, 1, 2, 0, 2], dtype=np.intp)
exp_idx = PeriodIndex(['2014-03', '2014-02', '2014-01'], freq='M')
arr, idx = idx2.factorize()
tm.assert_numpy_array_equal(arr, exp_arr)
tm.assert_index_equal(idx, exp_idx)
```

## Next Steps


---

*Source: test_factorize.py:25 | Complexity: Advanced | Last updated: 2026-06-02*