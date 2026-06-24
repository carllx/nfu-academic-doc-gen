# How To: Logical Operators

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test logical operators

## Prerequisites

**Required Modules:**
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = value

```python
df1 = {'a': {'a': True, 'b': False, 'c': False, 'd': True, 'e': True}, 'b': {'a': False, 'b': True, 'c': False, 'd': False, 'e': False}, 'c': {'a': False, 'b': False, 'c': True, 'd': False, 'e': False}, 'd': {'a': True, 'b': False, 'c': False, 'd': True, 'e': True}, 'e': {'a': True, 'b': False, 'c': False, 'd': True, 'e': True}}
```

**Verification:**
```python
assert result.values.dtype == np.bool_
```

### Step 2: Assign df2 = value

```python
df2 = {'a': {'a': True, 'b': False, 'c': True, 'd': False, 'e': False}, 'b': {'a': False, 'b': True, 'c': False, 'd': False, 'e': False}, 'c': {'a': True, 'b': False, 'c': True, 'd': False, 'e': False}, 'd': {'a': False, 'b': False, 'c': False, 'd': True, 'e': False}, 'e': {'a': False, 'b': False, 'c': False, 'd': False, 'e': True}}
```

**Verification:**
```python
assert result.values.dtype == np.bool_
```

### Step 3: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(df1)
```

### Step 4: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(df2)
```

### Step 5: Call _check_bin_op()

```python
_check_bin_op(operator.and_)
```

### Step 6: Call _check_bin_op()

```python
_check_bin_op(operator.or_)
```

### Step 7: Call _check_bin_op()

```python
_check_bin_op(operator.xor)
```

### Step 8: Call _check_unary_op()

```python
_check_unary_op(operator.inv)
```

### Step 9: Assign result = op(...)

```python
result = op(df1, df2)
```

### Step 10: Assign expected = DataFrame(...)

```python
expected = DataFrame(op(df1.values, df2.values), index=df1.index, columns=df1.columns)
```

**Verification:**
```python
assert result.values.dtype == np.bool_
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Assign result = op(...)

```python
result = op(df1)
```

### Step 13: Assign expected = DataFrame(...)

```python
expected = DataFrame(op(df1.values), index=df1.index, columns=df1.columns)
```

**Verification:**
```python
assert result.values.dtype == np.bool_
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
def _check_bin_op(op):
    result = op(df1, df2)
    expected = DataFrame(op(df1.values, df2.values), index=df1.index, columns=df1.columns)
    assert result.values.dtype == np.bool_
    tm.assert_frame_equal(result, expected)

def _check_unary_op(op):
    result = op(df1)
    expected = DataFrame(op(df1.values), index=df1.index, columns=df1.columns)
    assert result.values.dtype == np.bool_
    tm.assert_frame_equal(result, expected)
df1 = {'a': {'a': True, 'b': False, 'c': False, 'd': True, 'e': True}, 'b': {'a': False, 'b': True, 'c': False, 'd': False, 'e': False}, 'c': {'a': False, 'b': False, 'c': True, 'd': False, 'e': False}, 'd': {'a': True, 'b': False, 'c': False, 'd': True, 'e': True}, 'e': {'a': True, 'b': False, 'c': False, 'd': True, 'e': True}}
df2 = {'a': {'a': True, 'b': False, 'c': True, 'd': False, 'e': False}, 'b': {'a': False, 'b': True, 'c': False, 'd': False, 'e': False}, 'c': {'a': True, 'b': False, 'c': True, 'd': False, 'e': False}, 'd': {'a': False, 'b': False, 'c': False, 'd': True, 'e': False}, 'e': {'a': False, 'b': False, 'c': False, 'd': False, 'e': True}}
df1 = DataFrame(df1)
df2 = DataFrame(df2)
_check_bin_op(operator.and_)
_check_bin_op(operator.or_)
_check_bin_op(operator.xor)
_check_unary_op(operator.inv)
```

## Next Steps


---

*Source: test_logical_ops.py:117 | Complexity: Advanced | Last updated: 2026-06-02*