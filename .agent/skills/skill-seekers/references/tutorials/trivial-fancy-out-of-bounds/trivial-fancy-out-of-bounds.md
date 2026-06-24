# How To: Trivial Fancy Out Of Bounds

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test trivial fancy out of bounds

## Prerequisites

**Required Modules:**
- `functools`
- `inspect`
- `operator`
- `sys`
- `warnings`
- `itertools`
- `pytest`
- `numpy`
- `numpy._core._multiarray_tests`
- `numpy.exceptions`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.zeros(...)

```python
a = np.zeros(5)
```

**Verification:**
```python
assert_raises(IndexError, a.__getitem__, ind)
```

### Step 2: Assign ind = np.ones(...)

```python
ind = np.ones(20, dtype=np.intp)
```

**Verification:**
```python
assert_raises(IndexError, a.__setitem__, ind, 0)
```

### Step 3: Assign unknown = 10

```python
ind[-1] = 10
```

**Verification:**
```python
assert_raises(IndexError, a.__getitem__, ind)
```

### Step 4: Call assert_raises()

```python
assert_raises(IndexError, a.__getitem__, ind)
```

**Verification:**
```python
assert_raises(IndexError, a.__setitem__, ind, 0)
```

### Step 5: Call assert_raises()

```python
assert_raises(IndexError, a.__setitem__, ind, 0)
```

### Step 6: Assign ind = np.ones(...)

```python
ind = np.ones(20, dtype=np.intp)
```

### Step 7: Assign unknown = 11

```python
ind[0] = 11
```

### Step 8: Call assert_raises()

```python
assert_raises(IndexError, a.__getitem__, ind)
```

### Step 9: Call assert_raises()

```python
assert_raises(IndexError, a.__setitem__, ind, 0)
```


## Complete Example

```python
# Workflow
a = np.zeros(5)
ind = np.ones(20, dtype=np.intp)
ind[-1] = 10
assert_raises(IndexError, a.__getitem__, ind)
assert_raises(IndexError, a.__setitem__, ind, 0)
ind = np.ones(20, dtype=np.intp)
ind[0] = 11
assert_raises(IndexError, a.__getitem__, ind)
assert_raises(IndexError, a.__setitem__, ind, 0)
```

## Next Steps


---

*Source: test_indexing.py:371 | Complexity: Advanced | Last updated: 2026-06-02*