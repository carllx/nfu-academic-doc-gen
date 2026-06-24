# How To: Sort Index Nan Multiindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index nan multiindex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign tuples = value

```python
tuples = [[12, 13], [np.nan, np.nan], [np.nan, 3], [1, 2]]
```

### Step 2: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples(tuples)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(16).reshape(4, 4), index=mi, columns=list('ABCD'))
```

### Step 4: Assign s = Series(...)

```python
s = Series(np.arange(4), index=mi)
```

### Step 5: Assign df2 = DataFrame.set_index(...)

```python
df2 = DataFrame({'date': pd.DatetimeIndex(['20121002', '20121007', '20130130', '20130202', '20130305', '20121002', '20121207', '20130130', '20130202', '20130305', '20130202', '20130305']), 'user_id': [1, 1, 1, 1, 1, 3, 3, 3, 5, 5, 5, 5], 'whole_cost': [1790, np.nan, 280, 259, np.nan, 623, 90, 312, np.nan, 301, 359, 801], 'cost': [12, 15, 10, 24, 39, 1, 0, np.nan, 45, 34, 1, 12]}).set_index(['date', 'user_id'])
```

### Step 6: Assign result = df.sort_index(...)

```python
result = df.sort_index()
```

### Step 7: Assign expected = value

```python
expected = df.iloc[[3, 0, 2, 1], :]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = df.sort_index(...)

```python
result = df.sort_index(na_position='last')
```

### Step 10: Assign expected = value

```python
expected = df.iloc[[3, 0, 2, 1], :]
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Assign result = df.sort_index(...)

```python
result = df.sort_index(na_position='first')
```

### Step 13: Assign expected = value

```python
expected = df.iloc[[1, 2, 3, 0], :]
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 15: Assign result = df2.dropna.sort_index(...)

```python
result = df2.dropna().sort_index()
```

### Step 16: Assign expected = df2.sort_index.dropna(...)

```python
expected = df2.sort_index().dropna()
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 18: Assign result = s.sort_index(...)

```python
result = s.sort_index()
```

### Step 19: Assign expected = value

```python
expected = s.iloc[[3, 0, 2, 1]]
```

### Step 20: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 21: Assign result = s.sort_index(...)

```python
result = s.sort_index(na_position='last')
```

### Step 22: Assign expected = value

```python
expected = s.iloc[[3, 0, 2, 1]]
```

### Step 23: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 24: Assign result = s.sort_index(...)

```python
result = s.sort_index(na_position='first')
```

### Step 25: Assign expected = value

```python
expected = s.iloc[[1, 2, 3, 0]]
```

### Step 26: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
tuples = [[12, 13], [np.nan, np.nan], [np.nan, 3], [1, 2]]
mi = MultiIndex.from_tuples(tuples)
df = DataFrame(np.arange(16).reshape(4, 4), index=mi, columns=list('ABCD'))
s = Series(np.arange(4), index=mi)
df2 = DataFrame({'date': pd.DatetimeIndex(['20121002', '20121007', '20130130', '20130202', '20130305', '20121002', '20121207', '20130130', '20130202', '20130305', '20130202', '20130305']), 'user_id': [1, 1, 1, 1, 1, 3, 3, 3, 5, 5, 5, 5], 'whole_cost': [1790, np.nan, 280, 259, np.nan, 623, 90, 312, np.nan, 301, 359, 801], 'cost': [12, 15, 10, 24, 39, 1, 0, np.nan, 45, 34, 1, 12]}).set_index(['date', 'user_id'])
result = df.sort_index()
expected = df.iloc[[3, 0, 2, 1], :]
tm.assert_frame_equal(result, expected)
result = df.sort_index(na_position='last')
expected = df.iloc[[3, 0, 2, 1], :]
tm.assert_frame_equal(result, expected)
result = df.sort_index(na_position='first')
expected = df.iloc[[1, 2, 3, 0], :]
tm.assert_frame_equal(result, expected)
result = df2.dropna().sort_index()
expected = df2.sort_index().dropna()
tm.assert_frame_equal(result, expected)
result = s.sort_index()
expected = s.iloc[[3, 0, 2, 1]]
tm.assert_series_equal(result, expected)
result = s.sort_index(na_position='last')
expected = s.iloc[[3, 0, 2, 1]]
tm.assert_series_equal(result, expected)
result = s.sort_index(na_position='first')
expected = s.iloc[[1, 2, 3, 0]]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_sort_index.py:80 | Complexity: Advanced | Last updated: 2026-06-02*