# How To: Series Tz Localize Ambiguous Bool

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series tz localize ambiguous bool

## Prerequisites

**Required Modules:**
- `datetime`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2015-11-01 01:00:03')
```

### Step 2: Assign expected0 = Timestamp(...)

```python
expected0 = Timestamp('2015-11-01 01:00:03-0500', tz='US/Central')
```

### Step 3: Assign expected1 = Timestamp(...)

```python
expected1 = Timestamp('2015-11-01 01:00:03-0600', tz='US/Central')
```

### Step 4: Assign ser = Series(...)

```python
ser = Series([ts])
```

### Step 5: Assign expected0 = Series(...)

```python
expected0 = Series([expected0])
```

### Step 6: Assign expected1 = Series(...)

```python
expected1 = Series([expected1])
```

### Step 7: Assign result = ser.dt.tz_localize(...)

```python
result = ser.dt.tz_localize('US/Central', ambiguous=True)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected0)
```

### Step 9: Assign result = ser.dt.tz_localize(...)

```python
result = ser.dt.tz_localize('US/Central', ambiguous=[True])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected0)
```

### Step 11: Assign result = ser.dt.tz_localize(...)

```python
result = ser.dt.tz_localize('US/Central', ambiguous=False)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected1)
```

### Step 13: Assign result = ser.dt.tz_localize(...)

```python
result = ser.dt.tz_localize('US/Central', ambiguous=[False])
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected1)
```

### Step 15: Call ser.dt.tz_localize()

```python
ser.dt.tz_localize('US/Central')
```


## Complete Example

```python
# Workflow
ts = Timestamp('2015-11-01 01:00:03')
expected0 = Timestamp('2015-11-01 01:00:03-0500', tz='US/Central')
expected1 = Timestamp('2015-11-01 01:00:03-0600', tz='US/Central')
ser = Series([ts])
expected0 = Series([expected0])
expected1 = Series([expected1])
with tm.external_error_raised(pytz.AmbiguousTimeError):
    ser.dt.tz_localize('US/Central')
result = ser.dt.tz_localize('US/Central', ambiguous=True)
tm.assert_series_equal(result, expected0)
result = ser.dt.tz_localize('US/Central', ambiguous=[True])
tm.assert_series_equal(result, expected0)
result = ser.dt.tz_localize('US/Central', ambiguous=False)
tm.assert_series_equal(result, expected1)
result = ser.dt.tz_localize('US/Central', ambiguous=[False])
tm.assert_series_equal(result, expected1)
```

## Next Steps


---

*Source: test_tz_localize.py:19 | Complexity: Advanced | Last updated: 2026-06-02*