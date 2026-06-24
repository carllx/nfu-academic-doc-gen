# How To: Round Dst Border Nonexistent

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test round dst border nonexistent

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `hypothesis`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.period`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method, ts_str, freq, unit
```

## Step-by-Step Guide

### Step 1: Assign ts = Timestamp.as_unit(...)

```python
ts = Timestamp(ts_str, tz='America/Chicago').as_unit(unit)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = getattr(...)

```python
result = getattr(ts, method)(freq, nonexistent='shift_forward')
```

**Verification:**
```python
assert result._creso == getattr(NpyDatetimeUnit, f'NPY_FR_{unit}').value
```

### Step 3: Assign expected = Timestamp(...)

```python
expected = Timestamp('2018-03-11 03:00:00', tz='America/Chicago')
```

**Verification:**
```python
assert result is NaT
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(ts, method)(freq, nonexistent='NaT')
```

**Verification:**
```python
assert result is NaT
```

### Step 5: Assign msg = '2018-03-11 02:00:00'

```python
msg = '2018-03-11 02:00:00'
```

### Step 6: Call getattr()

```python
getattr(ts, method)(freq, nonexistent='raise')
```


## Complete Example

```python
# Setup
# Fixtures: method, ts_str, freq, unit

# Workflow
ts = Timestamp(ts_str, tz='America/Chicago').as_unit(unit)
result = getattr(ts, method)(freq, nonexistent='shift_forward')
expected = Timestamp('2018-03-11 03:00:00', tz='America/Chicago')
assert result == expected
assert result._creso == getattr(NpyDatetimeUnit, f'NPY_FR_{unit}').value
result = getattr(ts, method)(freq, nonexistent='NaT')
assert result is NaT
msg = '2018-03-11 02:00:00'
with pytest.raises(pytz.NonExistentTimeError, match=msg):
    getattr(ts, method)(freq, nonexistent='raise')
```

## Next Steps


---

*Source: test_round.py:206 | Complexity: Intermediate | Last updated: 2026-06-02*