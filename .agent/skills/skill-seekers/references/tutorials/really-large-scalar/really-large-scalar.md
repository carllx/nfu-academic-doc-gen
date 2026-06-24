# How To: Really Large Scalar

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test really large scalar

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
# Fixtures: large_val, signed, transform, errors
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

### Step 4: Assign val_is_string = isinstance(...)

```python
val_is_string = isinstance(val, str)
```

### Step 5: Assign msg = 'Integer out of range. at position 0'

```python
msg = 'Integer out of range. at position 0'
```

### Step 6: Assign expected = value

```python
expected = float(val) if errors == 'coerce' and val_is_string else val
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(to_numeric(val, **kwargs), expected)
```

### Step 8: Call to_numeric()

```python
to_numeric(val, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: large_val, signed, transform, errors

# Workflow
kwargs = {'errors': errors} if errors is not None else {}
val = -large_val if signed else large_val
val = transform(val)
val_is_string = isinstance(val, str)
if val_is_string and errors in (None, 'raise'):
    msg = 'Integer out of range. at position 0'
    with pytest.raises(ValueError, match=msg):
        to_numeric(val, **kwargs)
else:
    expected = float(val) if errors == 'coerce' and val_is_string else val
    tm.assert_almost_equal(to_numeric(val, **kwargs), expected)
```

## Next Steps


---

*Source: test_to_numeric.py:257 | Complexity: Advanced | Last updated: 2026-06-02*