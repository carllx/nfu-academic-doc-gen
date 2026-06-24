# How To: Unary Pyufunc O O Method Full

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Compare the result of the object loop with non-object one

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: ufunc
```

## Step-by-Step Guide

### Step 1: 'Compare the result of the object loop with non-object one'

```python
'Compare the result of the object loop with non-object one'
```

**Verification:**
```python
assert_array_almost_equal(res_num.astype('O'), res_obj)
```

### Step 2: Assign val = np.float64(...)

```python
val = np.float64(np.pi / 4)
```

### Step 3: Assign num_arr = np.array(...)

```python
num_arr = np.array(val, dtype=np.float64)
```

### Step 4: Assign obj_arr = np.array(...)

```python
obj_arr = np.array(MyFloat(val), dtype='O')
```

### Step 5: Assign res_num = ufunc(...)

```python
res_num = ufunc(num_arr)
```

### Step 6: Assign res_obj = ufunc(...)

```python
res_obj = ufunc(obj_arr)
```

### Step 7: Call assert_array_almost_equal()

```python
assert_array_almost_equal(res_num.astype('O'), res_obj)
```

### Step 8: Call ufunc()

```python
ufunc(obj_arr)
```


## Complete Example

```python
# Setup
# Fixtures: ufunc

# Workflow
'Compare the result of the object loop with non-object one'
val = np.float64(np.pi / 4)

class MyFloat(np.float64):

    def __getattr__(self, attr):
        try:
            return super().__getattr__(attr)
        except AttributeError:
            return lambda: getattr(np._core.umath, attr)(val)
num_arr = np.array(val, dtype=np.float64)
obj_arr = np.array(MyFloat(val), dtype='O')
with np.errstate(all='raise'):
    try:
        res_num = ufunc(num_arr)
    except Exception as exc:
        with assert_raises(type(exc)):
            ufunc(obj_arr)
    else:
        res_obj = ufunc(obj_arr)
        assert_array_almost_equal(res_num.astype('O'), res_obj)
```

## Next Steps


---

*Source: test_ufunc.py:171 | Complexity: Advanced | Last updated: 2026-06-02*