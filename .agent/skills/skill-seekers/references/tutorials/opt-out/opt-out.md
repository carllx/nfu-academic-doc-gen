# How To: Opt Out

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test opt out

## Prerequisites

**Required Modules:**
- `numbers`
- `operator`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign array_like = ArrayLike(...)

```python
array_like = ArrayLike(1)
```

**Verification:**
```python
assert_(array_like + opt_out is opt_out)
```

### Step 2: Assign opt_out = OptOut(...)

```python
opt_out = OptOut()
```

**Verification:**
```python
assert_(opt_out + array_like is opt_out)
```

### Step 3: Call assert_()

```python
assert_(array_like + opt_out is opt_out)
```

### Step 4: Call assert_()

```python
assert_(opt_out + array_like is opt_out)
```

### Step 5: """Object that opts out of __array_ufunc__."""

```python
"""Object that opts out of __array_ufunc__."""
```

### Step 6: Assign __array_ufunc__ = None

```python
__array_ufunc__ = None
```

### Step 7: array_like - opt_out

```python
array_like - opt_out
```

### Step 8: opt_out - array_like

```python
opt_out - array_like
```


## Complete Example

```python
# Workflow
class OptOut:
    """Object that opts out of __array_ufunc__."""
    __array_ufunc__ = None

    def __add__(self, other):
        return self

    def __radd__(self, other):
        return self
array_like = ArrayLike(1)
opt_out = OptOut()
assert_(array_like + opt_out is opt_out)
assert_(opt_out + array_like is opt_out)
with assert_raises(TypeError):
    array_like += opt_out
with assert_raises(TypeError):
    array_like - opt_out
with assert_raises(TypeError):
    opt_out - array_like
```

## Next Steps


---

*Source: test_mixins.py:121 | Complexity: Advanced | Last updated: 2026-06-02*