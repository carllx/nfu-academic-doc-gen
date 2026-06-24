# How To: Recarray Copy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test recarray copy

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

### Step 1: Assign dt = value

```python
dt = [('x', np.int16), ('y', np.float64)]
```

**Verification:**
```python
assert_(ra['x'] != rb['x'])
```

### Step 2: Assign ra = np.array(...)

```python
ra = np.array([(1, 2.3)], dtype=dt)
```

### Step 3: Assign rb = np.rec.array(...)

```python
rb = np.rec.array(ra, dtype=dt)
```

### Step 4: Assign unknown = 2.0

```python
rb['x'] = 2.0
```

### Step 5: Call assert_()

```python
assert_(ra['x'] != rb['x'])
```


## Complete Example

```python
# Workflow
dt = [('x', np.int16), ('y', np.float64)]
ra = np.array([(1, 2.3)], dtype=dt)
rb = np.rec.array(ra, dtype=dt)
rb['x'] = 2.0
assert_(ra['x'] != rb['x'])
```

## Next Steps


---

*Source: test_regression.py:570 | Complexity: Intermediate | Last updated: 2026-06-02*