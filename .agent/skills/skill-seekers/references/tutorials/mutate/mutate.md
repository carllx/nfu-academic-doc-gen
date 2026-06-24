# How To: Mutate

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mutate

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

### Step 1: Assign a = np.dtype(...)

```python
a = np.dtype([('yo', int)])
```

**Verification:**
```python
assert_dtype_equal(a, b)
```

### Step 2: Assign b = np.dtype(...)

```python
b = np.dtype([('yo', int)])
```

**Verification:**
```python
assert_dtype_not_equal(a, c)
```

### Step 3: Assign c = np.dtype(...)

```python
c = np.dtype([('ye', int)])
```

**Verification:**
```python
assert_dtype_equal(a, c)
```

### Step 4: Call assert_dtype_equal()

```python
assert_dtype_equal(a, b)
```

**Verification:**
```python
assert_dtype_not_equal(a, b)
```

### Step 5: Call assert_dtype_not_equal()

```python
assert_dtype_not_equal(a, c)
```

**Verification:**
```python
assert_dtype_equal(a, b)
```

### Step 6: Assign a.names = value

```python
a.names = ['ye']
```

**Verification:**
```python
assert_dtype_not_equal(a, c)
```

### Step 7: Call assert_dtype_equal()

```python
assert_dtype_equal(a, c)
```

### Step 8: Call assert_dtype_not_equal()

```python
assert_dtype_not_equal(a, b)
```

### Step 9: Assign state = value

```python
state = b.__reduce__()[2]
```

### Step 10: Call a.__setstate__()

```python
a.__setstate__(state)
```

### Step 11: Call assert_dtype_equal()

```python
assert_dtype_equal(a, b)
```

### Step 12: Call assert_dtype_not_equal()

```python
assert_dtype_not_equal(a, c)
```


## Complete Example

```python
# Workflow
a = np.dtype([('yo', int)])
b = np.dtype([('yo', int)])
c = np.dtype([('ye', int)])
assert_dtype_equal(a, b)
assert_dtype_not_equal(a, c)
a.names = ['ye']
assert_dtype_equal(a, c)
assert_dtype_not_equal(a, b)
state = b.__reduce__()[2]
a.__setstate__(state)
assert_dtype_equal(a, b)
assert_dtype_not_equal(a, c)
```

## Next Steps


---

*Source: test_dtype.py:299 | Complexity: Advanced | Last updated: 2026-06-02*