# How To: Take Accepts Empty Array

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test take accepts empty array

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = RangeIndex(...)

```python
idx = RangeIndex(1, 4, name='foo')
```

### Step 2: Assign result = idx.take(...)

```python
result = idx.take(np.array([]))
```

### Step 3: Assign expected = Index(...)

```python
expected = Index([], dtype=np.int64, name='foo')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign idx = RangeIndex(...)

```python
idx = RangeIndex(0, name='foo')
```

### Step 6: Assign result = idx.take(...)

```python
result = idx.take(np.array([]))
```

### Step 7: Assign expected = Index(...)

```python
expected = Index([], dtype=np.int64, name='foo')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = RangeIndex(1, 4, name='foo')
result = idx.take(np.array([]))
expected = Index([], dtype=np.int64, name='foo')
tm.assert_index_equal(result, expected)
idx = RangeIndex(0, name='foo')
result = idx.take(np.array([]))
expected = Index([], dtype=np.int64, name='foo')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:95 | Complexity: Advanced | Last updated: 2026-06-02*