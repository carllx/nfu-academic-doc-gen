# How To: Error Len Mismatch

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test error len mismatch

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

### Step 3: Assign other = value

```python
other = [scalar] * (len(data) - 1)
```

### Step 4: Assign err = ValueError

```python
err = ValueError
```

### Step 5: Assign msg = unknown.join(...)

```python
msg = '|'.join(['operands could not be broadcast together with shapes \\(3,\\) \\(4,\\)', 'operands could not be broadcast together with shapes \\(4,\\) \\(3,\\)'])
```

### Step 6: Assign err = TypeError

```python
err = TypeError
```

### Step 7: Assign msg = 'numpy boolean subtract, the `\\-` operator, is not supported, use the bitwise_xor, the `\\^` operator, or the logical_xor function instead'

```python
msg = 'numpy boolean subtract, the `\\-` operator, is not supported, use the bitwise_xor, the `\\^` operator, or the logical_xor function instead'
```

### Step 8: Assign s = pd.Series(...)

```python
s = pd.Series(data)
```

### Step 9: Assign msg = "operator '.*' not implemented for bool dtypes"

```python
msg = "operator '.*' not implemented for bool dtypes"
```

### Step 10: Assign err = NotImplementedError

```python
err = NotImplementedError
```

### Step 11: Call op()

```python
op(data, other)
```

### Step 12: Call op()

```python
op(s, other)
```


## Complete Example

```python
# Setup
# Fixtures: data, all_arithmetic_operators

# Workflow
data, scalar = data
op = tm.get_op_from_name(all_arithmetic_operators)
other = [scalar] * (len(data) - 1)
err = ValueError
msg = '|'.join(['operands could not be broadcast together with shapes \\(3,\\) \\(4,\\)', 'operands could not be broadcast together with shapes \\(4,\\) \\(3,\\)'])
if data.dtype.kind == 'b' and all_arithmetic_operators.strip('_') in ['sub', 'rsub']:
    err = TypeError
    msg = 'numpy boolean subtract, the `\\-` operator, is not supported, use the bitwise_xor, the `\\^` operator, or the logical_xor function instead'
elif is_bool_not_implemented(data, all_arithmetic_operators):
    msg = "operator '.*' not implemented for bool dtypes"
    err = NotImplementedError
for other in [other, np.array(other)]:
    with pytest.raises(err, match=msg):
        op(data, other)
    s = pd.Series(data)
    with pytest.raises(err, match=msg):
        op(s, other)
```

## Next Steps


---

*Source: test_arithmetic.py:190 | Complexity: Advanced | Last updated: 2026-06-02*