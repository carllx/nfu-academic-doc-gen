# How To: Scalar Coercion Same As Cast And Assignment

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Test that in most cases:
   * `np.array(scalar, dtype=dtype)`
   * `np.empty((), dtype=dtype)[()] = scalar`
   * `np.array(scalar).astype(dtype)`
should behave the same.  The only exceptions are parametric dtypes
(mainly datetime/timedelta without unit) and void without fields.

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
# Fixtures: cast_to
```

## Step-by-Step Guide

### Step 1: '\n        Test that in most cases:\n           * `np.array(scalar, dtype=dtype)`\n           * `np.empty((), dtype=dtype)[()] = scalar`\n           * `np.array(scalar).astype(dtype)`\n        should behave the same.  The only exceptions are parametric dtypes\n        (mainly datetime/timedelta without unit) and void without fields.\n        '

```python
'\n        Test that in most cases:\n           * `np.array(scalar, dtype=dtype)`\n           * `np.empty((), dtype=dtype)[()] = scalar`\n           * `np.array(scalar).astype(dtype)`\n        should behave the same.  The only exceptions are parametric dtypes\n        (mainly datetime/timedelta without unit) and void without fields.\n        '
```

**Verification:**
```python
assert_array_equal(arr, cast)
```

### Step 2: Assign dtype = value

```python
dtype = cast_to.dtype
```

**Verification:**
```python
assert_array_equal(ass, cast)
```

### Step 3: Assign scalar = value

```python
scalar = scalar.values[0]
```

### Step 4: Assign arr = np.array(...)

```python
arr = np.array(scalar, dtype=dtype)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(arr, cast)
```

### Step 6: Assign ass = np.zeros(...)

```python
ass = np.zeros((), dtype=dtype)
```

### Step 7: Assign unknown = scalar

```python
ass[()] = scalar
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(ass, cast)
```

### Step 9: Assign cast = np.array.astype(...)

```python
cast = np.array(scalar).astype(dtype)
```

### Step 10: Call np.array()

```python
np.array(scalar, dtype=dtype)
```

### Step 11: Call np.array()

```python
np.array([scalar], dtype=dtype)
```

### Step 12: Assign res = np.zeros(...)

```python
res = np.zeros((), dtype=dtype)
```

### Step 13: Call np.array.astype()

```python
np.array(scalar).astype(dtype)
```

### Step 14: Call np.array()

```python
np.array(scalar, dtype=dtype)
```

### Step 15: Call np.array()

```python
np.array([scalar], dtype=dtype)
```

### Step 16: Assign unknown = scalar

```python
res[()] = scalar
```


## Complete Example

```python
# Setup
# Fixtures: cast_to

# Workflow
'\n        Test that in most cases:\n           * `np.array(scalar, dtype=dtype)`\n           * `np.empty((), dtype=dtype)[()] = scalar`\n           * `np.array(scalar).astype(dtype)`\n        should behave the same.  The only exceptions are parametric dtypes\n        (mainly datetime/timedelta without unit) and void without fields.\n        '
dtype = cast_to.dtype
for scalar in scalar_instances(times=False):
    scalar = scalar.values[0]
    if dtype.type == np.void:
        if scalar.dtype.fields is not None and dtype.fields is None:
            with pytest.raises(TypeError):
                np.array(scalar).astype(dtype)
            np.array(scalar, dtype=dtype)
            np.array([scalar], dtype=dtype)
            continue
    try:
        cast = np.array(scalar).astype(dtype)
    except (TypeError, ValueError, RuntimeError):
        with pytest.raises(Exception):
            np.array(scalar, dtype=dtype)
        if isinstance(scalar, rational) and np.issubdtype(dtype, np.signedinteger):
            return
        with pytest.raises(Exception):
            np.array([scalar], dtype=dtype)
        res = np.zeros((), dtype=dtype)
        with pytest.raises(Exception):
            res[()] = scalar
        return
    arr = np.array(scalar, dtype=dtype)
    assert_array_equal(arr, cast)
    ass = np.zeros((), dtype=dtype)
    ass[()] = scalar
    assert_array_equal(ass, cast)
```

## Next Steps


---

*Source: test_array_coercion.py:288 | Complexity: Advanced | Last updated: 2026-06-02*