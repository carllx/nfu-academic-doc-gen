# How To: Vector Return Type

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test vector return type

## Prerequisites

**Required Modules:**
- `itertools`
- `os`
- `subprocess`
- `sys`
- `textwrap`
- `threading`
- `traceback`
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy._core`
- `numpy.exceptions`
- `numpy.linalg`
- `numpy.linalg._linalg`
- `numpy.testing`
- `numpy.linalg.lapack_lite`
- `resource`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([1, 0, 1])
```

**Verification:**
```python
assert_almost_equal(an, 0.0)
```

### Step 2: Assign exact_types = value

```python
exact_types = np.typecodes['AllInteger']
```

**Verification:**
```python
assert_almost_equal(an, 0.0)
```

### Step 3: Assign inexact_types = value

```python
inexact_types = np.typecodes['AllFloat']
```

**Verification:**
```python
assert_almost_equal(an, 2)
```

### Step 4: Assign all_types = value

```python
all_types = exact_types + inexact_types
```

**Verification:**
```python
assert_almost_equal(an, 2.0)
```

### Step 5: Assign at = a.astype(...)

```python
at = a.astype(each_type)
```

**Verification:**
```python
assert_almost_equal(an, an.dtype.type(2.0) ** an.dtype.type(1.0 / 2.0))
```

### Step 6: Assign an = norm(...)

```python
an = norm(at, -np.inf)
```

**Verification:**
```python
assert_almost_equal(an, an.dtype.type(2.0) ** an.dtype.type(1.0 / 4.0))
```

### Step 7: Call self.check_dtype()

```python
self.check_dtype(at, an)
```

**Verification:**
```python
assert_almost_equal(an, 1.0)
```

### Step 8: Call assert_almost_equal()

```python
assert_almost_equal(an, 0.0)
```

### Step 9: Assign an = norm(...)

```python
an = norm(at, 0)
```

### Step 10: Call self.check_dtype()

```python
self.check_dtype(at, an)
```

### Step 11: Call assert_almost_equal()

```python
assert_almost_equal(an, 2)
```

### Step 12: Assign an = norm(...)

```python
an = norm(at, 1)
```

### Step 13: Call self.check_dtype()

```python
self.check_dtype(at, an)
```

### Step 14: Call assert_almost_equal()

```python
assert_almost_equal(an, 2.0)
```

### Step 15: Assign an = norm(...)

```python
an = norm(at, 2)
```

### Step 16: Call self.check_dtype()

```python
self.check_dtype(at, an)
```

### Step 17: Call assert_almost_equal()

```python
assert_almost_equal(an, an.dtype.type(2.0) ** an.dtype.type(1.0 / 2.0))
```

### Step 18: Assign an = norm(...)

```python
an = norm(at, 4)
```

### Step 19: Call self.check_dtype()

```python
self.check_dtype(at, an)
```

### Step 20: Call assert_almost_equal()

```python
assert_almost_equal(an, an.dtype.type(2.0) ** an.dtype.type(1.0 / 4.0))
```

### Step 21: Assign an = norm(...)

```python
an = norm(at, np.inf)
```

### Step 22: Call self.check_dtype()

```python
self.check_dtype(at, an)
```

### Step 23: Call assert_almost_equal()

```python
assert_almost_equal(an, 1.0)
```

### Step 24: Call warnings.filterwarnings()

```python
warnings.filterwarnings('ignore', 'divide by zero encountered', RuntimeWarning)
```

### Step 25: Assign an = norm(...)

```python
an = norm(at, -1)
```

### Step 26: Call self.check_dtype()

```python
self.check_dtype(at, an)
```

### Step 27: Call assert_almost_equal()

```python
assert_almost_equal(an, 0.0)
```


## Complete Example

```python
# Workflow
a = np.array([1, 0, 1])
exact_types = np.typecodes['AllInteger']
inexact_types = np.typecodes['AllFloat']
all_types = exact_types + inexact_types
for each_type in all_types:
    at = a.astype(each_type)
    an = norm(at, -np.inf)
    self.check_dtype(at, an)
    assert_almost_equal(an, 0.0)
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', 'divide by zero encountered', RuntimeWarning)
        an = norm(at, -1)
        self.check_dtype(at, an)
        assert_almost_equal(an, 0.0)
    an = norm(at, 0)
    self.check_dtype(at, an)
    assert_almost_equal(an, 2)
    an = norm(at, 1)
    self.check_dtype(at, an)
    assert_almost_equal(an, 2.0)
    an = norm(at, 2)
    self.check_dtype(at, an)
    assert_almost_equal(an, an.dtype.type(2.0) ** an.dtype.type(1.0 / 2.0))
    an = norm(at, 4)
    self.check_dtype(at, an)
    assert_almost_equal(an, an.dtype.type(2.0) ** an.dtype.type(1.0 / 4.0))
    an = norm(at, np.inf)
    self.check_dtype(at, an)
    assert_almost_equal(an, 1.0)
```

## Next Steps


---

*Source: test_linalg.py:1319 | Complexity: Advanced | Last updated: 2026-06-02*