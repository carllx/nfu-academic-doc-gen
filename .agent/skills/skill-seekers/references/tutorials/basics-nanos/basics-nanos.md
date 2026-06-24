# How To: Basics Nanos

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basics nanos

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

### Step 1: Assign val = np.int64.view(...)

```python
val = np.int64(946684800000000000).view('M8[ns]')
```

**Verification:**
```python
assert stamp.year == 2000
```

### Step 2: Assign stamp = Timestamp(...)

```python
stamp = Timestamp(val.view('i8') + 500)
```

**Verification:**
```python
assert stamp.month == 1
```

### Step 3: Assign val = value

```python
val = np.iinfo(np.int64).min + 80000000000000
```

**Verification:**
```python
assert stamp.microsecond == 0
```

### Step 4: Assign stamp = Timestamp(...)

```python
stamp = Timestamp(val)
```

**Verification:**
```python
assert stamp.nanosecond == 500
```


## Complete Example

```python
# Workflow
val = np.int64(946684800000000000).view('M8[ns]')
stamp = Timestamp(val.view('i8') + 500)
assert stamp.year == 2000
assert stamp.month == 1
assert stamp.microsecond == 0
assert stamp.nanosecond == 500
val = np.iinfo(np.int64).min + 80000000000000
stamp = Timestamp(val)
assert stamp.year == 1677
assert stamp.month == 9
assert stamp.day == 21
assert stamp.microsecond == 145224
assert stamp.nanosecond == 192
```

## Next Steps


---

*Source: test_timestamp.py:342 | Complexity: Intermediate | Last updated: 2026-06-02*