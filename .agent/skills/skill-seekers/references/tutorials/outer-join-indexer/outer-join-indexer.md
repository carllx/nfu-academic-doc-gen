# How To: Outer Join Indexer

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test outer join indexer

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.join`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign indexer = value

```python
indexer = libjoin.outer_join_indexer
```

**Verification:**
```python
assert isinstance(result, np.ndarray)
```

### Step 2: Assign left = np.arange(...)

```python
left = np.arange(3, dtype=dtype)
```

**Verification:**
```python
assert isinstance(lindexer, np.ndarray)
```

### Step 3: Assign right = np.arange(...)

```python
right = np.arange(2, 5, dtype=dtype)
```

**Verification:**
```python
assert isinstance(rindexer, np.ndarray)
```

### Step 4: Assign empty = np.array(...)

```python
empty = np.array([], dtype=dtype)
```

### Step 5: Assign unknown = indexer(...)

```python
result, lindexer, rindexer = indexer(left, right)
```

**Verification:**
```python
assert isinstance(result, np.ndarray)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, np.arange(5, dtype=dtype))
```

### Step 7: Assign exp = np.array(...)

```python
exp = np.array([0, 1, 2, -1, -1], dtype=np.intp)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lindexer, exp)
```

### Step 9: Assign exp = np.array(...)

```python
exp = np.array([-1, -1, 0, 1, 2], dtype=np.intp)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(rindexer, exp)
```

### Step 11: Assign unknown = indexer(...)

```python
result, lindexer, rindexer = indexer(empty, right)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, right)
```

### Step 13: Assign exp = np.array(...)

```python
exp = np.array([-1, -1, -1], dtype=np.intp)
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lindexer, exp)
```

### Step 15: Assign exp = np.array(...)

```python
exp = np.array([0, 1, 2], dtype=np.intp)
```

### Step 16: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(rindexer, exp)
```

### Step 17: Assign unknown = indexer(...)

```python
result, lindexer, rindexer = indexer(left, empty)
```

### Step 18: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, left)
```

### Step 19: Assign exp = np.array(...)

```python
exp = np.array([0, 1, 2], dtype=np.intp)
```

### Step 20: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(lindexer, exp)
```

### Step 21: Assign exp = np.array(...)

```python
exp = np.array([-1, -1, -1], dtype=np.intp)
```

### Step 22: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(rindexer, exp)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
indexer = libjoin.outer_join_indexer
left = np.arange(3, dtype=dtype)
right = np.arange(2, 5, dtype=dtype)
empty = np.array([], dtype=dtype)
result, lindexer, rindexer = indexer(left, right)
assert isinstance(result, np.ndarray)
assert isinstance(lindexer, np.ndarray)
assert isinstance(rindexer, np.ndarray)
tm.assert_numpy_array_equal(result, np.arange(5, dtype=dtype))
exp = np.array([0, 1, 2, -1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(lindexer, exp)
exp = np.array([-1, -1, 0, 1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(rindexer, exp)
result, lindexer, rindexer = indexer(empty, right)
tm.assert_numpy_array_equal(result, right)
exp = np.array([-1, -1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(lindexer, exp)
exp = np.array([0, 1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(rindexer, exp)
result, lindexer, rindexer = indexer(left, empty)
tm.assert_numpy_array_equal(result, left)
exp = np.array([0, 1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(lindexer, exp)
exp = np.array([-1, -1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(rindexer, exp)
```

## Next Steps


---

*Source: test_join.py:17 | Complexity: Advanced | Last updated: 2026-06-02*