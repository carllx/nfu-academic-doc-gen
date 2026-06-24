# How To: To Datetime Format Yyyymmdd

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to datetime format YYYYMMDD

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: cache
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([19801222, 19801222] + [19810105] * 5)
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([Timestamp(x) for x in ser.apply(str)])
```

### Step 3: Assign result = to_datetime(...)

```python
result = to_datetime(ser, format='%Y%m%d', cache=cache)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = to_datetime(...)

```python
result = to_datetime(ser.apply(str), format='%Y%m%d', cache=cache)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: cache

# Workflow
ser = Series([19801222, 19801222] + [19810105] * 5)
expected = Series([Timestamp(x) for x in ser.apply(str)])
result = to_datetime(ser, format='%Y%m%d', cache=cache)
tm.assert_series_equal(result, expected)
result = to_datetime(ser.apply(str), format='%Y%m%d', cache=cache)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_to_datetime.py:131 | Complexity: Intermediate | Last updated: 2026-06-02*