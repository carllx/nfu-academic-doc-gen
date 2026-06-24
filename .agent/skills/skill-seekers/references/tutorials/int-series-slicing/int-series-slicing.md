# How To: Int Series Slicing

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test int series slicing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`

**Setup Required:**
```python
# Fixtures: multiindex_year_month_day_dataframe_random_data
```

## Step-by-Step Guide

### Step 1: Assign ymd = multiindex_year_month_day_dataframe_random_data

```python
ymd = multiindex_year_month_day_dataframe_random_data
```

### Step 2: Assign s = value

```python
s = ymd['A']
```

### Step 3: Assign result = value

```python
result = s[5:]
```

### Step 4: Assign expected = s.reindex(...)

```python
expected = s.reindex(s.index[5:])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign s = unknown.copy(...)

```python
s = ymd['A'].copy()
```

### Step 7: Assign exp = unknown.copy(...)

```python
exp = ymd['A'].copy()
```

### Step 8: Assign unknown = 0

```python
s[5:] = 0
```

### Step 9: Assign unknown = 0

```python
exp.iloc[5:] = 0
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(s.values, exp.values)
```

### Step 11: Assign result = value

```python
result = ymd[5:]
```

### Step 12: Assign expected = ymd.reindex(...)

```python
expected = ymd.reindex(s.index[5:])
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_year_month_day_dataframe_random_data

# Workflow
ymd = multiindex_year_month_day_dataframe_random_data
s = ymd['A']
result = s[5:]
expected = s.reindex(s.index[5:])
tm.assert_series_equal(result, expected)
s = ymd['A'].copy()
exp = ymd['A'].copy()
s[5:] = 0
exp.iloc[5:] = 0
tm.assert_numpy_array_equal(s.values, exp.values)
result = ymd[5:]
expected = ymd.reindex(s.index[5:])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_slice.py:735 | Complexity: Advanced | Last updated: 2026-06-02*