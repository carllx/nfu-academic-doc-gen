# How To: Fraction

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test Fraction

## Prerequisites

**Required Modules:**
- `pickle`
- `copy`
- `fractions`
- `functools`
- `pytest`
- `numpy`
- `numpy.polynomial.polynomial`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign f = Fraction(...)

```python
f = Fraction(2, 3)
```

**Verification:**
```python
assert_equal(x.coef, np.array([Fraction(16, 9), Fraction(20, 9), Fraction(4, 9)], dtype=object))
```

### Step 2: Assign one = Fraction(...)

```python
one = Fraction(1, 1)
```

**Verification:**
```python
assert_equal(p.domain, [zero, one])
```

### Step 3: Assign zero = Fraction(...)

```python
zero = Fraction(0, 1)
```

**Verification:**
```python
assert_equal(p.coef.dtype, np.dtypes.ObjectDType())
```

### Step 4: Assign p = poly.Polynomial(...)

```python
p = poly.Polynomial([f, f], domain=[zero, one], window=[zero, one])
```

**Verification:**
```python
assert_(isinstance(p(f), Fraction))
```

### Step 5: Assign x = value

```python
x = 2 * p + p ** 2
```

**Verification:**
```python
assert_equal(p(f), Fraction(10, 9))
```

### Step 6: Call assert_equal()

```python
assert_equal(x.coef, np.array([Fraction(16, 9), Fraction(20, 9), Fraction(4, 9)], dtype=object))
```

**Verification:**
```python
assert_equal(p.deriv(), p_deriv)
```

### Step 7: Call assert_equal()

```python
assert_equal(p.domain, [zero, one])
```

### Step 8: Call assert_equal()

```python
assert_equal(p.coef.dtype, np.dtypes.ObjectDType())
```

### Step 9: Call assert_()

```python
assert_(isinstance(p(f), Fraction))
```

### Step 10: Call assert_equal()

```python
assert_equal(p(f), Fraction(10, 9))
```

### Step 11: Assign p_deriv = poly.Polynomial(...)

```python
p_deriv = poly.Polynomial([Fraction(2, 3)], domain=[zero, one], window=[zero, one])
```

### Step 12: Call assert_equal()

```python
assert_equal(p.deriv(), p_deriv)
```


## Complete Example

```python
# Workflow
f = Fraction(2, 3)
one = Fraction(1, 1)
zero = Fraction(0, 1)
p = poly.Polynomial([f, f], domain=[zero, one], window=[zero, one])
x = 2 * p + p ** 2
assert_equal(x.coef, np.array([Fraction(16, 9), Fraction(20, 9), Fraction(4, 9)], dtype=object))
assert_equal(p.domain, [zero, one])
assert_equal(p.coef.dtype, np.dtypes.ObjectDType())
assert_(isinstance(p(f), Fraction))
assert_equal(p(f), Fraction(10, 9))
p_deriv = poly.Polynomial([Fraction(2, 3)], domain=[zero, one], window=[zero, one])
assert_equal(p.deriv(), p_deriv)
```

## Next Steps


---

*Source: test_polynomial.py:136 | Complexity: Advanced | Last updated: 2026-06-02*