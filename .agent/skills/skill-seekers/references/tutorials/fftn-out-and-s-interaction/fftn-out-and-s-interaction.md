# How To: Fftn Out And S Interaction

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fftn out and s interaction

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
# Fixtures: fft
```

## Step-by-Step Guide

### Step 1: Assign s = value

```python
s = (10, 5, 5)
```

**Verification:**
```python
assert result is out
```

### Step 2: Assign expected = fft(...)

```python
expected = fft(x, s=s, axes=(0, 1, 2))
```

**Verification:**
```python
assert_array_equal(result, expected)
```

### Step 3: Assign out = np.zeros_like(...)

```python
out = np.zeros_like(expected)
```

### Step 4: Assign result = fft(...)

```python
result = fft(x, s=s, axes=(0, 1, 2), out=out)
```

**Verification:**
```python
assert result is out
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(result, expected)
```

### Step 6: Assign x = random(...)

```python
x = random((10, 5, 6))
```

### Step 7: Assign x = value

```python
x = random((10, 5, 6)) + 1j * random((10, 5, 6))
```

### Step 8: Call fft()

```python
fft(x, out=np.zeros_like(x), s=(3, 3, 3), axes=(0, 1, 2))
```


## Complete Example

```python
# Setup
# Fixtures: fft

# Workflow
if fft is np.fft.rfftn:
    x = random((10, 5, 6))
else:
    x = random((10, 5, 6)) + 1j * random((10, 5, 6))
with pytest.raises(ValueError, match='has wrong shape'):
    fft(x, out=np.zeros_like(x), s=(3, 3, 3), axes=(0, 1, 2))
s = (10, 5, 5)
expected = fft(x, s=s, axes=(0, 1, 2))
out = np.zeros_like(expected)
result = fft(x, s=s, axes=(0, 1, 2), out=out)
assert result is out
assert_array_equal(result, expected)
```

## Next Steps


---

*Source: test_pocketfft.py:441 | Complexity: Advanced | Last updated: 2026-06-02*