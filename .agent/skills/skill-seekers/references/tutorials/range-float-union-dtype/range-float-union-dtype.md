# How To: Range Float Union Dtype

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test range float union dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._testing`
- `pandas.core.indexes.api`


## Step-by-Step Guide

### Step 1: Assign index = RangeIndex(...)

```python
index = RangeIndex(start=0, stop=3)
```

### Step 2: Assign other = Index(...)

```python
other = Index([0.5, 1.5], dtype=np.float64)
```

### Step 3: Assign result = index.union(...)

```python
result = index.union(other)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([0.0, 0.5, 1, 1.5, 2.0], dtype=np.float64)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign result = other.union(...)

```python
result = other.union(index)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
index = RangeIndex(start=0, stop=3)
other = Index([0.5, 1.5], dtype=np.float64)
result = index.union(other)
expected = Index([0.0, 0.5, 1, 1.5, 2.0], dtype=np.float64)
tm.assert_index_equal(result, expected)
result = other.union(index)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:66 | Complexity: Intermediate | Last updated: 2026-06-02*