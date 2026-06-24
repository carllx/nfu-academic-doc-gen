# How To: Construction With Ndarray

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construction with ndarray

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `functools`
- `operator`
- `dateutil`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign dates = value

```python
dates = [datetime(2013, 10, 7), datetime(2013, 10, 8), datetime(2013, 10, 9)]
```

### Step 2: Assign data = value

```python
data = DatetimeIndex(dates, freq=offsets.BDay()).values
```

### Step 3: Assign result = DatetimeIndex(...)

```python
result = DatetimeIndex(data, freq=offsets.BDay())
```

### Step 4: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['2013-10-07', '2013-10-08', '2013-10-09'], freq='B')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
dates = [datetime(2013, 10, 7), datetime(2013, 10, 8), datetime(2013, 10, 9)]
data = DatetimeIndex(dates, freq=offsets.BDay()).values
result = DatetimeIndex(data, freq=offsets.BDay())
expected = DatetimeIndex(['2013-10-07', '2013-10-08', '2013-10-09'], freq='B')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:577 | Complexity: Intermediate | Last updated: 2026-06-02*