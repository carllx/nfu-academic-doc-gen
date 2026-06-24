# How To: Dti Tz Localize Ambiguous Times

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dti tz localize ambiguous times

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

### Step 1: Assign dr = date_range(...)

```python
dr = date_range(datetime(2011, 3, 13, 1, 30), periods=3, freq=offsets.Hour())
```

### Step 2: Assign dr = date_range(...)

```python
dr = date_range(datetime(2011, 3, 13, 3, 30), periods=3, freq=offsets.Hour(), tz=tz)
```

### Step 3: Assign dr = date_range(...)

```python
dr = date_range(datetime(2011, 11, 6, 1, 30), periods=3, freq=offsets.Hour())
```

### Step 4: Assign dr = date_range(...)

```python
dr = date_range(datetime(2011, 3, 13), periods=48, freq=offsets.Minute(30), tz=pytz.utc)
```

### Step 5: Call dr.tz_localize()

```python
dr.tz_localize(tz)
```

### Step 6: Call dr.tz_localize()

```python
dr.tz_localize(tz)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
dr = date_range(datetime(2011, 3, 13, 1, 30), periods=3, freq=offsets.Hour())
with pytest.raises(pytz.NonExistentTimeError, match='2011-03-13 02:30:00'):
    dr.tz_localize(tz)
dr = date_range(datetime(2011, 3, 13, 3, 30), periods=3, freq=offsets.Hour(), tz=tz)
dr = date_range(datetime(2011, 11, 6, 1, 30), periods=3, freq=offsets.Hour())
with pytest.raises(pytz.AmbiguousTimeError, match='Cannot infer dst time'):
    dr.tz_localize(tz)
dr = date_range(datetime(2011, 3, 13), periods=48, freq=offsets.Minute(30), tz=pytz.utc)
```

## Next Steps


---

*Source: test_tz_localize.py:128 | Complexity: Intermediate | Last updated: 2026-06-02*