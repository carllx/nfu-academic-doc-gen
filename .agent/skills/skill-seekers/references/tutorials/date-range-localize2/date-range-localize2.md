# How To: Date Range Localize2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date range localize2

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
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('3/11/2012 00:00', periods=2, freq='h', tz='US/Eastern', unit=unit)
```

**Verification:**
```python
assert exp.hour == 0
```

### Step 2: Assign rng2 = DatetimeIndex(...)

```python
rng2 = DatetimeIndex(['3/11/2012 00:00', '3/11/2012 01:00'], dtype=f'M8[{unit}, US/Eastern]', freq='h')
```

**Verification:**
```python
assert rng[0] == exp
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(rng, rng2)
```

**Verification:**
```python
assert exp.hour == 1
```

### Step 4: Assign exp = Timestamp(...)

```python
exp = Timestamp('3/11/2012 00:00', tz='US/Eastern')
```

**Verification:**
```python
assert rng[1] == exp
```

### Step 5: Assign exp = Timestamp(...)

```python
exp = Timestamp('3/11/2012 01:00', tz='US/Eastern')
```

**Verification:**
```python
assert rng[2].hour == 3
```

### Step 6: Assign rng = date_range(...)

```python
rng = date_range('3/11/2012 00:00', periods=10, freq='h', tz='US/Eastern', unit=unit)
```

**Verification:**
```python
assert rng[2].hour == 3
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
rng = date_range('3/11/2012 00:00', periods=2, freq='h', tz='US/Eastern', unit=unit)
rng2 = DatetimeIndex(['3/11/2012 00:00', '3/11/2012 01:00'], dtype=f'M8[{unit}, US/Eastern]', freq='h')
tm.assert_index_equal(rng, rng2)
exp = Timestamp('3/11/2012 00:00', tz='US/Eastern')
assert exp.hour == 0
assert rng[0] == exp
exp = Timestamp('3/11/2012 01:00', tz='US/Eastern')
assert exp.hour == 1
assert rng[1] == exp
rng = date_range('3/11/2012 00:00', periods=10, freq='h', tz='US/Eastern', unit=unit)
assert rng[2].hour == 3
```

## Next Steps


---

*Source: test_timezones.py:136 | Complexity: Intermediate | Last updated: 2026-06-02*