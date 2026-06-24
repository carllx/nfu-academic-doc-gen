# How To: Basic Getitem With Labels

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basic getitem with labels

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign indices = value

```python
indices = datetime_series.index[[5, 10, 15]]
```

### Step 2: Assign result = value

```python
result = datetime_series[indices]
```

### Step 3: Assign expected = datetime_series.reindex(...)

```python
expected = datetime_series.reindex(indices)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = datetime_series[indices[0]:indices[2]]
```

### Step 6: Assign expected = value

```python
expected = datetime_series.loc[indices[0]:indices[2]]
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
indices = datetime_series.index[[5, 10, 15]]
result = datetime_series[indices]
expected = datetime_series.reindex(indices)
tm.assert_series_equal(result, expected)
result = datetime_series[indices[0]:indices[2]]
expected = datetime_series.loc[indices[0]:indices[2]]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:78 | Complexity: Intermediate | Last updated: 2026-06-02*