# How To: Store Datetime Fractional Secs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test store datetime fractional secs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas.tests.io.pytables.common`

**Setup Required:**
```python
# Fixtures: setup_path, unit
```

## Step-by-Step Guide

### Step 1: Assign dt = datetime.datetime(...)

```python
dt = datetime.datetime(2012, 1, 2, 3, 4, 5, 123456)
```

**Verification:**
```python
assert store['a'].index[0] == dt
```

### Step 2: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex([dt], dtype=f'M8[{unit}]')
```

### Step 3: Assign series = Series(...)

```python
series = Series([0], index=dti)
```

### Step 4: Assign unknown = series

```python
store['a'] = series
```

**Verification:**
```python
assert store['a'].index[0] == dt
```


## Complete Example

```python
# Setup
# Fixtures: setup_path, unit

# Workflow
dt = datetime.datetime(2012, 1, 2, 3, 4, 5, 123456)
dti = DatetimeIndex([dt], dtype=f'M8[{unit}]')
series = Series([0], index=dti)
with ensure_clean_store(setup_path) as store:
    store['a'] = series
    assert store['a'].index[0] == dt
```

## Next Steps


---

*Source: test_time_series.py:20 | Complexity: Intermediate | Last updated: 2026-06-02*