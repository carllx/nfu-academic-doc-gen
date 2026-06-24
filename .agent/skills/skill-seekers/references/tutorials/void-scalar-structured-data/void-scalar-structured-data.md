# How To: Void Scalar Structured Data

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test void scalar structured data

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy._core._multiarray_tests`
- `numpy._core._rational_tests`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign dt = np.dtype(...)

```python
dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
```

**Verification:**
```python
assert_(isinstance(x, np.void))
```

### Step 2: Assign x = value

```python
x = np.array(('ndarray_scalar', (1.2, 3.0)), dtype=dt)[()]
```

**Verification:**
```python
assert_equal(mv_x.itemsize, expected_size)
```

### Step 3: Call assert_()

```python
assert_(isinstance(x, np.void))
```

**Verification:**
```python
assert_equal(mv_x.ndim, 0)
```

### Step 4: Assign mv_x = memoryview(...)

```python
mv_x = memoryview(x)
```

**Verification:**
```python
assert_equal(mv_x.shape, ())
```

### Step 5: Assign expected_size = value

```python
expected_size = 16 * np.dtype((np.str_, 1)).itemsize
```

**Verification:**
```python
assert_equal(mv_x.strides, ())
```

### Step 6: Call assert_equal()

```python
assert_equal(mv_x.itemsize, expected_size)
```

**Verification:**
```python
assert_equal(mv_x.suboffsets, ())
```

### Step 7: Call assert_equal()

```python
assert_equal(mv_x.ndim, 0)
```

**Verification:**
```python
assert_(isinstance(a, np.ndarray))
```

### Step 8: Call assert_equal()

```python
assert_equal(mv_x.shape, ())
```

**Verification:**
```python
assert_equal(mv_x.itemsize, mv_a.itemsize)
```

### Step 9: Call assert_equal()

```python
assert_equal(mv_x.strides, ())
```

**Verification:**
```python
assert_equal(mv_x.format, mv_a.format)
```

### Step 10: Call assert_equal()

```python
assert_equal(mv_x.suboffsets, ())
```

### Step 11: Assign a = np.array(...)

```python
a = np.array([('Sarah', (8.0, 7.0)), ('John', (6.0, 7.0))], dtype=dt)
```

### Step 12: Call assert_()

```python
assert_(isinstance(a, np.ndarray))
```

### Step 13: Assign mv_a = memoryview(...)

```python
mv_a = memoryview(a)
```

### Step 14: Call assert_equal()

```python
assert_equal(mv_x.itemsize, mv_a.itemsize)
```

### Step 15: Call assert_equal()

```python
assert_equal(mv_x.format, mv_a.format)
```

### Step 16: Call get_buffer_info()

```python
get_buffer_info(x, ['WRITABLE'])
```


## Complete Example

```python
# Workflow
dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
x = np.array(('ndarray_scalar', (1.2, 3.0)), dtype=dt)[()]
assert_(isinstance(x, np.void))
mv_x = memoryview(x)
expected_size = 16 * np.dtype((np.str_, 1)).itemsize
expected_size += 2 * np.dtype(np.float64).itemsize
assert_equal(mv_x.itemsize, expected_size)
assert_equal(mv_x.ndim, 0)
assert_equal(mv_x.shape, ())
assert_equal(mv_x.strides, ())
assert_equal(mv_x.suboffsets, ())
a = np.array([('Sarah', (8.0, 7.0)), ('John', (6.0, 7.0))], dtype=dt)
assert_(isinstance(a, np.ndarray))
mv_a = memoryview(a)
assert_equal(mv_x.itemsize, mv_a.itemsize)
assert_equal(mv_x.format, mv_a.format)
with pytest.raises(BufferError, match='scalar buffer is readonly'):
    get_buffer_info(x, ['WRITABLE'])
```

## Next Steps


---

*Source: test_scalarbuffer.py:70 | Complexity: Advanced | Last updated: 2026-06-02*