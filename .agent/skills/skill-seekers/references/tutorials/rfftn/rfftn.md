# How To: Rfftn

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rfftn

## Prerequisites

**Required Modules:**
- `queue`
- `threading`
- `pytest`
- `numpy`
- `numpy.random`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = random(...)

```python
x = random((30, 20, 10))
```

**Verification:**
```python
assert_allclose(np.fft.fftn(x)[:, :, :6], np.fft.rfftn(x), atol=1e-06)
```

### Step 2: Call assert_allclose()

```python
assert_allclose(np.fft.fftn(x)[:, :, :6], np.fft.rfftn(x), atol=1e-06)
```

**Verification:**
```python
assert_allclose(np.fft.rfftn(x), np.fft.rfftn(x, norm='backward'), atol=1e-06)
```

### Step 3: Call assert_allclose()

```python
assert_allclose(np.fft.rfftn(x), np.fft.rfftn(x, norm='backward'), atol=1e-06)
```

**Verification:**
```python
assert_allclose(np.fft.rfftn(x) / np.sqrt(30 * 20 * 10), np.fft.rfftn(x, norm='ortho'), atol=1e-06)
```

### Step 4: Call assert_allclose()

```python
assert_allclose(np.fft.rfftn(x) / np.sqrt(30 * 20 * 10), np.fft.rfftn(x, norm='ortho'), atol=1e-06)
```

**Verification:**
```python
assert_allclose(np.fft.rfftn(x) / (30.0 * 20.0 * 10.0), np.fft.rfftn(x, norm='forward'), atol=1e-06)
```

### Step 5: Call assert_allclose()

```python
assert_allclose(np.fft.rfftn(x) / (30.0 * 20.0 * 10.0), np.fft.rfftn(x, norm='forward'), atol=1e-06)
```

**Verification:**
```python
assert result.shape == (10, 21)
```

### Step 6: Assign x = np.ones(...)

```python
x = np.ones((2, 3))
```

**Verification:**
```python
assert expected.shape == (10, 21)
```

### Step 7: Assign result = np.fft.rfftn(...)

```python
result = np.fft.rfftn(x, axes=(0, 0, 1), s=(10, 20, 40))
```

**Verification:**
```python
assert_allclose(result, expected, atol=1e-06)
```

### Step 8: Assign expected = np.fft.fft(...)

```python
expected = np.fft.fft(np.fft.fft(np.fft.rfft(x, axis=1, n=40), axis=0, n=20), axis=0, n=10)
```

**Verification:**
```python
assert expected.shape == (10, 21)
```

### Step 9: Call assert_allclose()

```python
assert_allclose(result, expected, atol=1e-06)
```


## Complete Example

```python
# Workflow
x = random((30, 20, 10))
assert_allclose(np.fft.fftn(x)[:, :, :6], np.fft.rfftn(x), atol=1e-06)
assert_allclose(np.fft.rfftn(x), np.fft.rfftn(x, norm='backward'), atol=1e-06)
assert_allclose(np.fft.rfftn(x) / np.sqrt(30 * 20 * 10), np.fft.rfftn(x, norm='ortho'), atol=1e-06)
assert_allclose(np.fft.rfftn(x) / (30.0 * 20.0 * 10.0), np.fft.rfftn(x, norm='forward'), atol=1e-06)
x = np.ones((2, 3))
result = np.fft.rfftn(x, axes=(0, 0, 1), s=(10, 20, 40))
assert result.shape == (10, 21)
expected = np.fft.fft(np.fft.fft(np.fft.rfft(x, axis=1, n=40), axis=0, n=20), axis=0, n=10)
assert expected.shape == (10, 21)
assert_allclose(result, expected, atol=1e-06)
```

## Next Steps


---

*Source: test_pocketfft.py:301 | Complexity: Advanced | Last updated: 2026-06-02*