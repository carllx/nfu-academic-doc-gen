# How To: Set Mask

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set mask

## Prerequisites

**Required Modules:**
- `pickle`
- `numpy`
- `numpy.ma`
- `numpy._core.records`
- `numpy.ma`
- `numpy.ma.mrecords`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign base = self.base.copy(...)

```python
base = self.base.copy()
```

**Verification:**
```python
assert_equal(ma.getmaskarray(mbase['b']), [1] * 5)
```

### Step 2: Assign mbase = base.view(...)

```python
mbase = base.view(mrecarray)
```

**Verification:**
```python
assert_equal(mbase['a']._mask, mbase['b']._mask)
```

### Step 3: Assign mbase.mask = masked

```python
mbase.mask = masked
```

**Verification:**
```python
assert_equal(mbase['a']._mask, mbase['c']._mask)
```

### Step 4: Call assert_equal()

```python
assert_equal(ma.getmaskarray(mbase['b']), [1] * 5)
```

**Verification:**
```python
assert_equal(mbase._mask.tolist(), np.array([(1, 1, 1)] * 5, dtype=bool))
```

### Step 5: Call assert_equal()

```python
assert_equal(mbase['a']._mask, mbase['b']._mask)
```

**Verification:**
```python
assert_equal(ma.getmaskarray(mbase['c']), [0] * 5)
```

### Step 6: Call assert_equal()

```python
assert_equal(mbase['a']._mask, mbase['c']._mask)
```

**Verification:**
```python
assert_equal(mbase._mask.tolist(), np.array([(0, 0, 0)] * 5, dtype=bool))
```

### Step 7: Call assert_equal()

```python
assert_equal(mbase._mask.tolist(), np.array([(1, 1, 1)] * 5, dtype=bool))
```

### Step 8: Assign mbase.mask = nomask

```python
mbase.mask = nomask
```

### Step 9: Call assert_equal()

```python
assert_equal(ma.getmaskarray(mbase['c']), [0] * 5)
```

### Step 10: Call assert_equal()

```python
assert_equal(mbase._mask.tolist(), np.array([(0, 0, 0)] * 5, dtype=bool))
```


## Complete Example

```python
# Workflow
base = self.base.copy()
mbase = base.view(mrecarray)
mbase.mask = masked
assert_equal(ma.getmaskarray(mbase['b']), [1] * 5)
assert_equal(mbase['a']._mask, mbase['b']._mask)
assert_equal(mbase['a']._mask, mbase['c']._mask)
assert_equal(mbase._mask.tolist(), np.array([(1, 1, 1)] * 5, dtype=bool))
mbase.mask = nomask
assert_equal(ma.getmaskarray(mbase['c']), [0] * 5)
assert_equal(mbase._mask.tolist(), np.array([(0, 0, 0)] * 5, dtype=bool))
```

## Next Steps


---

*Source: test_mrecords.py:160 | Complexity: Advanced | Last updated: 2026-06-02*