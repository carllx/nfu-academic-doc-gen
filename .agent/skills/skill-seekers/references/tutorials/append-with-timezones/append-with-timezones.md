# How To: Append With Timezones

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test append with timezones

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

### Step 1: Assign df_est = DataFrame(...)

```python
df_est = DataFrame({'A': [Timestamp('20130102 2:00:00', tz=gettz('US/Eastern')).as_unit('ns') + timedelta(hours=1) * i for i in range(5)]})
```

### Step 2: Assign df_crosses_dst = DataFrame(...)

```python
df_crosses_dst = DataFrame({'A': Timestamp('20130102', tz=gettz('US/Eastern')).as_unit('ns'), 'B': Timestamp('20130603', tz=gettz('US/Eastern')).as_unit('ns')}, index=range(5))
```

### Step 3: Assign df_mixed_tz = DataFrame(...)

```python
df_mixed_tz = DataFrame({'A': Timestamp('20130102', tz=gettz('US/Eastern')).as_unit('ns'), 'B': Timestamp('20130102', tz=gettz('EET')).as_unit('ns')}, index=range(5))
```

### Step 4: Assign df_different_tz = DataFrame(...)

```python
df_different_tz = DataFrame({'A': Timestamp('20130102', tz=gettz('US/Eastern')).as_unit('ns'), 'B': Timestamp('20130102', tz=gettz('CET')).as_unit('ns')}, index=range(5))
```

### Step 5: Call _maybe_remove()

```python
_maybe_remove(store, 'df_tz')
```

### Step 6: Call store.append()

```python
store.append('df_tz', df_est, data_columns=['A'])
```

### Step 7: Assign result = value

```python
result = store['df_tz']
```

### Step 8: Call _compare_with_tz()

```python
_compare_with_tz(result, df_est)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df_est)
```

### Step 10: Assign expected = value

```python
expected = df_est[df_est.A >= df_est.A[3]]
```

### Step 11: Assign result = store.select(...)

```python
result = store.select('df_tz', where='A>=df_est.A[3]')
```

### Step 12: Call _compare_with_tz()

```python
_compare_with_tz(result, expected)
```

### Step 13: Call _maybe_remove()

```python
_maybe_remove(store, 'df_tz')
```

### Step 14: Call store.append()

```python
store.append('df_tz', df_crosses_dst)
```

### Step 15: Assign result = value

```python
result = store['df_tz']
```

### Step 16: Call _compare_with_tz()

```python
_compare_with_tz(result, df_crosses_dst)
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df_crosses_dst)
```

### Step 18: Assign msg = 'invalid info for \\[values_block_1\\] for \\[tz\\], existing_value \\[(dateutil/.*)?(US/Eastern|America/New_York)\\] conflicts with new value \\[(dateutil/.*)?EET\\]'

```python
msg = 'invalid info for \\[values_block_1\\] for \\[tz\\], existing_value \\[(dateutil/.*)?(US/Eastern|America/New_York)\\] conflicts with new value \\[(dateutil/.*)?EET\\]'
```

### Step 19: Call _maybe_remove()

```python
_maybe_remove(store, 'df_tz')
```

### Step 20: Call store.append()

```python
store.append('df_tz', df_mixed_tz, data_columns=['A', 'B'])
```

### Step 21: Assign result = value

```python
result = store['df_tz']
```

### Step 22: Call _compare_with_tz()

```python
_compare_with_tz(result, df_mixed_tz)
```

### Step 23: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df_mixed_tz)
```

### Step 24: Assign msg = 'invalid info for \\[B\\] for \\[tz\\], existing_value \\[(dateutil/.*)?EET\\] conflicts with new value \\[(dateutil/.*)?CET\\]'

```python
msg = 'invalid info for \\[B\\] for \\[tz\\], existing_value \\[(dateutil/.*)?EET\\] conflicts with new value \\[(dateutil/.*)?CET\\]'
```

### Step 25: Call store.append()

```python
store.append('df_tz', df_mixed_tz)
```

### Step 26: Call store.append()

```python
store.append('df_tz', df_different_tz)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path, gettz

# Workflow
df_est = DataFrame({'A': [Timestamp('20130102 2:00:00', tz=gettz('US/Eastern')).as_unit('ns') + timedelta(hours=1) * i for i in range(5)]})
df_crosses_dst = DataFrame({'A': Timestamp('20130102', tz=gettz('US/Eastern')).as_unit('ns'), 'B': Timestamp('20130603', tz=gettz('US/Eastern')).as_unit('ns')}, index=range(5))
df_mixed_tz = DataFrame({'A': Timestamp('20130102', tz=gettz('US/Eastern')).as_unit('ns'), 'B': Timestamp('20130102', tz=gettz('EET')).as_unit('ns')}, index=range(5))
df_different_tz = DataFrame({'A': Timestamp('20130102', tz=gettz('US/Eastern')).as_unit('ns'), 'B': Timestamp('20130102', tz=gettz('CET')).as_unit('ns')}, index=range(5))
with ensure_clean_store(setup_path) as store:
    _maybe_remove(store, 'df_tz')
    store.append('df_tz', df_est, data_columns=['A'])
    result = store['df_tz']
    _compare_with_tz(result, df_est)
    tm.assert_frame_equal(result, df_est)
    expected = df_est[df_est.A >= df_est.A[3]]
    result = store.select('df_tz', where='A>=df_est.A[3]')
    _compare_with_tz(result, expected)
    _maybe_remove(store, 'df_tz')
    store.append('df_tz', df_crosses_dst)
    result = store['df_tz']
    _compare_with_tz(result, df_crosses_dst)
    tm.assert_frame_equal(result, df_crosses_dst)
    msg = 'invalid info for \\[values_block_1\\] for \\[tz\\], existing_value \\[(dateutil/.*)?(US/Eastern|America/New_York)\\] conflicts with new value \\[(dateutil/.*)?EET\\]'
    with pytest.raises(ValueError, match=msg):
        store.append('df_tz', df_mixed_tz)
    _maybe_remove(store, 'df_tz')
    store.append('df_tz', df_mixed_tz, data_columns=['A', 'B'])
    result = store['df_tz']
    _compare_with_tz(result, df_mixed_tz)
    tm.assert_frame_equal(result, df_mixed_tz)
    msg = 'invalid info for \\[B\\] for \\[tz\\], existing_value \\[(dateutil/.*)?EET\\] conflicts with new value \\[(dateutil/.*)?CET\\]'
    with pytest.raises(ValueError, match=msg):
        store.append('df_tz', df_different_tz)
```

## Next Steps


---

*Source: test_timezones.py:46 | Complexity: Advanced | Last updated: 2026-06-02*