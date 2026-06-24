# How To: Datetimelike Centered Offset Covers All

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test datetimelike centered offset covers all

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

### Step 1: Assign index = value

```python
index = [Timestamp('20130101 09:00:01'), Timestamp('20130101 09:00:02'), Timestamp('20130101 09:00:02')]
```

### Step 2: Assign df = frame_or_series(...)

```python
df = frame_or_series([1, 1, 1], index=index)
```

### Step 3: Assign result = df.rolling.sum(...)

```python
result = df.rolling(window, closed=closed, center=True).sum()
```

### Step 4: Assign expected = frame_or_series(...)

```python
expected = frame_or_series(expected, index=index)
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
index = [Timestamp('20130101 09:00:01'), Timestamp('20130101 09:00:02'), Timestamp('20130101 09:00:02')]
df = frame_or_series([1, 1, 1], index=index)
result = df.rolling(window, closed=closed, center=True).sum()
expected = frame_or_series(expected, index=index)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_rolling.py:257 | Complexity: Intermediate | Last updated: 2026-06-02*