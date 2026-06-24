# How To: Beta Expected Zero Frequency

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test beta expected zero frequency

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.random`
- `numpy.testing`
- `gc`
- `gc`


## Step-by-Step Guide

### Step 1: Assign mt19937 = self._create_generator(...)

```python
mt19937 = self._create_generator()
```

**Verification:**
```python
assert 0.95 * expected_freq < nzeros < 1.05 * expected_freq
```

### Step 2: Assign a = 0.0025

```python
a = 0.0025
```

### Step 3: Assign b = 0.0025

```python
b = 0.0025
```

### Step 4: Assign n = 1000000

```python
n = 1000000
```

### Step 5: Assign x = mt19937.beta(...)

```python
x = mt19937.beta(a, b, size=n)
```

### Step 6: Assign nzeros = np.count_nonzero(...)

```python
nzeros = np.count_nonzero(x == 0)
```

### Step 7: Assign expected_freq = 77616.90831318991

```python
expected_freq = 77616.90831318991
```

**Verification:**
```python
assert 0.95 * expected_freq < nzeros < 1.05 * expected_freq
```


## Complete Example

```python
# Workflow
mt19937 = self._create_generator()
a = 0.0025
b = 0.0025
n = 1000000
x = mt19937.beta(a, b, size=n)
nzeros = np.count_nonzero(x == 0)
expected_freq = 77616.90831318991
assert 0.95 * expected_freq < nzeros < 1.05 * expected_freq
```

## Next Steps


---

*Source: test_generator_mt19937_regressions.py:96 | Complexity: Intermediate | Last updated: 2026-06-02*