# How To: Dot Negative Stride

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dot negative stride

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

### Step 1: Assign x = np.array(...)

```python
x = np.array([[1, 5, 25, 125.0, 625]])
```

**Verification:**
```python
assert_equal(np.dot(x, z), np.dot(x, y2))
```

### Step 2: Assign y = np.array(...)

```python
y = np.array([[20.0], [160.0], [640.0], [1280.0], [1024.0]])
```

### Step 3: Assign z = unknown.copy(...)

```python
z = y[::-1].copy()
```

### Step 4: Assign y2 = value

```python
y2 = y[::-1]
```

### Step 5: Call assert_equal()

```python
assert_equal(np.dot(x, z), np.dot(x, y2))
```


## Complete Example

```python
# Workflow
x = np.array([[1, 5, 25, 125.0, 625]])
y = np.array([[20.0], [160.0], [640.0], [1280.0], [1024.0]])
z = y[::-1].copy()
y2 = y[::-1]
assert_equal(np.dot(x, z), np.dot(x, y2))
```

## Next Steps


---

*Source: test_regression.py:808 | Complexity: Intermediate | Last updated: 2026-06-02*