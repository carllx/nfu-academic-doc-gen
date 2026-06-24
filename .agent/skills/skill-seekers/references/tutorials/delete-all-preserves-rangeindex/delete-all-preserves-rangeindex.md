# How To: Delete All Preserves Rangeindex

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test delete all preserves rangeindex

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
loc = [0, 1, 2, 3, 4, 5]
```

### Step 3: Assign result = idx.delete(...)

```python
result = idx.delete(loc)
```

### Step 4: Assign expected = value

```python
expected = idx[:0]
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
loc = [0, 1, 2, 3, 4, 5]
result = idx.delete(loc)
expected = idx[:0]
tm.assert_index_equal(result, expected, exact=True)
result = idx.delete(loc[::-1])
tm.assert_index_equal(result, expected, exact=True)
```

## Next Steps


---

*Source: test_range.py:172 | Complexity: Intermediate | Last updated: 2026-06-02*