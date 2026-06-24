# How To: To Numpy Float

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to numpy float

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
arr = con([0.1, 0.2, 0.3], dtype='Float64')
```

### Step 3: Assign result = arr.to_numpy(...)

```python
result = arr.to_numpy(dtype='float64')
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([0.1, 0.2, 0.3], dtype='float64')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign arr = con(...)

```python
arr = con([0.1, 0.2, None], dtype='Float64')
```

### Step 7: Assign result = arr.to_numpy(...)

```python
result = arr.to_numpy(dtype='float64')
```

### Step 8: Assign expected = np.array(...)

```python
expected = np.array([0.1, 0.2, np.nan], dtype='float64')
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 10: Assign result = arr.to_numpy(...)

```python
result = arr.to_numpy(dtype='float64', na_value=np.nan)
```

### Step 11: Assign expected = np.array(...)

```python
expected = np.array([0.1, 0.2, np.nan], dtype='float64')
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: box

# Workflow
con = pd.Series if box else pd.array
arr = con([0.1, 0.2, 0.3], dtype='Float64')
result = arr.to_numpy(dtype='float64')
expected = np.array([0.1, 0.2, 0.3], dtype='float64')
tm.assert_numpy_array_equal(result, expected)
arr = con([0.1, 0.2, None], dtype='Float64')
result = arr.to_numpy(dtype='float64')
expected = np.array([0.1, 0.2, np.nan], dtype='float64')
tm.assert_numpy_array_equal(result, expected)
result = arr.to_numpy(dtype='float64', na_value=np.nan)
expected = np.array([0.1, 0.2, np.nan], dtype='float64')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_to_numpy.py:26 | Complexity: Advanced | Last updated: 2026-06-02*