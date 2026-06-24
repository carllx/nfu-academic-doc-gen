# How To: Dti Tz Convert Hour Overflow Dst Timestamps

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dti tz convert hour overflow dst timestamps

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign ts = value

```python
ts = [Timestamp('2008-05-12 09:50:00', tz=tz), Timestamp('2008-12-12 09:50:35', tz=tz), Timestamp('2009-05-12 09:50:32', tz=tz)]
```

### Step 2: Assign tt = DatetimeIndex(...)

```python
tt = DatetimeIndex(ts)
```

### Step 3: Assign ut = tt.tz_convert(...)

```python
ut = tt.tz_convert('UTC')
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([13, 14, 13], dtype=np.int32)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(ut.hour, expected)
```

### Step 6: Assign ts = value

```python
ts = [Timestamp('2008-05-12 13:50:00', tz='UTC'), Timestamp('2008-12-12 14:50:35', tz='UTC'), Timestamp('2009-05-12 13:50:32', tz='UTC')]
```

### Step 7: Assign tt = DatetimeIndex(...)

```python
tt = DatetimeIndex(ts)
```

### Step 8: Assign ut = tt.tz_convert(...)

```python
ut = tt.tz_convert('US/Eastern')
```

### Step 9: Assign expected = Index(...)

```python
expected = Index([9, 9, 9], dtype=np.int32)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(ut.hour, expected)
```

### Step 11: Assign ts = value

```python
ts = [Timestamp('2008-05-12 09:50:00', tz=tz), Timestamp('2008-12-12 09:50:35', tz=tz), Timestamp('2008-05-12 09:50:32', tz=tz)]
```

### Step 12: Assign tt = DatetimeIndex(...)

```python
tt = DatetimeIndex(ts)
```

### Step 13: Assign ut = tt.tz_convert(...)

```python
ut = tt.tz_convert('UTC')
```

### Step 14: Assign expected = Index(...)

```python
expected = Index([13, 14, 13], dtype=np.int32)
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(ut.hour, expected)
```

### Step 16: Assign ts = value

```python
ts = [Timestamp('2008-05-12 13:50:00', tz='UTC'), Timestamp('2008-12-12 14:50:35', tz='UTC'), Timestamp('2008-05-12 13:50:32', tz='UTC')]
```

### Step 17: Assign tt = DatetimeIndex(...)

```python
tt = DatetimeIndex(ts)
```

### Step 18: Assign ut = tt.tz_convert(...)

```python
ut = tt.tz_convert('US/Eastern')
```

### Step 19: Assign expected = Index(...)

```python
expected = Index([9, 9, 9], dtype=np.int32)
```

### Step 20: Call tm.assert_index_equal()

```python
tm.assert_index_equal(ut.hour, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
ts = [Timestamp('2008-05-12 09:50:00', tz=tz), Timestamp('2008-12-12 09:50:35', tz=tz), Timestamp('2009-05-12 09:50:32', tz=tz)]
tt = DatetimeIndex(ts)
ut = tt.tz_convert('UTC')
expected = Index([13, 14, 13], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)
ts = [Timestamp('2008-05-12 13:50:00', tz='UTC'), Timestamp('2008-12-12 14:50:35', tz='UTC'), Timestamp('2009-05-12 13:50:32', tz='UTC')]
tt = DatetimeIndex(ts)
ut = tt.tz_convert('US/Eastern')
expected = Index([9, 9, 9], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)
ts = [Timestamp('2008-05-12 09:50:00', tz=tz), Timestamp('2008-12-12 09:50:35', tz=tz), Timestamp('2008-05-12 09:50:32', tz=tz)]
tt = DatetimeIndex(ts)
ut = tt.tz_convert('UTC')
expected = Index([13, 14, 13], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)
ts = [Timestamp('2008-05-12 13:50:00', tz='UTC'), Timestamp('2008-12-12 14:50:35', tz='UTC'), Timestamp('2008-05-12 13:50:32', tz='UTC')]
tt = DatetimeIndex(ts)
ut = tt.tz_convert('US/Eastern')
expected = Index([9, 9, 9], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)
```

## Next Steps


---

*Source: test_tz_convert.py:99 | Complexity: Advanced | Last updated: 2026-06-02*