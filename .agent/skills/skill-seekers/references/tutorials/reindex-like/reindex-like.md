# How To: Reindex Like

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex like

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign other = value

```python
other = datetime_series[::2]
```

### Step 2: Call tm.assert_series_equal()

```python
tm.assert_series_equal(datetime_series.reindex(other.index), datetime_series.reindex_like(other))
```

### Step 3: Assign day1 = datetime(...)

```python
day1 = datetime(2013, 3, 5)
```

### Step 4: Assign day2 = datetime(...)

```python
day2 = datetime(2013, 5, 5)
```

### Step 5: Assign day3 = datetime(...)

```python
day3 = datetime(2014, 3, 5)
```

### Step 6: Assign series1 = Series(...)

```python
series1 = Series([5, None, None], [day1, day2, day3])
```

### Step 7: Assign series2 = Series(...)

```python
series2 = Series([None, None], [day1, day3])
```

### Step 8: Assign result = series1.reindex_like(...)

```python
result = series1.reindex_like(series2, method='pad')
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([5, np.nan], index=[day1, day3])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
other = datetime_series[::2]
tm.assert_series_equal(datetime_series.reindex(other.index), datetime_series.reindex_like(other))
day1 = datetime(2013, 3, 5)
day2 = datetime(2013, 5, 5)
day3 = datetime(2014, 3, 5)
series1 = Series([5, None, None], [day1, day2, day3])
series2 = Series([None, None], [day1, day3])
result = series1.reindex_like(series2, method='pad')
expected = Series([5, np.nan], index=[day1, day3])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reindex_like.py:9 | Complexity: Advanced | Last updated: 2026-06-02*