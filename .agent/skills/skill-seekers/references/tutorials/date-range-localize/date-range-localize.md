# How To: Date Range Localize

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date range localize

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
rng = date_range('3/11/2012 03:00', periods=15, freq='h', tz='US/Eastern', unit=unit)
```

**Verification:**
```python
assert val.hour == 3
```

### Step 2: Assign rng2 = DatetimeIndex(...)

```python
rng2 = DatetimeIndex(['3/11/2012 03:00', '3/11/2012 04:00'], dtype=f'M8[{unit}, US/Eastern]')
```

**Verification:**
```python
assert exp.hour == 3
```

### Step 3: Assign rng3 = date_range(...)

```python
rng3 = date_range('3/11/2012 03:00', periods=15, freq='h', unit=unit)
```

**Verification:**
```python
assert val == exp
```

### Step 4: Assign rng3 = rng3.tz_localize(...)

```python
rng3 = rng3.tz_localize('US/Eastern')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(rng._with_freq(None), rng3)
```

### Step 6: Assign val = value

```python
val = rng[0]
```

### Step 7: Assign exp = Timestamp(...)

```python
exp = Timestamp('3/11/2012 03:00', tz='US/Eastern')
```

**Verification:**
```python
assert val.hour == 3
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(rng[:2], rng2)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
rng = date_range('3/11/2012 03:00', periods=15, freq='h', tz='US/Eastern', unit=unit)
rng2 = DatetimeIndex(['3/11/2012 03:00', '3/11/2012 04:00'], dtype=f'M8[{unit}, US/Eastern]')
rng3 = date_range('3/11/2012 03:00', periods=15, freq='h', unit=unit)
rng3 = rng3.tz_localize('US/Eastern')
tm.assert_index_equal(rng._with_freq(None), rng3)
val = rng[0]
exp = Timestamp('3/11/2012 03:00', tz='US/Eastern')
assert val.hour == 3
assert exp.hour == 3
assert val == exp
tm.assert_index_equal(rng[:2], rng2)
```

## Next Steps


---

*Source: test_timezones.py:115 | Complexity: Advanced | Last updated: 2026-06-02*