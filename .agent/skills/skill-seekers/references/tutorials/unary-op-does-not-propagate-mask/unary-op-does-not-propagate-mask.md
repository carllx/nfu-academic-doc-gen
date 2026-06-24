# How To: Unary Op Does Not Propagate Mask

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unary op does not propagate mask

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `typing`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: data, op
```

## Step-by-Step Guide

### Step 1: Assign unknown = data

```python
data, _ = data
```

### Step 2: Assign ser = pd.Series(...)

```python
ser = pd.Series(data)
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(ser, op)()
```

### Step 4: Assign expected = result.copy(...)

```python
expected = result.copy(deep=True)
```

### Step 5: Assign unknown = None

```python
ser[0] = None
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign msg = "ufunc 'invert' not supported for the input types"

```python
msg = "ufunc 'invert' not supported for the input types"
```

### Step 8: Call getattr()

```python
getattr(ser, op)()
```

### Step 9: Call getattr()

```python
getattr(data, op)()
```

### Step 10: Call getattr()

```python
getattr(data._data, op)()
```


## Complete Example

```python
# Setup
# Fixtures: data, op

# Workflow
data, _ = data
ser = pd.Series(data)
if op == '__invert__' and data.dtype.kind == 'f':
    msg = "ufunc 'invert' not supported for the input types"
    with pytest.raises(TypeError, match=msg):
        getattr(ser, op)()
    with pytest.raises(TypeError, match=msg):
        getattr(data, op)()
    with pytest.raises(TypeError, match=msg):
        getattr(data._data, op)()
    return
result = getattr(ser, op)()
expected = result.copy(deep=True)
ser[0] = None
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:227 | Complexity: Advanced | Last updated: 2026-06-02*