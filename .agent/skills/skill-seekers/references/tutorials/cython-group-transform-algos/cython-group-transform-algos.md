# How To: Cython Group Transform Algos

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cython group transform algos

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.groupby`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign is_datetimelike = False

```python
is_datetimelike = False
```

### Step 2: Assign labels = np.array(...)

```python
labels = np.array([0, 0, 0, 0, 0], dtype=np.intp)
```

### Step 3: Assign ngroups = 1

```python
ngroups = 1
```

### Step 4: Assign data = np.array(...)

```python
data = np.array([[1], [2], [3], [np.nan], [4]], dtype='float64')
```

### Step 5: Assign actual = np.zeros_like(...)

```python
actual = np.zeros_like(data)
```

### Step 6: Call actual.fill()

```python
actual.fill(np.nan)
```

### Step 7: Call group_cumprod()

```python
group_cumprod(actual, data, labels, ngroups, is_datetimelike)
```

### Step 8: Assign expected = np.array(...)

```python
expected = np.array([1, 2, 6, np.nan, 24], dtype='float64')
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(actual[:, 0], expected)
```

### Step 10: Assign actual = np.zeros_like(...)

```python
actual = np.zeros_like(data)
```

### Step 11: Call actual.fill()

```python
actual.fill(np.nan)
```

### Step 12: Call group_cumsum()

```python
group_cumsum(actual, data, labels, ngroups, is_datetimelike)
```

### Step 13: Assign expected = np.array(...)

```python
expected = np.array([1, 3, 6, np.nan, 10], dtype='float64')
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(actual[:, 0], expected)
```

### Step 15: Assign is_datetimelike = True

```python
is_datetimelike = True
```

### Step 16: Assign data = value

```python
data = np.array([np.timedelta64(1, 'ns')] * 5, dtype='m8[ns]')[:, None]
```

### Step 17: Assign actual = np.zeros_like(...)

```python
actual = np.zeros_like(data, dtype='int64')
```

### Step 18: Call group_cumsum()

```python
group_cumsum(actual, data.view('int64'), labels, ngroups, is_datetimelike)
```

### Step 19: Assign expected = np.array(...)

```python
expected = np.array([np.timedelta64(1, 'ns'), np.timedelta64(2, 'ns'), np.timedelta64(3, 'ns'), np.timedelta64(4, 'ns'), np.timedelta64(5, 'ns')])
```

### Step 20: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(actual[:, 0].view('m8[ns]'), expected)
```


## Complete Example

```python
# Workflow
is_datetimelike = False
labels = np.array([0, 0, 0, 0, 0], dtype=np.intp)
ngroups = 1
data = np.array([[1], [2], [3], [np.nan], [4]], dtype='float64')
actual = np.zeros_like(data)
actual.fill(np.nan)
group_cumprod(actual, data, labels, ngroups, is_datetimelike)
expected = np.array([1, 2, 6, np.nan, 24], dtype='float64')
tm.assert_numpy_array_equal(actual[:, 0], expected)
actual = np.zeros_like(data)
actual.fill(np.nan)
group_cumsum(actual, data, labels, ngroups, is_datetimelike)
expected = np.array([1, 3, 6, np.nan, 10], dtype='float64')
tm.assert_numpy_array_equal(actual[:, 0], expected)
is_datetimelike = True
data = np.array([np.timedelta64(1, 'ns')] * 5, dtype='m8[ns]')[:, None]
actual = np.zeros_like(data, dtype='int64')
group_cumsum(actual, data.view('int64'), labels, ngroups, is_datetimelike)
expected = np.array([np.timedelta64(1, 'ns'), np.timedelta64(2, 'ns'), np.timedelta64(3, 'ns'), np.timedelta64(4, 'ns'), np.timedelta64(5, 'ns')])
tm.assert_numpy_array_equal(actual[:, 0].view('m8[ns]'), expected)
```

## Next Steps


---

*Source: test_libgroupby.py:202 | Complexity: Advanced | Last updated: 2026-06-02*