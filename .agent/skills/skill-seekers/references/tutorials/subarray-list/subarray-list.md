# How To: Subarray List

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test subarray list

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `ctypes`
- `gc`
- `inspect`
- `operator`
- `pickle`
- `sys`
- `types`
- `itertools`
- `typing`
- `hypothesis`
- `pytest`
- `hypothesis.extra`
- `numpy`
- `numpy.dtypes`
- `numpy._core._multiarray_tests`
- `numpy._core._rational_tests`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: obj, dtype, expected
```

## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype(dtype)
```

**Verification:**
```python
assert_array_equal(res, expected)
```

### Step 2: Assign res = np.array(...)

```python
res = np.array(obj, dtype=dtype)
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(res, expected)
```

### Step 4: Assign expected = np.empty(...)

```python
expected = np.empty(len(obj), dtype=dtype)
```

### Step 5: Assign unknown = value

```python
expected[i] = obj[i]
```


## Complete Example

```python
# Setup
# Fixtures: obj, dtype, expected

# Workflow
dtype = np.dtype(dtype)
res = np.array(obj, dtype=dtype)
if expected is None:
    expected = np.empty(len(obj), dtype=dtype)
    for i in range(len(expected)):
        expected[i] = obj[i]
assert_array_equal(res, expected)
```

## Next Steps


---

*Source: test_dtype.py:463 | Complexity: Intermediate | Last updated: 2026-06-02*