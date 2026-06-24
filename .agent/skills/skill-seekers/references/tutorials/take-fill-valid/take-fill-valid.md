# How To: Take Fill Valid

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test take fill valid

## Prerequisites

**Required Modules:**
- `__future__`
- `re`
- `warnings`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs.dtypes`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = arr1d

```python
arr = arr1d
```

**Verification:**
```python
assert result[0] == now
```

### Step 2: Assign dti = self.index_cls(...)

```python
dti = self.index_cls(arr1d)
```

### Step 3: Assign now = fixed_now_ts.tz_localize(...)

```python
now = fixed_now_ts.tz_localize(dti.tz)
```

### Step 4: Assign result = arr.take(...)

```python
result = arr.take([-1, 1], allow_fill=True, fill_value=now)
```

**Verification:**
```python
assert result[0] == now
```

### Step 5: Assign msg = value

```python
msg = f"value should be a '{arr1d._scalar_type.__name__}' or 'NaT'. Got"
```

### Step 6: Assign tz = value

```python
tz = None if dti.tz is not None else 'US/Eastern'
```

### Step 7: Assign now = fixed_now_ts.tz_localize(...)

```python
now = fixed_now_ts.tz_localize(tz)
```

### Step 8: Assign msg = 'Cannot compare tz-naive and tz-aware datetime-like objects'

```python
msg = 'Cannot compare tz-naive and tz-aware datetime-like objects'
```

### Step 9: Assign value = value

```python
value = NaT._value
```

### Step 10: Assign msg = value

```python
msg = f"value should be a '{arr1d._scalar_type.__name__}' or 'NaT'. Got"
```

### Step 11: Assign value = np.timedelta64(...)

```python
value = np.timedelta64('NaT', 'ns')
```

### Step 12: Call arr.take()

```python
arr.take([-1, 1], allow_fill=True, fill_value=now - now)
```

### Step 13: Call arr.take()

```python
arr.take([-1, 1], allow_fill=True, fill_value=Period('2014Q1'))
```

### Step 14: Call arr.take()

```python
arr.take([-1, 1], allow_fill=True, fill_value=now)
```

### Step 15: Call arr.take()

```python
arr.take([-1, 1], allow_fill=True, fill_value=value)
```

### Step 16: Call arr.take()

```python
arr.take([-1, 1], allow_fill=True, fill_value=value)
```

### Step 17: Assign value = fixed_now_ts.tz_localize(...)

```python
value = fixed_now_ts.tz_localize('Australia/Melbourne')
```

### Step 18: Assign result = arr.take(...)

```python
result = arr.take([-1, 1], allow_fill=True, fill_value=value)
```

### Step 19: Assign expected = arr.take(...)

```python
expected = arr.take([-1, 1], allow_fill=True, fill_value=value.tz_convert(arr.dtype.tz))
```

### Step 20: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = arr1d
dti = self.index_cls(arr1d)
now = fixed_now_ts.tz_localize(dti.tz)
result = arr.take([-1, 1], allow_fill=True, fill_value=now)
assert result[0] == now
msg = f"value should be a '{arr1d._scalar_type.__name__}' or 'NaT'. Got"
with pytest.raises(TypeError, match=msg):
    arr.take([-1, 1], allow_fill=True, fill_value=now - now)
with pytest.raises(TypeError, match=msg):
    arr.take([-1, 1], allow_fill=True, fill_value=Period('2014Q1'))
tz = None if dti.tz is not None else 'US/Eastern'
now = fixed_now_ts.tz_localize(tz)
msg = 'Cannot compare tz-naive and tz-aware datetime-like objects'
with pytest.raises(TypeError, match=msg):
    arr.take([-1, 1], allow_fill=True, fill_value=now)
value = NaT._value
msg = f"value should be a '{arr1d._scalar_type.__name__}' or 'NaT'. Got"
with pytest.raises(TypeError, match=msg):
    arr.take([-1, 1], allow_fill=True, fill_value=value)
value = np.timedelta64('NaT', 'ns')
with pytest.raises(TypeError, match=msg):
    arr.take([-1, 1], allow_fill=True, fill_value=value)
if arr.tz is not None:
    value = fixed_now_ts.tz_localize('Australia/Melbourne')
    result = arr.take([-1, 1], allow_fill=True, fill_value=value)
    expected = arr.take([-1, 1], allow_fill=True, fill_value=value.tz_convert(arr.dtype.tz))
    tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimelike.py:808 | Complexity: Advanced | Last updated: 2026-06-02*