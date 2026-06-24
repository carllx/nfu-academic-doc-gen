# How To: Duplicates

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test duplicates

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs.interval`
- `pandas.compat`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign left = np.array(...)

```python
left = np.array([0, 0, 0], dtype=dtype)
```

### Step 2: Assign tree = IntervalTree(...)

```python
tree = IntervalTree(left, left + 1)
```

### Step 3: Assign unknown = tree.get_indexer_non_unique(...)

```python
indexer, missing = tree.get_indexer_non_unique(np.array([0.5]))
```

### Step 4: Assign result = np.sort(...)

```python
result = np.sort(indexer)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([0, 1, 2], dtype='intp')
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Assign result = missing

```python
result = missing
```

### Step 8: Assign expected = np.array(...)

```python
expected = np.array([], dtype='intp')
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 10: Call tree.get_indexer()

```python
tree.get_indexer(np.array([0.5]))
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
left = np.array([0, 0, 0], dtype=dtype)
tree = IntervalTree(left, left + 1)
with pytest.raises(KeyError, match="'indexer does not intersect a unique set of intervals'"):
    tree.get_indexer(np.array([0.5]))
indexer, missing = tree.get_indexer_non_unique(np.array([0.5]))
result = np.sort(indexer)
expected = np.array([0, 1, 2], dtype='intp')
tm.assert_numpy_array_equal(result, expected)
result = missing
expected = np.array([], dtype='intp')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_interval_tree.py:106 | Complexity: Advanced | Last updated: 2026-06-02*