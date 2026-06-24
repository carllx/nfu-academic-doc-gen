# How To: Reindex Not All Tuples

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex not all tuples

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign keys = value

```python
keys = [('i', 'i'), ('i', 'j'), ('j', 'i'), 'j']
```

### Step 2: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples(keys[:-1])
```

### Step 3: Assign idx = Index(...)

```python
idx = Index(keys)
```

### Step 4: Assign unknown = mi.reindex(...)

```python
res, indexer = mi.reindex(idx)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, idx)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([0, 1, 2, -1], dtype=np.intp)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer, expected)
```


## Complete Example

```python
# Workflow
keys = [('i', 'i'), ('i', 'j'), ('j', 'i'), 'j']
mi = MultiIndex.from_tuples(keys[:-1])
idx = Index(keys)
res, indexer = mi.reindex(idx)
tm.assert_index_equal(res, idx)
expected = np.array([0, 1, 2, -1], dtype=np.intp)
tm.assert_numpy_array_equal(indexer, expected)
```

## Next Steps


---

*Source: test_reindex.py:126 | Complexity: Intermediate | Last updated: 2026-06-02*