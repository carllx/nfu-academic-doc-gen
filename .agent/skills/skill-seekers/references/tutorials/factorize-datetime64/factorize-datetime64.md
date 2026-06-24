# How To: Factorize Datetime64

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test factorize datetime64

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

### Step 1: Assign v1 = Timestamp(...)

```python
v1 = Timestamp('20130101 09:00:00.00004')
```

### Step 2: Assign v2 = Timestamp(...)

```python
v2 = Timestamp('20130101')
```

### Step 3: Assign x = Series(...)

```python
x = Series([v1, v1, v1, v2, v2, v1])
```

### Step 4: Assign unknown = algos.factorize(...)

```python
codes, uniques = algos.factorize(x)
```

### Step 5: Assign exp = np.array(...)

```python
exp = np.array([0, 0, 0, 1, 1, 0], dtype=np.intp)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(codes, exp)
```

### Step 7: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex([v1, v2])
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(uniques, exp)
```

### Step 9: Assign unknown = algos.factorize(...)

```python
codes, uniques = algos.factorize(x, sort=True)
```

### Step 10: Assign exp = np.array(...)

```python
exp = np.array([1, 1, 1, 0, 0, 1], dtype=np.intp)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(codes, exp)
```

### Step 12: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex([v2, v1])
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(uniques, exp)
```


## Complete Example

```python
# Workflow
v1 = Timestamp('20130101 09:00:00.00004')
v2 = Timestamp('20130101')
x = Series([v1, v1, v1, v2, v2, v1])
codes, uniques = algos.factorize(x)
exp = np.array([0, 0, 0, 1, 1, 0], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
exp = DatetimeIndex([v1, v2])
tm.assert_index_equal(uniques, exp)
codes, uniques = algos.factorize(x, sort=True)
exp = np.array([1, 1, 1, 0, 0, 1], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
exp = DatetimeIndex([v2, v1])
tm.assert_index_equal(uniques, exp)
```

## Next Steps


---

*Source: test_algos.py:167 | Complexity: Advanced | Last updated: 2026-06-02*