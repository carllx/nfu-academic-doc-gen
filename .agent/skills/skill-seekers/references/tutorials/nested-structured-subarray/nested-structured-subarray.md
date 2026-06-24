# How To: Nested Structured Subarray

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nested structured subarray

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `io`
- `tempfile`
- `pytest`
- `numpy`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign point = np.dtype(...)

```python
point = np.dtype([('x', float), ('y', float)])
```

**Verification:**
```python
assert_array_equal(np.loadtxt(data, dtype=dt, delimiter=','), expected)
```

### Step 2: Assign dt = np.dtype(...)

```python
dt = np.dtype([('code', int), ('points', point, (2,))])
```

### Step 3: Assign data = StringIO(...)

```python
data = StringIO('100,1,2,3,4\n200,5,6,7,8\n')
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([(100, [(1.0, 2.0), (3.0, 4.0)]), (200, [(5.0, 6.0), (7.0, 8.0)])], dtype=dt)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(np.loadtxt(data, dtype=dt, delimiter=','), expected)
```


## Complete Example

```python
# Workflow
point = np.dtype([('x', float), ('y', float)])
dt = np.dtype([('code', int), ('points', point, (2,))])
data = StringIO('100,1,2,3,4\n200,5,6,7,8\n')
expected = np.array([(100, [(1.0, 2.0), (3.0, 4.0)]), (200, [(5.0, 6.0), (7.0, 8.0)])], dtype=dt)
assert_array_equal(np.loadtxt(data, dtype=dt, delimiter=','), expected)
```

## Next Steps


---

*Source: test_loadtxt.py:106 | Complexity: Intermediate | Last updated: 2026-06-02*