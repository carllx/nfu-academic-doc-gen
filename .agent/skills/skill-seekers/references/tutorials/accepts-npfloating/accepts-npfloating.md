# How To: Accepts Npfloating

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test accepts npfloating

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
assert_array_almost_equal(grid64, grid32)
```

### Step 2: Assign grid32 = value

```python
grid32 = mgrid[np.float32(0.1):np.float32(0.33):np.float32(0.1),]
```

**Verification:**
```python
assert grid32.dtype == np.float32
```

### Step 3: Call assert_array_almost_equal()

```python
assert_array_almost_equal(grid64, grid32)
```

**Verification:**
```python
assert grid64.dtype == np.float64
```

### Step 4: Assign grid64 = value

```python
grid64 = mgrid[0.1:0.33:0.1]
```

**Verification:**
```python
assert_(grid32.dtype == np.float64)
```

### Step 5: Assign grid32 = value

```python
grid32 = mgrid[np.float32(0.1):np.float32(0.33):np.float32(0.1)]
```

**Verification:**
```python
assert_array_almost_equal(grid64, grid32)
```

### Step 6: Call assert_()

```python
assert_(grid32.dtype == np.float64)
```

### Step 7: Call assert_array_almost_equal()

```python
assert_array_almost_equal(grid64, grid32)
```


## Complete Example

```python
# Workflow
grid64 = mgrid[0.1:0.33:0.1,]
grid32 = mgrid[np.float32(0.1):np.float32(0.33):np.float32(0.1),]
assert_array_almost_equal(grid64, grid32)
assert grid32.dtype == np.float32
assert grid64.dtype == np.float64
grid64 = mgrid[0.1:0.33:0.1]
grid32 = mgrid[np.float32(0.1):np.float32(0.33):np.float32(0.1)]
assert_(grid32.dtype == np.float64)
assert_array_almost_equal(grid64, grid32)
```

## Next Steps


---

*Source: test_index_tricks.py:264 | Complexity: Intermediate | Last updated: 2026-06-02*