# How To: Nat Arithmetic Scalar

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nat arithmetic scalar

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: op_name, value, val_type
```

## Step-by-Step Guide

### Step 1: Assign invalid_ops = value

```python
invalid_ops = {'scalar': {'right_div_left'}, 'floating': {'right_div_left', 'left_minus_right', 'right_minus_left', 'left_plus_right', 'right_plus_left'}, 'str': set(_ops.keys()), 'timedelta': {'left_times_right', 'right_times_left'}, 'timestamp': {'left_times_right', 'right_times_left', 'left_div_right', 'right_div_left'}}
```

**Verification:**
```python
assert op(NaT, value) is expected
```

### Step 2: Assign op = value

```python
op = _ops[op_name]
```

**Verification:**
```python
assert op(NaT, value) is expected
```

### Step 3: Assign typs = '(Timedelta|NaTType)'

```python
typs = '(Timedelta|NaTType)'
```

### Step 4: Assign msg = value

```python
msg = f"unsupported operand type\\(s\\) for \\*: '{typs}' and '{typs}'"
```

### Step 5: Call op()

```python
op(NaT, value)
```

### Step 6: Assign expected = value

```python
expected = np.nan
```

### Step 7: Assign expected = NaT

```python
expected = NaT
```

### Step 8: Assign msg = unknown.join(...)

```python
msg = '|'.join(['can only concatenate str', 'unsupported operand type', "can't multiply sequence", "Can't convert 'NaTType'", 'must be str, not NaTType'])
```

### Step 9: Assign msg = 'unsupported operand type'

```python
msg = 'unsupported operand type'
```


## Complete Example

```python
# Setup
# Fixtures: op_name, value, val_type

# Workflow
invalid_ops = {'scalar': {'right_div_left'}, 'floating': {'right_div_left', 'left_minus_right', 'right_minus_left', 'left_plus_right', 'right_plus_left'}, 'str': set(_ops.keys()), 'timedelta': {'left_times_right', 'right_times_left'}, 'timestamp': {'left_times_right', 'right_times_left', 'left_div_right', 'right_div_left'}}
op = _ops[op_name]
if op_name in invalid_ops.get(val_type, set()):
    if val_type == 'timedelta' and 'times' in op_name and isinstance(value, Timedelta):
        typs = '(Timedelta|NaTType)'
        msg = f"unsupported operand type\\(s\\) for \\*: '{typs}' and '{typs}'"
    elif val_type == 'str':
        msg = '|'.join(['can only concatenate str', 'unsupported operand type', "can't multiply sequence", "Can't convert 'NaTType'", 'must be str, not NaTType'])
    else:
        msg = 'unsupported operand type'
    with pytest.raises(TypeError, match=msg):
        op(NaT, value)
else:
    if val_type == 'timedelta' and 'div' in op_name:
        expected = np.nan
    else:
        expected = NaT
    assert op(NaT, value) is expected
```

## Next Steps


---

*Source: test_nat.py:368 | Complexity: Advanced | Last updated: 2026-06-02*