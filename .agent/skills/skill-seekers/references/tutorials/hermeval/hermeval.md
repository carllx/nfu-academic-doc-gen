# How To: Hermeval

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hermeval

## Prerequisites

**Required Modules:**
- `functools`
- `numpy`
- `numpy.polynomial.hermite_e`
- `numpy.polynomial.polynomial`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Call assert_equal()

```python
assert_equal(herme.hermeval([], [1]).size, 0)
```

**Verification:**
```python
assert_equal(herme.hermeval([], [1]).size, 0)
```

### Step 2: Assign x = np.linspace(...)

```python
x = np.linspace(-1, 1)
```

**Verification:**
```python
assert_almost_equal(res, tgt, err_msg=msg)
```

### Step 3: Assign y = value

```python
y = [polyval(x, c) for c in Helist]
```

**Verification:**
```python
assert_equal(herme.hermeval(x, [1]).shape, dims)
```

### Step 4: Assign msg = value

```python
msg = f'At i={i}'
```

**Verification:**
```python
assert_equal(herme.hermeval(x, [1, 0]).shape, dims)
```

### Step 5: Assign tgt = value

```python
tgt = y[i]
```

**Verification:**
```python
assert_equal(herme.hermeval(x, [1, 0, 0]).shape, dims)
```

### Step 6: Assign res = herme.hermeval(...)

```python
res = herme.hermeval(x, [0] * i + [1])
```

### Step 7: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt, err_msg=msg)
```

### Step 8: Assign dims = value

```python
dims = [2] * i
```

### Step 9: Assign x = np.zeros(...)

```python
x = np.zeros(dims)
```

### Step 10: Call assert_equal()

```python
assert_equal(herme.hermeval(x, [1]).shape, dims)
```

### Step 11: Call assert_equal()

```python
assert_equal(herme.hermeval(x, [1, 0]).shape, dims)
```

### Step 12: Call assert_equal()

```python
assert_equal(herme.hermeval(x, [1, 0, 0]).shape, dims)
```


## Complete Example

```python
# Workflow
assert_equal(herme.hermeval([], [1]).size, 0)
x = np.linspace(-1, 1)
y = [polyval(x, c) for c in Helist]
for i in range(10):
    msg = f'At i={i}'
    tgt = y[i]
    res = herme.hermeval(x, [0] * i + [1])
    assert_almost_equal(res, tgt, err_msg=msg)
for i in range(3):
    dims = [2] * i
    x = np.zeros(dims)
    assert_equal(herme.hermeval(x, [1]).shape, dims)
    assert_equal(herme.hermeval(x, [1, 0]).shape, dims)
    assert_equal(herme.hermeval(x, [1, 0, 0]).shape, dims)
```

## Next Steps


---

*Source: test_hermite_e.py:120 | Complexity: Advanced | Last updated: 2026-06-02*