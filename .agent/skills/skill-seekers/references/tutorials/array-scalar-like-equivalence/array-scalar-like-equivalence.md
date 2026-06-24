# How To: Array Scalar Like Equivalence

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array scalar like equivalence

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
data, scalar = data
```

### Step 2: Assign op = tm.get_op_from_name(...)

```python
op = tm.get_op_from_name(all_arithmetic_operators)
```

### Step 3: Call check_skip()

```python
check_skip(data, all_arithmetic_operators)
```

### Step 4: Assign scalar_array = pd.array(...)

```python
scalar_array = pd.array([scalar] * len(data), dtype=data.dtype)
```

### Step 5: Assign msg = "operator '.*' not implemented for bool dtypes"

```python
msg = "operator '.*' not implemented for bool dtypes"
```

### Step 6: Assign result = op(...)

```python
result = op(data, scalar)
```

### Step 7: Assign expected = op(...)

```python
expected = op(data, scalar_array)
```

### Step 8: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 9: Call op()

```python
op(data, scalar)
```

### Step 10: Call op()

```python
op(data, scalar_array)
```


## Complete Example

```python
# Setup
# Fixtures: data, all_arithmetic_operators

# Workflow
data, scalar = data
op = tm.get_op_from_name(all_arithmetic_operators)
check_skip(data, all_arithmetic_operators)
scalar_array = pd.array([scalar] * len(data), dtype=data.dtype)
for scalar in [scalar, data.dtype.type(scalar)]:
    if is_bool_not_implemented(data, all_arithmetic_operators):
        msg = "operator '.*' not implemented for bool dtypes"
        with pytest.raises(NotImplementedError, match=msg):
            op(data, scalar)
        with pytest.raises(NotImplementedError, match=msg):
            op(data, scalar_array)
    else:
        result = op(data, scalar)
        expected = op(data, scalar_array)
        tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:50 | Complexity: Advanced | Last updated: 2026-06-02*