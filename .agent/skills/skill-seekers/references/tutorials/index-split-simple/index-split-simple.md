# How To: Index Split Simple

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test index split simple

## Prerequisites

**Required Modules:**
- `functools`
- `sys`
- `pytest`
- `numpy`
- `numpy`
- `numpy.exceptions`
- `numpy.testing`
- `numpy.random`
- `numpy.random`
- `numpy.random`


## Step-by-Step Guide

### Step 1: Assign a = np.arange(...)

```python
a = np.arange(10)
```

### Step 2: Assign indices = value

```python
indices = [1, 5, 7]
```

### Step 3: Assign res = array_split(...)

```python
res = array_split(a, indices, axis=-1)
```

### Step 4: Assign desired = value

```python
desired = [np.arange(0, 1), np.arange(1, 5), np.arange(5, 7), np.arange(7, 10)]
```

### Step 5: Call compare_results()

```python
compare_results(res, desired)
```


## Complete Example

```python
# Workflow
a = np.arange(10)
indices = [1, 5, 7]
res = array_split(a, indices, axis=-1)
desired = [np.arange(0, 1), np.arange(1, 5), np.arange(5, 7), np.arange(7, 10)]
compare_results(res, desired)
```

## Next Steps


---

*Source: test_shape_base.py:458 | Complexity: Intermediate | Last updated: 2026-06-02*