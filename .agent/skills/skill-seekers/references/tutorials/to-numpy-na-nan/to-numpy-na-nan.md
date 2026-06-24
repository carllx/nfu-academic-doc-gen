# How To: To Numpy Na Nan

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to numpy na nan

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.generic`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.integer`

**Setup Required:**
```python
# Fixtures: in_series
```

## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([0, 1, None], dtype='Int64')
```

### Step 2: Assign result = a.to_numpy(...)

```python
result = a.to_numpy(dtype='float64', na_value=np.nan)
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([0.0, 1.0, np.nan], dtype='float64')
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = a.to_numpy(...)

```python
result = a.to_numpy(dtype='int64', na_value=-1)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([0, 1, -1], dtype='int64')
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 8: Assign result = a.to_numpy(...)

```python
result = a.to_numpy(dtype='bool', na_value=False)
```

### Step 9: Assign expected = np.array(...)

```python
expected = np.array([False, True, False], dtype='bool')
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 11: Assign a = pd.Series(...)

```python
a = pd.Series(a)
```


## Complete Example

```python
# Setup
# Fixtures: in_series

# Workflow
a = pd.array([0, 1, None], dtype='Int64')
if in_series:
    a = pd.Series(a)
result = a.to_numpy(dtype='float64', na_value=np.nan)
expected = np.array([0.0, 1.0, np.nan], dtype='float64')
tm.assert_numpy_array_equal(result, expected)
result = a.to_numpy(dtype='int64', na_value=-1)
expected = np.array([0, 1, -1], dtype='int64')
tm.assert_numpy_array_equal(result, expected)
result = a.to_numpy(dtype='bool', na_value=False)
expected = np.array([False, True, False], dtype='bool')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes.py:244 | Complexity: Advanced | Last updated: 2026-06-02*