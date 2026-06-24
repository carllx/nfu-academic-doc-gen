# How To: Numeric Compat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numeric compat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `weakref`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: simple_index
```

## Step-by-Step Guide

### Step 1: Assign idx = simple_index

```python
idx = simple_index
```

**Verification:**
```python
assert not isinstance(idx, MultiIndex)
```

### Step 2: Assign typ = value

```python
typ = type(idx._data).__name__
```

### Step 3: Assign cls = value

```python
cls = type(idx).__name__
```

### Step 4: Assign lmsg = unknown.join(...)

```python
lmsg = '|'.join([f"unsupported operand type\\(s\\) for \\*: '{typ}' and 'int'", f'cannot perform (__mul__|__truediv__|__floordiv__) with this index type: ({cls}|{typ})'])
```

### Step 5: Assign rmsg = unknown.join(...)

```python
rmsg = '|'.join([f"unsupported operand type\\(s\\) for \\*: 'int' and '{typ}'", f'cannot perform (__rmul__|__rtruediv__|__rfloordiv__) with this index type: ({cls}|{typ})'])
```

### Step 6: Assign div_err = lmsg.replace(...)

```python
div_err = lmsg.replace('*', '/')
```

### Step 7: Assign div_err = rmsg.replace(...)

```python
div_err = rmsg.replace('*', '/')
```

### Step 8: Assign floordiv_err = lmsg.replace(...)

```python
floordiv_err = lmsg.replace('*', '//')
```

### Step 9: Assign floordiv_err = rmsg.replace(...)

```python
floordiv_err = rmsg.replace('*', '//')
```

### Step 10: Call pytest.skip()

```python
pytest.skip('Not applicable for Index')
```

### Step 11: Call pytest.skip()

```python
pytest.skip('Tested elsewhere.')
```

### Step 12: idx * 1

```python
idx * 1
```

### Step 13: 1 * idx

```python
1 * idx
```

### Step 14: idx / 1

```python
idx / 1
```

### Step 15: 1 / idx

```python
1 / idx
```

### Step 16: idx // 1

```python
idx // 1
```

### Step 17: 1 // idx

```python
1 // idx
```


## Complete Example

```python
# Setup
# Fixtures: simple_index

# Workflow
idx = simple_index
assert not isinstance(idx, MultiIndex)
if type(idx) is Index:
    pytest.skip('Not applicable for Index')
if is_numeric_dtype(simple_index.dtype) or isinstance(simple_index, TimedeltaIndex):
    pytest.skip('Tested elsewhere.')
typ = type(idx._data).__name__
cls = type(idx).__name__
lmsg = '|'.join([f"unsupported operand type\\(s\\) for \\*: '{typ}' and 'int'", f'cannot perform (__mul__|__truediv__|__floordiv__) with this index type: ({cls}|{typ})'])
with pytest.raises(TypeError, match=lmsg):
    idx * 1
rmsg = '|'.join([f"unsupported operand type\\(s\\) for \\*: 'int' and '{typ}'", f'cannot perform (__rmul__|__rtruediv__|__rfloordiv__) with this index type: ({cls}|{typ})'])
with pytest.raises(TypeError, match=rmsg):
    1 * idx
div_err = lmsg.replace('*', '/')
with pytest.raises(TypeError, match=div_err):
    idx / 1
div_err = rmsg.replace('*', '/')
with pytest.raises(TypeError, match=div_err):
    1 / idx
floordiv_err = lmsg.replace('*', '//')
with pytest.raises(TypeError, match=floordiv_err):
    idx // 1
floordiv_err = rmsg.replace('*', '//')
with pytest.raises(TypeError, match=floordiv_err):
    1 // idx
```

## Next Steps


---

*Source: test_old_base.py:166 | Complexity: Advanced | Last updated: 2026-06-02*