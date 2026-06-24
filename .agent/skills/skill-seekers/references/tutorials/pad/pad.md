# How To: Pad

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pad

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pandas._libs`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign old = np.array(...)

```python
old = np.array([1, 5, 10], dtype=np.int64)
```

### Step 2: Assign new = np.array(...)

```python
new = np.array(list(range(12)), dtype=np.int64)
```

### Step 3: Assign filler = unknown(...)

```python
filler = libalgos.pad['int64_t'](old, new)
```

### Step 4: Assign expect_filler = np.array(...)

```python
expect_filler = np.array([-1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(filler, expect_filler)
```

### Step 6: Assign old = np.array(...)

```python
old = np.array([5, 10], dtype=np.int64)
```

### Step 7: Assign new = np.arange(...)

```python
new = np.arange(5, dtype=np.int64)
```

### Step 8: Assign filler = unknown(...)

```python
filler = libalgos.pad['int64_t'](old, new)
```

### Step 9: Assign expect_filler = np.array(...)

```python
expect_filler = np.array([-1, -1, -1, -1, -1], dtype=np.intp)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(filler, expect_filler)
```


## Complete Example

```python
# Workflow
old = np.array([1, 5, 10], dtype=np.int64)
new = np.array(list(range(12)), dtype=np.int64)
filler = libalgos.pad['int64_t'](old, new)
expect_filler = np.array([-1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2], dtype=np.intp)
tm.assert_numpy_array_equal(filler, expect_filler)
old = np.array([5, 10], dtype=np.int64)
new = np.arange(5, dtype=np.int64)
filler = libalgos.pad['int64_t'](old, new)
expect_filler = np.array([-1, -1, -1, -1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(filler, expect_filler)
```

## Next Steps


---

*Source: test_libalgos.py:76 | Complexity: Advanced | Last updated: 2026-06-02*