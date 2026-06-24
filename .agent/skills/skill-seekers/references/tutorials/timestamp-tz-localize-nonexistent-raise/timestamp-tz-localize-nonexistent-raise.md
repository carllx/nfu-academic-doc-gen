# How To: Timestamp Tz Localize Nonexistent Raise

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test timestamp tz localize nonexistent raise

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `dateutil.tz`
- `pytest`
- `pytz`
- `pytz.exceptions`
- `pandas._libs.tslibs.dtypes`
- `pandas.errors`
- `pandas`
- `zoneinfo`

**Setup Required:**
```python
# Fixtures: warsaw, unit
```

## Step-by-Step Guide

### Step 1: Assign tz = warsaw

```python
tz = warsaw
```

### Step 2: Assign ts = Timestamp.as_unit(...)

```python
ts = Timestamp('2015-03-29 02:20:00').as_unit(unit)
```

### Step 3: Assign msg = '2015-03-29 02:20:00'

```python
msg = '2015-03-29 02:20:00'
```

### Step 4: Assign msg = "The nonexistent argument must be one of 'raise', 'NaT', 'shift_forward', 'shift_backward' or a timedelta object"

```python
msg = "The nonexistent argument must be one of 'raise', 'NaT', 'shift_forward', 'shift_backward' or a timedelta object"
```

### Step 5: Call ts.tz_localize()

```python
ts.tz_localize(tz, nonexistent='raise')
```

### Step 6: Call ts.tz_localize()

```python
ts.tz_localize(tz, nonexistent='foo')
```


## Complete Example

```python
# Setup
# Fixtures: warsaw, unit

# Workflow
tz = warsaw
ts = Timestamp('2015-03-29 02:20:00').as_unit(unit)
msg = '2015-03-29 02:20:00'
with pytest.raises(pytz.NonExistentTimeError, match=msg):
    ts.tz_localize(tz, nonexistent='raise')
msg = "The nonexistent argument must be one of 'raise', 'NaT', 'shift_forward', 'shift_backward' or a timedelta object"
with pytest.raises(ValueError, match=msg):
    ts.tz_localize(tz, nonexistent='foo')
```

## Next Steps


---

*Source: test_tz_localize.py:339 | Complexity: Intermediate | Last updated: 2026-06-02*