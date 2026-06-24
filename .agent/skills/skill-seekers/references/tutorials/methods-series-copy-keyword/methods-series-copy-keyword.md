# How To: Methods Series Copy Keyword

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test methods series copy keyword

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: request, method, copy, using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign index = None

```python
index = None
```

**Verification:**
```python
assert np.shares_memory(get_array(ser2), get_array(ser))
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1, 2, 3], index=index)
```

**Verification:**
```python
assert not np.shares_memory(get_array(ser2), get_array(ser))
```

### Step 3: Assign share_memory = value

```python
share_memory = using_copy_on_write or copy is False
```

### Step 4: Assign index = period_range(...)

```python
index = period_range('2012-01-01', freq='D', periods=3)
```

### Step 5: Assign msg = "'Series.swapaxes' is deprecated"

```python
msg = "'Series.swapaxes' is deprecated"
```

### Step 6: Assign ser2 = method(...)

```python
ser2 = method(ser, copy=copy)
```

**Verification:**
```python
assert np.shares_memory(get_array(ser2), get_array(ser))
```

### Step 7: Assign index = date_range(...)

```python
index = date_range('2012-01-01', freq='D', periods=3)
```

### Step 8: Assign ser2 = method(...)

```python
ser2 = method(ser, copy=copy)
```

### Step 9: Assign index = date_range(...)

```python
index = date_range('2012-01-01', freq='D', periods=3)
```

### Step 10: Assign index = date_range(...)

```python
index = date_range('2012-01-01', freq='D', periods=3, tz='Europe/Brussels')
```

### Step 11: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays([[1, 2, 3], [4, 5, 6]])
```


## Complete Example

```python
# Setup
# Fixtures: request, method, copy, using_copy_on_write

# Workflow
index = None
if 'to_timestamp' in request.node.callspec.id:
    index = period_range('2012-01-01', freq='D', periods=3)
elif 'to_period' in request.node.callspec.id:
    index = date_range('2012-01-01', freq='D', periods=3)
elif 'tz_localize' in request.node.callspec.id:
    index = date_range('2012-01-01', freq='D', periods=3)
elif 'tz_convert' in request.node.callspec.id:
    index = date_range('2012-01-01', freq='D', periods=3, tz='Europe/Brussels')
elif 'swaplevel' in request.node.callspec.id:
    index = MultiIndex.from_arrays([[1, 2, 3], [4, 5, 6]])
ser = Series([1, 2, 3], index=index)
if 'swapaxes' in request.node.callspec.id:
    msg = "'Series.swapaxes' is deprecated"
    with tm.assert_produces_warning(FutureWarning, match=msg):
        ser2 = method(ser, copy=copy)
else:
    ser2 = method(ser, copy=copy)
share_memory = using_copy_on_write or copy is False
if share_memory:
    assert np.shares_memory(get_array(ser2), get_array(ser))
else:
    assert not np.shares_memory(get_array(ser2), get_array(ser))
```

## Next Steps


---

*Source: test_methods.py:204 | Complexity: Advanced | Last updated: 2026-06-02*