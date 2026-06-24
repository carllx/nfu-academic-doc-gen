# How To: Division Int Reduce

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test division int reduce

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `fnmatch`
- `inspect`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `collections`
- `fractions`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.umath`
- `numpy._core`
- `numpy.testing`
- `numpy.testing._private.utils`
- `operator`
- `platform`
- `decimal`
- `cmath`

**Setup Required:**
```python
# Fixtures: dtype, ex_val
```

## Step-by-Step Guide

### Step 1: Assign fo = np.iinfo(...)

```python
fo = np.iinfo(dtype)
```

**Verification:**
```python
assert div_a == div_lst, msg
```

### Step 2: Assign a = eval(...)

```python
a = eval(ex_val)
```

### Step 3: Assign lst = a.tolist(...)

```python
lst = a.tolist()
```

### Step 4: Assign c_div = value

```python
c_div = lambda n, d: 0 if d == 0 or (n and n == fo.min and (d == -1)) else n // d
```

### Step 5: Assign div_lst = reduce(...)

```python
div_lst = reduce(c_div, lst)
```

### Step 6: Assign msg = 'Reduce floor integer division check'

```python
msg = 'Reduce floor integer division check'
```

**Verification:**
```python
assert div_a == div_lst, msg
```

### Step 7: Assign div_a = np.floor_divide.reduce(...)

```python
div_a = np.floor_divide.reduce(a)
```

### Step 8: Call np.floor_divide.reduce()

```python
np.floor_divide.reduce(np.arange(-100, 100).astype(dtype))
```

### Step 9: Call np.floor_divide.reduce()

```python
np.floor_divide.reduce(np.array([fo.min, 1, -1], dtype=dtype))
```


## Complete Example

```python
# Setup
# Fixtures: dtype, ex_val

# Workflow
fo = np.iinfo(dtype)
a = eval(ex_val)
lst = a.tolist()
c_div = lambda n, d: 0 if d == 0 or (n and n == fo.min and (d == -1)) else n // d
with np.errstate(divide='ignore'):
    div_a = np.floor_divide.reduce(a)
div_lst = reduce(c_div, lst)
msg = 'Reduce floor integer division check'
assert div_a == div_lst, msg
with np.errstate(divide='raise', over='raise'):
    with pytest.raises(FloatingPointError, match='divide by zero encountered in reduce'):
        np.floor_divide.reduce(np.arange(-100, 100).astype(dtype))
    if fo.min:
        with pytest.raises(FloatingPointError, match='overflow encountered in reduce'):
            np.floor_divide.reduce(np.array([fo.min, 1, -1], dtype=dtype))
```

## Next Steps


---

*Source: test_umath.py:574 | Complexity: Advanced | Last updated: 2026-06-02*