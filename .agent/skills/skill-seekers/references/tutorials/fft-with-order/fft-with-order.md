# How To: Fft With Order

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fft with order

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `queue`
- `threading`
- `pytest`
- `numpy`
- `numpy.random`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: dtype, order, fft
```

## Step-by-Step Guide

### Step 1: Assign rng = np.random.RandomState(...)

```python
rng = np.random.RandomState(42)
```

**Verification:**
```python
assert_allclose(X_res, Y_res, atol=_tol, rtol=_tol)
```

### Step 2: Assign X = rng.rand.astype(...)

```python
X = rng.rand(8, 7, 13).astype(dtype, copy=False)
```

**Verification:**
```python
assert_allclose(X_res, Y_res, atol=_tol, rtol=_tol)
```

### Step 3: Assign _tol = value

```python
_tol = 8.0 * np.sqrt(np.log2(X.size)) * np.finfo(X.dtype).eps
```

### Step 4: Assign Y = np.asfortranarray(...)

```python
Y = np.asfortranarray(X)
```

### Step 5: Assign Y = value

```python
Y = X[::-1]
```

### Step 6: Assign X = np.ascontiguousarray(...)

```python
X = np.ascontiguousarray(X[::-1])
```

### Step 7: Assign X_res = fft(...)

```python
X_res = fft(X, axis=axis)
```

### Step 8: Assign Y_res = fft(...)

```python
Y_res = fft(Y, axis=axis)
```

### Step 9: Call assert_allclose()

```python
assert_allclose(X_res, Y_res, atol=_tol, rtol=_tol)
```

### Step 10: Assign axes = value

```python
axes = [(0, 1), (1, 2), (0, 2)]
```

### Step 11: Call axes.extend()

```python
axes.extend([(0,), (1,), (2,), None])
```

### Step 12: Assign X_res = fft(...)

```python
X_res = fft(X, axes=ax)
```

### Step 13: Assign Y_res = fft(...)

```python
Y_res = fft(Y, axes=ax)
```

### Step 14: Call assert_allclose()

```python
assert_allclose(X_res, Y_res, atol=_tol, rtol=_tol)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, order, fft

# Workflow
rng = np.random.RandomState(42)
X = rng.rand(8, 7, 13).astype(dtype, copy=False)
_tol = 8.0 * np.sqrt(np.log2(X.size)) * np.finfo(X.dtype).eps
if order == 'F':
    Y = np.asfortranarray(X)
else:
    Y = X[::-1]
    X = np.ascontiguousarray(X[::-1])
if fft.__name__.endswith('fft'):
    for axis in range(3):
        X_res = fft(X, axis=axis)
        Y_res = fft(Y, axis=axis)
        assert_allclose(X_res, Y_res, atol=_tol, rtol=_tol)
elif fft.__name__.endswith(('fft2', 'fftn')):
    axes = [(0, 1), (1, 2), (0, 2)]
    if fft.__name__.endswith('fftn'):
        axes.extend([(0,), (1,), (2,), None])
    for ax in axes:
        X_res = fft(X, axes=ax)
        Y_res = fft(Y, axes=ax)
        assert_allclose(X_res, Y_res, atol=_tol, rtol=_tol)
else:
    raise ValueError
```

## Next Steps


---

*Source: test_pocketfft.py:477 | Complexity: Advanced | Last updated: 2026-06-02*