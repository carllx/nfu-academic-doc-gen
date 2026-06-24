# How To: Float Spacing

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test float spacing

## Prerequisites

**Required Modules:**
- `gc`
- `sys`
- `textwrap`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `numpy`
- `numpy._core.arrayprint`
- `numpy.testing`
- `numpy.testing._private.utils`


## Step-by-Step Guide

### Step 1: Assign x = np.array(...)

```python
x = np.array([1.0, 2.0, 3.0])
```

**Verification:**
```python
assert_equal(repr(x), 'array([1., 2., 3.])')
```

### Step 2: Assign y = np.array(...)

```python
y = np.array([1.0, 2.0, -10.0])
```

**Verification:**
```python
assert_equal(repr(y), 'array([  1.,   2., -10.])')
```

### Step 3: Assign z = np.array(...)

```python
z = np.array([100.0, 2.0, -1.0])
```

**Verification:**
```python
assert_equal(repr(np.array(y[0])), 'array(1.)')
```

### Step 4: Assign w = np.array(...)

```python
w = np.array([-100.0, 2.0, 1.0])
```

**Verification:**
```python
assert_equal(repr(np.array(y[-1])), 'array(-10.)')
```

### Step 5: Call assert_equal()

```python
assert_equal(repr(x), 'array([1., 2., 3.])')
```

**Verification:**
```python
assert_equal(repr(z), 'array([100.,   2.,  -1.])')
```

### Step 6: Call assert_equal()

```python
assert_equal(repr(y), 'array([  1.,   2., -10.])')
```

**Verification:**
```python
assert_equal(repr(w), 'array([-100.,    2.,    1.])')
```

### Step 7: Call assert_equal()

```python
assert_equal(repr(np.array(y[0])), 'array(1.)')
```

**Verification:**
```python
assert_equal(repr(np.array([np.nan, np.inf])), 'array([nan, inf])')
```

### Step 8: Call assert_equal()

```python
assert_equal(repr(np.array(y[-1])), 'array(-10.)')
```

**Verification:**
```python
assert_equal(repr(np.array([np.nan, -np.inf])), 'array([ nan, -inf])')
```

### Step 9: Call assert_equal()

```python
assert_equal(repr(z), 'array([100.,   2.,  -1.])')
```

**Verification:**
```python
assert_equal(repr(x), 'array([     inf, 1.00e+05, 1.12e+00])')
```

### Step 10: Call assert_equal()

```python
assert_equal(repr(w), 'array([-100.,    2.,    1.])')
```

**Verification:**
```python
assert_equal(repr(y), 'array([      inf,  1.00e+05, -1.12e+00])')
```

### Step 11: Call assert_equal()

```python
assert_equal(repr(np.array([np.nan, np.inf])), 'array([nan, inf])')
```

**Verification:**
```python
assert_equal(repr(z), 'array([       inf,  1.12e+000, -1.00e+120])')
```

### Step 12: Call assert_equal()

```python
assert_equal(repr(np.array([np.nan, -np.inf])), 'array([ nan, -inf])')
```

### Step 13: Assign x = np.array(...)

```python
x = np.array([np.inf, 100000, 1.1234])
```

### Step 14: Assign y = np.array(...)

```python
y = np.array([np.inf, 100000, -1.1234])
```

### Step 15: Assign z = np.array(...)

```python
z = np.array([np.inf, 1.1234, -1e+120])
```

### Step 16: Call np.set_printoptions()

```python
np.set_printoptions(precision=2)
```

### Step 17: Call assert_equal()

```python
assert_equal(repr(x), 'array([     inf, 1.00e+05, 1.12e+00])')
```

### Step 18: Call assert_equal()

```python
assert_equal(repr(y), 'array([      inf,  1.00e+05, -1.12e+00])')
```

### Step 19: Call assert_equal()

```python
assert_equal(repr(z), 'array([       inf,  1.12e+000, -1.00e+120])')
```


## Complete Example

```python
# Workflow
x = np.array([1.0, 2.0, 3.0])
y = np.array([1.0, 2.0, -10.0])
z = np.array([100.0, 2.0, -1.0])
w = np.array([-100.0, 2.0, 1.0])
assert_equal(repr(x), 'array([1., 2., 3.])')
assert_equal(repr(y), 'array([  1.,   2., -10.])')
assert_equal(repr(np.array(y[0])), 'array(1.)')
assert_equal(repr(np.array(y[-1])), 'array(-10.)')
assert_equal(repr(z), 'array([100.,   2.,  -1.])')
assert_equal(repr(w), 'array([-100.,    2.,    1.])')
assert_equal(repr(np.array([np.nan, np.inf])), 'array([nan, inf])')
assert_equal(repr(np.array([np.nan, -np.inf])), 'array([ nan, -inf])')
x = np.array([np.inf, 100000, 1.1234])
y = np.array([np.inf, 100000, -1.1234])
z = np.array([np.inf, 1.1234, -1e+120])
np.set_printoptions(precision=2)
assert_equal(repr(x), 'array([     inf, 1.00e+05, 1.12e+00])')
assert_equal(repr(y), 'array([      inf,  1.00e+05, -1.12e+00])')
assert_equal(repr(z), 'array([       inf,  1.12e+000, -1.00e+120])')
```

## Next Steps


---

*Source: test_arrayprint.py:741 | Complexity: Advanced | Last updated: 2026-06-02*