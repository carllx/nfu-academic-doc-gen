# How To: Integer Split 2D Rows Greater Max Int32

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test integer split 2D rows greater max int32

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

### Step 1: Assign a = np.broadcast_to(...)

```python
a = np.broadcast_to([0], (1 << 32, 2))
```

**Verification:**
```python
assert_equal(res[i].shape, tgt[i].shape)
```

### Step 2: Assign res = array_split(...)

```python
res = array_split(a, 4)
```

### Step 3: Assign chunk = np.broadcast_to(...)

```python
chunk = np.broadcast_to([0], (1 << 30, 2))
```

### Step 4: Assign tgt = value

```python
tgt = [chunk] * 4
```

### Step 5: Call assert_equal()

```python
assert_equal(res[i].shape, tgt[i].shape)
```


## Complete Example

```python
# Workflow
a = np.broadcast_to([0], (1 << 32, 2))
res = array_split(a, 4)
chunk = np.broadcast_to([0], (1 << 30, 2))
tgt = [chunk] * 4
for i in range(len(tgt)):
    assert_equal(res[i].shape, tgt[i].shape)
```

## Next Steps


---

*Source: test_shape_base.py:450 | Complexity: Intermediate | Last updated: 2026-06-02*