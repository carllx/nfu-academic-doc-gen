# How To: Nep50 Weak Integers With Inexact

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nep50 weak integers with inexact

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `hypothesis`
- `pytest`
- `hypothesis`
- `numpy`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign scalar_type = value

```python
scalar_type = np.dtype(dtype).type
```

**Verification:**
```python
assert res.dtype == dtype
```

### Step 2: Assign too_big_int = value

```python
too_big_int = int(np.finfo(dtype).max) * 2
```

**Verification:**
```python
assert res == np.inf
```

### Step 3: scalar_type(1) + too_big_int

```python
scalar_type(1) + too_big_int
```

**Verification:**
```python
assert res.dtype == dtype
```

### Step 4: np.array(1, dtype=dtype) + too_big_int

```python
np.array(1, dtype=dtype) + too_big_int
```

**Verification:**
```python
assert res == np.inf
```

### Step 5: Assign res = value

```python
res = scalar_type(1) + too_big_int
```

### Step 6: Assign res = np.add(...)

```python
res = np.add(np.array(1, dtype=dtype), too_big_int, dtype=dtype)
```

### Step 7: Call str()

```python
str(too_big_int)
```

### Step 8: Call pytest.skip()

```python
pytest.skip('`huge_int -> string -> longdouble` failed')
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
scalar_type = np.dtype(dtype).type
too_big_int = int(np.finfo(dtype).max) * 2
if dtype in 'dDG':
    with pytest.raises(OverflowError):
        scalar_type(1) + too_big_int
    with pytest.raises(OverflowError):
        np.array(1, dtype=dtype) + too_big_int
else:
    if dtype in 'gG':
        try:
            str(too_big_int)
        except ValueError:
            pytest.skip('`huge_int -> string -> longdouble` failed')
    with pytest.warns(RuntimeWarning):
        res = scalar_type(1) + too_big_int
    assert res.dtype == dtype
    assert res == np.inf
    with pytest.warns(RuntimeWarning):
        res = np.add(np.array(1, dtype=dtype), too_big_int, dtype=dtype)
    assert res.dtype == dtype
    assert res == np.inf
```

## Next Steps


---

*Source: test_nep50_promotions.py:67 | Complexity: Advanced | Last updated: 2026-06-02*