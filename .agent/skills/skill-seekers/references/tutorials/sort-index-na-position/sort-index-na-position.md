# How To: Sort Index Na Position

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index na position

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign series = Series(...)

```python
series = Series(index=[3, 2, 1, 4, 3, np.nan], dtype=object)
```

### Step 2: Assign expected_series_first = Series(...)

```python
expected_series_first = Series(index=[np.nan, 1, 2, 3, 3, 4], dtype=object)
```

### Step 3: Assign index_sorted_series = series.sort_index(...)

```python
index_sorted_series = series.sort_index(na_position='first')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected_series_first, index_sorted_series)
```

### Step 5: Assign expected_series_last = Series(...)

```python
expected_series_last = Series(index=[1, 2, 3, 3, 4, np.nan], dtype=object)
```

### Step 6: Assign index_sorted_series = series.sort_index(...)

```python
index_sorted_series = series.sort_index(na_position='last')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected_series_last, index_sorted_series)
```


## Complete Example

```python
# Workflow
series = Series(index=[3, 2, 1, 4, 3, np.nan], dtype=object)
expected_series_first = Series(index=[np.nan, 1, 2, 3, 3, 4], dtype=object)
index_sorted_series = series.sort_index(na_position='first')
tm.assert_series_equal(expected_series_first, index_sorted_series)
expected_series_last = Series(index=[1, 2, 3, 3, 4, np.nan], dtype=object)
index_sorted_series = series.sort_index(na_position='last')
tm.assert_series_equal(expected_series_last, index_sorted_series)
```

## Next Steps


---

*Source: test_sort_index.py:122 | Complexity: Intermediate | Last updated: 2026-06-02*