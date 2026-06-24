# How To: Fft Out Argument

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fft out argument

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
# Fixtures: dtype, transpose, axis
```

## Step-by-Step Guide

### Step 1: Assign expected = fft(...)

```python
expected = fft(y, axis=axis)
```

**Verification:**
```python
assert result is out
```

### Step 2: Assign out = zeros_like(...)

```python
out = zeros_like(expected)
```

**Verification:**
```python
assert_array_equal(result, expected)
```

### Step 3: Assign result = fft(...)

```python
result = fft(y, out=out, axis=axis)
```

**Verification:**
```python
assert result2 is out2
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(result, expected)
```

**Verification:**
```python
assert_array_equal(result2, expected2)
```

### Step 5: Assign expected2 = ifft(...)

```python
expected2 = ifft(expected, axis=axis)
```

### Step 6: Assign out2 = value

```python
out2 = out if dtype is complex else zeros_like(expected2)
```

### Step 7: Assign result2 = ifft(...)

```python
result2 = ifft(out, out=out2, axis=axis)
```

**Verification:**
```python
assert result2 is out2
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(result2, expected2)
```

### Step 9: Assign y = value

```python
y = random((10, 20)) + 1j * random((10, 20))
```

### Step 10: Assign unknown = value

```python
fft, ifft = (np.fft.fft, np.fft.ifft)
```

### Step 11: Assign y = random(...)

```python
y = random((10, 20))
```

### Step 12: Assign unknown = value

```python
fft, ifft = (np.fft.rfft, np.fft.irfft)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, transpose, axis

# Workflow
def zeros_like(x):
    if transpose:
        return np.zeros_like(x.T).T
    else:
        return np.zeros_like(x)
if dtype is complex:
    y = random((10, 20)) + 1j * random((10, 20))
    fft, ifft = (np.fft.fft, np.fft.ifft)
else:
    y = random((10, 20))
    fft, ifft = (np.fft.rfft, np.fft.irfft)
expected = fft(y, axis=axis)
out = zeros_like(expected)
result = fft(y, out=out, axis=axis)
assert result is out
assert_array_equal(result, expected)
expected2 = ifft(expected, axis=axis)
out2 = out if dtype is complex else zeros_like(expected2)
result2 = ifft(out, out=out2, axis=axis)
assert result2 is out2
assert_array_equal(result2, expected2)
```

## Next Steps


---

*Source: test_pocketfft.py:90 | Complexity: Advanced | Last updated: 2026-06-02*