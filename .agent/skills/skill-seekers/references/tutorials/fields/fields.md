# How To: Fields

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fields

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = timedelta_range(...)

```python
rng = timedelta_range('1 days, 10:11:12.100123456', periods=2, freq='s')
```

**Verification:**
```python
assert rng.days.name == 'name'
```

### Step 2: Call tm.assert_index_equal()

```python
tm.assert_index_equal(rng.days, Index([1, 1], dtype=np.int64))
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(rng.seconds, Index([10 * 3600 + 11 * 60 + 12, 10 * 3600 + 11 * 60 + 13], dtype=np.int32))
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(rng.microseconds, Index([100 * 1000 + 123, 100 * 1000 + 123], dtype=np.int32))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(rng.nanoseconds, Index([456, 456], dtype=np.int32))
```

### Step 6: Assign msg = "'TimedeltaIndex' object has no attribute '{}'"

```python
msg = "'TimedeltaIndex' object has no attribute '{}'"
```

### Step 7: Assign s = Series(...)

```python
s = Series(rng)
```

### Step 8: Assign unknown = value

```python
s[1] = np.nan
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s.dt.days, Series([1, np.nan], index=[0, 1]))
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s.dt.seconds, Series([10 * 3600 + 11 * 60 + 12, np.nan], index=[0, 1]))
```

### Step 11: Assign rng.name = 'name'

```python
rng.name = 'name'
```

**Verification:**
```python
assert rng.days.name == 'name'
```

### Step 12: rng.hours

```python
rng.hours
```

### Step 13: rng.minutes

```python
rng.minutes
```

### Step 14: rng.milliseconds

```python
rng.milliseconds
```


## Complete Example

```python
# Workflow
rng = timedelta_range('1 days, 10:11:12.100123456', periods=2, freq='s')
tm.assert_index_equal(rng.days, Index([1, 1], dtype=np.int64))
tm.assert_index_equal(rng.seconds, Index([10 * 3600 + 11 * 60 + 12, 10 * 3600 + 11 * 60 + 13], dtype=np.int32))
tm.assert_index_equal(rng.microseconds, Index([100 * 1000 + 123, 100 * 1000 + 123], dtype=np.int32))
tm.assert_index_equal(rng.nanoseconds, Index([456, 456], dtype=np.int32))
msg = "'TimedeltaIndex' object has no attribute '{}'"
with pytest.raises(AttributeError, match=msg.format('hours')):
    rng.hours
with pytest.raises(AttributeError, match=msg.format('minutes')):
    rng.minutes
with pytest.raises(AttributeError, match=msg.format('milliseconds')):
    rng.milliseconds
s = Series(rng)
s[1] = np.nan
tm.assert_series_equal(s.dt.days, Series([1, np.nan], index=[0, 1]))
tm.assert_series_equal(s.dt.seconds, Series([10 * 3600 + 11 * 60 + 12, np.nan], index=[0, 1]))
rng.name = 'name'
assert rng.days.name == 'name'
```

## Next Steps


---

*Source: test_timedelta.py:29 | Complexity: Advanced | Last updated: 2026-06-02*