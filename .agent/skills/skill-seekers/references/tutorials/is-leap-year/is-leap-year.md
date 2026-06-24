# How To: Is Leap Year

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is leap year

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: tz_naive_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_naive_fixture

```python
tz = tz_naive_fixture
```

**Verification:**
```python
assert dt.is_leap_year
```

### Step 2: Assign dt = Timestamp(...)

```python
dt = Timestamp('2000-01-01 00:00:00', tz=tz)
```

**Verification:**
```python
assert isinstance(dt.is_leap_year, bool)
```

### Step 3: Assign dt = Timestamp(...)

```python
dt = Timestamp('1999-01-01 00:00:00', tz=tz)
```

**Verification:**
```python
assert not dt.is_leap_year
```

### Step 4: Assign dt = Timestamp(...)

```python
dt = Timestamp('2004-01-01 00:00:00', tz=tz)
```

**Verification:**
```python
assert dt.is_leap_year
```

### Step 5: Assign dt = Timestamp(...)

```python
dt = Timestamp('2100-01-01 00:00:00', tz=tz)
```

**Verification:**
```python
assert not dt.is_leap_year
```

### Step 6: Call pytest.skip()

```python
pytest.skip('tzlocal() on a 32 bit platform causes internal overflow errors')
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture

# Workflow
tz = tz_naive_fixture
if not IS64 and tz == tzlocal():
    pytest.skip('tzlocal() on a 32 bit platform causes internal overflow errors')
dt = Timestamp('2000-01-01 00:00:00', tz=tz)
assert dt.is_leap_year
assert isinstance(dt.is_leap_year, bool)
dt = Timestamp('1999-01-01 00:00:00', tz=tz)
assert not dt.is_leap_year
dt = Timestamp('2004-01-01 00:00:00', tz=tz)
assert dt.is_leap_year
dt = Timestamp('2100-01-01 00:00:00', tz=tz)
assert not dt.is_leap_year
```

## Next Steps


---

*Source: test_timestamp.py:159 | Complexity: Intermediate | Last updated: 2026-06-02*