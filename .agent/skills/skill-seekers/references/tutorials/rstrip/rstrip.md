# How To: Rstrip

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rstrip

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy._core.multiarray`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
A, B = (self.A(), self.B())
```

**Verification:**
```python
assert_(issubclass(A.rstrip().dtype.type, np.bytes_))
```

### Step 2: Call assert_()

```python
assert_(issubclass(A.rstrip().dtype.type, np.bytes_))
```

**Verification:**
```python
assert_array_equal(A.rstrip(), tgt)
```

### Step 3: Assign tgt = value

```python
tgt = [[b' abc', b''], [b'12345', b'MixedCase'], [b'123 \t 345', b'UPPER']]
```

**Verification:**
```python
assert_array_equal(A.rstrip([b'5', b'ER']), tgt)
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(A.rstrip(), tgt)
```

**Verification:**
```python
assert_(issubclass(B.rstrip().dtype.type, np.str_))
```

### Step 5: Assign tgt = value

```python
tgt = [[b' abc ', b''], [b'1234', b'MixedCase'], [b'123 \t 345 \x00', b'UPP']]
```

**Verification:**
```python
assert_array_equal(B.rstrip(), tgt)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(A.rstrip([b'5', b'ER']), tgt)
```

### Step 7: Assign tgt = value

```python
tgt = [[' Σ', ''], ['12345', 'MixedCase'], ['123 \t 345', 'UPPER']]
```

### Step 8: Call assert_()

```python
assert_(issubclass(B.rstrip().dtype.type, np.str_))
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(B.rstrip(), tgt)
```


## Complete Example

```python
# Workflow
A, B = (self.A(), self.B())
assert_(issubclass(A.rstrip().dtype.type, np.bytes_))
tgt = [[b' abc', b''], [b'12345', b'MixedCase'], [b'123 \t 345', b'UPPER']]
assert_array_equal(A.rstrip(), tgt)
tgt = [[b' abc ', b''], [b'1234', b'MixedCase'], [b'123 \t 345 \x00', b'UPP']]
assert_array_equal(A.rstrip([b'5', b'ER']), tgt)
tgt = [[' Σ', ''], ['12345', 'MixedCase'], ['123 \t 345', 'UPPER']]
assert_(issubclass(B.rstrip().dtype.type, np.str_))
assert_array_equal(B.rstrip(), tgt)
```

## Next Steps


---

*Source: test_defchararray.py:569 | Complexity: Advanced | Last updated: 2026-06-02*