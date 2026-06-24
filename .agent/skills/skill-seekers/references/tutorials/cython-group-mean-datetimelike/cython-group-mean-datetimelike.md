# How To: Cython Group Mean Datetimelike

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cython group mean datetimelike

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

### Step 1: Assign actual = np.zeros(...)

```python
actual = np.zeros(shape=(1, 1), dtype='float64')
```

### Step 2: Assign counts = np.array(...)

```python
counts = np.array([0], dtype='int64')
```

### Step 3: Assign data = unknown.view.astype(...)

```python
data = np.array([np.timedelta64(2, 'ns'), np.timedelta64(4, 'ns'), np.timedelta64('NaT')], dtype='m8[ns]')[:, None].view('int64').astype('float64')
```

### Step 4: Assign labels = np.zeros(...)

```python
labels = np.zeros(len(data), dtype=np.intp)
```

### Step 5: Call group_mean()

```python
group_mean(actual, counts, data, labels, is_datetimelike=True)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(actual[:, 0], np.array([3], dtype='float64'))
```


## Complete Example

```python
# Workflow
actual = np.zeros(shape=(1, 1), dtype='float64')
counts = np.array([0], dtype='int64')
data = np.array([np.timedelta64(2, 'ns'), np.timedelta64(4, 'ns'), np.timedelta64('NaT')], dtype='m8[ns]')[:, None].view('int64').astype('float64')
labels = np.zeros(len(data), dtype=np.intp)
group_mean(actual, counts, data, labels, is_datetimelike=True)
tm.assert_numpy_array_equal(actual[:, 0], np.array([3], dtype='float64'))
```

## Next Steps


---

*Source: test_libgroupby.py:240 | Complexity: Intermediate | Last updated: 2026-06-02*