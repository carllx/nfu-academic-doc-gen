# How To: Append With Timezones As Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test append with timezones as index

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
# Fixtures: setup_path, gettz
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2000-1-1', periods=3, freq='h', tz=gettz('US/Eastern'))
```

### Step 2: Assign dti = dti._with_freq(...)

```python
dti = dti._with_freq(None)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'A': Series(range(3), index=dti)})
```

### Step 4: Call _maybe_remove()

```python
_maybe_remove(store, 'df')
```

### Step 5: Call store.put()

```python
store.put('df', df)
```

### Step 6: Assign result = store.select(...)

```python
result = store.select('df')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 8: Call _maybe_remove()

```python
_maybe_remove(store, 'df')
```

### Step 9: Call store.append()

```python
store.append('df', df)
```

### Step 10: Assign result = store.select(...)

```python
result = store.select('df')
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path, gettz

# Workflow
dti = date_range('2000-1-1', periods=3, freq='h', tz=gettz('US/Eastern'))
dti = dti._with_freq(None)
df = DataFrame({'A': Series(range(3), index=dti)})
with ensure_clean_store(setup_path) as store:
    _maybe_remove(store, 'df')
    store.put('df', df)
    result = store.select('df')
    tm.assert_frame_equal(result, df)
    _maybe_remove(store, 'df')
    store.append('df', df)
    result = store.select('df')
    tm.assert_frame_equal(result, df)
```

## Next Steps


---

*Source: test_timezones.py:131 | Complexity: Advanced | Last updated: 2026-06-02*