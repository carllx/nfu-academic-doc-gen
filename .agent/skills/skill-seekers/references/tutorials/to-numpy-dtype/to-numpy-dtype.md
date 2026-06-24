# How To: To Numpy Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to numpy dtype

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
# Fixtures: dtype, in_series
```

## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([0, 1], dtype='Int64')
```

### Step 2: Assign result = a.to_numpy(...)

```python
result = a.to_numpy(dtype=dtype)
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([0, 1], dtype=dtype)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign a = pd.Series(...)

```python
a = pd.Series(a)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, in_series

# Workflow
a = pd.array([0, 1], dtype='Int64')
if in_series:
    a = pd.Series(a)
result = a.to_numpy(dtype=dtype)
expected = np.array([0, 1], dtype=dtype)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes.py:264 | Complexity: Intermediate | Last updated: 2026-06-02*