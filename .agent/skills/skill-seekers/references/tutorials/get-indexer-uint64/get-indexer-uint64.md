# How To: Get Indexer Uint64

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer uint64

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: index_large
```

## Step-by-Step Guide

### Step 1: Assign target = Index(...)

```python
target = Index(np.arange(10).astype('uint64') * 5 + 2 ** 63)
```

### Step 2: Assign indexer = index_large.get_indexer(...)

```python
indexer = index_large.get_indexer(target)
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([0, -1, 1, 2, 3, 4, -1, -1, -1, -1], dtype=np.intp)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer, expected)
```

### Step 5: Assign target = Index(...)

```python
target = Index(np.arange(10).astype('uint64') * 5 + 2 ** 63)
```

### Step 6: Assign indexer = index_large.get_indexer(...)

```python
indexer = index_large.get_indexer(target, method='pad')
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array([0, 0, 1, 2, 3, 4, 4, 4, 4, 4], dtype=np.intp)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer, expected)
```

### Step 9: Assign target = Index(...)

```python
target = Index(np.arange(10).astype('uint64') * 5 + 2 ** 63)
```

### Step 10: Assign indexer = index_large.get_indexer(...)

```python
indexer = index_large.get_indexer(target, method='backfill')
```

### Step 11: Assign expected = np.array(...)

```python
expected = np.array([0, 1, 1, 2, 3, 4, -1, -1, -1, -1], dtype=np.intp)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer, expected)
```


## Complete Example

```python
# Setup
# Fixtures: index_large

# Workflow
target = Index(np.arange(10).astype('uint64') * 5 + 2 ** 63)
indexer = index_large.get_indexer(target)
expected = np.array([0, -1, 1, 2, 3, 4, -1, -1, -1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(indexer, expected)
target = Index(np.arange(10).astype('uint64') * 5 + 2 ** 63)
indexer = index_large.get_indexer(target, method='pad')
expected = np.array([0, 0, 1, 2, 3, 4, 4, 4, 4, 4], dtype=np.intp)
tm.assert_numpy_array_equal(indexer, expected)
target = Index(np.arange(10).astype('uint64') * 5 + 2 ** 63)
indexer = index_large.get_indexer(target, method='backfill')
expected = np.array([0, 1, 1, 2, 3, 4, -1, -1, -1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(indexer, expected)
```

## Next Steps


---

*Source: test_indexing.py:306 | Complexity: Advanced | Last updated: 2026-06-02*