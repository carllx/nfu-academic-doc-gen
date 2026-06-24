# How To: Fft Output Order

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fft output order

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
# Fixtures: order, n
```

## Step-by-Step Guide

### Step 1: Assign rng = np.random.RandomState(...)

```python
rng = np.random.RandomState(42)
```

**Verification:**
```python
assert res.flags.c_contiguous == x.flags.c_contiguous
```

### Step 2: Assign x = rng.rand(...)

```python
x = rng.rand(10)
```

**Verification:**
```python
assert res.flags.f_contiguous == x.flags.f_contiguous
```

### Step 3: Assign x = np.asarray(...)

```python
x = np.asarray(x, dtype=np.complex64, order=order)
```

### Step 4: Assign res = np.fft.fft(...)

```python
res = np.fft.fft(x, n=n)
```

**Verification:**
```python
assert res.flags.c_contiguous == x.flags.c_contiguous
```


## Complete Example

```python
# Setup
# Fixtures: order, n

# Workflow
rng = np.random.RandomState(42)
x = rng.rand(10)
x = np.asarray(x, dtype=np.complex64, order=order)
res = np.fft.fft(x, n=n)
assert res.flags.c_contiguous == x.flags.c_contiguous
assert res.flags.f_contiguous == x.flags.f_contiguous
```

## Next Steps


---

*Source: test_pocketfft.py:510 | Complexity: Intermediate | Last updated: 2026-06-02*