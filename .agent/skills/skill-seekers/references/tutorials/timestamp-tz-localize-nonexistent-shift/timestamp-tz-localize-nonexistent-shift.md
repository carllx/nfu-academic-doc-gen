# How To: Timestamp Tz Localize Nonexistent Shift

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test timestamp tz localize nonexistent shift

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
# Fixtures: start_ts, tz, end_ts, shift, tz_type, unit
```

## Step-by-Step Guide

### Step 1: Assign tz = value

```python
tz = tz_type + tz
```

**Verification:**
```python
assert result == expected.replace(nanosecond=0)
```

### Step 2: Assign ts = Timestamp.as_unit(...)

```python
ts = Timestamp(start_ts).as_unit(unit)
```

**Verification:**
```python
assert result == expected.replace(microsecond=micros, nanosecond=0)
```

### Step 3: Assign result = ts.tz_localize(...)

```python
result = ts.tz_localize(tz, nonexistent=shift)
```

**Verification:**
```python
assert result == expected.replace(microsecond=0, nanosecond=0)
```

### Step 4: Assign expected = Timestamp.tz_localize(...)

```python
expected = Timestamp(end_ts).tz_localize(tz)
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign shift = value

```python
shift = 'shift_' + shift
```

**Verification:**
```python
assert result._creso == getattr(NpyDatetimeUnit, f'NPY_FR_{unit}').value
```

### Step 6: Assign micros = value

```python
micros = expected.microsecond - expected.microsecond % 1000
```

**Verification:**
```python
assert result == expected.replace(microsecond=micros, nanosecond=0)
```


## Complete Example

```python
# Setup
# Fixtures: start_ts, tz, end_ts, shift, tz_type, unit

# Workflow
tz = tz_type + tz
if isinstance(shift, str):
    shift = 'shift_' + shift
ts = Timestamp(start_ts).as_unit(unit)
result = ts.tz_localize(tz, nonexistent=shift)
expected = Timestamp(end_ts).tz_localize(tz)
if unit == 'us':
    assert result == expected.replace(nanosecond=0)
elif unit == 'ms':
    micros = expected.microsecond - expected.microsecond % 1000
    assert result == expected.replace(microsecond=micros, nanosecond=0)
elif unit == 's':
    assert result == expected.replace(microsecond=0, nanosecond=0)
else:
    assert result == expected
assert result._creso == getattr(NpyDatetimeUnit, f'NPY_FR_{unit}').value
```

## Next Steps


---

*Source: test_tz_localize.py:299 | Complexity: Intermediate | Last updated: 2026-06-02*