# How To: Get Indexer Int64

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer int64

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index(range(0, 20, 2), dtype=np.int64)
```

### Step 2: Assign target = Index(...)

```python
target = Index(np.arange(10), dtype=np.int64)
```

### Step 3: Assign indexer = index.get_indexer(...)

```python
indexer = index.get_indexer(target)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([0, -1, 1, -1, 2, -1, 3, -1, 4, -1], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer, expected)
```

### Step 6: Assign target = Index(...)

```python
target = Index(np.arange(10), dtype=np.int64)
```

### Step 7: Assign indexer = index.get_indexer(...)

```python
indexer = index.get_indexer(target, method='pad')
```

### Step 8: Assign expected = np.array(...)

```python
expected = np.array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4], dtype=np.intp)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer, expected)
```

### Step 10: Assign target = Index(...)

```python
target = Index(np.arange(10), dtype=np.int64)
```

### Step 11: Assign indexer = index.get_indexer(...)

```python
indexer = index.get_indexer(target, method='backfill')
```

### Step 12: Assign expected = np.array(...)

```python
expected = np.array([0, 1, 1, 2, 2, 3, 3, 4, 4, 5], dtype=np.intp)
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer, expected)
```


## Complete Example

```python
# Workflow
index = Index(range(0, 20, 2), dtype=np.int64)
target = Index(np.arange(10), dtype=np.int64)
indexer = index.get_indexer(target)
expected = np.array([0, -1, 1, -1, 2, -1, 3, -1, 4, -1], dtype=np.intp)
tm.assert_numpy_array_equal(indexer, expected)
target = Index(np.arange(10), dtype=np.int64)
indexer = index.get_indexer(target, method='pad')
expected = np.array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4], dtype=np.intp)
tm.assert_numpy_array_equal(indexer, expected)
target = Index(np.arange(10), dtype=np.int64)
indexer = index.get_indexer(target, method='backfill')
expected = np.array([0, 1, 1, 2, 2, 3, 3, 4, 4, 5], dtype=np.intp)
tm.assert_numpy_array_equal(indexer, expected)
```

## Next Steps


---

*Source: test_indexing.py:289 | Complexity: Advanced | Last updated: 2026-06-02*