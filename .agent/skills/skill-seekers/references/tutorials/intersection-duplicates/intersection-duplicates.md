# How To: Intersection Duplicates

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersection duplicates

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = IntervalIndex.from_tuples(...)

```python
index = IntervalIndex.from_tuples([(1, 2), (1, 2), (2, 3), (3, 4)])
```

### Step 2: Assign other = IntervalIndex.from_tuples(...)

```python
other = IntervalIndex.from_tuples([(1, 2), (2, 3)])
```

### Step 3: Assign expected = IntervalIndex.from_tuples(...)

```python
expected = IntervalIndex.from_tuples([(1, 2), (2, 3)])
```

### Step 4: Assign result = index.intersection(...)

```python
result = index.intersection(other)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
index = IntervalIndex.from_tuples([(1, 2), (1, 2), (2, 3), (3, 4)])
other = IntervalIndex.from_tuples([(1, 2), (2, 3)])
expected = IntervalIndex.from_tuples([(1, 2), (2, 3)])
result = index.intersection(other)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:123 | Complexity: Intermediate | Last updated: 2026-06-02*