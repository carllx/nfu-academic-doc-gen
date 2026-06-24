# How To: Union Rangeindex Sort True

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union rangeindex sort true

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign idx1 = RangeIndex(...)

```python
idx1 = RangeIndex(1, 100, 6)
```

### Step 2: Assign idx2 = RangeIndex(...)

```python
idx2 = RangeIndex(1, 50, 3)
```

### Step 3: Assign result = idx1.union(...)

```python
result = idx1.union(idx2, sort=True)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 55, 61, 67, 73, 79, 85, 91, 97])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx1 = RangeIndex(1, 100, 6)
idx2 = RangeIndex(1, 50, 3)
result = idx1.union(idx2, sort=True)
expected = Index([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 55, 61, 67, 73, 79, 85, 91, 97])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:636 | Complexity: Intermediate | Last updated: 2026-06-02*