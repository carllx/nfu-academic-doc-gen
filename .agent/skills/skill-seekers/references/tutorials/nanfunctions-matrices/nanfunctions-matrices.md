# How To: Nanfunctions Matrices

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nanfunctions matrices

## Prerequisites

**Required Modules:**
- `textwrap`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign mat = np.matrix(...)

```python
mat = np.matrix(np.eye(3))
```

**Verification:**
```python
assert_(isinstance(res, np.matrix))
```

### Step 2: Assign unknown = value

```python
mat[1] = np.nan
```

**Verification:**
```python
assert_(res.shape == (1, 3))
```

### Step 3: Assign res = f(...)

```python
res = f(mat, axis=0)
```

**Verification:**
```python
assert_(isinstance(res, np.matrix))
```

### Step 4: Call assert_()

```python
assert_(isinstance(res, np.matrix))
```

**Verification:**
```python
assert_(res.shape == (3, 1))
```

### Step 5: Call assert_()

```python
assert_(res.shape == (1, 3))
```

**Verification:**
```python
assert_(np.isscalar(res))
```

### Step 6: Assign res = f(...)

```python
res = f(mat, axis=1)
```

**Verification:**
```python
assert_(isinstance(res, np.matrix))
```

### Step 7: Call assert_()

```python
assert_(isinstance(res, np.matrix))
```

**Verification:**
```python
assert_(not np.any(np.isnan(res)))
```

### Step 8: Call assert_()

```python
assert_(res.shape == (3, 1))
```

**Verification:**
```python
assert_(len(w) == 0)
```

### Step 9: Assign res = f(...)

```python
res = f(mat)
```

**Verification:**
```python
assert_(isinstance(res, np.matrix))
```

### Step 10: Call assert_()

```python
assert_(np.isscalar(res))
```

**Verification:**
```python
assert_(np.isnan(res[1, 0]) and (not np.isnan(res[0, 0])) and (not np.isnan(res[2, 0])))
```

### Step 11: Call warnings.simplefilter()

```python
warnings.simplefilter('always')
```

**Verification:**
```python
assert_(len(w) == 1, 'no warning raised')
```

### Step 12: Assign res = f(...)

```python
res = f(mat, axis=0)
```

**Verification:**
```python
assert_(issubclass(w[0].category, RuntimeWarning))
```

### Step 13: Call assert_()

```python
assert_(isinstance(res, np.matrix))
```

**Verification:**
```python
assert_(np.isscalar(res))
```

### Step 14: Call assert_()

```python
assert_(not np.any(np.isnan(res)))
```

**Verification:**
```python
assert_(res != np.nan)
```

### Step 15: Call assert_()

```python
assert_(len(w) == 0)
```

**Verification:**
```python
assert_(len(w) == 0)
```

### Step 16: Call warnings.simplefilter()

```python
warnings.simplefilter('always')
```

### Step 17: Assign res = f(...)

```python
res = f(mat, axis=1)
```

### Step 18: Call assert_()

```python
assert_(isinstance(res, np.matrix))
```

### Step 19: Call assert_()

```python
assert_(np.isnan(res[1, 0]) and (not np.isnan(res[0, 0])) and (not np.isnan(res[2, 0])))
```

### Step 20: Call assert_()

```python
assert_(len(w) == 1, 'no warning raised')
```

### Step 21: Call assert_()

```python
assert_(issubclass(w[0].category, RuntimeWarning))
```

### Step 22: Call warnings.simplefilter()

```python
warnings.simplefilter('always')
```

### Step 23: Assign res = f(...)

```python
res = f(mat)
```

### Step 24: Call assert_()

```python
assert_(np.isscalar(res))
```

### Step 25: Call assert_()

```python
assert_(res != np.nan)
```

### Step 26: Call assert_()

```python
assert_(len(w) == 0)
```


## Complete Example

```python
# Workflow
mat = np.matrix(np.eye(3))
for f in [np.nanmin, np.nanmax]:
    res = f(mat, axis=0)
    assert_(isinstance(res, np.matrix))
    assert_(res.shape == (1, 3))
    res = f(mat, axis=1)
    assert_(isinstance(res, np.matrix))
    assert_(res.shape == (3, 1))
    res = f(mat)
    assert_(np.isscalar(res))
mat[1] = np.nan
for f in [np.nanmin, np.nanmax]:
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        res = f(mat, axis=0)
        assert_(isinstance(res, np.matrix))
        assert_(not np.any(np.isnan(res)))
        assert_(len(w) == 0)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        res = f(mat, axis=1)
        assert_(isinstance(res, np.matrix))
        assert_(np.isnan(res[1, 0]) and (not np.isnan(res[0, 0])) and (not np.isnan(res[2, 0])))
        assert_(len(w) == 1, 'no warning raised')
        assert_(issubclass(w[0].category, RuntimeWarning))
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        res = f(mat)
        assert_(np.isscalar(res))
        assert_(res != np.nan)
        assert_(len(w) == 0)
```

## Next Steps


---

*Source: test_interaction.py:168 | Complexity: Advanced | Last updated: 2026-06-02*