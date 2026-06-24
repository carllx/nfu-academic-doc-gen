# How To: Get Indexer Nans In Index And Target

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer nans in index and target

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex([1, 2, np.nan, 3])
```

### Step 2: Assign other1 = value

```python
other1 = [2, 3, 4, np.nan]
```

### Step 3: Assign res1 = ci.get_indexer(...)

```python
res1 = ci.get_indexer(other1)
```

### Step 4: Assign expected1 = np.array(...)

```python
expected1 = np.array([1, 3, -1, 2], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res1, expected1)
```

### Step 6: Assign other2 = value

```python
other2 = [1, 4, 2, 3]
```

### Step 7: Assign res2 = ci.get_indexer(...)

```python
res2 = ci.get_indexer(other2)
```

### Step 8: Assign expected2 = np.array(...)

```python
expected2 = np.array([0, -1, 1, 3], dtype=np.intp)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res2, expected2)
```


## Complete Example

```python
# Workflow
ci = CategoricalIndex([1, 2, np.nan, 3])
other1 = [2, 3, 4, np.nan]
res1 = ci.get_indexer(other1)
expected1 = np.array([1, 3, -1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(res1, expected1)
other2 = [1, 4, 2, 3]
res2 = ci.get_indexer(other2)
expected2 = np.array([0, -1, 1, 3], dtype=np.intp)
tm.assert_numpy_array_equal(res2, expected2)
```

## Next Steps


---

*Source: test_indexing.py:296 | Complexity: Advanced | Last updated: 2026-06-02*