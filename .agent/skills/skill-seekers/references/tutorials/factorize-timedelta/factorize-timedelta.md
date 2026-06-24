# How To: Factorize Timedelta

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test factorize timedelta

## Prerequisites

**Required Modules:**
- `datetime`
- `struct`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.arrays`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign v1 = to_timedelta(...)

```python
v1 = to_timedelta('1 day 1 min')
```

### Step 2: Assign v2 = to_timedelta(...)

```python
v2 = to_timedelta('1 day')
```

### Step 3: Assign x = Series(...)

```python
x = Series([v1, v2, v1, v1, v2, v2, v1])
```

### Step 4: Assign unknown = algos.factorize(...)

```python
codes, uniques = algos.factorize(x)
```

### Step 5: Assign exp = np.array(...)

```python
exp = np.array([0, 1, 0, 0, 1, 1, 0], dtype=np.intp)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(codes, exp)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(uniques, to_timedelta([v1, v2]))
```

### Step 8: Assign unknown = algos.factorize(...)

```python
codes, uniques = algos.factorize(x, sort=True)
```

### Step 9: Assign exp = np.array(...)

```python
exp = np.array([1, 0, 1, 1, 0, 0, 1], dtype=np.intp)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(codes, exp)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(uniques, to_timedelta([v2, v1]))
```


## Complete Example

```python
# Workflow
v1 = to_timedelta('1 day 1 min')
v2 = to_timedelta('1 day')
x = Series([v1, v2, v1, v1, v2, v2, v1])
codes, uniques = algos.factorize(x)
exp = np.array([0, 1, 0, 0, 1, 1, 0], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
tm.assert_index_equal(uniques, to_timedelta([v1, v2]))
codes, uniques = algos.factorize(x, sort=True)
exp = np.array([1, 0, 1, 1, 0, 0, 1], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
tm.assert_index_equal(uniques, to_timedelta([v2, v1]))
```

## Next Steps


---

*Source: test_algos.py:202 | Complexity: Advanced | Last updated: 2026-06-02*