# How To: Sort Values Nan

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, np.nan, 1, 6, 8, 4], 'B': [9, np.nan, 5, 2, 5, 4, 5]})
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [np.nan, 1, 1, 2, 4, 6, 8], 'B': [5, 9, 2, np.nan, 5, 5, 4]}, index=[2, 0, 3, 1, 6, 4, 5])
```

### Step 3: Assign sorted_df = df.sort_values(...)

```python
sorted_df = df.sort_values(['A'], na_position='first')
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [np.nan, 8, 6, 4, 2, 1, 1], 'B': [5, 4, 5, 5, np.nan, 9, 2]}, index=[2, 5, 4, 6, 1, 0, 3])
```

### Step 6: Assign sorted_df = df.sort_values(...)

```python
sorted_df = df.sort_values(['A'], na_position='first', ascending=False)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```

### Step 8: Assign expected = df.reindex(...)

```python
expected = df.reindex(columns=['B', 'A'])
```

### Step 9: Assign sorted_df = df.sort_values(...)

```python
sorted_df = df.sort_values(by=1, axis=1, na_position='first')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [1, 1, 2, 4, 6, 8, np.nan], 'B': [2, 9, np.nan, 5, 5, 4, 5]}, index=[3, 0, 1, 6, 4, 5, 2])
```

### Step 12: Assign sorted_df = df.sort_values(...)

```python
sorted_df = df.sort_values(['A', 'B'])
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```

### Step 14: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [np.nan, 1, 1, 2, 4, 6, 8], 'B': [5, 2, 9, np.nan, 5, 5, 4]}, index=[2, 3, 0, 1, 6, 4, 5])
```

### Step 15: Assign sorted_df = df.sort_values(...)

```python
sorted_df = df.sort_values(['A', 'B'], na_position='first')
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```

### Step 17: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [np.nan, 1, 1, 2, 4, 6, 8], 'B': [5, 9, 2, np.nan, 5, 5, 4]}, index=[2, 0, 3, 1, 6, 4, 5])
```

### Step 18: Assign sorted_df = df.sort_values(...)

```python
sorted_df = df.sort_values(['A', 'B'], ascending=[1, 0], na_position='first')
```

### Step 19: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```

### Step 20: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [8, 6, 4, 2, 1, 1, np.nan], 'B': [4, 5, 5, np.nan, 2, 9, 5]}, index=[5, 4, 6, 1, 3, 0, 2])
```

### Step 21: Assign sorted_df = df.sort_values(...)

```python
sorted_df = df.sort_values(['A', 'B'], ascending=[0, 1], na_position='last')
```

### Step 22: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(sorted_df, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [1, 2, np.nan, 1, 6, 8, 4], 'B': [9, np.nan, 5, 2, 5, 4, 5]})
expected = DataFrame({'A': [np.nan, 1, 1, 2, 4, 6, 8], 'B': [5, 9, 2, np.nan, 5, 5, 4]}, index=[2, 0, 3, 1, 6, 4, 5])
sorted_df = df.sort_values(['A'], na_position='first')
tm.assert_frame_equal(sorted_df, expected)
expected = DataFrame({'A': [np.nan, 8, 6, 4, 2, 1, 1], 'B': [5, 4, 5, 5, np.nan, 9, 2]}, index=[2, 5, 4, 6, 1, 0, 3])
sorted_df = df.sort_values(['A'], na_position='first', ascending=False)
tm.assert_frame_equal(sorted_df, expected)
expected = df.reindex(columns=['B', 'A'])
sorted_df = df.sort_values(by=1, axis=1, na_position='first')
tm.assert_frame_equal(sorted_df, expected)
expected = DataFrame({'A': [1, 1, 2, 4, 6, 8, np.nan], 'B': [2, 9, np.nan, 5, 5, 4, 5]}, index=[3, 0, 1, 6, 4, 5, 2])
sorted_df = df.sort_values(['A', 'B'])
tm.assert_frame_equal(sorted_df, expected)
expected = DataFrame({'A': [np.nan, 1, 1, 2, 4, 6, 8], 'B': [5, 2, 9, np.nan, 5, 5, 4]}, index=[2, 3, 0, 1, 6, 4, 5])
sorted_df = df.sort_values(['A', 'B'], na_position='first')
tm.assert_frame_equal(sorted_df, expected)
expected = DataFrame({'A': [np.nan, 1, 1, 2, 4, 6, 8], 'B': [5, 9, 2, np.nan, 5, 5, 4]}, index=[2, 0, 3, 1, 6, 4, 5])
sorted_df = df.sort_values(['A', 'B'], ascending=[1, 0], na_position='first')
tm.assert_frame_equal(sorted_df, expected)
expected = DataFrame({'A': [8, 6, 4, 2, 1, 1, np.nan], 'B': [4, 5, 5, np.nan, 2, 9, 5]}, index=[5, 4, 6, 1, 3, 0, 2])
sorted_df = df.sort_values(['A', 'B'], ascending=[0, 1], na_position='last')
tm.assert_frame_equal(sorted_df, expected)
```

## Next Steps


---

*Source: test_sort_values.py:178 | Complexity: Advanced | Last updated: 2026-06-02*