# How To: Accepts Longdouble

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test accepts longdouble

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.lib._index_tricks_impl`
- `numpy.testing`
- `numpy`


## Step-by-Step Guide

### Step 1: Assign grid64 = value

```python
grid64 = mgrid[0.1:0.33:0.1,]
```

**Verification:**
```python
assert_(grid128.dtype == np.longdouble)
```

### Step 2: Assign grid128 = value

```python
grid128 = mgrid[np.longdouble(0.1):np.longdouble(0.33):np.longdouble(0.1),]
```

**Verification:**
```python
assert_array_almost_equal(grid64, grid128)
```

### Step 3: Call assert_()

```python
assert_(grid128.dtype == np.longdouble)
```

**Verification:**
```python
assert_(grid128c_a.dtype == grid128c_b.dtype == np.longdouble)
```

### Step 4: Call assert_array_almost_equal()

```python
assert_array_almost_equal(grid64, grid128)
```

**Verification:**
```python
assert_array_equal(grid128c_a, grid128c_b[0])
```

### Step 5: Assign grid128c_a = value

```python
grid128c_a = mgrid[0:np.longdouble(1):3.4j]
```

**Verification:**
```python
assert_(grid128.dtype == np.longdouble)
```

### Step 6: Assign grid128c_b = value

```python
grid128c_b = mgrid[0:np.longdouble(1):3.4j,]
```

**Verification:**
```python
assert_array_almost_equal(grid64, grid128)
```

### Step 7: Call assert_()

```python
assert_(grid128c_a.dtype == grid128c_b.dtype == np.longdouble)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(grid128c_a, grid128c_b[0])
```

### Step 9: Assign grid64 = value

```python
grid64 = mgrid[0.1:0.33:0.1]
```

### Step 10: Assign grid128 = value

```python
grid128 = mgrid[np.longdouble(0.1):np.longdouble(0.33):np.longdouble(0.1)]
```

### Step 11: Call assert_()

```python
assert_(grid128.dtype == np.longdouble)
```

### Step 12: Call assert_array_almost_equal()

```python
assert_array_almost_equal(grid64, grid128)
```


## Complete Example

```python
# Workflow
grid64 = mgrid[0.1:0.33:0.1,]
grid128 = mgrid[np.longdouble(0.1):np.longdouble(0.33):np.longdouble(0.1),]
assert_(grid128.dtype == np.longdouble)
assert_array_almost_equal(grid64, grid128)
grid128c_a = mgrid[0:np.longdouble(1):3.4j]
grid128c_b = mgrid[0:np.longdouble(1):3.4j,]
assert_(grid128c_a.dtype == grid128c_b.dtype == np.longdouble)
assert_array_equal(grid128c_a, grid128c_b[0])
grid64 = mgrid[0.1:0.33:0.1]
grid128 = mgrid[np.longdouble(0.1):np.longdouble(0.33):np.longdouble(0.1)]
assert_(grid128.dtype == np.longdouble)
assert_array_almost_equal(grid64, grid128)
```

## Next Steps


---

*Source: test_index_tricks.py:279 | Complexity: Advanced | Last updated: 2026-06-02*