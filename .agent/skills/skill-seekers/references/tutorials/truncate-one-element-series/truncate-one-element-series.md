# How To: Truncate One Element Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test truncate one element series

## Prerequisites

**Required Modules:**
- `datetime`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign series = Series(...)

```python
series = Series([0.1], index=pd.DatetimeIndex(['2020-08-04']))
```

### Step 2: Assign before = pd.Timestamp(...)

```python
before = pd.Timestamp('2020-08-02')
```

### Step 3: Assign after = pd.Timestamp(...)

```python
after = pd.Timestamp('2020-08-04')
```

### Step 4: Assign result = series.truncate(...)

```python
result = series.truncate(before=before, after=after)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, series)
```


## Complete Example

```python
# Workflow
series = Series([0.1], index=pd.DatetimeIndex(['2020-08-04']))
before = pd.Timestamp('2020-08-02')
after = pd.Timestamp('2020-08-04')
result = series.truncate(before=before, after=after)
tm.assert_series_equal(result, series)
```

## Next Steps


---

*Source: test_truncate.py:50 | Complexity: Intermediate | Last updated: 2026-06-02*