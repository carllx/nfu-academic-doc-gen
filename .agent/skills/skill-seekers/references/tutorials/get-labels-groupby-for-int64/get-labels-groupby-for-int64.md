# How To: Get Labels Groupby For Int64

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get labels groupby for Int64

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections.abc`
- `contextlib`
- `re`
- `struct`
- `tracemalloc`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`

**Setup Required:**
```python
# Fixtures: writable
```

## Step-by-Step Guide

### Step 1: Assign table = ht.Int64HashTable(...)

```python
table = ht.Int64HashTable()
```

### Step 2: Assign vals = np.array(...)

```python
vals = np.array([1, 2, -1, 2, 1, -1], dtype=np.int64)
```

### Step 3: Assign vals.flags.writeable = writable

```python
vals.flags.writeable = writable
```

### Step 4: Assign unknown = table.get_labels_groupby(...)

```python
arr, unique = table.get_labels_groupby(vals)
```

### Step 5: Assign expected_arr = np.array(...)

```python
expected_arr = np.array([0, 1, -1, 1, 0, -1], dtype=np.intp)
```

### Step 6: Assign expected_unique = np.array(...)

```python
expected_unique = np.array([1, 2], dtype=np.int64)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, expected_arr)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(unique, expected_unique)
```


## Complete Example

```python
# Setup
# Fixtures: writable

# Workflow
table = ht.Int64HashTable()
vals = np.array([1, 2, -1, 2, 1, -1], dtype=np.int64)
vals.flags.writeable = writable
arr, unique = table.get_labels_groupby(vals)
expected_arr = np.array([0, 1, -1, 1, 0, -1], dtype=np.intp)
expected_unique = np.array([1, 2], dtype=np.int64)
tm.assert_numpy_array_equal(arr, expected_arr)
tm.assert_numpy_array_equal(unique, expected_unique)
```

## Next Steps


---

*Source: test_hashtable.py:451 | Complexity: Advanced | Last updated: 2026-06-02*