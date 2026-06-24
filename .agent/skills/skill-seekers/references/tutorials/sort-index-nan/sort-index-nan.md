# How To: Sort Index Nan

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, np.nan, 1, 6, 8, 4], 'B': [9, np.nan, 5, 2, 5, 4, 5]}, index=[1, 2, 3, 4, 5, 6, np.nan])
```

### Step 2: Assign sorted_df = df.sort_index(...)

```python
sorted_df = df.sort_index(kind='quicksort', ascending=True, na_position='last')
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [1, 2, np.nan, 1, 6, 8, 4], 'B': [9, np.nan, 5, 2, 5, 4, 5]}, index=[1, 2, 3, 4, 5, 6, np.nan])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```

### Step 5: Assign sorted_df = df.sort_index(...)

```python
sorted_df = df.sort_index(na_position='first')
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [4, 1, 2, np.nan, 1, 6, 8], 'B': [5, 9, np.nan, 5, 2, 5, 4]}, index=[np.nan, 1, 2, 3, 4, 5, 6])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```

### Step 8: Assign sorted_df = df.sort_index(...)

```python
sorted_df = df.sort_index(kind='quicksort', ascending=False)
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [8, 6, 1, np.nan, 2, 1, 4], 'B': [4, 5, 2, 5, np.nan, 9, 5]}, index=[6, 5, 4, 3, 2, 1, np.nan])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```

### Step 11: Assign sorted_df = df.sort_index(...)

```python
sorted_df = df.sort_index(kind='quicksort', ascending=False, na_position='first')
```

### Step 12: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [4, 8, 6, 1, np.nan, 2, 1], 'B': [5, 4, 5, 2, 5, np.nan, 9]}, index=[np.nan, 6, 5, 4, 3, 2, 1])
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [1, 2, np.nan, 1, 6, 8, 4], 'B': [9, np.nan, 5, 2, 5, 4, 5]}, index=[1, 2, 3, 4, 5, 6, np.nan])
sorted_df = df.sort_index(kind='quicksort', ascending=True, na_position='last')
expected = DataFrame({'A': [1, 2, np.nan, 1, 6, 8, 4], 'B': [9, np.nan, 5, 2, 5, 4, 5]}, index=[1, 2, 3, 4, 5, 6, np.nan])
tm.assert_frame_equal(sorted_df, expected)
sorted_df = df.sort_index(na_position='first')
expected = DataFrame({'A': [4, 1, 2, np.nan, 1, 6, 8], 'B': [5, 9, np.nan, 5, 2, 5, 4]}, index=[np.nan, 1, 2, 3, 4, 5, 6])
tm.assert_frame_equal(sorted_df, expected)
sorted_df = df.sort_index(kind='quicksort', ascending=False)
expected = DataFrame({'A': [8, 6, 1, np.nan, 2, 1, 4], 'B': [4, 5, 2, 5, np.nan, 9, 5]}, index=[6, 5, 4, 3, 2, 1, np.nan])
tm.assert_frame_equal(sorted_df, expected)
sorted_df = df.sort_index(kind='quicksort', ascending=False, na_position='first')
expected = DataFrame({'A': [4, 8, 6, 1, np.nan, 2, 1], 'B': [5, 4, 5, 2, 5, np.nan, 9]}, index=[np.nan, 6, 5, 4, 3, 2, 1])
tm.assert_frame_equal(sorted_df, expected)
```

## Next Steps


---

*Source: test_sort_index.py:161 | Complexity: Advanced | Last updated: 2026-06-02*