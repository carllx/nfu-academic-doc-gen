# How To: Get Indexer Numeric Vs Bool

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer numeric vs bool

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign left = Index(...)

```python
left = Index([1, 2, 3])
```

### Step 2: Assign right = Index(...)

```python
right = Index([True, False])
```

### Step 3: Assign res = left.get_indexer(...)

```python
res = left.get_indexer(right)
```

### Step 4: Assign expected = value

```python
expected = -1 * np.ones(len(right), dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 6: Assign res = right.get_indexer(...)

```python
res = right.get_indexer(left)
```

### Step 7: Assign expected = value

```python
expected = -1 * np.ones(len(left), dtype=np.intp)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 9: Assign res = value

```python
res = left.get_indexer_non_unique(right)[0]
```

### Step 10: Assign expected = value

```python
expected = -1 * np.ones(len(right), dtype=np.intp)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 12: Assign res = value

```python
res = right.get_indexer_non_unique(left)[0]
```

### Step 13: Assign expected = value

```python
expected = -1 * np.ones(len(left), dtype=np.intp)
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```


## Complete Example

```python
# Workflow
left = Index([1, 2, 3])
right = Index([True, False])
res = left.get_indexer(right)
expected = -1 * np.ones(len(right), dtype=np.intp)
tm.assert_numpy_array_equal(res, expected)
res = right.get_indexer(left)
expected = -1 * np.ones(len(left), dtype=np.intp)
tm.assert_numpy_array_equal(res, expected)
res = left.get_indexer_non_unique(right)[0]
expected = -1 * np.ones(len(right), dtype=np.intp)
tm.assert_numpy_array_equal(res, expected)
res = right.get_indexer_non_unique(left)[0]
expected = -1 * np.ones(len(left), dtype=np.intp)
tm.assert_numpy_array_equal(res, expected)
```

## Next Steps


---

*Source: test_indexing.py:246 | Complexity: Advanced | Last updated: 2026-06-02*