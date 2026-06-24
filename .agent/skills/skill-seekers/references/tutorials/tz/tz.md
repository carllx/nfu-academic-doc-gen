# How To: Tz

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tz

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

### Step 1: Assign tstr = '2014-02-01 09:00'

```python
tstr = '2014-02-01 09:00'
```

**Verification:**
```python
assert local.hour == 9
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp(tstr)
```

**Verification:**
```python
assert local == Timestamp(tstr, tz='Asia/Tokyo')
```

### Step 3: Assign local = ts.tz_localize(...)

```python
local = ts.tz_localize('Asia/Tokyo')
```

**Verification:**
```python
assert conv == Timestamp('2014-01-31 19:00', tz='US/Eastern')
```

### Step 4: Assign conv = local.tz_convert(...)

```python
conv = local.tz_convert('US/Eastern')
```

**Verification:**
```python
assert conv.hour == 19
```

### Step 5: Assign ts = value

```python
ts = Timestamp(tstr) + offsets.Nano(5)
```

**Verification:**
```python
assert local.hour == 9
```

### Step 6: Assign local = ts.tz_localize(...)

```python
local = ts.tz_localize('Asia/Tokyo')
```

**Verification:**
```python
assert local.nanosecond == 5
```

### Step 7: Assign conv = local.tz_convert(...)

```python
conv = local.tz_convert('US/Eastern')
```

**Verification:**
```python
assert conv.nanosecond == 5
```


## Complete Example

```python
# Workflow
tstr = '2014-02-01 09:00'
ts = Timestamp(tstr)
local = ts.tz_localize('Asia/Tokyo')
assert local.hour == 9
assert local == Timestamp(tstr, tz='Asia/Tokyo')
conv = local.tz_convert('US/Eastern')
assert conv == Timestamp('2014-01-31 19:00', tz='US/Eastern')
assert conv.hour == 19
ts = Timestamp(tstr) + offsets.Nano(5)
local = ts.tz_localize('Asia/Tokyo')
assert local.hour == 9
assert local.nanosecond == 5
conv = local.tz_convert('US/Eastern')
assert conv.nanosecond == 5
assert conv.hour == 19
```

## Next Steps


---

*Source: test_timestamp.py:276 | Complexity: Intermediate | Last updated: 2026-06-02*