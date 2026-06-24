# How To: Delete Preserves Rangeindex List Middle

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test delete preserves rangeindex list middle

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = RangeIndex(...)

```python
idx = RangeIndex(0, 6, 1)
```

### Step 2: Assign loc = value

```python
loc = [1, 2, 3, 4]
```

### Step 3: Assign result = idx.delete(...)

```python
result = idx.delete(loc)
```

### Step 4: Assign expected = RangeIndex(...)

```python
expected = RangeIndex(0, 6, 5)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 6: Assign result = idx.delete(...)

```python
result = idx.delete(loc[::-1])
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```


## Complete Example

```python
# Workflow
idx = RangeIndex(0, 6, 1)
loc = [1, 2, 3, 4]
result = idx.delete(loc)
expected = RangeIndex(0, 6, 5)
tm.assert_index_equal(result, expected, exact=True)
result = idx.delete(loc[::-1])
tm.assert_index_equal(result, expected, exact=True)
```

## Next Steps


---

*Source: test_range.py:161 | Complexity: Intermediate | Last updated: 2026-06-02*