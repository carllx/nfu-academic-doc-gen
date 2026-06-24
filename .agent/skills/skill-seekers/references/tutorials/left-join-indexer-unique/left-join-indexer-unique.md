# How To: Left Join Indexer Unique

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test left join indexer unique

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
# Fixtures: readonly
```

## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([1, 2, 3, 4, 5], dtype=np.int64)
```

### Step 2: Assign b = np.array(...)

```python
b = np.array([2, 2, 3, 4, 4], dtype=np.int64)
```

### Step 3: Assign result = libjoin.left_join_indexer_unique(...)

```python
result = libjoin.left_join_indexer_unique(b, a)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([1, 1, 2, 3, 3], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Call a.setflags()

```python
a.setflags(write=False)
```

### Step 7: Call b.setflags()

```python
b.setflags(write=False)
```


## Complete Example

```python
# Setup
# Fixtures: readonly

# Workflow
a = np.array([1, 2, 3, 4, 5], dtype=np.int64)
b = np.array([2, 2, 3, 4, 4], dtype=np.int64)
if readonly:
    a.setflags(write=False)
    b.setflags(write=False)
result = libjoin.left_join_indexer_unique(b, a)
expected = np.array([1, 1, 2, 3, 3], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:142 | Complexity: Intermediate | Last updated: 2026-06-02*