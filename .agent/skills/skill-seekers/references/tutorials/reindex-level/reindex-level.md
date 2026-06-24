# How To: Reindex Level

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex level

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: multiindex_year_month_day_dataframe_random_data
```

## Step-by-Step Guide

### Step 1: Assign ymd = multiindex_year_month_day_dataframe_random_data

```python
ymd = multiindex_year_month_day_dataframe_random_data
```

### Step 2: Assign month_sums = ymd.groupby.sum(...)

```python
month_sums = ymd.groupby('month').sum()
```

### Step 3: Assign result = month_sums.reindex(...)

```python
result = month_sums.reindex(ymd.index, level=1)
```

### Step 4: Assign expected = ymd.groupby.transform(...)

```python
expected = ymd.groupby(level='month').transform('sum')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = unknown.reindex(...)

```python
result = month_sums['A'].reindex(ymd.index, level=1)
```

### Step 7: Assign expected = unknown.groupby.transform(...)

```python
expected = ymd['A'].groupby(level='month').transform('sum')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected, check_names=False)
```

### Step 9: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 10: Assign month_sums = gb.sum(...)

```python
month_sums = gb.sum()
```

### Step 11: Assign result = month_sums.reindex(...)

```python
result = month_sums.reindex(columns=ymd.index, level=1)
```

### Step 12: Assign expected = value

```python
expected = ymd.groupby(level='month').transform('sum').T
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign gb = ymd.T.groupby(...)

```python
gb = ymd.T.groupby('month', axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_year_month_day_dataframe_random_data

# Workflow
ymd = multiindex_year_month_day_dataframe_random_data
month_sums = ymd.groupby('month').sum()
result = month_sums.reindex(ymd.index, level=1)
expected = ymd.groupby(level='month').transform('sum')
tm.assert_frame_equal(result, expected)
result = month_sums['A'].reindex(ymd.index, level=1)
expected = ymd['A'].groupby(level='month').transform('sum')
tm.assert_series_equal(result, expected, check_names=False)
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    gb = ymd.T.groupby('month', axis=1)
month_sums = gb.sum()
result = month_sums.reindex(columns=ymd.index, level=1)
expected = ymd.groupby(level='month').transform('sum').T
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_multilevel.py:16 | Complexity: Advanced | Last updated: 2026-06-02*