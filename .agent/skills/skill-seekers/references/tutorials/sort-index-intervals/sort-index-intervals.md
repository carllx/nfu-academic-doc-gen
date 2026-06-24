# How To: Sort Index Intervals

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index intervals

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([np.nan, 1, 2, 3], IntervalIndex.from_arrays([0, 1, 2, 3], [1, 2, 3, 4]))
```

### Step 2: Assign result = s.sort_index(...)

```python
result = s.sort_index()
```

### Step 3: Assign expected = s

```python
expected = s
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = s.sort_index(...)

```python
result = s.sort_index(ascending=False)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([3, 2, 1, np.nan], IntervalIndex.from_arrays([3, 2, 1, 0], [4, 3, 2, 1]))
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Series([np.nan, 1, 2, 3], IntervalIndex.from_arrays([0, 1, 2, 3], [1, 2, 3, 4]))
result = s.sort_index()
expected = s
tm.assert_series_equal(result, expected)
result = s.sort_index(ascending=False)
expected = Series([3, 2, 1, np.nan], IntervalIndex.from_arrays([3, 2, 1, 0], [4, 3, 2, 1]))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_sort_index.py:134 | Complexity: Intermediate | Last updated: 2026-06-02*