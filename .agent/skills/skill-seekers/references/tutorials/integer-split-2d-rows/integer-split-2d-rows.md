# How To: Integer Split 2D Rows

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test integer split 2D rows

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

### Step 1: Assign a = np.array(...)

```python
a = np.array([np.arange(10), np.arange(10)])
```

**Verification:**
```python
assert_(a.dtype.type is res[-1].dtype.type)
```

### Step 2: Assign res = array_split(...)

```python
res = array_split(a, 3, axis=0)
```

**Verification:**
```python
assert_(a.dtype.type is res[-1].dtype.type)
```

### Step 3: Assign tgt = value

```python
tgt = [np.array([np.arange(10)]), np.array([np.arange(10)]), np.zeros((0, 10))]
```

### Step 4: Call compare_results()

```python
compare_results(res, tgt)
```

### Step 5: Call assert_()

```python
assert_(a.dtype.type is res[-1].dtype.type)
```

### Step 6: Assign res = array_split(...)

```python
res = array_split(a, [0, 1], axis=0)
```

### Step 7: Assign tgt = value

```python
tgt = [np.zeros((0, 10)), np.array([np.arange(10)]), np.array([np.arange(10)])]
```

### Step 8: Call compare_results()

```python
compare_results(res, tgt)
```

### Step 9: Call assert_()

```python
assert_(a.dtype.type is res[-1].dtype.type)
```


## Complete Example

```python
# Workflow
a = np.array([np.arange(10), np.arange(10)])
res = array_split(a, 3, axis=0)
tgt = [np.array([np.arange(10)]), np.array([np.arange(10)]), np.zeros((0, 10))]
compare_results(res, tgt)
assert_(a.dtype.type is res[-1].dtype.type)
res = array_split(a, [0, 1], axis=0)
tgt = [np.zeros((0, 10)), np.array([np.arange(10)]), np.array([np.arange(10)])]
compare_results(res, tgt)
assert_(a.dtype.type is res[-1].dtype.type)
```

## Next Steps


---

*Source: test_shape_base.py:415 | Complexity: Advanced | Last updated: 2026-06-02*