# How To: Getitem Partial

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem partial

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
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

### Step 2: Assign ymd = value

```python
ymd = ymd.T
```

### Step 3: Assign result = value

```python
result = ymd[2000, 2]
```

### Step 4: Assign expected = ymd.reindex(...)

```python
expected = ymd.reindex(columns=ymd.columns[ymd.columns.codes[1] == 1])
```

### Step 5: Assign expected.columns = expected.columns.droplevel.droplevel(...)

```python
expected.columns = expected.columns.droplevel(0).droplevel(0)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_year_month_day_dataframe_random_data

# Workflow
ymd = multiindex_year_month_day_dataframe_random_data
ymd = ymd.T
result = ymd[2000, 2]
expected = ymd.reindex(columns=ymd.columns[ymd.columns.codes[1] == 1])
expected.columns = expected.columns.droplevel(0).droplevel(0)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_partial.py:78 | Complexity: Intermediate | Last updated: 2026-06-02*