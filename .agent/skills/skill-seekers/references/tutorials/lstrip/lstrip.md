# How To: Lstrip

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test lstrip

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
assert_(issubclass(A.lstrip().dtype.type, np.bytes_))
```

### Step 2: Assign tgt = value

```python
tgt = [[b'abc ', b''], [b'12345', b'MixedCase'], [b'123 \t 345 \x00 ', b'UPPER']]
```

**Verification:**
```python
assert_array_equal(A.lstrip(), tgt)
```

### Step 3: Call assert_()

```python
assert_(issubclass(A.lstrip().dtype.type, np.bytes_))
```

**Verification:**
```python
assert_array_equal(A.lstrip([b'1', b'M']), tgt)
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(A.lstrip(), tgt)
```

**Verification:**
```python
assert_(issubclass(B.lstrip().dtype.type, np.str_))
```

### Step 5: Assign tgt = value

```python
tgt = [[b' abc', b''], [b'2345', b'ixedCase'], [b'23 \t 345 \x00', b'UPPER']]
```

**Verification:**
```python
assert_array_equal(B.lstrip(), tgt)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(A.lstrip([b'1', b'M']), tgt)
```

### Step 7: Assign tgt = value

```python
tgt = [['Σ ', ''], ['12345', 'MixedCase'], ['123 \t 345 \x00 ', 'UPPER']]
```

### Step 8: Call assert_()

```python
assert_(issubclass(B.lstrip().dtype.type, np.str_))
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(B.lstrip(), tgt)
```


## Complete Example

```python
# Workflow
A, B = (self.A(), self.B())
tgt = [[b'abc ', b''], [b'12345', b'MixedCase'], [b'123 \t 345 \x00 ', b'UPPER']]
assert_(issubclass(A.lstrip().dtype.type, np.bytes_))
assert_array_equal(A.lstrip(), tgt)
tgt = [[b' abc', b''], [b'2345', b'ixedCase'], [b'23 \t 345 \x00', b'UPPER']]
assert_array_equal(A.lstrip([b'1', b'M']), tgt)
tgt = [['Σ ', ''], ['12345', 'MixedCase'], ['123 \t 345 \x00 ', 'UPPER']]
assert_(issubclass(B.lstrip().dtype.type, np.str_))
assert_array_equal(B.lstrip(), tgt)
```

## Next Steps


---

*Source: test_defchararray.py:452 | Complexity: Advanced | Last updated: 2026-06-02*