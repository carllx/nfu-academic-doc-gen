# How To: Fixed Offset Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fixed offset tz

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
# Fixtures: setup_path
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000 00:00:00-07:00', '1/30/2000 00:00:00-07:00')
```

**Verification:**
```python
assert rng.tz == recons.index.tz
```

### Step 2: Assign frame = DataFrame(...)

```python
frame = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 4)), index=rng)
```

### Step 3: Assign unknown = frame

```python
store['frame'] = frame
```

### Step 4: Assign recons = value

```python
recons = store['frame']
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(recons.index, rng)
```

**Verification:**
```python
assert rng.tz == recons.index.tz
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
rng = date_range('1/1/2000 00:00:00-07:00', '1/30/2000 00:00:00-07:00')
frame = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 4)), index=rng)
with ensure_clean_store(setup_path) as store:
    store['frame'] = frame
    recons = store['frame']
    tm.assert_index_equal(recons.index, rng)
    assert rng.tz == recons.index.tz
```

## Next Steps


---

*Source: test_timezones.py:275 | Complexity: Intermediate | Last updated: 2026-06-02*