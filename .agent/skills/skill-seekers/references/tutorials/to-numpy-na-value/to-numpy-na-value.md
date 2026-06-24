# How To: To Numpy Na Value

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to numpy na value

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
arr = con([0.0, 1.0, None], dtype='Float64')
```

### Step 3: Assign result = arr.to_numpy(...)

```python
result = arr.to_numpy(dtype=object, na_value=None)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([0.0, 1.0, None], dtype='object')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign result = arr.to_numpy(...)

```python
result = arr.to_numpy(dtype=bool, na_value=False)
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array([False, True, False], dtype='bool')
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 9: Assign result = arr.to_numpy(...)

```python
result = arr.to_numpy(dtype='int64', na_value=-99)
```

### Step 10: Assign expected = np.array(...)

```python
expected = np.array([0, 1, -99], dtype='int64')
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: box

# Workflow
con = pd.Series if box else pd.array
arr = con([0.0, 1.0, None], dtype='Float64')
result = arr.to_numpy(dtype=object, na_value=None)
expected = np.array([0.0, 1.0, None], dtype='object')
tm.assert_numpy_array_equal(result, expected)
result = arr.to_numpy(dtype=bool, na_value=False)
expected = np.array([False, True, False], dtype='bool')
tm.assert_numpy_array_equal(result, expected)
result = arr.to_numpy(dtype='int64', na_value=-99)
expected = np.array([0, 1, -99], dtype='int64')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_to_numpy.py:67 | Complexity: Advanced | Last updated: 2026-06-02*