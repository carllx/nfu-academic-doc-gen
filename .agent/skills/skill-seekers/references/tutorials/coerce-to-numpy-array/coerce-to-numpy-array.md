# How To: Coerce To Numpy Array

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test coerce to numpy array

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `pandas.core.arrays.boolean`


## Step-by-Step Guide

### Step 1: Assign arr = pd.array(...)

```python
arr = pd.array([True, False, None], dtype='boolean')
```

### Step 2: Assign result = np.array(...)

```python
result = np.array(arr)
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([True, False, pd.NA], dtype='object')
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign arr = pd.array(...)

```python
arr = pd.array([True, False, True], dtype='boolean')
```

### Step 6: Assign result = np.array(...)

```python
result = np.array(arr)
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array([True, False, True], dtype='bool')
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 9: Assign result = np.array(...)

```python
result = np.array(arr, dtype='bool')
```

### Step 10: Assign expected = np.array(...)

```python
expected = np.array([True, False, True], dtype='bool')
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 12: Assign arr = pd.array(...)

```python
arr = pd.array([True, False, None], dtype='boolean')
```

### Step 13: Assign msg = "cannot convert to 'bool'-dtype NumPy array with missing values. Specify an appropriate 'na_value' for this dtype."

```python
msg = "cannot convert to 'bool'-dtype NumPy array with missing values. Specify an appropriate 'na_value' for this dtype."
```

### Step 14: Call np.array()

```python
np.array(arr, dtype='bool')
```


## Complete Example

```python
# Workflow
arr = pd.array([True, False, None], dtype='boolean')
result = np.array(arr)
expected = np.array([True, False, pd.NA], dtype='object')
tm.assert_numpy_array_equal(result, expected)
arr = pd.array([True, False, True], dtype='boolean')
result = np.array(arr)
expected = np.array([True, False, True], dtype='bool')
tm.assert_numpy_array_equal(result, expected)
result = np.array(arr, dtype='bool')
expected = np.array([True, False, True], dtype='bool')
tm.assert_numpy_array_equal(result, expected)
arr = pd.array([True, False, None], dtype='boolean')
msg = "cannot convert to 'bool'-dtype NumPy array with missing values. Specify an appropriate 'na_value' for this dtype."
with pytest.raises(ValueError, match=msg):
    np.array(arr, dtype='bool')
```

## Next Steps


---

*Source: test_construction.py:216 | Complexity: Advanced | Last updated: 2026-06-02*