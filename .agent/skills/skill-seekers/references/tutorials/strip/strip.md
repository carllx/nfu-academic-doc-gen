# How To: Strip

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test strip

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
assert_(issubclass(A.strip().dtype.type, np.bytes_))
```

### Step 2: Assign tgt = value

```python
tgt = [[b'abc', b''], [b'12345', b'MixedCase'], [b'123 \t 345', b'UPPER']]
```

**Verification:**
```python
assert_array_equal(A.strip(), tgt)
```

### Step 3: Call assert_()

```python
assert_(issubclass(A.strip().dtype.type, np.bytes_))
```

**Verification:**
```python
assert_array_equal(A.strip([b'15', b'EReM']), tgt)
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(A.strip(), tgt)
```

**Verification:**
```python
assert_(issubclass(B.strip().dtype.type, np.str_))
```

### Step 5: Assign tgt = value

```python
tgt = [[b' abc ', b''], [b'234', b'ixedCas'], [b'23 \t 345 \x00', b'UPP']]
```

**Verification:**
```python
assert_array_equal(B.strip(), tgt)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(A.strip([b'15', b'EReM']), tgt)
```

### Step 7: Assign tgt = value

```python
tgt = [['Σ', ''], ['12345', 'MixedCase'], ['123 \t 345', 'UPPER']]
```

### Step 8: Call assert_()

```python
assert_(issubclass(B.strip().dtype.type, np.str_))
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(B.strip(), tgt)
```


## Complete Example

```python
# Workflow
A, B = (self.A(), self.B())
tgt = [[b'abc', b''], [b'12345', b'MixedCase'], [b'123 \t 345', b'UPPER']]
assert_(issubclass(A.strip().dtype.type, np.bytes_))
assert_array_equal(A.strip(), tgt)
tgt = [[b' abc ', b''], [b'234', b'ixedCas'], [b'23 \t 345 \x00', b'UPP']]
assert_array_equal(A.strip([b'15', b'EReM']), tgt)
tgt = [['Σ', ''], ['12345', 'MixedCase'], ['123 \t 345', 'UPPER']]
assert_(issubclass(B.strip().dtype.type, np.str_))
assert_array_equal(B.strip(), tgt)
```

## Next Steps


---

*Source: test_defchararray.py:590 | Complexity: Advanced | Last updated: 2026-06-02*