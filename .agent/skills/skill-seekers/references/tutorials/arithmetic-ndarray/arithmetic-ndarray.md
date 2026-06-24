# How To: Arithmetic Ndarray

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test arithmetic ndarray

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pickle`
- `numpy`
- `pytest`
- `pandas._libs.missing`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: shape, all_arithmetic_functions
```

## Step-by-Step Guide

### Step 1: Assign op = all_arithmetic_functions

```python
op = all_arithmetic_functions
```

### Step 2: Assign a = np.zeros(...)

```python
a = np.zeros(shape)
```

### Step 3: Assign result = op(...)

```python
result = op(NA, a)
```

### Step 4: Assign expected = np.full(...)

```python
expected = np.full(a.shape, NA, dtype=object)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: shape, all_arithmetic_functions

# Workflow
op = all_arithmetic_functions
a = np.zeros(shape)
if op.__name__ == 'pow':
    a += 5
result = op(NA, a)
expected = np.full(a.shape, NA, dtype=object)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_na_scalar.py:204 | Complexity: Intermediate | Last updated: 2026-06-02*