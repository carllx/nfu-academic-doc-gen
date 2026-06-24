# How To: Get Indexer Backfill

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer backfill

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = RangeIndex(...)

```python
index = RangeIndex(start=0, stop=20, step=2)
```

### Step 2: Assign target = RangeIndex(...)

```python
target = RangeIndex(10)
```

### Step 3: Assign indexer = index.get_indexer(...)

```python
indexer = index.get_indexer(target, method='backfill')
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([0, 1, 1, 2, 2, 3, 3, 4, 4, 5], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer, expected)
```


## Complete Example

```python
# Workflow
index = RangeIndex(start=0, stop=20, step=2)
target = RangeIndex(10)
indexer = index.get_indexer(target, method='backfill')
expected = np.array([0, 1, 1, 2, 2, 3, 3, 4, 4, 5], dtype=np.intp)
tm.assert_numpy_array_equal(indexer, expected)
```

## Next Steps


---

*Source: test_indexing.py:26 | Complexity: Intermediate | Last updated: 2026-06-02*