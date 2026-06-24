# How To: All 1D Norm Preserving

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all 1d norm preserving

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
x = random(30)
```

**Verification:**
```python
assert_allclose(x_norm, np.linalg.norm(tmp), atol=1e-06)
```

### Step 2: Assign x_norm = np.linalg.norm(...)

```python
x_norm = np.linalg.norm(x)
```

### Step 3: Assign n = value

```python
n = x.size * 2
```

### Step 4: Assign func_pairs = value

```python
func_pairs = [(np.fft.fft, np.fft.ifft), (np.fft.rfft, np.fft.irfft), (np.fft.ihfft, np.fft.hfft)]
```

### Step 5: Assign tmp = forw(...)

```python
tmp = forw(x, n=n, norm=norm)
```

### Step 6: Assign tmp = back(...)

```python
tmp = back(tmp, n=n, norm=norm)
```

### Step 7: Call assert_allclose()

```python
assert_allclose(x_norm, np.linalg.norm(tmp), atol=1e-06)
```


## Complete Example

```python
# Workflow
x = random(30)
x_norm = np.linalg.norm(x)
n = x.size * 2
func_pairs = [(np.fft.fft, np.fft.ifft), (np.fft.rfft, np.fft.irfft), (np.fft.ihfft, np.fft.hfft)]
for forw, back in func_pairs:
    for n in [x.size, 2 * x.size]:
        for norm in [None, 'backward', 'ortho', 'forward']:
            tmp = forw(x, n=n, norm=norm)
            tmp = back(tmp, n=n, norm=norm)
            assert_allclose(x_norm, np.linalg.norm(tmp), atol=1e-06)
```

## Next Steps


---

*Source: test_pocketfft.py:391 | Complexity: Intermediate | Last updated: 2026-06-02*