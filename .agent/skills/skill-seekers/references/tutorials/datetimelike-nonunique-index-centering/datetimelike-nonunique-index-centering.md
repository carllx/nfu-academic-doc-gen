# How To: Datetimelike Nonunique Index Centering

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test datetimelike nonunique index centering

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.indexers.objects`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: window, closed, expected, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign index = DatetimeIndex(...)

```python
index = DatetimeIndex(['2020-01-01', '2020-01-01', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03', '2020-01-04', '2020-01-04'])
```

### Step 2: Assign df = frame_or_series(...)

```python
df = frame_or_series([1] * 8, index=index, dtype=float)
```

### Step 3: Assign expected = frame_or_series(...)

```python
expected = frame_or_series(expected, index=index, dtype=float)
```

### Step 4: Assign result = df.rolling.sum(...)

```python
result = df.rolling(window, center=True, closed=closed).sum()
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: window, closed, expected, frame_or_series

# Workflow
index = DatetimeIndex(['2020-01-01', '2020-01-01', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-03', '2020-01-04', '2020-01-04'])
df = frame_or_series([1] * 8, index=index, dtype=float)
expected = frame_or_series(expected, index=index, dtype=float)
result = df.rolling(window, center=True, closed=closed).sum()
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_rolling.py:283 | Complexity: Intermediate | Last updated: 2026-06-02*