# How To: Groupby Multilevel

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby multilevel

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

**Verification:**
```python
assert result.index.names == ymd.index.names[:2]
```

### Step 2: Assign result = ymd.groupby.mean(...)

```python
result = ymd.groupby(level=[0, 1]).mean()
```

### Step 3: Assign k1 = ymd.index.get_level_values(...)

```python
k1 = ymd.index.get_level_values(0)
```

### Step 4: Assign k2 = ymd.index.get_level_values(...)

```python
k2 = ymd.index.get_level_values(1)
```

### Step 5: Assign expected = ymd.groupby.mean(...)

```python
expected = ymd.groupby([k1, k2]).mean()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_names=False)
```

**Verification:**
```python
assert result.index.names == ymd.index.names[:2]
```

### Step 7: Assign result2 = ymd.groupby.mean(...)

```python
result2 = ymd.groupby(level=ymd.index.names[:2]).mean()
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, result2)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_year_month_day_dataframe_random_data

# Workflow
ymd = multiindex_year_month_day_dataframe_random_data
result = ymd.groupby(level=[0, 1]).mean()
k1 = ymd.index.get_level_values(0)
k2 = ymd.index.get_level_values(1)
expected = ymd.groupby([k1, k2]).mean()
tm.assert_frame_equal(result, expected, check_names=False)
assert result.index.names == ymd.index.names[:2]
result2 = ymd.groupby(level=ymd.index.names[:2]).mean()
tm.assert_frame_equal(result, result2)
```

## Next Steps


---

*Source: test_multilevel.py:151 | Complexity: Advanced | Last updated: 2026-06-02*