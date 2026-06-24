# How To: Roots

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test roots

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.polynomial.polynomial`
- `numpy.testing`
- `decimal`


## Step-by-Step Guide

### Step 1: Call assert_array_equal()

```python
assert_array_equal(np.roots([1, 0, 0]), [0, 0])
```

**Verification:**
```python
assert_array_equal(np.roots([1, 0, 0]), [0, 0])
```

### Step 2: Assign tgt = np.array(...)

```python
tgt = np.array([-1, 1, i])
```

**Verification:**
```python
assert_almost_equal(res, tgt, 14 - int(np.log10(i)))
```

### Step 3: Assign res = np.sort(...)

```python
res = np.sort(np.roots(poly.polyfromroots(tgt)[::-1]))
```

**Verification:**
```python
assert_almost_equal(res, tgt, 14 - int(np.log10(i)))
```

### Step 4: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt, 14 - int(np.log10(i)))
```

### Step 5: Assign tgt = np.array(...)

```python
tgt = np.array([-1, 1.01, i])
```

### Step 6: Assign res = np.sort(...)

```python
res = np.sort(np.roots(poly.polyfromroots(tgt)[::-1]))
```

### Step 7: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt, 14 - int(np.log10(i)))
```


## Complete Example

```python
# Workflow
assert_array_equal(np.roots([1, 0, 0]), [0, 0])
for i in np.logspace(10, 25, num=1000, base=10):
    tgt = np.array([-1, 1, i])
    res = np.sort(np.roots(poly.polyfromroots(tgt)[::-1]))
    assert_almost_equal(res, tgt, 14 - int(np.log10(i)))
for i in np.logspace(10, 25, num=1000, base=10):
    tgt = np.array([-1, 1.01, i])
    res = np.sort(np.roots(poly.polyfromroots(tgt)[::-1]))
    assert_almost_equal(res, tgt, 14 - int(np.log10(i)))
```

## Next Steps


---

*Source: test_polynomial.py:128 | Complexity: Intermediate | Last updated: 2026-06-02*