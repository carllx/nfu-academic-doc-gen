# How To: Constructor With Ambiguous Keyword Arg

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor with ambiguous keyword arg

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

### Step 1: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['2020-11-01 01:00:00', '2020-11-02 01:00:00'], dtype='datetime64[ns, America/New_York]', freq='D', ambiguous=False)
```

### Step 2: Assign timezone = 'America/New_York'

```python
timezone = 'America/New_York'
```

### Step 3: Assign start = Timestamp.tz_localize(...)

```python
start = Timestamp(year=2020, month=11, day=1, hour=1).tz_localize(timezone, ambiguous=False)
```

### Step 4: Assign result = date_range(...)

```python
result = date_range(start=start, periods=2, ambiguous=False)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign timezone = 'America/New_York'

```python
timezone = 'America/New_York'
```

### Step 7: Assign end = Timestamp.tz_localize(...)

```python
end = Timestamp(year=2020, month=11, day=2, hour=1).tz_localize(timezone, ambiguous=False)
```

### Step 8: Assign result = date_range(...)

```python
result = date_range(end=end, periods=2, ambiguous=False)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
expected = DatetimeIndex(['2020-11-01 01:00:00', '2020-11-02 01:00:00'], dtype='datetime64[ns, America/New_York]', freq='D', ambiguous=False)
timezone = 'America/New_York'
start = Timestamp(year=2020, month=11, day=1, hour=1).tz_localize(timezone, ambiguous=False)
result = date_range(start=start, periods=2, ambiguous=False)
tm.assert_index_equal(result, expected)
timezone = 'America/New_York'
end = Timestamp(year=2020, month=11, day=2, hour=1).tz_localize(timezone, ambiguous=False)
result = date_range(end=end, periods=2, ambiguous=False)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:858 | Complexity: Advanced | Last updated: 2026-06-02*