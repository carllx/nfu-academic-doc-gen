# How To: Grouper Index Level As String Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test grouper index level as string series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: series, levels
```

## Step-by-Step Guide

### Step 1: Assign expected = series.groupby.mean(...)

```python
expected = series.groupby(groupers).mean()
```

### Step 2: Assign result = series.groupby.mean(...)

```python
result = series.groupby(levels).mean()
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 4: Assign groupers = value

```python
groupers = [pd.Grouper(level=lv) for lv in levels]
```

### Step 5: Assign groupers = pd.Grouper(...)

```python
groupers = pd.Grouper(level=levels)
```


## Complete Example

```python
# Setup
# Fixtures: series, levels

# Workflow
if isinstance(levels, list):
    groupers = [pd.Grouper(level=lv) for lv in levels]
else:
    groupers = pd.Grouper(level=levels)
expected = series.groupby(groupers).mean()
result = series.groupby(levels).mean()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_index_as_string.py:74 | Complexity: Intermediate | Last updated: 2026-06-02*