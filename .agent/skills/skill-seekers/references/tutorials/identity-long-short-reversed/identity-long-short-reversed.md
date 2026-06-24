# How To: Identity Long Short Reversed

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test identity long short reversed

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
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign maxlen = 16

```python
maxlen = 16
```

**Verification:**
```python
assert check_via_c.dtype == x.dtype
```

### Step 2: Assign atol = value

```python
atol = 6 * np.spacing(np.array(1.0, dtype=dtype))
```

**Verification:**
```python
assert_allclose(check_via_c, xx[0:i], atol=atol, rtol=0)
```

### Step 3: Assign x = value

```python
x = random(maxlen).astype(dtype) + 1j * random(maxlen).astype(dtype)
```

**Verification:**
```python
assert check_via_r.dtype == x.dtype
```

### Step 4: Assign xx = np.concatenate(...)

```python
xx = np.concatenate([x, np.zeros_like(x)])
```

**Verification:**
```python
assert_allclose(check_via_r, yy[0:n], atol=atol, rtol=0)
```

### Step 5: Assign check_via_c = np.fft.fft(...)

```python
check_via_c = np.fft.fft(np.fft.ifft(x, n=i), n=i)
```

**Verification:**
```python
assert check_via_c.dtype == x.dtype
```

### Step 6: Call assert_allclose()

```python
assert_allclose(check_via_c, xx[0:i], atol=atol, rtol=0)
```

### Step 7: Assign y = x.copy(...)

```python
y = x.copy()
```

### Step 8: Assign n = value

```python
n = i // 2 + 1
```

### Step 9: Assign unknown = 0

```python
y.imag[0] = 0
```

### Step 10: Assign yy = np.concatenate(...)

```python
yy = np.concatenate([y, np.zeros_like(y)])
```

### Step 11: Assign check_via_r = np.fft.rfft(...)

```python
check_via_r = np.fft.rfft(np.fft.irfft(x, n=i), n=i)
```

**Verification:**
```python
assert check_via_r.dtype == x.dtype
```

### Step 12: Call assert_allclose()

```python
assert_allclose(check_via_r, yy[0:n], atol=atol, rtol=0)
```

### Step 13: Assign unknown = 0

```python
y.imag[n - 1:] = 0
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
maxlen = 16
atol = 6 * np.spacing(np.array(1.0, dtype=dtype))
x = random(maxlen).astype(dtype) + 1j * random(maxlen).astype(dtype)
xx = np.concatenate([x, np.zeros_like(x)])
for i in range(1, maxlen * 2):
    check_via_c = np.fft.fft(np.fft.ifft(x, n=i), n=i)
    assert check_via_c.dtype == x.dtype
    assert_allclose(check_via_c, xx[0:i], atol=atol, rtol=0)
    y = x.copy()
    n = i // 2 + 1
    y.imag[0] = 0
    if i % 2 == 0:
        y.imag[n - 1:] = 0
    yy = np.concatenate([y, np.zeros_like(y)])
    check_via_r = np.fft.rfft(np.fft.irfft(x, n=i), n=i)
    assert check_via_r.dtype == x.dtype
    assert_allclose(check_via_r, yy[0:n], atol=atol, rtol=0)
```

## Next Steps


---

*Source: test_pocketfft.py:55 | Complexity: Advanced | Last updated: 2026-06-02*