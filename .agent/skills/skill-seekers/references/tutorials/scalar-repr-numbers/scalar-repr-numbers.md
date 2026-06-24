# How To: Scalar Repr Numbers

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test scalar repr numbers

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `gc`
- `sys`
- `textwrap`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `numpy`
- `numpy._core.arrayprint`
- `numpy.testing`
- `numpy.testing._private.utils`

**Setup Required:**
```python
# Fixtures: dtype, value
```

## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype(dtype)
```

**Verification:**
```python
assert isinstance(scalar, np.generic)
```

### Step 2: Assign scalar = value

```python
scalar = np.array(value, dtype=dtype)[()]
```

**Verification:**
```python
assert representation == f"np.longdouble('{repr_string}')"
```

### Step 3: Assign string = str(...)

```python
string = str(scalar)
```

**Verification:**
```python
assert representation == f"np.clongdouble('{repr_string}')"
```

### Step 4: Assign repr_string = string.strip(...)

```python
repr_string = string.strip('()')
```

**Verification:**
```python
assert representation == f'np.{normalized_name}({repr_string})'
```

### Step 5: Assign representation = repr(...)

```python
representation = repr(scalar)
```

**Verification:**
```python
assert repr(scalar) == string
```

### Step 6: Assign normalized_name = value

```python
normalized_name = np.dtype(f'{dtype.kind}{dtype.itemsize}').type.__name__
```

**Verification:**
```python
assert representation == f'np.{normalized_name}({repr_string})'
```


## Complete Example

```python
# Setup
# Fixtures: dtype, value

# Workflow
dtype = np.dtype(dtype)
scalar = np.array(value, dtype=dtype)[()]
assert isinstance(scalar, np.generic)
string = str(scalar)
repr_string = string.strip('()')
representation = repr(scalar)
if dtype.char == 'g':
    assert representation == f"np.longdouble('{repr_string}')"
elif dtype.char == 'G':
    assert representation == f"np.clongdouble('{repr_string}')"
else:
    normalized_name = np.dtype(f'{dtype.kind}{dtype.itemsize}').type.__name__
    assert representation == f'np.{normalized_name}({repr_string})'
with np.printoptions(legacy='1.25'):
    assert repr(scalar) == string
```

## Next Steps


---

*Source: test_arrayprint.py:1219 | Complexity: Intermediate | Last updated: 2026-06-02*