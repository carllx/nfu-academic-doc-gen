# How To: Hardmask

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hardmask

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
assert_(mbase._hardmask)
```

### Step 2: Assign mbase = base.view(...)

```python
mbase = base.view(mrecarray)
```

**Verification:**
```python
assert_equal_records(mbase._mask, base._mask)
```

### Step 3: Call mbase.harden_mask()

```python
mbase.harden_mask()
```

**Verification:**
```python
assert_(not mbase._hardmask)
```

### Step 4: Call assert_()

```python
assert_(mbase._hardmask)
```

**Verification:**
```python
assert_equal_records(mbase._mask, ma.make_mask_none(base.shape, base.dtype))
```

### Step 5: Assign mbase.mask = nomask

```python
mbase.mask = nomask
```

**Verification:**
```python
assert_(ma.make_mask(mbase['b']._mask) is nomask)
```

### Step 6: Call assert_equal_records()

```python
assert_equal_records(mbase._mask, base._mask)
```

**Verification:**
```python
assert_equal(mbase['a']._mask, mbase['b']._mask)
```

### Step 7: Call mbase.soften_mask()

```python
mbase.soften_mask()
```

### Step 8: Call assert_()

```python
assert_(not mbase._hardmask)
```

### Step 9: Assign mbase.mask = nomask

```python
mbase.mask = nomask
```

### Step 10: Call assert_equal_records()

```python
assert_equal_records(mbase._mask, ma.make_mask_none(base.shape, base.dtype))
```

### Step 11: Call assert_()

```python
assert_(ma.make_mask(mbase['b']._mask) is nomask)
```

### Step 12: Call assert_equal()

```python
assert_equal(mbase['a']._mask, mbase['b']._mask)
```


## Complete Example

```python
# Workflow
base = self.base.copy()
mbase = base.view(mrecarray)
mbase.harden_mask()
assert_(mbase._hardmask)
mbase.mask = nomask
assert_equal_records(mbase._mask, base._mask)
mbase.soften_mask()
assert_(not mbase._hardmask)
mbase.mask = nomask
assert_equal_records(mbase._mask, ma.make_mask_none(base.shape, base.dtype))
assert_(ma.make_mask(mbase['b']._mask) is nomask)
assert_equal(mbase['a']._mask, mbase['b']._mask)
```

## Next Steps


---

*Source: test_mrecords.py:268 | Complexity: Advanced | Last updated: 2026-06-02*