# How To: Boolean Shape Mismatch

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test boolean shape mismatch

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

### Step 1: Assign arr = np.ones(...)

```python
arr = np.ones((5, 4, 3))
```

**Verification:**
```python
assert_raises(IndexError, arr.__getitem__, index)
```

### Step 2: Assign index = np.array(...)

```python
index = np.array([True])
```

**Verification:**
```python
assert_raises(IndexError, arr.__getitem__, index)
```

### Step 3: Call assert_raises()

```python
assert_raises(IndexError, arr.__getitem__, index)
```

**Verification:**
```python
assert_raises(IndexError, arr.__getitem__, index)
```

### Step 4: Assign index = np.array(...)

```python
index = np.array([False] * 6)
```

**Verification:**
```python
assert_raises(IndexError, arr.__getitem__, (slice(None), index))
```

### Step 5: Call assert_raises()

```python
assert_raises(IndexError, arr.__getitem__, index)
```

### Step 6: Assign index = np.zeros(...)

```python
index = np.zeros((4, 4), dtype=bool)
```

### Step 7: Call assert_raises()

```python
assert_raises(IndexError, arr.__getitem__, index)
```

### Step 8: Call assert_raises()

```python
assert_raises(IndexError, arr.__getitem__, (slice(None), index))
```


## Complete Example

```python
# Workflow
arr = np.ones((5, 4, 3))
index = np.array([True])
assert_raises(IndexError, arr.__getitem__, index)
index = np.array([False] * 6)
assert_raises(IndexError, arr.__getitem__, index)
index = np.zeros((4, 4), dtype=bool)
assert_raises(IndexError, arr.__getitem__, index)
assert_raises(IndexError, arr.__getitem__, (slice(None), index))
```

## Next Steps


---

*Source: test_indexing.py:225 | Complexity: Advanced | Last updated: 2026-06-02*