# How To: Arraylike

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arraylike

## Prerequisites

**Required Modules:**
- `datetime`
- `locale`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.tools.times`


## Step-by-Step Guide

### Step 1: Assign arg = value

```python
arg = ['14:15', '20:20']
```

**Verification:**
```python
assert to_time(arg) == expected_arr
```

### Step 2: Assign expected_arr = value

```python
expected_arr = [time(14, 15), time(20, 20)]
```

**Verification:**
```python
assert to_time(arg, format='%H:%M') == expected_arr
```

### Step 3: Assign msg = "errors='ignore' is deprecated"

```python
msg = "errors='ignore' is deprecated"
```

**Verification:**
```python
assert to_time(arg, infer_time_format=True) == expected_arr
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, np.array(arg, dtype=np.object_))
```

**Verification:**
```python
assert to_time(arg, format='%I:%M%p', errors='coerce') == [None, None]
```

### Step 5: Assign msg = 'Cannot convert.+to a time with given format'

```python
msg = 'Cannot convert.+to a time with given format'
```

**Verification:**
```python
assert isinstance(res, list)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(to_time(Series(arg, name='test')), Series(expected_arr, name='test'))
```

**Verification:**
```python
assert res == expected_arr
```

### Step 7: Assign res = to_time(...)

```python
res = to_time(np.array(arg))
```

**Verification:**
```python
assert isinstance(res, list)
```

### Step 8: Assign res = to_time(...)

```python
res = to_time(arg, format='%I:%M%p', errors='ignore')
```

### Step 9: Call to_time()

```python
to_time(arg, format='%I:%M%p', errors='raise')
```


## Complete Example

```python
# Workflow
arg = ['14:15', '20:20']
expected_arr = [time(14, 15), time(20, 20)]
assert to_time(arg) == expected_arr
assert to_time(arg, format='%H:%M') == expected_arr
assert to_time(arg, infer_time_format=True) == expected_arr
assert to_time(arg, format='%I:%M%p', errors='coerce') == [None, None]
msg = "errors='ignore' is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = to_time(arg, format='%I:%M%p', errors='ignore')
tm.assert_numpy_array_equal(res, np.array(arg, dtype=np.object_))
msg = 'Cannot convert.+to a time with given format'
with pytest.raises(ValueError, match=msg):
    to_time(arg, format='%I:%M%p', errors='raise')
tm.assert_series_equal(to_time(Series(arg, name='test')), Series(expected_arr, name='test'))
res = to_time(np.array(arg))
assert isinstance(res, list)
assert res == expected_arr
```

## Next Steps


---

*Source: test_to_time.py:49 | Complexity: Advanced | Last updated: 2026-06-02*