# How To: To Datetime Cache Coerce 50 Lines Outofbounds

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to datetime cache coerce 50 lines outofbounds

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
# Fixtures: series_length
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([datetime.fromisoformat('1446-04-12 00:00:00+00:00')] + [datetime.fromisoformat('1991-10-20 00:00:00+00:00')] * series_length, dtype=object)
```

### Step 2: Assign result1 = to_datetime(...)

```python
result1 = to_datetime(ser, errors='coerce', utc=True)
```

### Step 3: Assign expected1 = Series(...)

```python
expected1 = Series([NaT] + [Timestamp('1991-10-20 00:00:00+00:00')] * series_length)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result1, expected1)
```

### Step 5: Assign result2 = to_datetime(...)

```python
result2 = to_datetime(ser, errors='ignore', utc=True)
```

### Step 6: Assign expected2 = Series(...)

```python
expected2 = Series([datetime.fromisoformat('1446-04-12 00:00:00+00:00')] + [datetime.fromisoformat('1991-10-20 00:00:00+00:00')] * series_length)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result2, expected2)
```

### Step 8: Call to_datetime()

```python
to_datetime(ser, errors='raise', utc=True)
```


## Complete Example

```python
# Setup
# Fixtures: series_length

# Workflow
ser = Series([datetime.fromisoformat('1446-04-12 00:00:00+00:00')] + [datetime.fromisoformat('1991-10-20 00:00:00+00:00')] * series_length, dtype=object)
result1 = to_datetime(ser, errors='coerce', utc=True)
expected1 = Series([NaT] + [Timestamp('1991-10-20 00:00:00+00:00')] * series_length)
tm.assert_series_equal(result1, expected1)
result2 = to_datetime(ser, errors='ignore', utc=True)
expected2 = Series([datetime.fromisoformat('1446-04-12 00:00:00+00:00')] + [datetime.fromisoformat('1991-10-20 00:00:00+00:00')] * series_length)
tm.assert_series_equal(result2, expected2)
with pytest.raises(OutOfBoundsDatetime, match='Out of bounds nanosecond timestamp'):
    to_datetime(ser, errors='raise', utc=True)
```

## Next Steps


---

*Source: test_to_datetime.py:3653 | Complexity: Advanced | Last updated: 2026-06-02*