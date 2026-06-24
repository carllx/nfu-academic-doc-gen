# How To: Cython Group Mean Inf At Begining And End

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cython group mean Inf at begining and end

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

### Step 1: Assign actual = np.array(...)

```python
actual = np.array([[np.nan, np.nan], [np.nan, np.nan]], dtype='float64')
```

### Step 2: Assign counts = np.array(...)

```python
counts = np.array([0, 0], dtype='int64')
```

### Step 3: Assign data = np.array(...)

```python
data = np.array([[np.inf, 1.0], [1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0], [5, np.inf]], dtype='float64')
```

### Step 4: Assign labels = np.array(...)

```python
labels = np.array([0, 1, 0, 1, 0, 1], dtype=np.intp)
```

### Step 5: Call group_mean()

```python
group_mean(actual, counts, data, labels, is_datetimelike=False)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([[np.inf, 3], [3, np.inf]], dtype='float64')
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(actual, expected)
```


## Complete Example

```python
# Workflow
actual = np.array([[np.nan, np.nan], [np.nan, np.nan]], dtype='float64')
counts = np.array([0, 0], dtype='int64')
data = np.array([[np.inf, 1.0], [1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0], [5, np.inf]], dtype='float64')
labels = np.array([0, 1, 0, 1, 0, 1], dtype=np.intp)
group_mean(actual, counts, data, labels, is_datetimelike=False)
expected = np.array([[np.inf, 3], [3, np.inf]], dtype='float64')
tm.assert_numpy_array_equal(actual, expected)
```

## Next Steps


---

*Source: test_libgroupby.py:288 | Complexity: Intermediate | Last updated: 2026-06-02*