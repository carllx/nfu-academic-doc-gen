# How To: Identity Long Short

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test identity long short

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
assert check_c.real.dtype == dtype
```

### Step 2: Assign atol = value

```python
atol = 5 * np.spacing(np.array(1.0, dtype=dtype))
```

**Verification:**
```python
assert_allclose(check_c, xx[0:i], atol=atol, rtol=0)
```

### Step 3: Assign x = value

```python
x = random(maxlen).astype(dtype) + 1j * random(maxlen).astype(dtype)
```

**Verification:**
```python
assert check_r.dtype == dtype
```

### Step 4: Assign xx = np.concatenate(...)

```python
xx = np.concatenate([x, np.zeros_like(x)])
```

**Verification:**
```python
assert_allclose(check_r, xxr[0:i], atol=atol, rtol=0)
```

### Step 5: Assign xr = random.astype(...)

```python
xr = random(maxlen).astype(dtype)
```

### Step 6: Assign xxr = np.concatenate(...)

```python
xxr = np.concatenate([xr, np.zeros_like(xr)])
```

### Step 7: Assign check_c = np.fft.ifft(...)

```python
check_c = np.fft.ifft(np.fft.fft(x, n=i), n=i)
```

**Verification:**
```python
assert check_c.real.dtype == dtype
```

### Step 8: Call assert_allclose()

```python
assert_allclose(check_c, xx[0:i], atol=atol, rtol=0)
```

### Step 9: Assign check_r = np.fft.irfft(...)

```python
check_r = np.fft.irfft(np.fft.rfft(xr, n=i), n=i)
```

**Verification:**
```python
assert check_r.dtype == dtype
```

### Step 10: Call assert_allclose()

```python
assert_allclose(check_r, xxr[0:i], atol=atol, rtol=0)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
maxlen = 16
atol = 5 * np.spacing(np.array(1.0, dtype=dtype))
x = random(maxlen).astype(dtype) + 1j * random(maxlen).astype(dtype)
xx = np.concatenate([x, np.zeros_like(x)])
xr = random(maxlen).astype(dtype)
xxr = np.concatenate([xr, np.zeros_like(xr)])
for i in range(1, maxlen * 2):
    check_c = np.fft.ifft(np.fft.fft(x, n=i), n=i)
    assert check_c.real.dtype == dtype
    assert_allclose(check_c, xx[0:i], atol=atol, rtol=0)
    check_r = np.fft.irfft(np.fft.rfft(xr, n=i), n=i)
    assert check_r.dtype == dtype
    assert_allclose(check_r, xxr[0:i], atol=atol, rtol=0)
```

## Next Steps


---

*Source: test_pocketfft.py:37 | Complexity: Advanced | Last updated: 2026-06-02*