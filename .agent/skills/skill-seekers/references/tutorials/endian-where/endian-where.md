# How To: Endian Where

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test endian where

## Prerequisites

**Required Modules:**
- `copy`
- `gc`
- `pickle`
- `sys`
- `tempfile`
- `warnings`
- `io`
- `itertools`
- `os`
- `pytest`
- `numpy`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.lib.stride_tricks`
- `numpy.testing`
- `numpy.testing._private.utils`
- `math`
- `numpy`
- `hashlib`
- `numpy`
- `re`
- `numpy`
- `operator`


## Step-by-Step Guide

### Step 1: Assign net = np.zeros(...)

```python
net = np.zeros(3, dtype='>f4')
```

**Verification:**
```python
assert_array_almost_equal(test, correct)
```

### Step 2: Assign unknown = 0.00458849

```python
net[1] = 0.00458849
```

### Step 3: Assign unknown = 0.605202

```python
net[2] = 0.605202
```

### Step 4: Assign max_net = net.max(...)

```python
max_net = net.max()
```

### Step 5: Assign test = np.where(...)

```python
test = np.where(net <= 0.0, max_net, net)
```

### Step 6: Assign correct = np.array(...)

```python
correct = np.array([0.60520202, 0.00458849, 0.60520202])
```

### Step 7: Call assert_array_almost_equal()

```python
assert_array_almost_equal(test, correct)
```


## Complete Example

```python
# Workflow
net = np.zeros(3, dtype='>f4')
net[1] = 0.00458849
net[2] = 0.605202
max_net = net.max()
test = np.where(net <= 0.0, max_net, net)
correct = np.array([0.60520202, 0.00458849, 0.60520202])
assert_array_almost_equal(test, correct)
```

## Next Steps


---

*Source: test_regression.py:178 | Complexity: Intermediate | Last updated: 2026-06-02*