# How To: From String Array

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from string array

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy._core.multiarray`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign A = np.array(...)

```python
A = np.array([[b'abc', b'foo'], [b'long   ', b'0123456789']])
```

**Verification:**
```python
assert_equal(A.dtype.type, np.bytes_)
```

### Step 2: Call assert_equal()

```python
assert_equal(A.dtype.type, np.bytes_)
```

**Verification:**
```python
assert_array_equal(B, A)
```

### Step 3: Assign B = np.char.array(...)

```python
B = np.char.array(A)
```

**Verification:**
```python
assert_equal(B.dtype, A.dtype)
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(B, A)
```

**Verification:**
```python
assert_equal(B.shape, A.shape)
```

### Step 5: Call assert_equal()

```python
assert_equal(B.dtype, A.dtype)
```

**Verification:**
```python
assert_(B[0, 0] != A[0, 0])
```

### Step 6: Call assert_equal()

```python
assert_equal(B.shape, A.shape)
```

**Verification:**
```python
assert_array_equal(C, A)
```

### Step 7: Assign unknown = 'changed'

```python
B[0, 0] = 'changed'
```

**Verification:**
```python
assert_equal(C.dtype, A.dtype)
```

### Step 8: Call assert_()

```python
assert_(B[0, 0] != A[0, 0])
```

**Verification:**
```python
assert_(C[0, 0] != B[0, 0])
```

### Step 9: Assign C = np.char.asarray(...)

```python
C = np.char.asarray(A)
```

**Verification:**
```python
assert_(C[0, 0] == A[0, 0])
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(C, A)
```

### Step 11: Call assert_equal()

```python
assert_equal(C.dtype, A.dtype)
```

### Step 12: Assign unknown = 'changed again'

```python
C[0, 0] = 'changed again'
```

### Step 13: Call assert_()

```python
assert_(C[0, 0] != B[0, 0])
```

### Step 14: Call assert_()

```python
assert_(C[0, 0] == A[0, 0])
```


## Complete Example

```python
# Workflow
A = np.array([[b'abc', b'foo'], [b'long   ', b'0123456789']])
assert_equal(A.dtype.type, np.bytes_)
B = np.char.array(A)
assert_array_equal(B, A)
assert_equal(B.dtype, A.dtype)
assert_equal(B.shape, A.shape)
B[0, 0] = 'changed'
assert_(B[0, 0] != A[0, 0])
C = np.char.asarray(A)
assert_array_equal(C, A)
assert_equal(C.dtype, A.dtype)
C[0, 0] = 'changed again'
assert_(C[0, 0] != B[0, 0])
assert_(C[0, 0] == A[0, 0])
```

## Next Steps


---

*Source: test_defchararray.py:34 | Complexity: Advanced | Last updated: 2026-06-02*