# How To: Store Index Name With Tz

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test store index name with tz

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2]})
```

### Step 2: Assign df.index = DatetimeIndex(...)

```python
df.index = DatetimeIndex([1234567890123456787, 1234567890123456788])
```

### Step 3: Assign df.index = df.index.tz_localize(...)

```python
df.index = df.index.tz_localize('UTC')
```

### Step 4: Assign df.index.name = 'foo'

```python
df.index.name = 'foo'
```

### Step 5: Call store.put()

```python
store.put('frame', df, format='table')
```

### Step 6: Assign recons = value

```python
recons = store['frame']
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(recons, df)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
df = DataFrame({'A': [1, 2]})
df.index = DatetimeIndex([1234567890123456787, 1234567890123456788])
df.index = df.index.tz_localize('UTC')
df.index.name = 'foo'
with ensure_clean_store(setup_path) as store:
    store.put('frame', df, format='table')
    recons = store['frame']
    tm.assert_frame_equal(recons, df)
```

## Next Steps


---

*Source: test_timezones.py:167 | Complexity: Intermediate | Last updated: 2026-06-02*