# How To: Objects

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test objects

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
p = np.poly1d([Decimal('4.0'), Decimal('3.0'), Decimal('2.0')])
```

**Verification:**
```python
assert_(p2[1] == Decimal('3.9999999999999990'))
```

### Step 2: Assign p2 = value

```python
p2 = p * Decimal('1.333333333333333')
```

**Verification:**
```python
assert_(p2[1] == Decimal('8.0'))
```

### Step 3: Call assert_()

```python
assert_(p2[1] == Decimal('3.9999999999999990'))
```

**Verification:**
```python
assert_(p2[3] == Decimal('1.333333333333333333333333333'))
```

### Step 4: Assign p2 = p.deriv(...)

```python
p2 = p.deriv()
```

**Verification:**
```python
assert_(p2[2] == Decimal('1.5'))
```

### Step 5: Call assert_()

```python
assert_(p2[1] == Decimal('8.0'))
```

**Verification:**
```python
assert_(np.issubdtype(p2.coeffs.dtype, np.object_))
```

### Step 6: Assign p2 = p.integ(...)

```python
p2 = p.integ()
```

**Verification:**
```python
assert_equal(np.poly([Decimal(1), Decimal(2)]), [1, Decimal(-3), Decimal(2)])
```

### Step 7: Call assert_()

```python
assert_(p2[3] == Decimal('1.333333333333333333333333333'))
```

### Step 8: Call assert_()

```python
assert_(p2[2] == Decimal('1.5'))
```

### Step 9: Call assert_()

```python
assert_(np.issubdtype(p2.coeffs.dtype, np.object_))
```

### Step 10: Assign p = np.poly(...)

```python
p = np.poly([Decimal(1), Decimal(2)])
```

### Step 11: Call assert_equal()

```python
assert_equal(np.poly([Decimal(1), Decimal(2)]), [1, Decimal(-3), Decimal(2)])
```


## Complete Example

```python
# Workflow
from decimal import Decimal
p = np.poly1d([Decimal('4.0'), Decimal('3.0'), Decimal('2.0')])
p2 = p * Decimal('1.333333333333333')
assert_(p2[1] == Decimal('3.9999999999999990'))
p2 = p.deriv()
assert_(p2[1] == Decimal('8.0'))
p2 = p.integ()
assert_(p2[3] == Decimal('1.333333333333333333333333333'))
assert_(p2[2] == Decimal('1.5'))
assert_(np.issubdtype(p2.coeffs.dtype, np.object_))
p = np.poly([Decimal(1), Decimal(2)])
assert_equal(np.poly([Decimal(1), Decimal(2)]), [1, Decimal(-3), Decimal(2)])
```

## Next Steps


---

*Source: test_polynomial.py:232 | Complexity: Advanced | Last updated: 2026-06-02*