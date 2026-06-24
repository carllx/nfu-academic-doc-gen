# How To: Trivial Fancy Not Possible

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test trivial fancy not possible

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

### Step 1: Assign a = np.arange(...)

```python
a = np.arange(6)
```

**Verification:**
```python
assert_array_equal(a[idx], idx)
```

### Step 2: Assign idx = value

```python
idx = np.arange(6, dtype=np.intp).reshape(2, 1, 3)[:, :, 0]
```

**Verification:**
```python
assert_array_equal(a, res)
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(a[idx], idx)
```

### Step 4: Assign unknown = value

```python
a[idx] = -1
```

### Step 5: Assign res = np.arange(...)

```python
res = np.arange(6)
```

### Step 6: Assign unknown = value

```python
res[0] = -1
```

### Step 7: Assign unknown = value

```python
res[3] = -1
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(a, res)
```


## Complete Example

```python
# Workflow
a = np.arange(6)
idx = np.arange(6, dtype=np.intp).reshape(2, 1, 3)[:, :, 0]
assert_array_equal(a[idx], idx)
a[idx] = -1
res = np.arange(6)
res[0] = -1
res[3] = -1
assert_array_equal(a, res)
```

## Next Steps


---

*Source: test_indexing.py:382 | Complexity: Advanced | Last updated: 2026-06-02*