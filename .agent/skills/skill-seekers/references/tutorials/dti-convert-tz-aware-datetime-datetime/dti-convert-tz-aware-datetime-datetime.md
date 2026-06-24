# How To: Dti Convert Tz Aware Datetime Datetime

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dti convert tz aware datetime datetime

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign dates = value

```python
dates = [datetime(2000, 1, 1), datetime(2000, 1, 2), datetime(2000, 1, 3)]
```

**Verification:**
```python
assert timezones.tz_compare(result.tz, tz)
```

### Step 2: Assign dates_aware = value

```python
dates_aware = [conversion.localize_pydatetime(x, tz) for x in dates]
```

**Verification:**
```python
assert converted.tz is timezone.utc
```

### Step 3: Assign result = DatetimeIndex.as_unit(...)

```python
result = DatetimeIndex(dates_aware).as_unit('ns')
```

**Verification:**
```python
assert timezones.tz_compare(result.tz, tz)
```

### Step 4: Assign converted = to_datetime.as_unit(...)

```python
converted = to_datetime(dates_aware, utc=True).as_unit('ns')
```

### Step 5: Assign ex_vals = np.array(...)

```python
ex_vals = np.array([Timestamp(x).as_unit('ns')._value for x in dates_aware])
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(converted.asi8, ex_vals)
```

**Verification:**
```python
assert converted.tz is timezone.utc
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
dates = [datetime(2000, 1, 1), datetime(2000, 1, 2), datetime(2000, 1, 3)]
dates_aware = [conversion.localize_pydatetime(x, tz) for x in dates]
result = DatetimeIndex(dates_aware).as_unit('ns')
assert timezones.tz_compare(result.tz, tz)
converted = to_datetime(dates_aware, utc=True).as_unit('ns')
ex_vals = np.array([Timestamp(x).as_unit('ns')._value for x in dates_aware])
tm.assert_numpy_array_equal(converted.asi8, ex_vals)
assert converted.tz is timezone.utc
```

## Next Steps


---

*Source: test_timezones.py:240 | Complexity: Intermediate | Last updated: 2026-06-02*