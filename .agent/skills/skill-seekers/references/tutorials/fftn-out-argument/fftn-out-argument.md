# How To: Fftn Out Argument

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fftn out argument

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
# Fixtures: dtype, transpose, axes
```

## Step-by-Step Guide

### Step 1: Assign expected = fft(...)

```python
expected = fft(x, axes=axes)
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
result = fft(x, out=out, axes=axes)
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
expected2 = ifft(expected, axes=axes)
```

### Step 6: Assign out2 = value

```python
out2 = out if dtype is complex else zeros_like(expected2)
```

### Step 7: Assign result2 = ifft(...)

```python
result2 = ifft(out, out=out2, axes=axes)
```

**Verification:**
```python
assert result2 is out2
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(result2, expected2)
```

### Step 9: Assign x = value

```python
x = random((10, 5, 6)) + 1j * random((10, 5, 6))
```

### Step 10: Assign unknown = value

```python
fft, ifft = (np.fft.fftn, np.fft.ifftn)
```

### Step 11: Assign x = random(...)

```python
x = random((10, 5, 6))
```

### Step 12: Assign unknown = value

```python
fft, ifft = (np.fft.rfftn, np.fft.irfftn)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, transpose, axes

# Workflow
def zeros_like(x):
    if transpose:
        return np.zeros_like(x.T).T
    else:
        return np.zeros_like(x)
if dtype is complex:
    x = random((10, 5, 6)) + 1j * random((10, 5, 6))
    fft, ifft = (np.fft.fftn, np.fft.ifftn)
else:
    x = random((10, 5, 6))
    fft, ifft = (np.fft.rfftn, np.fft.irfftn)
expected = fft(x, axes=axes)
out = zeros_like(expected)
result = fft(x, out=out, axes=axes)
assert result is out
assert_array_equal(result, expected)
expected2 = ifft(expected, axes=axes)
out2 = out if dtype is complex else zeros_like(expected2)
result2 = ifft(out, out=out2, axes=axes)
assert result2 is out2
assert_array_equal(result2, expected2)
```

## Next Steps


---

*Source: test_pocketfft.py:413 | Complexity: Advanced | Last updated: 2026-06-02*