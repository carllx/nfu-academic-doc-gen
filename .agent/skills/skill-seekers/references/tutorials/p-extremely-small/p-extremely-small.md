# How To: P Extremely Small

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test p extremely small

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign n = 50000000000

```python
n = 50000000000
```

**Verification:**
```python
assert low_bound > 0, 'bad test params: 6-sigma lower bound is negative'
```

### Step 2: Assign p = 5e-17

```python
p = 5e-17
```

**Verification:**
```python
assert abs(expected_mean - sample_mean) < 6 * sigma, test_msg
```

### Step 3: Assign sample_size = 20000000

```python
sample_size = 20000000
```

### Step 4: Assign x = random.binomial(...)

```python
x = random.binomial(n, p, size=sample_size)
```

### Step 5: Assign sample_mean = x.mean(...)

```python
sample_mean = x.mean()
```

### Step 6: Assign expected_mean = value

```python
expected_mean = n * p
```

### Step 7: Assign sigma = np.sqrt(...)

```python
sigma = np.sqrt(n * p * (1 - p) / sample_size)
```

### Step 8: Assign low_bound = value

```python
low_bound = expected_mean - 6 * sigma
```

**Verification:**
```python
assert low_bound > 0, 'bad test params: 6-sigma lower bound is negative'
```

### Step 9: Assign test_msg = value

```python
test_msg = f'sample mean {sample_mean} deviates from the expected mean {expected_mean} by more than 6*sigma'
```

**Verification:**
```python
assert abs(expected_mean - sample_mean) < 6 * sigma, test_msg
```


## Complete Example

```python
# Workflow
n = 50000000000
p = 5e-17
sample_size = 20000000
x = random.binomial(n, p, size=sample_size)
sample_mean = x.mean()
expected_mean = n * p
sigma = np.sqrt(n * p * (1 - p) / sample_size)
low_bound = expected_mean - 6 * sigma
assert low_bound > 0, 'bad test params: 6-sigma lower bound is negative'
test_msg = f'sample mean {sample_mean} deviates from the expected mean {expected_mean} by more than 6*sigma'
assert abs(expected_mean - sample_mean) < 6 * sigma, test_msg
```

## Next Steps


---

*Source: test_generator_mt19937.py:102 | Complexity: Advanced | Last updated: 2026-06-02*