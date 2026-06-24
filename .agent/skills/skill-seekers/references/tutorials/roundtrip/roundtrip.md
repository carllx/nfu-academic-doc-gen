# How To: Roundtrip

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test roundtrip

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

### Step 1: Assign base = Timestamp.as_unit(...)

```python
base = Timestamp('20140101 00:00:00').as_unit('ns')
```

**Verification:**
```python
assert result == Timestamp(f'{base}.005000')
```

### Step 2: Assign result = Timestamp(...)

```python
result = Timestamp(base._value + Timedelta('5ms')._value)
```

**Verification:**
```python
assert result.microsecond == 5000
```

### Step 3: Assign result = Timestamp(...)

```python
result = Timestamp(base._value + Timedelta('5us')._value)
```

**Verification:**
```python
assert result == Timestamp(f'{base}.000005')
```

### Step 4: Assign result = Timestamp(...)

```python
result = Timestamp(base._value + Timedelta('5ns')._value)
```

**Verification:**
```python
assert result.microsecond == 5
```

### Step 5: Assign result = Timestamp(...)

```python
result = Timestamp(base._value + Timedelta('6ms 5us')._value)
```

**Verification:**
```python
assert result == Timestamp(f'{base}.000000005')
```

### Step 6: Assign result = Timestamp(...)

```python
result = Timestamp(base._value + Timedelta('200ms 5us')._value)
```

**Verification:**
```python
assert result.nanosecond == 5
```


## Complete Example

```python
# Workflow
base = Timestamp('20140101 00:00:00').as_unit('ns')
result = Timestamp(base._value + Timedelta('5ms')._value)
assert result == Timestamp(f'{base}.005000')
assert result.microsecond == 5000
result = Timestamp(base._value + Timedelta('5us')._value)
assert result == Timestamp(f'{base}.000005')
assert result.microsecond == 5
result = Timestamp(base._value + Timedelta('5ns')._value)
assert result == Timestamp(f'{base}.000000005')
assert result.nanosecond == 5
assert result.microsecond == 0
result = Timestamp(base._value + Timedelta('6ms 5us')._value)
assert result == Timestamp(f'{base}.006005')
assert result.microsecond == 5 + 6 * 1000
result = Timestamp(base._value + Timedelta('200ms 5us')._value)
assert result == Timestamp(f'{base}.200005')
assert result.microsecond == 5 + 200 * 1000
```

## Next Steps


---

*Source: test_timestamp.py:359 | Complexity: Intermediate | Last updated: 2026-06-02*