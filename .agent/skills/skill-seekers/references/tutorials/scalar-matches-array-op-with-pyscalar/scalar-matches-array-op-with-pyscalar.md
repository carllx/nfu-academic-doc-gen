# How To: Scalar Matches Array Op With Pyscalar

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test scalar matches array op with pyscalar

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `hypothesis.strategies`
- `numpy`
- `numpy._core._rational_tests`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: op, sctype, other_type, rop
```

## Step-by-Step Guide

### Step 1: Assign val1 = sctype(...)

```python
val1 = sctype(2)
```

**Verification:**
```python
assert res == expected
```

### Step 2: Assign val2 = other_type(...)

```python
val2 = other_type(2)
```

**Verification:**
```python
assert np.array(res).dtype == expected.dtype
```

### Step 3: Assign _op = op

```python
_op = op
```

**Verification:**
```python
assert res.dtype == expected.dtype
```

### Step 4: Assign op = value

```python
op = lambda x, y: _op(y, x)
```

### Step 5: Assign res = op(...)

```python
res = op(val1, val2)
```

### Step 6: Assign expected = op(...)

```python
expected = op(np.asarray(val1), val2)
```

**Verification:**
```python
assert np.array(res).dtype == expected.dtype
```

### Step 7: Assign expected = op(...)

```python
expected = op(np.asarray(val1), val2)
```


## Complete Example

```python
# Setup
# Fixtures: op, sctype, other_type, rop

# Workflow
val1 = sctype(2)
val2 = other_type(2)
if rop:
    _op = op
    op = lambda x, y: _op(y, x)
try:
    res = op(val1, val2)
except TypeError:
    try:
        expected = op(np.asarray(val1), val2)
        raise AssertionError("ufunc didn't raise.")
    except TypeError:
        return
else:
    expected = op(np.asarray(val1), val2)
assert res == expected
if isinstance(val1, float) and other_type is complex and rop:
    assert np.array(res).dtype == expected.dtype
else:
    assert res.dtype == expected.dtype
```

## Next Steps


---

*Source: test_scalarmath.py:1140 | Complexity: Advanced | Last updated: 2026-06-02*