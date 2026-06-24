# How To: Safe Sort Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test safe sort multiindex

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.common`
- `pandas.core.sorting`


## Step-by-Step Guide

### Step 1: Assign arr1 = Series(...)

```python
arr1 = Series([2, 1, NA, NA], dtype='Int64')
```

### Step 2: Assign arr2 = value

```python
arr2 = [2, 1, 3, 3]
```

### Step 3: Assign midx = MultiIndex.from_arrays(...)

```python
midx = MultiIndex.from_arrays([arr1, arr2])
```

### Step 4: Assign result = safe_sort(...)

```python
result = safe_sort(midx)
```

### Step 5: Assign expected = MultiIndex.from_arrays(...)

```python
expected = MultiIndex.from_arrays([Series([1, 2, NA, NA], dtype='Int64'), [1, 2, 3, 3]])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr1 = Series([2, 1, NA, NA], dtype='Int64')
arr2 = [2, 1, 3, 3]
midx = MultiIndex.from_arrays([arr1, arr2])
result = safe_sort(midx)
expected = MultiIndex.from_arrays([Series([1, 2, NA, NA], dtype='Int64'), [1, 2, 3, 3]])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_sorting.py:478 | Complexity: Intermediate | Last updated: 2026-06-02*