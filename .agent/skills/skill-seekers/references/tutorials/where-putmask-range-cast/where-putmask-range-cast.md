# How To: Where Putmask Range Cast

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where putmask range cast

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = RangeIndex(...)

```python
idx = RangeIndex(0, 5, name='test')
```

### Step 2: Assign mask = np.array(...)

```python
mask = np.array([True, True, False, False, False])
```

### Step 3: Assign result = idx.putmask(...)

```python
result = idx.putmask(mask, 10)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([10, 10, 2, 3, 4], dtype=np.int64, name='test')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign result = idx.where(...)

```python
result = idx.where(~mask, 10)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = RangeIndex(0, 5, name='test')
mask = np.array([True, True, False, False, False])
result = idx.putmask(mask, 10)
expected = Index([10, 10, 2, 3, 4], dtype=np.int64, name='test')
tm.assert_index_equal(result, expected)
result = idx.where(~mask, 10)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:127 | Complexity: Intermediate | Last updated: 2026-06-02*