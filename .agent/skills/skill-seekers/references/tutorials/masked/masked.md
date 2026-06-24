# How To: Masked

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test masked

## Prerequisites

**Required Modules:**
- `inspect`
- `warnings`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.numeric`
- `numpy.exceptions`
- `numpy.lib._nanfunctions_impl`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign mat = np.ma.fix_invalid(...)

```python
mat = np.ma.fix_invalid(_ndat)
```

**Verification:**
```python
assert_equal(res, tgt)
```

### Step 2: Assign msk = mat._mask.copy(...)

```python
msk = mat._mask.copy()
```

**Verification:**
```python
assert_equal(mat._mask, msk)
```

### Step 3: Assign res = f(...)

```python
res = f(mat, axis=1)
```

**Verification:**
```python
assert_(not np.isinf(mat).any())
```

### Step 4: Assign tgt = f(...)

```python
tgt = f(_ndat, axis=1)
```

### Step 5: Call assert_equal()

```python
assert_equal(res, tgt)
```

### Step 6: Call assert_equal()

```python
assert_equal(mat._mask, msk)
```

### Step 7: Call assert_()

```python
assert_(not np.isinf(mat).any())
```


## Complete Example

```python
# Workflow
mat = np.ma.fix_invalid(_ndat)
msk = mat._mask.copy()
for f in [np.nanmin]:
    res = f(mat, axis=1)
    tgt = f(_ndat, axis=1)
    assert_equal(res, tgt)
    assert_equal(mat._mask, msk)
    assert_(not np.isinf(mat).any())
```

## Next Steps


---

*Source: test_nanfunctions.py:159 | Complexity: Intermediate | Last updated: 2026-06-02*