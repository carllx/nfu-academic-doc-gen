# How To: Floating Array Constructor

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test floating array constructor

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.arrays.floating`


## Step-by-Step Guide

### Step 1: Assign values = np.array(...)

```python
values = np.array([1, 2, 3, 4], dtype='float64')
```

### Step 2: Assign mask = np.array(...)

```python
mask = np.array([False, False, False, True], dtype='bool')
```

### Step 3: Assign result = FloatingArray(...)

```python
result = FloatingArray(values, mask)
```

### Step 4: Assign expected = pd.array(...)

```python
expected = pd.array([1, 2, 3, np.nan], dtype='Float64')
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result._data, values)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result._mask, mask)
```

### Step 8: Assign msg = ".* should be .* numpy array. Use the 'pd.array' function instead"

```python
msg = ".* should be .* numpy array. Use the 'pd.array' function instead"
```

### Step 9: Assign msg = "__init__\\(\\) missing 1 required positional argument: 'mask'"

```python
msg = "__init__\\(\\) missing 1 required positional argument: 'mask'"
```

### Step 10: Call FloatingArray()

```python
FloatingArray(values.tolist(), mask)
```

### Step 11: Call FloatingArray()

```python
FloatingArray(values, mask.tolist())
```

### Step 12: Call FloatingArray()

```python
FloatingArray(values.astype(int), mask)
```

### Step 13: Call FloatingArray()

```python
FloatingArray(values)
```


## Complete Example

```python
# Workflow
values = np.array([1, 2, 3, 4], dtype='float64')
mask = np.array([False, False, False, True], dtype='bool')
result = FloatingArray(values, mask)
expected = pd.array([1, 2, 3, np.nan], dtype='Float64')
tm.assert_extension_array_equal(result, expected)
tm.assert_numpy_array_equal(result._data, values)
tm.assert_numpy_array_equal(result._mask, mask)
msg = ".* should be .* numpy array. Use the 'pd.array' function instead"
with pytest.raises(TypeError, match=msg):
    FloatingArray(values.tolist(), mask)
with pytest.raises(TypeError, match=msg):
    FloatingArray(values, mask.tolist())
with pytest.raises(TypeError, match=msg):
    FloatingArray(values.astype(int), mask)
msg = "__init__\\(\\) missing 1 required positional argument: 'mask'"
with pytest.raises(TypeError, match=msg):
    FloatingArray(values)
```

## Next Steps


---

*Source: test_construction.py:18 | Complexity: Advanced | Last updated: 2026-06-02*