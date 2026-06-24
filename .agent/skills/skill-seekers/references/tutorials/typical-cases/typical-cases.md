# How To: Typical Cases

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test typical cases

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `hashlib`
- `os.path`
- `sys`
- `warnings`
- `pytest`
- `numpy`
- `numpy.exceptions`
- `numpy.linalg`
- `numpy.random`
- `numpy.testing`
- `pickle`
- `gzip`
- `pickle`
- `threading`

**Setup Required:**
```python
# Fixtures: nsample, method, size
```

## Step-by-Step Guide

### Step 1: Assign random = Generator(...)

```python
random = Generator(MT19937(self.seed))
```

**Verification:**
```python
assert_equal(sample.shape, expected_shape)
```

### Step 2: Assign colors = np.array(...)

```python
colors = np.array([10, 5, 20, 25])
```

**Verification:**
```python
assert_((sample >= 0).all())
```

### Step 3: Assign sample = random.multivariate_hypergeometric(...)

```python
sample = random.multivariate_hypergeometric(colors, nsample, size, method=method)
```

**Verification:**
```python
assert_((sample <= colors).all())
```

### Step 4: Call assert_equal()

```python
assert_equal(sample.shape, expected_shape)
```

**Verification:**
```python
assert_array_equal(sample.sum(axis=-1), np.full(size, fill_value=nsample, dtype=int))
```

### Step 5: Call assert_()

```python
assert_((sample >= 0).all())
```

**Verification:**
```python
assert_allclose(sample.mean(axis=0), nsample * colors / colors.sum(), rtol=0.001, atol=0.005)
```

### Step 6: Call assert_()

```python
assert_((sample <= colors).all())
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(sample.sum(axis=-1), np.full(size, fill_value=nsample, dtype=int))
```

### Step 8: Assign expected_shape = value

```python
expected_shape = (size,) + colors.shape
```

### Step 9: Assign expected_shape = value

```python
expected_shape = size + colors.shape
```

### Step 10: Call assert_allclose()

```python
assert_allclose(sample.mean(axis=0), nsample * colors / colors.sum(), rtol=0.001, atol=0.005)
```


## Complete Example

```python
# Setup
# Fixtures: nsample, method, size

# Workflow
random = Generator(MT19937(self.seed))
colors = np.array([10, 5, 20, 25])
sample = random.multivariate_hypergeometric(colors, nsample, size, method=method)
if isinstance(size, int):
    expected_shape = (size,) + colors.shape
else:
    expected_shape = size + colors.shape
assert_equal(sample.shape, expected_shape)
assert_((sample >= 0).all())
assert_((sample <= colors).all())
assert_array_equal(sample.sum(axis=-1), np.full(size, fill_value=nsample, dtype=int))
if isinstance(size, int) and size >= 100000:
    assert_allclose(sample.mean(axis=0), nsample * colors / colors.sum(), rtol=0.001, atol=0.005)
```

## Next Steps


---

*Source: test_generator_mt19937.py:251 | Complexity: Advanced | Last updated: 2026-06-02*