# How To: Astype To Larger Numpy

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype to larger numpy

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.generic`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.integer`


## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([1, 2], dtype='Int32')
```

### Step 2: Assign result = a.astype(...)

```python
result = a.astype('int64')
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([1, 2], dtype='int64')
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign a = pd.array(...)

```python
a = pd.array([1, 2], dtype='UInt32')
```

### Step 6: Assign result = a.astype(...)

```python
result = a.astype('uint64')
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array([1, 2], dtype='uint64')
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = pd.array([1, 2], dtype='Int32')
result = a.astype('int64')
expected = np.array([1, 2], dtype='int64')
tm.assert_numpy_array_equal(result, expected)
a = pd.array([1, 2], dtype='UInt32')
result = a.astype('uint64')
expected = np.array([1, 2], dtype='uint64')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes.py:184 | Complexity: Advanced | Last updated: 2026-06-02*