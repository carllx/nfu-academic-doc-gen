# How To: Where

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test where

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

### Step 1: Assign ar = np.arange.reshape.astype(...)

```python
ar = np.arange(9).reshape(3, 3).astype(dtype)
```

**Verification:**
```python
assert ret.dtype == dtype_reference
```

### Step 2: Assign unknown = value

```python
ar[0, :] = np.nan
```

### Step 3: Assign where = np.ones_like(...)

```python
where = np.ones_like(ar, dtype=np.bool)
```

### Step 4: Assign unknown = False

```python
where[:, 0] = False
```

### Step 5: Assign reference = f_std(...)

```python
reference = f_std(ar[where][2:])
```

### Step 6: Assign dtype_reference = value

```python
dtype_reference = dtype if f is np.nanmean else ar.real.dtype
```

### Step 7: Assign ret = f(...)

```python
ret = f(ar, where=where)
```

**Verification:**
```python
assert ret.dtype == dtype_reference
```

### Step 8: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose(ret, reference)
```


## Complete Example

```python
# Workflow
ar = np.arange(9).reshape(3, 3).astype(dtype)
ar[0, :] = np.nan
where = np.ones_like(ar, dtype=np.bool)
where[:, 0] = False
for f, f_std in zip(self.nanfuncs, self.stdfuncs):
    reference = f_std(ar[where][2:])
    dtype_reference = dtype if f is np.nanmean else ar.real.dtype
    ret = f(ar, where=where)
    assert ret.dtype == dtype_reference
    np.testing.assert_allclose(ret, reference)
```

## Next Steps


---

*Source: test_nanfunctions.py:783 | Complexity: Advanced | Last updated: 2026-06-02*