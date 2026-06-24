# How To: Definition

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test definition

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy`
- `numpy.testing`
- `numpy._core`


## Step-by-Step Guide

### Step 1: Assign x = value

```python
x = [0, 1, 2, 3, 4, -4, -3, -2, -1]
```

**Verification:**
```python
assert_array_almost_equal(fft.fftshift(x), y)
```

### Step 2: Assign y = value

```python
y = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
```

**Verification:**
```python
assert_array_almost_equal(fft.ifftshift(y), x)
```

### Step 3: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.fftshift(x), y)
```

**Verification:**
```python
assert_array_almost_equal(fft.fftshift(x), y)
```

### Step 4: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.ifftshift(y), x)
```

**Verification:**
```python
assert_array_almost_equal(fft.ifftshift(y), x)
```

### Step 5: Assign x = value

```python
x = [0, 1, 2, 3, 4, -5, -4, -3, -2, -1]
```

### Step 6: Assign y = value

```python
y = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
```

### Step 7: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.fftshift(x), y)
```

### Step 8: Call assert_array_almost_equal()

```python
assert_array_almost_equal(fft.ifftshift(y), x)
```


## Complete Example

```python
# Workflow
x = [0, 1, 2, 3, 4, -4, -3, -2, -1]
y = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
assert_array_almost_equal(fft.fftshift(x), y)
assert_array_almost_equal(fft.ifftshift(y), x)
x = [0, 1, 2, 3, 4, -5, -4, -3, -2, -1]
y = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
assert_array_almost_equal(fft.fftshift(x), y)
assert_array_almost_equal(fft.ifftshift(y), x)
```

## Next Steps


---

*Source: test_helper.py:13 | Complexity: Advanced | Last updated: 2026-06-02*