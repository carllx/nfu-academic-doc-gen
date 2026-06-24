# How To: Signature All None

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test signature all None

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

### Step 1: Assign res1 = np.add(...)

```python
res1 = np.add([3], [4], sig=(None, None, None))
```

**Verification:**
```python
assert_array_equal(res1, res2)
```

### Step 2: Assign res2 = np.add(...)

```python
res2 = np.add([3], [4])
```

**Verification:**
```python
assert_array_equal(res1, res2)
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(res1, res2)
```

### Step 4: Assign res1 = np.maximum(...)

```python
res1 = np.maximum([3], [4], sig=(None, None, None))
```

### Step 5: Assign res2 = np.maximum(...)

```python
res2 = np.maximum([3], [4])
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(res1, res2)
```

### Step 7: Call np.add()

```python
np.add(3, 4, signature=(None,))
```


## Complete Example

```python
# Workflow
res1 = np.add([3], [4], sig=(None, None, None))
res2 = np.add([3], [4])
assert_array_equal(res1, res2)
res1 = np.maximum([3], [4], sig=(None, None, None))
res2 = np.maximum([3], [4])
assert_array_equal(res1, res2)
with pytest.raises(TypeError):
    np.add(3, 4, signature=(None,))
```

## Next Steps


---

*Source: test_ufunc.py:474 | Complexity: Intermediate | Last updated: 2026-06-02*