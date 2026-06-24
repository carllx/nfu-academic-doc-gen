# How To: Array Na

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array NA

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
# Fixtures: data, all_arithmetic_operators
```

## Step-by-Step Guide

### Step 1: Assign unknown = data

```python
data, _ = data
```

### Step 2: Assign op = tm.get_op_from_name(...)

```python
op = tm.get_op_from_name(all_arithmetic_operators)
```

### Step 3: Call check_skip()

```python
check_skip(data, all_arithmetic_operators)
```

### Step 4: Assign scalar = value

```python
scalar = pd.NA
```

### Step 5: Assign scalar_array = pd.array(...)

```python
scalar_array = pd.array([pd.NA] * len(data), dtype=data.dtype)
```

### Step 6: Assign mask = data._mask.copy(...)

```python
mask = data._mask.copy()
```

### Step 7: Assign result = op(...)

```python
result = op(data, scalar)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(mask, data._mask)
```

### Step 9: Assign expected = op(...)

```python
expected = op(data, scalar_array)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(mask, data._mask)
```

### Step 11: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 12: Assign msg = "operator '.*' not implemented for bool dtypes"

```python
msg = "operator '.*' not implemented for bool dtypes"
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(mask, data._mask)
```

### Step 14: Call op()

```python
op(data, scalar)
```


## Complete Example

```python
# Setup
# Fixtures: data, all_arithmetic_operators

# Workflow
data, _ = data
op = tm.get_op_from_name(all_arithmetic_operators)
check_skip(data, all_arithmetic_operators)
scalar = pd.NA
scalar_array = pd.array([pd.NA] * len(data), dtype=data.dtype)
mask = data._mask.copy()
if is_bool_not_implemented(data, all_arithmetic_operators):
    msg = "operator '.*' not implemented for bool dtypes"
    with pytest.raises(NotImplementedError, match=msg):
        op(data, scalar)
    tm.assert_numpy_array_equal(mask, data._mask)
    return
result = op(data, scalar)
tm.assert_numpy_array_equal(mask, data._mask)
expected = op(data, scalar_array)
tm.assert_numpy_array_equal(mask, data._mask)
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:71 | Complexity: Advanced | Last updated: 2026-06-02*