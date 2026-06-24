# How To: Dti Tz Localize Utc Conversion

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dti tz localize utc conversion

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `zoneinfo`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('3/10/2012', '3/11/2012', freq='30min')
```

### Step 2: Assign converted = rng.tz_localize(...)

```python
converted = rng.tz_localize(tz)
```

### Step 3: Assign expected_naive = value

```python
expected_naive = rng + offsets.Hour(5)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(converted.asi8, expected_naive.asi8)
```

### Step 5: Assign rng = date_range(...)

```python
rng = date_range('3/11/2012', '3/12/2012', freq='30min')
```

### Step 6: Call rng.tz_localize()

```python
rng.tz_localize(tz)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
rng = date_range('3/10/2012', '3/11/2012', freq='30min')
converted = rng.tz_localize(tz)
expected_naive = rng + offsets.Hour(5)
tm.assert_numpy_array_equal(converted.asi8, expected_naive.asi8)
rng = date_range('3/11/2012', '3/12/2012', freq='30min')
with pytest.raises(pytz.NonExistentTimeError, match='2012-03-11 02:00:00'):
    rng.tz_localize(tz)
```

## Next Steps


---

*Source: test_tz_localize.py:193 | Complexity: Intermediate | Last updated: 2026-06-02*