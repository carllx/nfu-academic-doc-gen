# How To: Integer Array Constructor

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test integer array constructor

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.arrays`
- `pandas.core.arrays.integer`


## Step-by-Step Guide

### Step 1: Assign values = np.array(...)

```python
values = np.array([1, 2, 3, 4], dtype='int64')
```

### Step 2: Assign mask = np.array(...)

```python
mask = np.array([False, False, False, True], dtype='bool')
```

### Step 3: Assign result = IntegerArray(...)

```python
result = IntegerArray(values, mask)
```

### Step 4: Assign expected = pd.array(...)

```python
expected = pd.array([1, 2, 3, np.nan], dtype='Int64')
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 6: Assign msg = ".* should be .* numpy array. Use the 'pd.array' function instead"

```python
msg = ".* should be .* numpy array. Use the 'pd.array' function instead"
```

### Step 7: Assign msg = "__init__\\(\\) missing 1 required positional argument: 'mask'"

```python
msg = "__init__\\(\\) missing 1 required positional argument: 'mask'"
```

### Step 8: Call IntegerArray()

```python
IntegerArray(values.tolist(), mask)
```

### Step 9: Call IntegerArray()

```python
IntegerArray(values, mask.tolist())
```

### Step 10: Call IntegerArray()

```python
IntegerArray(values.astype(float), mask)
```

### Step 11: Call IntegerArray()

```python
IntegerArray(values)
```


## Complete Example

```python
# Workflow
values = np.array([1, 2, 3, 4], dtype='int64')
mask = np.array([False, False, False, True], dtype='bool')
result = IntegerArray(values, mask)
expected = pd.array([1, 2, 3, np.nan], dtype='Int64')
tm.assert_extension_array_equal(result, expected)
msg = ".* should be .* numpy array. Use the 'pd.array' function instead"
with pytest.raises(TypeError, match=msg):
    IntegerArray(values.tolist(), mask)
with pytest.raises(TypeError, match=msg):
    IntegerArray(values, mask.tolist())
with pytest.raises(TypeError, match=msg):
    IntegerArray(values.astype(float), mask)
msg = "__init__\\(\\) missing 1 required positional argument: 'mask'"
with pytest.raises(TypeError, match=msg):
    IntegerArray(values)
```

## Next Steps


---

*Source: test_construction.py:75 | Complexity: Advanced | Last updated: 2026-06-02*