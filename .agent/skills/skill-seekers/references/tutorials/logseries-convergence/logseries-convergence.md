# How To: Logseries Convergence

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test logseries convergence

## Prerequisites

**Required Modules:**
- `sys`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `gc`
- `gc`


## Step-by-Step Guide

### Step 1: Assign N = 1000

```python
N = 1000
```

**Verification:**
```python
assert_(freq > 0.45, msg)
```

### Step 2: Call random.seed()

```python
random.seed(0)
```

**Verification:**
```python
assert_(freq < 0.23, msg)
```

### Step 3: Assign rvsn = random.logseries(...)

```python
rvsn = random.logseries(0.8, size=N)
```

### Step 4: Assign freq = value

```python
freq = np.sum(rvsn == 1) / N
```

### Step 5: Assign msg = value

```python
msg = f'Frequency was {freq:f}, should be > 0.45'
```

### Step 6: Call assert_()

```python
assert_(freq > 0.45, msg)
```

### Step 7: Assign freq = value

```python
freq = np.sum(rvsn == 2) / N
```

### Step 8: Assign msg = value

```python
msg = f'Frequency was {freq:f}, should be < 0.23'
```

### Step 9: Call assert_()

```python
assert_(freq < 0.23, msg)
```


## Complete Example

```python
# Workflow
N = 1000
random.seed(0)
rvsn = random.logseries(0.8, size=N)
freq = np.sum(rvsn == 1) / N
msg = f'Frequency was {freq:f}, should be > 0.45'
assert_(freq > 0.45, msg)
freq = np.sum(rvsn == 2) / N
msg = f'Frequency was {freq:f}, should be < 0.23'
assert_(freq < 0.23, msg)
```

## Next Steps


---

*Source: test_randomstate_regression.py:35 | Complexity: Advanced | Last updated: 2026-06-02*