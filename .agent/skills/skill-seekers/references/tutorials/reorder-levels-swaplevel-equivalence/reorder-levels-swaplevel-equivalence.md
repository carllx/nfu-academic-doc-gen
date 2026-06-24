# How To: Reorder Levels Swaplevel Equivalence

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reorder levels swaplevel equivalence

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
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

### Step 2: Assign result = ymd.reorder_levels(...)

```python
result = ymd.reorder_levels(['month', 'day', 'year'])
```

### Step 3: Assign expected = ymd.swaplevel.swaplevel(...)

```python
expected = ymd.swaplevel(0, 1).swaplevel(1, 2)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = unknown.reorder_levels(...)

```python
result = ymd['A'].reorder_levels(['month', 'day', 'year'])
```

### Step 6: Assign expected = unknown.swaplevel.swaplevel(...)

```python
expected = ymd['A'].swaplevel(0, 1).swaplevel(1, 2)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = ymd.T.reorder_levels(...)

```python
result = ymd.T.reorder_levels(['month', 'day', 'year'], axis=1)
```

### Step 9: Assign expected = ymd.T.swaplevel.swaplevel(...)

```python
expected = ymd.T.swaplevel(0, 1, axis=1).swaplevel(1, 2, axis=1)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Call ymd.reorder_levels()

```python
ymd.reorder_levels([1, 2], axis=1)
```

### Step 12: Call ymd.index.reorder_levels()

```python
ymd.index.reorder_levels([1, 2, 3])
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_year_month_day_dataframe_random_data

# Workflow
ymd = multiindex_year_month_day_dataframe_random_data
result = ymd.reorder_levels(['month', 'day', 'year'])
expected = ymd.swaplevel(0, 1).swaplevel(1, 2)
tm.assert_frame_equal(result, expected)
result = ymd['A'].reorder_levels(['month', 'day', 'year'])
expected = ymd['A'].swaplevel(0, 1).swaplevel(1, 2)
tm.assert_series_equal(result, expected)
result = ymd.T.reorder_levels(['month', 'day', 'year'], axis=1)
expected = ymd.T.swaplevel(0, 1, axis=1).swaplevel(1, 2, axis=1)
tm.assert_frame_equal(result, expected)
with pytest.raises(TypeError, match='hierarchical axis'):
    ymd.reorder_levels([1, 2], axis=1)
with pytest.raises(IndexError, match='Too many levels'):
    ymd.index.reorder_levels([1, 2, 3])
```

## Next Steps


---

*Source: test_reorder_levels.py:53 | Complexity: Advanced | Last updated: 2026-06-02*