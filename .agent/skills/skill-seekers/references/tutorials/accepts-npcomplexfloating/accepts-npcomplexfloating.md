# How To: Accepts Npcomplexfloating

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test accepts npcomplexfloating

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.lib._index_tricks_impl`
- `numpy.testing`
- `numpy`


## Step-by-Step Guide

### Step 1: Call assert_array_almost_equal()

```python
assert_array_almost_equal(mgrid[0.1:0.3:3j,], mgrid[0.1:0.3:np.complex64(3j),])
```

**Verification:**
```python
assert_array_almost_equal(mgrid[0.1:0.3:3j,], mgrid[0.1:0.3:np.complex64(3j),])
```

### Step 2: Call assert_array_almost_equal()

```python
assert_array_almost_equal(mgrid[0.1:0.3:3j], mgrid[0.1:0.3:np.complex64(3j)])
```

**Verification:**
```python
assert_array_almost_equal(mgrid[0.1:0.3:3j], mgrid[0.1:0.3:np.complex64(3j)])
```

### Step 3: Assign grid64_a = value

```python
grid64_a = mgrid[0.1:0.3:3.3j]
```

**Verification:**
```python
assert_(grid64_a.dtype == grid64_b.dtype == np.float64)
```

### Step 4: Assign grid64_b = value

```python
grid64_b = mgrid[0.1:0.3:3.3j,][0]
```

**Verification:**
```python
assert_array_equal(grid64_a, grid64_b)
```

### Step 5: Call assert_()

```python
assert_(grid64_a.dtype == grid64_b.dtype == np.float64)
```

**Verification:**
```python
assert_(grid128_a.dtype == grid128_b.dtype == np.longdouble)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(grid64_a, grid64_b)
```

**Verification:**
```python
assert_array_equal(grid64_a, grid64_b)
```

### Step 7: Assign grid128_a = value

```python
grid128_a = mgrid[0.1:0.3:np.clongdouble(3.3j)]
```

### Step 8: Assign grid128_b = value

```python
grid128_b = mgrid[0.1:0.3:np.clongdouble(3.3j),][0]
```

### Step 9: Call assert_()

```python
assert_(grid128_a.dtype == grid128_b.dtype == np.longdouble)
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(grid64_a, grid64_b)
```


## Complete Example

```python
# Workflow
assert_array_almost_equal(mgrid[0.1:0.3:3j,], mgrid[0.1:0.3:np.complex64(3j),])
assert_array_almost_equal(mgrid[0.1:0.3:3j], mgrid[0.1:0.3:np.complex64(3j)])
grid64_a = mgrid[0.1:0.3:3.3j]
grid64_b = mgrid[0.1:0.3:3.3j,][0]
assert_(grid64_a.dtype == grid64_b.dtype == np.float64)
assert_array_equal(grid64_a, grid64_b)
grid128_a = mgrid[0.1:0.3:np.clongdouble(3.3j)]
grid128_b = mgrid[0.1:0.3:np.clongdouble(3.3j),][0]
assert_(grid128_a.dtype == grid128_b.dtype == np.longdouble)
assert_array_equal(grid64_a, grid64_b)
```

## Next Steps


---

*Source: test_index_tricks.py:301 | Complexity: Advanced | Last updated: 2026-06-02*