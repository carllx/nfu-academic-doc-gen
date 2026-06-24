# How To: Uneven Dims

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test 2D input, which has uneven dimension sizes 

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy`
- `numpy.testing`
- `numpy._core`


## Step-by-Step Guide

### Step 1: ' Test 2D input, which has uneven dimension sizes '

```python
' Test 2D input, which has uneven dimension sizes '
```

**Verification:**
```python
assert_array_almost_equal(fft.fftshift(freqs, axes=0), shift_dim0)
```

### Step 2: Assign freqs = value

```python
freqs = [[0, 1], [2, 3], [4, 5]]
```

**Verification:**
```python
assert_array_almost_equal(fft.ifftshift(shift_dim0, axes=0), freqs)
```

### Step 3: Assign shift_dim0 = value

```python
shift_dim0 = [[4, 5], [0, 1], [2, 3]]
```

**Verification:**
```python
assert_array_almost_equal(fft.fftshift(freqs, axes=(0,)), shift_dim0)
```

### Step 4: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.fftshift(freqs, axes=0), shift_dim0)
```

**Verification:**
```python
assert_array_almost_equal(fft.ifftshift(shift_dim0, axes=[0]), freqs)
```

### Step 5: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.ifftshift(shift_dim0, axes=0), freqs)
```

**Verification:**
```python
assert_array_almost_equal(fft.fftshift(freqs, axes=1), shift_dim1)
```

### Step 6: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.fftshift(freqs, axes=(0,)), shift_dim0)
```

**Verification:**
```python
assert_array_almost_equal(fft.ifftshift(shift_dim1, axes=1), freqs)
```

### Step 7: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.ifftshift(shift_dim0, axes=[0]), freqs)
```

**Verification:**
```python
assert_array_almost_equal(fft.fftshift(freqs, axes=(0, 1)), shift_dim_both)
```

### Step 8: Assign shift_dim1 = value

```python
shift_dim1 = [[1, 0], [3, 2], [5, 4]]
```

**Verification:**
```python
assert_array_almost_equal(fft.ifftshift(shift_dim_both, axes=(0, 1)), freqs)
```

### Step 9: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.fftshift(freqs, axes=1), shift_dim1)
```

**Verification:**
```python
assert_array_almost_equal(fft.fftshift(freqs, axes=[0, 1]), shift_dim_both)
```

### Step 10: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.ifftshift(shift_dim1, axes=1), freqs)
```

**Verification:**
```python
assert_array_almost_equal(fft.ifftshift(shift_dim_both, axes=[0, 1]), freqs)
```

### Step 11: Assign shift_dim_both = value

```python
shift_dim_both = [[5, 4], [1, 0], [3, 2]]
```

**Verification:**
```python
assert_array_almost_equal(fft.fftshift(freqs, axes=None), shift_dim_both)
```

### Step 12: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.fftshift(freqs, axes=(0, 1)), shift_dim_both)
```

**Verification:**
```python
assert_array_almost_equal(fft.ifftshift(shift_dim_both, axes=None), freqs)
```

### Step 13: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.ifftshift(shift_dim_both, axes=(0, 1)), freqs)
```

**Verification:**
```python
assert_array_almost_equal(fft.fftshift(freqs), shift_dim_both)
```

### Step 14: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.fftshift(freqs, axes=[0, 1]), shift_dim_both)
```

**Verification:**
```python
assert_array_almost_equal(fft.ifftshift(shift_dim_both), freqs)
```

### Step 15: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.ifftshift(shift_dim_both, axes=[0, 1]), freqs)
```

### Step 16: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.fftshift(freqs, axes=None), shift_dim_both)
```

### Step 17: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.ifftshift(shift_dim_both, axes=None), freqs)
```

### Step 18: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.fftshift(freqs), shift_dim_both)
```

### Step 19: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.ifftshift(shift_dim_both), freqs)
```


## Complete Example

```python
# Workflow
' Test 2D input, which has uneven dimension sizes '
freqs = [[0, 1], [2, 3], [4, 5]]
shift_dim0 = [[4, 5], [0, 1], [2, 3]]
assert_array_almost_equal(fft.fftshift(freqs, axes=0), shift_dim0)
assert_array_almost_equal(fft.ifftshift(shift_dim0, axes=0), freqs)
assert_array_almost_equal(fft.fftshift(freqs, axes=(0,)), shift_dim0)
assert_array_almost_equal(fft.ifftshift(shift_dim0, axes=[0]), freqs)
shift_dim1 = [[1, 0], [3, 2], [5, 4]]
assert_array_almost_equal(fft.fftshift(freqs, axes=1), shift_dim1)
assert_array_almost_equal(fft.ifftshift(shift_dim1, axes=1), freqs)
shift_dim_both = [[5, 4], [1, 0], [3, 2]]
assert_array_almost_equal(fft.fftshift(freqs, axes=(0, 1)), shift_dim_both)
assert_array_almost_equal(fft.ifftshift(shift_dim_both, axes=(0, 1)), freqs)
assert_array_almost_equal(fft.fftshift(freqs, axes=[0, 1]), shift_dim_both)
assert_array_almost_equal(fft.ifftshift(shift_dim_both, axes=[0, 1]), freqs)
assert_array_almost_equal(fft.fftshift(freqs, axes=None), shift_dim_both)
assert_array_almost_equal(fft.ifftshift(shift_dim_both, axes=None), freqs)
assert_array_almost_equal(fft.fftshift(freqs), shift_dim_both)
assert_array_almost_equal(fft.ifftshift(shift_dim_both), freqs)
```

## Next Steps


---

*Source: test_helper.py:41 | Complexity: Advanced | Last updated: 2026-06-02*