# How To: Nonequivalent Record

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test whether different subarray dtypes hash differently.

## Prerequisites

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


## Step-by-Step Guide

### Step 1: 'Test whether different subarray dtypes hash differently.'

```python
'Test whether different subarray dtypes hash differently.'
```

**Verification:**
```python
assert_dtype_not_equal(a, b)
```

### Step 2: Assign a = np.dtype(...)

```python
a = np.dtype((int, (2, 3)))
```

**Verification:**
```python
assert_dtype_not_equal(a, b)
```

### Step 3: Assign b = np.dtype(...)

```python
b = np.dtype((int, (3, 2)))
```

**Verification:**
```python
assert_dtype_not_equal(a, b)
```

### Step 4: Call assert_dtype_not_equal()

```python
assert_dtype_not_equal(a, b)
```

### Step 5: Assign a = np.dtype(...)

```python
a = np.dtype((int, (2, 3)))
```

### Step 6: Assign b = np.dtype(...)

```python
b = np.dtype((int, (2, 2)))
```

### Step 7: Call assert_dtype_not_equal()

```python
assert_dtype_not_equal(a, b)
```

### Step 8: Assign a = np.dtype(...)

```python
a = np.dtype((int, (1, 2, 3)))
```

### Step 9: Assign b = np.dtype(...)

```python
b = np.dtype((int, (1, 2)))
```

### Step 10: Call assert_dtype_not_equal()

```python
assert_dtype_not_equal(a, b)
```


## Complete Example

```python
# Workflow
'Test whether different subarray dtypes hash differently.'
a = np.dtype((int, (2, 3)))
b = np.dtype((int, (3, 2)))
assert_dtype_not_equal(a, b)
a = np.dtype((int, (2, 3)))
b = np.dtype((int, (2, 2)))
assert_dtype_not_equal(a, b)
a = np.dtype((int, (1, 2, 3)))
b = np.dtype((int, (1, 2)))
assert_dtype_not_equal(a, b)
```

## Next Steps


---

*Source: test_dtype.py:648 | Complexity: Advanced | Last updated: 2026-06-02*