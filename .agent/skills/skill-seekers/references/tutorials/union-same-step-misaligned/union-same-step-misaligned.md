# How To: Union Same Step Misaligned

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union same step misaligned

## Prerequisites

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign left = RangeIndex(...)

```python
left = RangeIndex(range(0, 20, 4))
```

### Step 2: Assign right = RangeIndex(...)

```python
right = RangeIndex(range(1, 21, 4))
```

### Step 3: Assign result = left.union(...)

```python
result = left.union(right)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([0, 1, 4, 5, 8, 9, 12, 13, 16, 17])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```


## Complete Example

```python
# Workflow
left = RangeIndex(range(0, 20, 4))
right = RangeIndex(range(1, 21, 4))
result = left.union(right)
expected = Index([0, 1, 4, 5, 8, 9, 12, 13, 16, 17])
tm.assert_index_equal(result, expected, exact=True)
```

## Next Steps


---

*Source: test_setops.py:298 | Complexity: Intermediate | Last updated: 2026-06-02*