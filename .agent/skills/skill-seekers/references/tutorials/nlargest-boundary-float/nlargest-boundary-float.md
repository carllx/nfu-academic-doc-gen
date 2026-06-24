# How To: Nlargest Boundary Float

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nlargest boundary float

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: nselect_method, float_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign dtype_info = np.finfo(...)

```python
dtype_info = np.finfo(float_numpy_dtype)
```

**Verification:**
```python
assert_check_nselect_boundary(vals, float_numpy_dtype, nselect_method)
```

### Step 2: Assign unknown = value

```python
min_val, max_val = (dtype_info.min, dtype_info.max)
```

### Step 3: Assign unknown = np.nextafter(...)

```python
min_2nd, max_2nd = np.nextafter([min_val, max_val], 0, dtype=float_numpy_dtype)
```

### Step 4: Assign vals = value

```python
vals = [min_val, min_2nd, max_2nd, max_val]
```

### Step 5: Call assert_check_nselect_boundary()

```python
assert_check_nselect_boundary(vals, float_numpy_dtype, nselect_method)
```


## Complete Example

```python
# Setup
# Fixtures: nselect_method, float_numpy_dtype

# Workflow
dtype_info = np.finfo(float_numpy_dtype)
min_val, max_val = (dtype_info.min, dtype_info.max)
min_2nd, max_2nd = np.nextafter([min_val, max_val], 0, dtype=float_numpy_dtype)
vals = [min_val, min_2nd, max_2nd, max_val]
assert_check_nselect_boundary(vals, float_numpy_dtype, nselect_method)
```

## Next Steps


---

*Source: test_nlargest.py:178 | Complexity: Intermediate | Last updated: 2026-06-02*