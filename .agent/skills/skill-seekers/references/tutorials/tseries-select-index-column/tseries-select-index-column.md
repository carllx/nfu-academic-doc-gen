# How To: Tseries Select Index Column

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tseries select index column

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
rng = date_range('1/1/2000', '1/30/2000')
```

**Verification:**
```python
assert rng.tz == DatetimeIndex(result.values).tz
```

### Step 2: Assign frame = DataFrame(...)

```python
frame = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 4)), index=rng)
```

**Verification:**
```python
assert rng.tz == result.dt.tz
```

### Step 3: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000', '1/30/2000', tz='UTC')
```

**Verification:**
```python
assert rng.tz == result.dt.tz
```

### Step 4: Assign frame = DataFrame(...)

```python
frame = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 4)), index=rng)
```

### Step 5: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000', '1/30/2000', tz='US/Eastern')
```

### Step 6: Assign frame = DataFrame(...)

```python
frame = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 4)), index=rng)
```

### Step 7: Call store.append()

```python
store.append('frame', frame)
```

### Step 8: Assign result = store.select_column(...)

```python
result = store.select_column('frame', 'index')
```

**Verification:**
```python
assert rng.tz == DatetimeIndex(result.values).tz
```

### Step 9: Call store.append()

```python
store.append('frame', frame)
```

### Step 10: Assign result = store.select_column(...)

```python
result = store.select_column('frame', 'index')
```

**Verification:**
```python
assert rng.tz == result.dt.tz
```

### Step 11: Call store.append()

```python
store.append('frame', frame)
```

### Step 12: Assign result = store.select_column(...)

```python
result = store.select_column('frame', 'index')
```

**Verification:**
```python
assert rng.tz == result.dt.tz
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
rng = date_range('1/1/2000', '1/30/2000')
frame = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 4)), index=rng)
with ensure_clean_store(setup_path) as store:
    store.append('frame', frame)
    result = store.select_column('frame', 'index')
    assert rng.tz == DatetimeIndex(result.values).tz
rng = date_range('1/1/2000', '1/30/2000', tz='UTC')
frame = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 4)), index=rng)
with ensure_clean_store(setup_path) as store:
    store.append('frame', frame)
    result = store.select_column('frame', 'index')
    assert rng.tz == result.dt.tz
rng = date_range('1/1/2000', '1/30/2000', tz='US/Eastern')
frame = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 4)), index=rng)
with ensure_clean_store(setup_path) as store:
    store.append('frame', frame)
    result = store.select_column('frame', 'index')
    assert rng.tz == result.dt.tz
```

## Next Steps


---

*Source: test_timezones.py:180 | Complexity: Advanced | Last updated: 2026-06-02*