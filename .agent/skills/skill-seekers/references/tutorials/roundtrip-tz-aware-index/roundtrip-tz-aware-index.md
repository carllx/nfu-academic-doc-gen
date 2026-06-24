# How To: Roundtrip Tz Aware Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test roundtrip tz aware index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.io.pytables.common`

**Setup Required:**
```python
# Fixtures: setup_path, unit
```

## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2000-01-01 01:00:00', tz='US/Eastern')
```

**Verification:**
```python
assert value == 946706400000000000 // denom
```

### Step 2: Assign dti = DatetimeIndex.as_unit(...)

```python
dti = DatetimeIndex([ts]).as_unit(unit)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(data=[0], index=dti)
```

### Step 4: Assign value = value

```python
value = recons.index[0]._value
```

### Step 5: Assign denom = value

```python
denom = {'ns': 1, 'us': 1000, 'ms': 10 ** 6, 's': 10 ** 9}[unit]
```

**Verification:**
```python
assert value == 946706400000000000 // denom
```

### Step 6: Call store.put()

```python
store.put('frame', df, format='fixed')
```

### Step 7: Assign recons = value

```python
recons = store['frame']
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(recons, df)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path, unit

# Workflow
ts = Timestamp('2000-01-01 01:00:00', tz='US/Eastern')
dti = DatetimeIndex([ts]).as_unit(unit)
df = DataFrame(data=[0], index=dti)
with ensure_clean_store(setup_path) as store:
    store.put('frame', df, format='fixed')
    recons = store['frame']
    tm.assert_frame_equal(recons, df)
value = recons.index[0]._value
denom = {'ns': 1, 'us': 1000, 'ms': 10 ** 6, 's': 10 ** 9}[unit]
assert value == 946706400000000000 // denom
```

## Next Steps


---

*Source: test_timezones.py:151 | Complexity: Advanced | Last updated: 2026-06-02*