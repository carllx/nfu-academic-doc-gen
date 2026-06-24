# How To: To Datetime Mixed Types Matching Tzs

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to datetime mixed types matching tzs

## Prerequisites

**Required Modules:**
- `calendar`
- `collections`
- `datetime`
- `decimal`
- `locale`
- `dateutil.parser`
- `dateutil.tz.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.tools`
- `pandas.core.tools.datetimes`
- `pandas.tests.indexes.datetimes.test_timezones`


## Step-by-Step Guide

### Step 1: Assign dtstr = '2023-11-01 09:22:03-07:00'

```python
dtstr = '2023-11-01 09:22:03-07:00'
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp(dtstr)
```

### Step 3: Assign arr = value

```python
arr = [ts, dtstr]
```

### Step 4: Assign res1 = to_datetime(...)

```python
res1 = to_datetime(arr)
```

### Step 5: Assign res2 = value

```python
res2 = to_datetime(arr[::-1])[::-1]
```

### Step 6: Assign res3 = to_datetime(...)

```python
res3 = to_datetime(arr, format='mixed')
```

### Step 7: Assign res4 = DatetimeIndex(...)

```python
res4 = DatetimeIndex(arr)
```

### Step 8: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([ts, ts])
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res1, expected)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res2, expected)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res3, expected)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res4, expected)
```


## Complete Example

```python
# Workflow
dtstr = '2023-11-01 09:22:03-07:00'
ts = Timestamp(dtstr)
arr = [ts, dtstr]
res1 = to_datetime(arr)
res2 = to_datetime(arr[::-1])[::-1]
res3 = to_datetime(arr, format='mixed')
res4 = DatetimeIndex(arr)
expected = DatetimeIndex([ts, ts])
tm.assert_index_equal(res1, expected)
tm.assert_index_equal(res2, expected)
tm.assert_index_equal(res3, expected)
tm.assert_index_equal(res4, expected)
```

## Next Steps


---

*Source: test_to_datetime.py:3810 | Complexity: Advanced | Last updated: 2026-06-02*