# How To: To Numpy Int

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to numpy int

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: box
```

## Step-by-Step Guide

### Step 1: Assign con = value

```python
con = pd.Series if box else pd.array
```

### Step 2: Assign arr = con(...)

```python
arr = con([1.0, 2.0, 3.0], dtype='Float64')
```

### Step 3: Assign result = arr.to_numpy(...)

```python
result = arr.to_numpy(dtype='int64')
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([1, 2, 3], dtype='int64')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign arr = con(...)

```python
arr = con([1.0, 2.0, None], dtype='Float64')
```

### Step 7: Assign arr = con(...)

```python
arr = con([0.1, 0.9, 1.1], dtype='Float64')
```

### Step 8: Assign result = arr.to_numpy(...)

```python
result = arr.to_numpy(dtype='int64')
```

### Step 9: Assign expected = np.array(...)

```python
expected = np.array([0, 0, 1], dtype='int64')
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 11: Assign result = arr.to_numpy(...)

```python
result = arr.to_numpy(dtype='int64')
```


## Complete Example

```python
# Setup
# Fixtures: box

# Workflow
con = pd.Series if box else pd.array
arr = con([1.0, 2.0, 3.0], dtype='Float64')
result = arr.to_numpy(dtype='int64')
expected = np.array([1, 2, 3], dtype='int64')
tm.assert_numpy_array_equal(result, expected)
arr = con([1.0, 2.0, None], dtype='Float64')
with pytest.raises(ValueError, match="cannot convert to 'int64'-dtype"):
    result = arr.to_numpy(dtype='int64')
arr = con([0.1, 0.9, 1.1], dtype='Float64')
result = arr.to_numpy(dtype='int64')
expected = np.array([0, 0, 1], dtype='int64')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_to_numpy.py:46 | Complexity: Advanced | Last updated: 2026-06-02*