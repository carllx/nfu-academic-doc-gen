# How To: Select Iterator Non Complete 8014

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test select iterator non complete 8014

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.io.pytables`

**Setup Required:**
```python
# Fixtures: setup_path
```

## Step-by-Step Guide

### Step 1: Assign chunksize = 10000.0

```python
chunksize = 10000.0
```

**Verification:**
```python
assert 0 == len(results)
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.random.default_rng(2).standard_normal((100064, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=100064, freq='s'))
```

### Step 3: Call _maybe_remove()

```python
_maybe_remove(store, 'df')
```

### Step 4: Call store.append()

```python
store.append('df', expected)
```

### Step 5: Assign beg_dt = value

```python
beg_dt = expected.index[1]
```

### Step 6: Assign end_dt = value

```python
end_dt = expected.index[-2]
```

### Step 7: Assign where = value

```python
where = f"index >= '{beg_dt}'"
```

### Step 8: Assign results = list(...)

```python
results = list(store.select('df', where=where, chunksize=chunksize))
```

### Step 9: Assign result = concat(...)

```python
result = concat(results)
```

### Step 10: Assign rexpected = value

```python
rexpected = expected[expected.index >= beg_dt]
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(rexpected, result)
```

### Step 12: Assign where = value

```python
where = f"index <= '{end_dt}'"
```

### Step 13: Assign results = list(...)

```python
results = list(store.select('df', where=where, chunksize=chunksize))
```

### Step 14: Assign result = concat(...)

```python
result = concat(results)
```

### Step 15: Assign rexpected = value

```python
rexpected = expected[expected.index <= end_dt]
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(rexpected, result)
```

### Step 17: Assign where = value

```python
where = f"index >= '{beg_dt}' & index <= '{end_dt}'"
```

### Step 18: Assign results = list(...)

```python
results = list(store.select('df', where=where, chunksize=chunksize))
```

### Step 19: Assign result = concat(...)

```python
result = concat(results)
```

### Step 20: Assign rexpected = value

```python
rexpected = expected[(expected.index >= beg_dt) & (expected.index <= end_dt)]
```

### Step 21: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(rexpected, result)
```

### Step 22: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.random.default_rng(2).standard_normal((100064, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=100064, freq='s'))
```

### Step 23: Call _maybe_remove()

```python
_maybe_remove(store, 'df')
```

### Step 24: Call store.append()

```python
store.append('df', expected)
```

### Step 25: Assign end_dt = value

```python
end_dt = expected.index[-1]
```

### Step 26: Assign where = value

```python
where = f"index > '{end_dt}'"
```

### Step 27: Assign results = list(...)

```python
results = list(store.select('df', where=where, chunksize=chunksize))
```

**Verification:**
```python
assert 0 == len(results)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
chunksize = 10000.0
with ensure_clean_store(setup_path) as store:
    expected = DataFrame(np.random.default_rng(2).standard_normal((100064, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=100064, freq='s'))
    _maybe_remove(store, 'df')
    store.append('df', expected)
    beg_dt = expected.index[1]
    end_dt = expected.index[-2]
    where = f"index >= '{beg_dt}'"
    results = list(store.select('df', where=where, chunksize=chunksize))
    result = concat(results)
    rexpected = expected[expected.index >= beg_dt]
    tm.assert_frame_equal(rexpected, result)
    where = f"index <= '{end_dt}'"
    results = list(store.select('df', where=where, chunksize=chunksize))
    result = concat(results)
    rexpected = expected[expected.index <= end_dt]
    tm.assert_frame_equal(rexpected, result)
    where = f"index >= '{beg_dt}' & index <= '{end_dt}'"
    results = list(store.select('df', where=where, chunksize=chunksize))
    result = concat(results)
    rexpected = expected[(expected.index >= beg_dt) & (expected.index <= end_dt)]
    tm.assert_frame_equal(rexpected, result)
with ensure_clean_store(setup_path) as store:
    expected = DataFrame(np.random.default_rng(2).standard_normal((100064, 4)), columns=Index(list('ABCD')), index=date_range('2000-01-01', periods=100064, freq='s'))
    _maybe_remove(store, 'df')
    store.append('df', expected)
    end_dt = expected.index[-1]
    where = f"index > '{end_dt}'"
    results = list(store.select('df', where=where, chunksize=chunksize))
    assert 0 == len(results)
```

## Next Steps


---

*Source: test_select.py:494 | Complexity: Advanced | Last updated: 2026-06-02*