# How To: As Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test as series

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.polynomial.polyutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Call assert_raises()

```python
assert_raises(ValueError, pu.as_series, [[]])
```

**Verification:**
```python
assert_raises(ValueError, pu.as_series, [[]])
```

### Step 2: Call assert_raises()

```python
assert_raises(ValueError, pu.as_series, [[[1, 2]]])
```

**Verification:**
```python
assert_raises(ValueError, pu.as_series, [[[1, 2]]])
```

### Step 3: Call assert_raises()

```python
assert_raises(ValueError, pu.as_series, [[1], ['a']])
```

**Verification:**
```python
assert_raises(ValueError, pu.as_series, [[1], ['a']])
```

### Step 4: Assign types = value

```python
types = ['i', 'd', 'O']
```

**Verification:**
```python
assert_(resi.dtype.char == resj.dtype.char)
```

### Step 5: Assign ci = np.ones(...)

```python
ci = np.ones(1, types[i])
```

**Verification:**
```python
assert_(resj.dtype.char == types[i])
```

### Step 6: Assign cj = np.ones(...)

```python
cj = np.ones(1, types[j])
```

### Step 7: Assign unknown = pu.as_series(...)

```python
[resi, resj] = pu.as_series([ci, cj])
```

### Step 8: Call assert_()

```python
assert_(resi.dtype.char == resj.dtype.char)
```

### Step 9: Call assert_()

```python
assert_(resj.dtype.char == types[i])
```


## Complete Example

```python
# Workflow
assert_raises(ValueError, pu.as_series, [[]])
assert_raises(ValueError, pu.as_series, [[[1, 2]]])
assert_raises(ValueError, pu.as_series, [[1], ['a']])
types = ['i', 'd', 'O']
for i in range(len(types)):
    for j in range(i):
        ci = np.ones(1, types[i])
        cj = np.ones(1, types[j])
        [resi, resj] = pu.as_series([ci, cj])
        assert_(resi.dtype.char == resj.dtype.char)
        assert_(resj.dtype.char == types[i])
```

## Next Steps


---

*Source: test_polyutils.py:21 | Complexity: Advanced | Last updated: 2026-06-02*