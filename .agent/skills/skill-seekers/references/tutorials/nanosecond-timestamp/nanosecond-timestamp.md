# How To: Nanosecond Timestamp

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nanosecond timestamp

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

### Step 1: Assign expected = 1293840000000000005

```python
expected = 1293840000000000005
```

**Verification:**
```python
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000005')"
```

### Step 2: Assign t = value

```python
t = Timestamp('2011-01-01') + offsets.Nano(5)
```

**Verification:**
```python
assert t._value == expected
```

### Step 3: Assign t = Timestamp(...)

```python
t = Timestamp(t)
```

**Verification:**
```python
assert t.nanosecond == 5
```

### Step 4: Assign t = Timestamp(...)

```python
t = Timestamp('2011-01-01 00:00:00.000000005')
```

**Verification:**
```python
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000005')"
```

### Step 5: Assign expected = 1293840000000000010

```python
expected = 1293840000000000010
```

**Verification:**
```python
assert t._value == expected
```

### Step 6: Assign t = value

```python
t = t + offsets.Nano(5)
```

**Verification:**
```python
assert t.nanosecond == 5
```

### Step 7: Assign t = Timestamp(...)

```python
t = Timestamp(t)
```

**Verification:**
```python
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000005')"
```

### Step 8: Assign t = Timestamp(...)

```python
t = Timestamp('2011-01-01 00:00:00.000000010')
```

**Verification:**
```python
assert t._value == expected
```


## Complete Example

```python
# Workflow
expected = 1293840000000000005
t = Timestamp('2011-01-01') + offsets.Nano(5)
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000005')"
assert t._value == expected
assert t.nanosecond == 5
t = Timestamp(t)
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000005')"
assert t._value == expected
assert t.nanosecond == 5
t = Timestamp('2011-01-01 00:00:00.000000005')
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000005')"
assert t._value == expected
assert t.nanosecond == 5
expected = 1293840000000000010
t = t + offsets.Nano(5)
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000010')"
assert t._value == expected
assert t.nanosecond == 10
t = Timestamp(t)
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000010')"
assert t._value == expected
assert t.nanosecond == 10
t = Timestamp('2011-01-01 00:00:00.000000010')
assert repr(t) == "Timestamp('2011-01-01 00:00:00.000000010')"
assert t._value == expected
assert t.nanosecond == 10
```

## Next Steps


---

*Source: test_timestamp.py:444 | Complexity: Advanced | Last updated: 2026-06-02*