# How To: Ufunc Out Casterrors

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ufunc out casterrors

## Prerequisites

**Required Modules:**
- `ctypes`
- `inspect`
- `itertools`
- `pickle`
- `sys`
- `warnings`
- `pytest`
- `pytest`
- `numpy`
- `numpy._core._operand_flag_tests`
- `numpy._core._rational_tests`
- `numpy._core._umath_tests`
- `numpy._core.umath`
- `numpy.linalg._umath_linalg`
- `numpy.exceptions`
- `numpy.testing`
- `numpy.testing._private.utils`
- `numpy._core._struct_ufunc_tests`


## Step-by-Step Guide

### Step 1: Assign value = 123

```python
value = 123
```

**Verification:**
```python
assert count == sys.getrefcount(value)
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([value] * int(ncu.BUFSIZE * 1.5) + ['string'] + [value] * int(1.5 * ncu.BUFSIZE), dtype=object)
```

**Verification:**
```python
assert out[-1] == 1
```

### Step 3: Assign out = np.ones(...)

```python
out = np.ones(len(arr), dtype=np.intp)
```

**Verification:**
```python
assert count == sys.getrefcount(value)
```

### Step 4: Assign count = sys.getrefcount(...)

```python
count = sys.getrefcount(value)
```

**Verification:**
```python
assert out[-1] == 1
```

### Step 5: Call np.add()

```python
np.add(arr, arr, out=out, casting='unsafe')
```

### Step 6: Call np.add()

```python
np.add(arr, arr, out=out, dtype=np.intp, casting='unsafe')
```


## Complete Example

```python
# Workflow
value = 123
arr = np.array([value] * int(ncu.BUFSIZE * 1.5) + ['string'] + [value] * int(1.5 * ncu.BUFSIZE), dtype=object)
out = np.ones(len(arr), dtype=np.intp)
count = sys.getrefcount(value)
with pytest.raises(ValueError):
    np.add(arr, arr, out=out, casting='unsafe')
assert count == sys.getrefcount(value)
assert out[-1] == 1
with pytest.raises(ValueError):
    np.add(arr, arr, out=out, dtype=np.intp, casting='unsafe')
assert count == sys.getrefcount(value)
assert out[-1] == 1
```

## Next Steps


---

*Source: test_ufunc.py:2926 | Complexity: Intermediate | Last updated: 2026-06-02*