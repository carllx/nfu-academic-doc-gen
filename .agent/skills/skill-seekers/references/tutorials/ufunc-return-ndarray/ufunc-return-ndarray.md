# How To: Ufunc Return Ndarray

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ufunc return ndarray

## Prerequisites

**Required Modules:**
- `mmap`
- `os`
- `sys`
- `warnings`
- `pathlib`
- `tempfile`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign fp = memmap(...)

```python
fp = memmap(self.tmpfp, dtype=self.dtype, shape=self.shape)
```

**Verification:**
```python
assert_(isscalar(result))
```

### Step 2: Assign unknown = value

```python
fp[:] = self.data
```

**Verification:**
```python
assert_(result.__class__ is self.data[0, 0].__class__)
```

### Step 3: Call add()

```python
add(fp, 1, out=fp)
```

**Verification:**
```python
assert_(unary_op(fp, axis=0).__class__ is ndarray)
```

### Step 4: Call warnings.filterwarnings()

```python
warnings.filterwarnings('ignore', 'np.average currently does not preserve', FutureWarning)
```

**Verification:**
```python
assert_(unary_op(fp, axis=1).__class__ is ndarray)
```

### Step 5: Call assert_()

```python
assert_(binary_op(fp, self.data).__class__ is ndarray)
```

**Verification:**
```python
assert_(binary_op(fp, self.data).__class__ is ndarray)
```

### Step 6: Call assert_()

```python
assert_(binary_op(self.data, fp).__class__ is ndarray)
```

**Verification:**
```python
assert_(binary_op(self.data, fp).__class__ is ndarray)
```

### Step 7: Call assert_()

```python
assert_(binary_op(fp, fp).__class__ is ndarray)
```

**Verification:**
```python
assert_(binary_op(fp, fp).__class__ is ndarray)
```

### Step 8: Assign result = unary_op(...)

```python
result = unary_op(fp)
```

**Verification:**
```python
assert fp.__class__ is memmap
```

### Step 9: Call assert_()

```python
assert_(isscalar(result))
```

**Verification:**
```python
assert fp.__class__ is memmap
```

### Step 10: Call assert_()

```python
assert_(result.__class__ is self.data[0, 0].__class__)
```

### Step 11: Call assert_()

```python
assert_(unary_op(fp, axis=0).__class__ is ndarray)
```

### Step 12: Call assert_()

```python
assert_(unary_op(fp, axis=1).__class__ is ndarray)
```


## Complete Example

```python
# Workflow
fp = memmap(self.tmpfp, dtype=self.dtype, shape=self.shape)
fp[:] = self.data
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', 'np.average currently does not preserve', FutureWarning)
    for unary_op in [sum, average, prod]:
        result = unary_op(fp)
        assert_(isscalar(result))
        assert_(result.__class__ is self.data[0, 0].__class__)
        assert_(unary_op(fp, axis=0).__class__ is ndarray)
        assert_(unary_op(fp, axis=1).__class__ is ndarray)
for binary_op in [add, subtract, multiply]:
    assert_(binary_op(fp, self.data).__class__ is ndarray)
    assert_(binary_op(self.data, fp).__class__ is ndarray)
    assert_(binary_op(fp, fp).__class__ is ndarray)
fp += 1
assert fp.__class__ is memmap
add(fp, 1, out=fp)
assert fp.__class__ is memmap
```

## Next Steps


---

*Source: test_memmap.py:167 | Complexity: Advanced | Last updated: 2026-06-02*