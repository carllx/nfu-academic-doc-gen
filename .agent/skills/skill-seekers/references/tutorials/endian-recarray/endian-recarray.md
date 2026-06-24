# How To: Endian Recarray

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test endian recarray

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

### Step 1: Assign dt = np.dtype(...)

```python
dt = np.dtype([('head', '>u4'), ('data', '>u4', 2)])
```

**Verification:**
```python
assert_(buf[0]['head'] == 1)
```

### Step 2: Assign buf = np.recarray(...)

```python
buf = np.recarray(1, dtype=dt)
```

### Step 3: Assign unknown = 1

```python
buf[0]['head'] = 1
```

### Step 4: Assign unknown = value

```python
buf[0]['data'][:] = [1, 1]
```

### Step 5: Assign h = value

```python
h = buf[0]['head']
```

### Step 6: Assign d = value

```python
d = buf[0]['data'][0]
```

### Step 7: Assign unknown = h

```python
buf[0]['head'] = h
```

### Step 8: Assign unknown = d

```python
buf[0]['data'][0] = d
```

### Step 9: Call assert_()

```python
assert_(buf[0]['head'] == 1)
```


## Complete Example

```python
# Workflow
dt = np.dtype([('head', '>u4'), ('data', '>u4', 2)])
buf = np.recarray(1, dtype=dt)
buf[0]['head'] = 1
buf[0]['data'][:] = [1, 1]
h = buf[0]['head']
d = buf[0]['data'][0]
buf[0]['head'] = h
buf[0]['data'][0] = d
assert_(buf[0]['head'] == 1)
```

## Next Steps


---

*Source: test_regression.py:188 | Complexity: Advanced | Last updated: 2026-06-02*