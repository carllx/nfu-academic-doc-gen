# How To: Rjust

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rjust

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy._core.multiarray`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign A = self.A(...)

```python
A = self.A()
```

**Verification:**
```python
assert_(issubclass(A.rjust(10).dtype.type, np.bytes_))
```

### Step 2: Call assert_()

```python
assert_(issubclass(A.rjust(10).dtype.type, np.bytes_))
```

**Verification:**
```python
assert_array_equal(np.char.str_len(C), [[10, 20], [10, 20], [12, 20]])
```

### Step 3: Assign C = A.rjust(...)

```python
C = A.rjust([10, 20])
```

**Verification:**
```python
assert_(np.all(C.startswith(b'#')))
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(np.char.str_len(C), [[10, 20], [10, 20], [12, 20]])
```

**Verification:**
```python
assert_array_equal(C.endswith(b'#'), [[False, True], [False, False], [False, False]])
```

### Step 5: Assign C = A.rjust(...)

```python
C = A.rjust(20, b'#')
```

**Verification:**
```python
assert_(issubclass(C.dtype.type, np.bytes_))
```

### Step 6: Call assert_()

```python
assert_(np.all(C.startswith(b'#')))
```

**Verification:**
```python
assert_array_equal(C, tgt)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(C.endswith(b'#'), [[False, True], [False, False], [False, False]])
```

### Step 8: Assign C = np.char.rjust(...)

```python
C = np.char.rjust(b'FOO', [[10, 20], [15, 8]])
```

### Step 9: Assign tgt = value

```python
tgt = [[b'       FOO', b'                 FOO'], [b'            FOO', b'     FOO']]
```

### Step 10: Call assert_()

```python
assert_(issubclass(C.dtype.type, np.bytes_))
```

### Step 11: Call assert_array_equal()

```python
assert_array_equal(C, tgt)
```


## Complete Example

```python
# Workflow
A = self.A()
assert_(issubclass(A.rjust(10).dtype.type, np.bytes_))
C = A.rjust([10, 20])
assert_array_equal(np.char.str_len(C), [[10, 20], [10, 20], [12, 20]])
C = A.rjust(20, b'#')
assert_(np.all(C.startswith(b'#')))
assert_array_equal(C.endswith(b'#'), [[False, True], [False, False], [False, False]])
C = np.char.rjust(b'FOO', [[10, 20], [15, 8]])
tgt = [[b'       FOO', b'                 FOO'], [b'            FOO', b'     FOO']]
assert_(issubclass(C.dtype.type, np.bytes_))
assert_array_equal(C, tgt)
```

## Next Steps


---

*Source: test_defchararray.py:534 | Complexity: Advanced | Last updated: 2026-06-02*