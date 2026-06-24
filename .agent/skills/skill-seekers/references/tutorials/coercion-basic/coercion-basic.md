# How To: Coercion Basic

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test coercion basic

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy._core._rational_tests`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: dtype, scalar
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array(scalar, dtype=dtype)
```

**Verification:**
```python
assert_array_equal(arr, cast)
```

### Step 2: Assign cast = np.array.astype(...)

```python
cast = np.array(scalar).astype(dtype)
```

**Verification:**
```python
assert_array_equal(ass, cast)
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(arr, cast)
```

### Step 4: Assign ass = np.ones(...)

```python
ass = np.ones((), dtype=dtype)
```

### Step 5: Assign unknown = scalar

```python
ass[()] = scalar
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(ass, cast)
```

### Step 7: Assign unknown = scalar

```python
ass[()] = scalar
```


## Complete Example

```python
# Setup
# Fixtures: dtype, scalar

# Workflow
arr = np.array(scalar, dtype=dtype)
cast = np.array(scalar).astype(dtype)
assert_array_equal(arr, cast)
ass = np.ones((), dtype=dtype)
if issubclass(dtype, np.integer):
    with pytest.raises(TypeError):
        ass[()] = scalar
else:
    ass[()] = scalar
    assert_array_equal(ass, cast)
```

## Next Steps


---

*Source: test_array_coercion.py:407 | Complexity: Intermediate | Last updated: 2026-06-02*