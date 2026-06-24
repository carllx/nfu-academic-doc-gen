# How To: Pyscalar Subclasses

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test pyscalar subclasses

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
# Fixtures: subtype, __op__, __rop__, op, cmp
```

## Step-by-Step Guide

### Step 1: Assign myt = type(...)

```python
myt = type('myt', (subtype,), {__op__: op_func, __rop__: rop_func, '__array_ufunc__': None})
```

**Verification:**
```python
assert op(myt(1), np.float64(2)) == __op__
```

### Step 2: Assign myt = type(...)

```python
myt = type('myt', (subtype,), {__rop__: rop_func})
```

**Verification:**
```python
assert op(np.float64(1), myt(2)) == __rop__
```

### Step 3: Assign behaves_like = value

```python
behaves_like = lambda x: np.array(subtype(x))[()]
```

**Verification:**
```python
assert res == expected
```

### Step 4: Assign res = op(...)

```python
res = op(myt(1), np.float16(2))
```

**Verification:**
```python
assert type(res) == type(expected)
```

### Step 5: Assign expected = op(...)

```python
expected = op(behaves_like(1), np.float16(2))
```

**Verification:**
```python
assert res == expected
```

### Step 6: Assign res = op(...)

```python
res = op(np.float32(2), myt(1))
```

**Verification:**
```python
assert type(res) == type(expected)
```

### Step 7: Assign expected = op(...)

```python
expected = op(np.float32(2), behaves_like(1))
```

**Verification:**
```python
assert res == expected
```

### Step 8: Assign res = op(...)

```python
res = op(myt(1), np.longdouble(2))
```

**Verification:**
```python
assert np.dtype(type(res)) == np.dtype(type(expected))
```

### Step 9: Assign expected = op(...)

```python
expected = op(behaves_like(1), np.longdouble(2))
```

**Verification:**
```python
assert res == expected
```

### Step 10: Assign res = op(...)

```python
res = op(np.float32(2), myt(1))
```

**Verification:**
```python
assert np.dtype(type(res)) == np.dtype(type(expected))
```

### Step 11: Assign expected = op(...)

```python
expected = op(np.float32(2), behaves_like(1))
```

**Verification:**
```python
assert res == expected
```


## Complete Example

```python
# Setup
# Fixtures: subtype, __op__, __rop__, op, cmp

# Workflow
def op_func(self, other):
    return __op__

def rop_func(self, other):
    return __rop__
myt = type('myt', (subtype,), {__op__: op_func, __rop__: rop_func, '__array_ufunc__': None})
assert op(myt(1), np.float64(2)) == __op__
assert op(np.float64(1), myt(2)) == __rop__
if op in {operator.mod, operator.floordiv} and subtype == complex:
    return
if __rop__ == __op__:
    return
myt = type('myt', (subtype,), {__rop__: rop_func})
behaves_like = lambda x: np.array(subtype(x))[()]
res = op(myt(1), np.float16(2))
expected = op(behaves_like(1), np.float16(2))
assert res == expected
assert type(res) == type(expected)
res = op(np.float32(2), myt(1))
expected = op(np.float32(2), behaves_like(1))
assert res == expected
assert type(res) == type(expected)
res = op(myt(1), np.longdouble(2))
expected = op(behaves_like(1), np.longdouble(2))
assert res == expected
assert np.dtype(type(res)) == np.dtype(type(expected))
res = op(np.float32(2), myt(1))
expected = op(np.float32(2), behaves_like(1))
assert res == expected
assert np.dtype(type(res)) == np.dtype(type(expected))
```

## Next Steps


---

*Source: test_scalarmath.py:1077 | Complexity: Advanced | Last updated: 2026-06-02*