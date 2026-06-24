# How To: Astype Dict Like

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test astype dict like

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `importlib`
- `string`
- `sys`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dtype_class
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(range(0, 10, 2), name='abc')
```

### Step 2: Assign dt1 = dtype_class(...)

```python
dt1 = dtype_class({'abc': str})
```

### Step 3: Assign result = ser.astype(...)

```python
result = ser.astype(dt1)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(['0', '2', '4', '6', '8'], name='abc', dtype='str')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign dt2 = dtype_class(...)

```python
dt2 = dtype_class({'abc': 'float64'})
```

### Step 7: Assign result = ser.astype(...)

```python
result = ser.astype(dt2)
```

### Step 8: Assign expected = Series(...)

```python
expected = Series([0.0, 2.0, 4.0, 6.0, 8.0], dtype='float64', name='abc')
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign dt3 = dtype_class(...)

```python
dt3 = dtype_class({'abc': str, 'def': str})
```

### Step 11: Assign msg = 'Only the Series name can be used for the key in Series dtype mappings\\.'

```python
msg = 'Only the Series name can be used for the key in Series dtype mappings\\.'
```

### Step 12: Assign dt4 = dtype_class(...)

```python
dt4 = dtype_class({0: str})
```

### Step 13: Call ser.astype()

```python
ser.astype(dt3)
```

### Step 14: Call ser.astype()

```python
ser.astype(dt4)
```

### Step 15: Assign dt5 = dtype_class(...)

```python
dt5 = dtype_class({}, dtype=object)
```

### Step 16: Assign dt5 = dtype_class(...)

```python
dt5 = dtype_class({})
```

### Step 17: Call ser.astype()

```python
ser.astype(dt5)
```


## Complete Example

```python
# Setup
# Fixtures: dtype_class

# Workflow
ser = Series(range(0, 10, 2), name='abc')
dt1 = dtype_class({'abc': str})
result = ser.astype(dt1)
expected = Series(['0', '2', '4', '6', '8'], name='abc', dtype='str')
tm.assert_series_equal(result, expected)
dt2 = dtype_class({'abc': 'float64'})
result = ser.astype(dt2)
expected = Series([0.0, 2.0, 4.0, 6.0, 8.0], dtype='float64', name='abc')
tm.assert_series_equal(result, expected)
dt3 = dtype_class({'abc': str, 'def': str})
msg = 'Only the Series name can be used for the key in Series dtype mappings\\.'
with pytest.raises(KeyError, match=msg):
    ser.astype(dt3)
dt4 = dtype_class({0: str})
with pytest.raises(KeyError, match=msg):
    ser.astype(dt4)
if dtype_class is Series:
    dt5 = dtype_class({}, dtype=object)
else:
    dt5 = dtype_class({})
with pytest.raises(KeyError, match=msg):
    ser.astype(dt5)
```

## Next Steps


---

*Source: test_astype.py:73 | Complexity: Advanced | Last updated: 2026-06-02*