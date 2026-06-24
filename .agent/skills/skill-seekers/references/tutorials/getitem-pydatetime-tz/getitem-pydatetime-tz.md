# How To: Getitem Pydatetime Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test getitem pydatetime tz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: tzstr
```

## Step-by-Step Guide

### Step 1: Assign tz = timezones.maybe_get_tz(...)

```python
tz = timezones.maybe_get_tz(tzstr)
```

**Verification:**
```python
assert ts[time_pandas] == ts[time_datetime]
```

### Step 2: Assign index = date_range(...)

```python
index = date_range(start='2012-12-24 16:00', end='2012-12-24 18:00', freq='h', tz=tzstr)
```

### Step 3: Assign ts = Series(...)

```python
ts = Series(index=index, data=index.hour)
```

### Step 4: Assign time_pandas = Timestamp(...)

```python
time_pandas = Timestamp('2012-12-24 17:00', tz=tzstr)
```

### Step 5: Assign dt = datetime(...)

```python
dt = datetime(2012, 12, 24, 17, 0)
```

### Step 6: Assign time_datetime = conversion.localize_pydatetime(...)

```python
time_datetime = conversion.localize_pydatetime(dt, tz)
```

**Verification:**
```python
assert ts[time_pandas] == ts[time_datetime]
```


## Complete Example

```python
# Setup
# Fixtures: tzstr

# Workflow
tz = timezones.maybe_get_tz(tzstr)
index = date_range(start='2012-12-24 16:00', end='2012-12-24 18:00', freq='h', tz=tzstr)
ts = Series(index=index, data=index.hour)
time_pandas = Timestamp('2012-12-24 17:00', tz=tzstr)
dt = datetime(2012, 12, 24, 17, 0)
time_datetime = conversion.localize_pydatetime(dt, tz)
assert ts[time_pandas] == ts[time_datetime]
```

## Next Steps


---

*Source: test_getitem.py:136 | Complexity: Intermediate | Last updated: 2026-06-02*