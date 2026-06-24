# How To: Searchsorted Numeric Dtypes Scalar

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test searchsorted numeric dtypes scalar

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_real_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign arr = pd.array(...)

```python
arr = pd.array([1, 3, 90], dtype=any_real_numpy_dtype)
```

**Verification:**
```python
assert is_scalar(result)
```

### Step 2: Assign result = arr.searchsorted(...)

```python
result = arr.searchsorted(30)
```

**Verification:**
```python
assert result == 2
```

### Step 3: Assign result = arr.searchsorted(...)

```python
result = arr.searchsorted([30])
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([2], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_real_numpy_dtype

# Workflow
arr = pd.array([1, 3, 90], dtype=any_real_numpy_dtype)
result = arr.searchsorted(30)
assert is_scalar(result)
assert result == 2
result = arr.searchsorted([30])
expected = np.array([2], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:21 | Complexity: Intermediate | Last updated: 2026-06-02*