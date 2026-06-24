# How To: Poly1D Math

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test poly1d math

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.polynomial.polynomial`
- `numpy.testing`
- `decimal`


## Step-by-Step Guide

### Step 1: Assign p = np.poly1d(...)

```python
p = np.poly1d([1.0, 2, 4])
```

**Verification:**
```python
assert_equal(p / q, (np.poly1d([0.25]), np.poly1d([1.5, 3.75])))
```

### Step 2: Assign q = np.poly1d(...)

```python
q = np.poly1d([4.0, 2, 1])
```

**Verification:**
```python
assert_equal(p.integ(), np.poly1d([1 / 3, 1.0, 4.0, 0.0]))
```

### Step 3: Call assert_equal()

```python
assert_equal(p / q, (np.poly1d([0.25]), np.poly1d([1.5, 3.75])))
```

**Verification:**
```python
assert_equal(p.integ(1), np.poly1d([1 / 3, 1.0, 4.0, 0.0]))
```

### Step 4: Call assert_equal()

```python
assert_equal(p.integ(), np.poly1d([1 / 3, 1.0, 4.0, 0.0]))
```

**Verification:**
```python
assert_equal(p * q, np.poly1d([3.0, 8.0, 14.0, 8.0, 3.0]))
```

### Step 5: Call assert_equal()

```python
assert_equal(p.integ(1), np.poly1d([1 / 3, 1.0, 4.0, 0.0]))
```

**Verification:**
```python
assert_equal(p + q, np.poly1d([4.0, 4.0, 4.0]))
```

### Step 6: Assign p = np.poly1d(...)

```python
p = np.poly1d([1.0, 2, 3])
```

**Verification:**
```python
assert_equal(p - q, np.poly1d([-2.0, 0.0, 2.0]))
```

### Step 7: Assign q = np.poly1d(...)

```python
q = np.poly1d([3.0, 2, 1])
```

**Verification:**
```python
assert_equal(p ** 4, np.poly1d([1.0, 8.0, 36.0, 104.0, 214.0, 312.0, 324.0, 216.0, 81.0]))
```

### Step 8: Call assert_equal()

```python
assert_equal(p * q, np.poly1d([3.0, 8.0, 14.0, 8.0, 3.0]))
```

**Verification:**
```python
assert_equal(p(q), np.poly1d([9.0, 12.0, 16.0, 8.0, 6.0]))
```

### Step 9: Call assert_equal()

```python
assert_equal(p + q, np.poly1d([4.0, 4.0, 4.0]))
```

**Verification:**
```python
assert_equal(q(p), np.poly1d([3.0, 12.0, 32.0, 40.0, 34.0]))
```

### Step 10: Call assert_equal()

```python
assert_equal(p - q, np.poly1d([-2.0, 0.0, 2.0]))
```

**Verification:**
```python
assert_equal(p.deriv(), np.poly1d([2.0, 2.0]))
```

### Step 11: Call assert_equal()

```python
assert_equal(p ** 4, np.poly1d([1.0, 8.0, 36.0, 104.0, 214.0, 312.0, 324.0, 216.0, 81.0]))
```

**Verification:**
```python
assert_equal(p.deriv(2), np.poly1d([2.0]))
```

### Step 12: Call assert_equal()

```python
assert_equal(p(q), np.poly1d([9.0, 12.0, 16.0, 8.0, 6.0]))
```

**Verification:**
```python
assert_equal(np.polydiv(np.poly1d([1, 0, -1]), np.poly1d([1, 1])), (np.poly1d([1.0, -1.0]), np.poly1d([0.0])))
```

### Step 13: Call assert_equal()

```python
assert_equal(q(p), np.poly1d([3.0, 12.0, 32.0, 40.0, 34.0]))
```

### Step 14: Call assert_equal()

```python
assert_equal(p.deriv(), np.poly1d([2.0, 2.0]))
```

### Step 15: Call assert_equal()

```python
assert_equal(p.deriv(2), np.poly1d([2.0]))
```

### Step 16: Call assert_equal()

```python
assert_equal(np.polydiv(np.poly1d([1, 0, -1]), np.poly1d([1, 1])), (np.poly1d([1.0, -1.0]), np.poly1d([0.0])))
```


## Complete Example

```python
# Workflow
p = np.poly1d([1.0, 2, 4])
q = np.poly1d([4.0, 2, 1])
assert_equal(p / q, (np.poly1d([0.25]), np.poly1d([1.5, 3.75])))
assert_equal(p.integ(), np.poly1d([1 / 3, 1.0, 4.0, 0.0]))
assert_equal(p.integ(1), np.poly1d([1 / 3, 1.0, 4.0, 0.0]))
p = np.poly1d([1.0, 2, 3])
q = np.poly1d([3.0, 2, 1])
assert_equal(p * q, np.poly1d([3.0, 8.0, 14.0, 8.0, 3.0]))
assert_equal(p + q, np.poly1d([4.0, 4.0, 4.0]))
assert_equal(p - q, np.poly1d([-2.0, 0.0, 2.0]))
assert_equal(p ** 4, np.poly1d([1.0, 8.0, 36.0, 104.0, 214.0, 312.0, 324.0, 216.0, 81.0]))
assert_equal(p(q), np.poly1d([9.0, 12.0, 16.0, 8.0, 6.0]))
assert_equal(q(p), np.poly1d([3.0, 12.0, 32.0, 40.0, 34.0]))
assert_equal(p.deriv(), np.poly1d([2.0, 2.0]))
assert_equal(p.deriv(2), np.poly1d([2.0]))
assert_equal(np.polydiv(np.poly1d([1, 0, -1]), np.poly1d([1, 1])), (np.poly1d([1.0, -1.0]), np.poly1d([0.0])))
```

## Next Steps


---

*Source: test_polynomial.py:51 | Complexity: Advanced | Last updated: 2026-06-02*