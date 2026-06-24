# How To: Division Complex

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test division complex

## Prerequisites

**Required Modules:**
- `fnmatch`
- `inspect`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `collections`
- `fractions`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.umath`
- `numpy._core`
- `numpy.testing`
- `numpy.testing._private.utils`
- `operator`
- `platform`
- `decimal`
- `cmath`


## Step-by-Step Guide

### Step 1: Assign msg = 'Complex division implementation check'

```python
msg = 'Complex division implementation check'
```

**Verification:**
```python
assert_almost_equal(x ** 2 / x, x, err_msg=msg)
```

### Step 2: Assign x = np.array(...)

```python
x = np.array([1.0 + 1.0 * 1j, 1.0 + 0.5 * 1j, 1.0 + 2.0 * 1j], dtype=np.complex128)
```

**Verification:**
```python
assert_almost_equal(y / x, [1, 1], err_msg=msg)
```

### Step 3: Call assert_almost_equal()

```python
assert_almost_equal(x ** 2 / x, x, err_msg=msg)
```

### Step 4: Assign msg = 'Complex division overflow/underflow check'

```python
msg = 'Complex division overflow/underflow check'
```

### Step 5: Assign x = np.array(...)

```python
x = np.array([1e+110, 1e-110], dtype=np.complex128)
```

### Step 6: Assign y = value

```python
y = x ** 2 / x
```

### Step 7: Call assert_almost_equal()

```python
assert_almost_equal(y / x, [1, 1], err_msg=msg)
```


## Complete Example

```python
# Workflow
msg = 'Complex division implementation check'
x = np.array([1.0 + 1.0 * 1j, 1.0 + 0.5 * 1j, 1.0 + 2.0 * 1j], dtype=np.complex128)
assert_almost_equal(x ** 2 / x, x, err_msg=msg)
msg = 'Complex division overflow/underflow check'
x = np.array([1e+110, 1e-110], dtype=np.complex128)
y = x ** 2 / x
assert_almost_equal(y / x, [1, 1], err_msg=msg)
```

## Next Steps


---

*Source: test_umath.py:633 | Complexity: Intermediate | Last updated: 2026-06-02*