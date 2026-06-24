# How To: Numpy Array Equivalence

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numpy array equivalence

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

### Step 4: Assign numpy_array = np.array(...)

```python
numpy_array = np.array([scalar] * len(data), dtype=data.dtype.numpy_dtype)
```

### Step 5: Assign pd_array = pd.array(...)

```python
pd_array = pd.array(numpy_array, dtype=data.dtype)
```

### Step 6: Assign result = op(...)

```python
result = op(data, numpy_array)
```

### Step 7: Assign expected = op(...)

```python
expected = op(data, pd_array)
```

### Step 8: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 9: Assign msg = "operator '.*' not implemented for bool dtypes"

```python
msg = "operator '.*' not implemented for bool dtypes"
```

### Step 10: Call op()

```python
op(data, numpy_array)
```

### Step 11: Call op()

```python
op(data, pd_array)
```


## Complete Example

```python
# Setup
# Fixtures: data, all_arithmetic_operators

# Workflow
data, scalar = data
op = tm.get_op_from_name(all_arithmetic_operators)
check_skip(data, all_arithmetic_operators)
numpy_array = np.array([scalar] * len(data), dtype=data.dtype.numpy_dtype)
pd_array = pd.array(numpy_array, dtype=data.dtype)
if is_bool_not_implemented(data, all_arithmetic_operators):
    msg = "operator '.*' not implemented for bool dtypes"
    with pytest.raises(NotImplementedError, match=msg):
        op(data, numpy_array)
    with pytest.raises(NotImplementedError, match=msg):
        op(data, pd_array)
    return
result = op(data, numpy_array)
expected = op(data, pd_array)
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:99 | Complexity: Advanced | Last updated: 2026-06-02*