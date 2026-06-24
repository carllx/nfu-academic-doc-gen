# How To: Series Getitem

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series getitem

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`

**Setup Required:**
```python
# Fixtures: multiindex_year_month_day_dataframe_random_data, indexer_sl
```

## Step-by-Step Guide

### Step 1: Assign s = value

```python
s = multiindex_year_month_day_dataframe_random_data['A']
```

### Step 2: Assign expected = s.reindex(...)

```python
expected = s.reindex(s.index[42:65])
```

### Step 3: Assign expected.index = expected.index.droplevel.droplevel(...)

```python
expected.index = expected.index.droplevel(0).droplevel(0)
```

### Step 4: Assign result = value

```python
result = indexer_sl(s)[2000, 3]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_year_month_day_dataframe_random_data, indexer_sl

# Workflow
s = multiindex_year_month_day_dataframe_random_data['A']
expected = s.reindex(s.index[42:65])
expected.index = expected.index.droplevel(0).droplevel(0)
result = indexer_sl(s)[2000, 3]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:66 | Complexity: Intermediate | Last updated: 2026-06-02*