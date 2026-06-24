# How To: Reindex Duplicate Target

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex duplicate target

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cat = CategoricalIndex(...)

```python
cat = CategoricalIndex(['a', 'b', 'c'], categories=['a', 'b', 'c', 'd'])
```

### Step 2: Assign unknown = cat.reindex(...)

```python
res, indexer = cat.reindex(['a', 'c', 'c'])
```

### Step 3: Assign exp = Index(...)

```python
exp = Index(['a', 'c', 'c'])
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp, exact=True)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer, np.array([0, 2, 2], dtype=np.intp))
```

### Step 6: Assign unknown = cat.reindex(...)

```python
res, indexer = cat.reindex(CategoricalIndex(['a', 'c', 'c'], categories=['a', 'b', 'c', 'd']))
```

### Step 7: Assign exp = CategoricalIndex(...)

```python
exp = CategoricalIndex(['a', 'c', 'c'], categories=['a', 'b', 'c', 'd'])
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp, exact=True)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer, np.array([0, 2, 2], dtype=np.intp))
```


## Complete Example

```python
# Workflow
cat = CategoricalIndex(['a', 'b', 'c'], categories=['a', 'b', 'c', 'd'])
res, indexer = cat.reindex(['a', 'c', 'c'])
exp = Index(['a', 'c', 'c'])
tm.assert_index_equal(res, exp, exact=True)
tm.assert_numpy_array_equal(indexer, np.array([0, 2, 2], dtype=np.intp))
res, indexer = cat.reindex(CategoricalIndex(['a', 'c', 'c'], categories=['a', 'b', 'c', 'd']))
exp = CategoricalIndex(['a', 'c', 'c'], categories=['a', 'b', 'c', 'd'])
tm.assert_index_equal(res, exp, exact=True)
tm.assert_numpy_array_equal(indexer, np.array([0, 2, 2], dtype=np.intp))
```

## Next Steps


---

*Source: test_reindex.py:39 | Complexity: Advanced | Last updated: 2026-06-02*