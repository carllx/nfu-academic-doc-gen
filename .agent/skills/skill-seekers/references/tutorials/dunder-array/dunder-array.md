# How To: Dunder Array

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dunder array

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: array
```

## Step-by-Step Guide

### Step 1: Assign obj = PeriodIndex(...)

```python
obj = PeriodIndex(['2000-01-01', '2001-01-01'], freq='D')
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array([obj[0], obj[1]], dtype=object)
```

### Step 3: Assign result = np.array(...)

```python
result = np.array(obj)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = np.asarray(...)

```python
result = np.asarray(obj)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Assign expected = value

```python
expected = obj.asi8
```

### Step 8: Assign obj = value

```python
obj = obj._data
```

### Step 9: Assign result = np.array(...)

```python
result = np.array(obj, dtype=dtype)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 11: Assign result = np.asarray(...)

```python
result = np.asarray(obj, dtype=dtype)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 13: Assign msg = 'argument must be'

```python
msg = 'argument must be'
```

### Step 14: Call np.array()

```python
np.array(obj, dtype=dtype)
```

### Step 15: Call np.array()

```python
np.array(obj, dtype=getattr(np, dtype))
```


## Complete Example

```python
# Setup
# Fixtures: array

# Workflow
obj = PeriodIndex(['2000-01-01', '2001-01-01'], freq='D')
if array:
    obj = obj._data
expected = np.array([obj[0], obj[1]], dtype=object)
result = np.array(obj)
tm.assert_numpy_array_equal(result, expected)
result = np.asarray(obj)
tm.assert_numpy_array_equal(result, expected)
expected = obj.asi8
for dtype in ['i8', 'int64', np.int64]:
    result = np.array(obj, dtype=dtype)
    tm.assert_numpy_array_equal(result, expected)
    result = np.asarray(obj, dtype=dtype)
    tm.assert_numpy_array_equal(result, expected)
for dtype in ['float64', 'int32', 'uint64']:
    msg = 'argument must be'
    with pytest.raises(TypeError, match=msg):
        np.array(obj, dtype=dtype)
    with pytest.raises(TypeError, match=msg):
        np.array(obj, dtype=getattr(np, dtype))
```

## Next Steps


---

*Source: test_period.py:206 | Complexity: Advanced | Last updated: 2026-06-02*