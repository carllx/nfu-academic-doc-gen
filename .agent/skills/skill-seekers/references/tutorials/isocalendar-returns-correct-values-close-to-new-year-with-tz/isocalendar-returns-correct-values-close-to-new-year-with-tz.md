# How To: Isocalendar Returns Correct Values Close To New Year With Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isocalendar returns correct values close to new year with tz

## Prerequisites

**Required Modules:**
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dates = value

```python
dates = ['2013/12/29', '2013/12/30', '2013/12/31']
```

### Step 2: Assign dates = DatetimeIndex(...)

```python
dates = DatetimeIndex(dates, tz='Europe/Brussels')
```

### Step 3: Assign result = dates.isocalendar(...)

```python
result = dates.isocalendar()
```

### Step 4: Assign expected_data_frame = DataFrame(...)

```python
expected_data_frame = DataFrame([[2013, 52, 7], [2014, 1, 1], [2014, 1, 2]], columns=['year', 'week', 'day'], index=dates, dtype='UInt32')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected_data_frame)
```


## Complete Example

```python
# Workflow
dates = ['2013/12/29', '2013/12/30', '2013/12/31']
dates = DatetimeIndex(dates, tz='Europe/Brussels')
result = dates.isocalendar()
expected_data_frame = DataFrame([[2013, 52, 7], [2014, 1, 1], [2014, 1, 2]], columns=['year', 'week', 'day'], index=dates, dtype='UInt32')
tm.assert_frame_equal(result, expected_data_frame)
```

## Next Steps


---

*Source: test_isocalendar.py:9 | Complexity: Intermediate | Last updated: 2026-06-02*