# How To: Openblas Threading

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test openblas threading

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = np.arange(...)

```python
x = np.arange(500000, dtype=np.float64)
```

**Verification:**
```python
assert False, 'unexpected result from matmul, probably due to OpenBLAS threading issues'
```

### Step 2: Assign src = value

```python
src = np.vstack((x, -10 * x)).T
```

### Step 3: Assign matrix = np.array(...)

```python
matrix = np.array([[0, 1], [1, 0]])
```

### Step 4: Assign expected = value

```python
expected = np.vstack((-10 * x, x)).T
```

### Step 5: Assign result = value

```python
result = src @ matrix
```

### Step 6: Assign mismatches = unknown.sum(...)

```python
mismatches = (~np.isclose(result, expected)).sum()
```

**Verification:**
```python
assert False, 'unexpected result from matmul, probably due to OpenBLAS threading issues'
```


## Complete Example

```python
# Workflow
x = np.arange(500000, dtype=np.float64)
src = np.vstack((x, -10 * x)).T
matrix = np.array([[0, 1], [1, 0]])
expected = np.vstack((-10 * x, x)).T
for i in range(200):
    result = src @ matrix
    mismatches = (~np.isclose(result, expected)).sum()
    if mismatches != 0:
        assert False, 'unexpected result from matmul, probably due to OpenBLAS threading issues'
```

## Next Steps


---

*Source: test_regression.py:169 | Complexity: Intermediate | Last updated: 2026-06-02*