# How To: Really Large In Arr

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test really large in arr

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `numpy`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: large_val, signed, transform, multiple_elts, errors
```

## Step-by-Step Guide

### Step 1: Assign kwargs = value

```python
kwargs = {'errors': errors} if errors is not None else {}
```

### Step 2: Assign val = value

```python
val = -large_val if signed else large_val
```

### Step 3: Assign val = transform(...)

```python
val = transform(val)
```

### Step 4: Assign extra_elt = 'string'

```python
extra_elt = 'string'
```

### Step 5: Assign arr = value

```python
arr = [val] + multiple_elts * [extra_elt]
```

### Step 6: Assign val_is_string = isinstance(...)

```python
val_is_string = isinstance(val, str)
```

### Step 7: Assign coercing = value

```python
coercing = errors == 'coerce'
```

### Step 8: Assign result = to_numeric(...)

```python
result = to_numeric(arr, **kwargs)
```

### Step 9: Assign exp_val = value

```python
exp_val = float(val) if coercing and val_is_string else val
```

### Step 10: Assign expected = value

```python
expected = [exp_val]
```

### Step 11: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, np.array(expected, dtype=exp_dtype))
```

### Step 12: Assign msg = 'Integer out of range. at position 0'

```python
msg = 'Integer out of range. at position 0'
```

### Step 13: Assign msg = 'Unable to parse string "string" at position 1'

```python
msg = 'Unable to parse string "string" at position 1'
```

### Step 14: Call to_numeric()

```python
to_numeric(arr, **kwargs)
```

### Step 15: Assign exp_dtype = value

```python
exp_dtype = float if isinstance(exp_val, (int, float)) else object
```

### Step 16: Call expected.append()

```python
expected.append(np.nan)
```

### Step 17: Assign exp_dtype = float

```python
exp_dtype = float
```

### Step 18: Call expected.append()

```python
expected.append(extra_elt)
```

### Step 19: Assign exp_dtype = object

```python
exp_dtype = object
```


## Complete Example

```python
# Setup
# Fixtures: large_val, signed, transform, multiple_elts, errors

# Workflow
kwargs = {'errors': errors} if errors is not None else {}
val = -large_val if signed else large_val
val = transform(val)
extra_elt = 'string'
arr = [val] + multiple_elts * [extra_elt]
val_is_string = isinstance(val, str)
coercing = errors == 'coerce'
if errors in (None, 'raise') and (val_is_string or multiple_elts):
    if val_is_string:
        msg = 'Integer out of range. at position 0'
    else:
        msg = 'Unable to parse string "string" at position 1'
    with pytest.raises(ValueError, match=msg):
        to_numeric(arr, **kwargs)
else:
    result = to_numeric(arr, **kwargs)
    exp_val = float(val) if coercing and val_is_string else val
    expected = [exp_val]
    if multiple_elts:
        if coercing:
            expected.append(np.nan)
            exp_dtype = float
        else:
            expected.append(extra_elt)
            exp_dtype = object
    else:
        exp_dtype = float if isinstance(exp_val, (int, float)) else object
    tm.assert_almost_equal(result, np.array(expected, dtype=exp_dtype))
```

## Next Steps


---

*Source: test_to_numeric.py:275 | Complexity: Advanced | Last updated: 2026-06-02*