# How To: Comparison Functions

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test comparison functions

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
# Fixtures: dtype, py_comp, np_comp
```

## Step-by-Step Guide

### Step 1: Assign np_scalar = np.dtype.type(...)

```python
np_scalar = np.dtype(dtype).type(scalar)
```

**Verification:**
```python
assert_(comp_b.tolist() == comp_b_list, f'Failed comparison ({py_comp.__name__})')
```

### Step 2: Assign a_lst = a.tolist(...)

```python
a_lst = a.tolist()
```

**Verification:**
```python
assert_(comp_s1.tolist() == comp_s1_list, f'Failed comparison ({py_comp.__name__})')
```

### Step 3: Assign b_lst = b.tolist(...)

```python
b_lst = b.tolist()
```

**Verification:**
```python
assert_(comp_s2.tolist() == comp_s2_list, f'Failed comparison ({py_comp.__name__})')
```

### Step 4: Assign comp_b = np_comp.view(...)

```python
comp_b = np_comp(a, b).view(np.uint8)
```

### Step 5: Assign comp_b_list = value

```python
comp_b_list = [int(py_comp(x, y)) for x, y in zip(a_lst, b_lst)]
```

### Step 6: Assign comp_s1 = np_comp.view(...)

```python
comp_s1 = np_comp(np_scalar, b).view(np.uint8)
```

### Step 7: Assign comp_s1_list = value

```python
comp_s1_list = [int(py_comp(scalar, x)) for x in b_lst]
```

### Step 8: Assign comp_s2 = np_comp.view(...)

```python
comp_s2 = np_comp(a, np_scalar).view(np.uint8)
```

### Step 9: Assign comp_s2_list = value

```python
comp_s2_list = [int(py_comp(x, scalar)) for x in a_lst]
```

### Step 10: Call assert_()

```python
assert_(comp_b.tolist() == comp_b_list, f'Failed comparison ({py_comp.__name__})')
```

### Step 11: Call assert_()

```python
assert_(comp_s1.tolist() == comp_s1_list, f'Failed comparison ({py_comp.__name__})')
```

### Step 12: Call assert_()

```python
assert_(comp_s2.tolist() == comp_s2_list, f'Failed comparison ({py_comp.__name__})')
```

### Step 13: Assign a = np.random.choice(...)

```python
a = np.random.choice(a=[False, True], size=1000)
```

### Step 14: Assign b = np.random.choice(...)

```python
b = np.random.choice(a=[False, True], size=1000)
```

### Step 15: Assign scalar = True

```python
scalar = True
```

### Step 16: Assign a = np.random.randint.astype(...)

```python
a = np.random.randint(low=1, high=10, size=1000).astype(dtype)
```

### Step 17: Assign b = np.random.randint.astype(...)

```python
b = np.random.randint(low=1, high=10, size=1000).astype(dtype)
```

### Step 18: Assign scalar = 5

```python
scalar = 5
```


## Complete Example

```python
# Setup
# Fixtures: dtype, py_comp, np_comp

# Workflow
if dtype == np.bool:
    a = np.random.choice(a=[False, True], size=1000)
    b = np.random.choice(a=[False, True], size=1000)
    scalar = True
else:
    a = np.random.randint(low=1, high=10, size=1000).astype(dtype)
    b = np.random.randint(low=1, high=10, size=1000).astype(dtype)
    scalar = 5
np_scalar = np.dtype(dtype).type(scalar)
a_lst = a.tolist()
b_lst = b.tolist()
comp_b = np_comp(a, b).view(np.uint8)
comp_b_list = [int(py_comp(x, y)) for x, y in zip(a_lst, b_lst)]
comp_s1 = np_comp(np_scalar, b).view(np.uint8)
comp_s1_list = [int(py_comp(scalar, x)) for x in b_lst]
comp_s2 = np_comp(a, np_scalar).view(np.uint8)
comp_s2_list = [int(py_comp(x, scalar)) for x in a_lst]
assert_(comp_b.tolist() == comp_b_list, f'Failed comparison ({py_comp.__name__})')
assert_(comp_s1.tolist() == comp_s1_list, f'Failed comparison ({py_comp.__name__})')
assert_(comp_s2.tolist() == comp_s2_list, f'Failed comparison ({py_comp.__name__})')
```

## Next Steps


---

*Source: test_umath.py:303 | Complexity: Advanced | Last updated: 2026-06-02*