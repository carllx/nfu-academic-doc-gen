# How To: Reverse Strides And Subspace Bufferinit

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reverse strides and subspace bufferinit

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

### Step 1: Assign a = np.ones(...)

```python
a = np.ones(5)
```

**Verification:**
```python
assert_equal(a[0], 0)
```

### Step 2: Assign b = value

```python
b = np.zeros(5, dtype=np.intp)[::-1]
```

**Verification:**
```python
assert_equal(a[0], [0, 1])
```

### Step 3: Assign c = value

```python
c = np.arange(5)[::-1]
```

### Step 4: Assign unknown = c

```python
a[b] = c
```

### Step 5: Call assert_equal()

```python
assert_equal(a[0], 0)
```

### Step 6: Assign a = np.ones(...)

```python
a = np.ones((5, 2))
```

### Step 7: Assign c = value

```python
c = np.arange(10).reshape(5, 2)[::-1]
```

### Step 8: Assign unknown = c

```python
a[b, :] = c
```

### Step 9: Call assert_equal()

```python
assert_equal(a[0], [0, 1])
```


## Complete Example

```python
# Workflow
a = np.ones(5)
b = np.zeros(5, dtype=np.intp)[::-1]
c = np.arange(5)[::-1]
a[b] = c
assert_equal(a[0], 0)
a = np.ones((5, 2))
c = np.arange(10).reshape(5, 2)[::-1]
a[b, :] = c
assert_equal(a[0], [0, 1])
```

## Next Steps


---

*Source: test_indexing.py:303 | Complexity: Advanced | Last updated: 2026-06-02*