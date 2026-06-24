# How To: To Datetime Format Integer

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to datetime format integer

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
ser = Series([2000, 2001, 2002])
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([Timestamp(x) for x in ser.apply(str)])
```

### Step 3: Assign result = to_datetime(...)

```python
result = to_datetime(ser, format='%Y', cache=cache)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign ser = Series(...)

```python
ser = Series([200001, 200105, 200206])
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([Timestamp(x[:4] + '-' + x[4:]) for x in ser.apply(str)])
```

### Step 7: Assign result = to_datetime(...)

```python
result = to_datetime(ser, format='%Y%m', cache=cache)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: cache

# Workflow
ser = Series([2000, 2001, 2002])
expected = Series([Timestamp(x) for x in ser.apply(str)])
result = to_datetime(ser, format='%Y', cache=cache)
tm.assert_series_equal(result, expected)
ser = Series([200001, 200105, 200206])
expected = Series([Timestamp(x[:4] + '-' + x[4:]) for x in ser.apply(str)])
result = to_datetime(ser, format='%Y%m', cache=cache)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_to_datetime.py:290 | Complexity: Advanced | Last updated: 2026-06-02*