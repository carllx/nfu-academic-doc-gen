# How To: Nanosecond String Parsing

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nanosecond string parsing

## Prerequisites

**Required Modules:**
- `calendar`
- `datetime`
- `locale`
- `time`
- `unicodedata`
- `dateutil.tz`
- `hypothesis`
- `numpy`
- `pytest`
- `pytz`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.timezones`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.tseries`
- `pandas.tseries.frequencies`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2013-05-01 07:15:45.123456789')
```

**Verification:**
```python
assert ts._value == expected_value
```

### Step 2: Assign expected_repr = '2013-05-01 07:15:45.123456789'

```python
expected_repr = '2013-05-01 07:15:45.123456789'
```

**Verification:**
```python
assert expected_repr in repr(ts)
```

### Step 3: Assign expected_value = 1367392545123456789

```python
expected_value = 1367392545123456789
```

**Verification:**
```python
assert ts._value == expected_value - 9 * 3600 * 1000000000
```

### Step 4: Assign ts = Timestamp(...)

```python
ts = Timestamp('2013-05-01 07:15:45.123456789+09:00', tz='Asia/Tokyo')
```

**Verification:**
```python
assert expected_repr in repr(ts)
```

### Step 5: Assign ts = Timestamp(...)

```python
ts = Timestamp('2013-05-01 07:15:45.123456789', tz='UTC')
```

**Verification:**
```python
assert ts._value == expected_value
```

### Step 6: Assign ts = Timestamp(...)

```python
ts = Timestamp('2013-05-01 07:15:45.123456789', tz='US/Eastern')
```

**Verification:**
```python
assert expected_repr in repr(ts)
```

### Step 7: Assign ts = Timestamp(...)

```python
ts = Timestamp('20130501T071545.123456789')
```

**Verification:**
```python
assert ts._value == expected_value + 4 * 3600 * 1000000000
```


## Complete Example

```python
# Workflow
ts = Timestamp('2013-05-01 07:15:45.123456789')
expected_repr = '2013-05-01 07:15:45.123456789'
expected_value = 1367392545123456789
assert ts._value == expected_value
assert expected_repr in repr(ts)
ts = Timestamp('2013-05-01 07:15:45.123456789+09:00', tz='Asia/Tokyo')
assert ts._value == expected_value - 9 * 3600 * 1000000000
assert expected_repr in repr(ts)
ts = Timestamp('2013-05-01 07:15:45.123456789', tz='UTC')
assert ts._value == expected_value
assert expected_repr in repr(ts)
ts = Timestamp('2013-05-01 07:15:45.123456789', tz='US/Eastern')
assert ts._value == expected_value + 4 * 3600 * 1000000000
assert expected_repr in repr(ts)
ts = Timestamp('20130501T071545.123456789')
assert ts._value == expected_value
assert expected_repr in repr(ts)
```

## Next Steps


---

*Source: test_timestamp.py:419 | Complexity: Intermediate | Last updated: 2026-06-02*