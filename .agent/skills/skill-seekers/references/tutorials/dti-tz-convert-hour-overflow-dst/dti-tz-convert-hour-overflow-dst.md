# How To: Dti Tz Convert Hour Overflow Dst

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti tz convert hour overflow dst

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign ts = value

```python
ts = ['2008-05-12 09:50:00', '2008-12-12 09:50:35', '2009-05-12 09:50:32']
```

### Step 2: Assign tt = DatetimeIndex.tz_localize(...)

```python
tt = DatetimeIndex(ts).tz_localize('US/Eastern')
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
ts = ['2008-05-12 13:50:00', '2008-12-12 14:50:35', '2009-05-12 13:50:32']
```

### Step 7: Assign tt = DatetimeIndex.tz_localize(...)

```python
tt = DatetimeIndex(ts).tz_localize('UTC')
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
ts = ['2008-05-12 09:50:00', '2008-12-12 09:50:35', '2008-05-12 09:50:32']
```

### Step 12: Assign tt = DatetimeIndex.tz_localize(...)

```python
tt = DatetimeIndex(ts).tz_localize('US/Eastern')
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
ts = ['2008-05-12 13:50:00', '2008-12-12 14:50:35', '2008-05-12 13:50:32']
```

### Step 17: Assign tt = DatetimeIndex.tz_localize(...)

```python
tt = DatetimeIndex(ts).tz_localize('UTC')
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
# Workflow
ts = ['2008-05-12 09:50:00', '2008-12-12 09:50:35', '2009-05-12 09:50:32']
tt = DatetimeIndex(ts).tz_localize('US/Eastern')
ut = tt.tz_convert('UTC')
expected = Index([13, 14, 13], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)
ts = ['2008-05-12 13:50:00', '2008-12-12 14:50:35', '2009-05-12 13:50:32']
tt = DatetimeIndex(ts).tz_localize('UTC')
ut = tt.tz_convert('US/Eastern')
expected = Index([9, 9, 9], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)
ts = ['2008-05-12 09:50:00', '2008-12-12 09:50:35', '2008-05-12 09:50:32']
tt = DatetimeIndex(ts).tz_localize('US/Eastern')
ut = tt.tz_convert('UTC')
expected = Index([13, 14, 13], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)
ts = ['2008-05-12 13:50:00', '2008-12-12 14:50:35', '2008-05-12 13:50:32']
tt = DatetimeIndex(ts).tz_localize('UTC')
ut = tt.tz_convert('US/Eastern')
expected = Index([9, 9, 9], dtype=np.int32)
tm.assert_index_equal(ut.hour, expected)
```

## Next Steps


---

*Source: test_tz_convert.py:67 | Complexity: Advanced | Last updated: 2026-06-02*