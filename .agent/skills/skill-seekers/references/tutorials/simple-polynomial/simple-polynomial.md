# How To: Simple Polynomial

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simple polynomial

## Prerequisites

**Required Modules:**
- `decimal`
- `fractions`
- `math`
- `pytest`
- `numpy.polynomial`
- `numpy._core`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign p = poly.Polynomial(...)

```python
p = poly.Polynomial([1, 2, 3])
```

**Verification:**
```python
assert_equal(self.as_latex(p), '$x \\mapsto 1.0 + 2.0\\,x + 3.0\\,x^{2}$')
```

### Step 2: Call assert_equal()

```python
assert_equal(self.as_latex(p), '$x \\mapsto 1.0 + 2.0\\,x + 3.0\\,x^{2}$')
```

**Verification:**
```python
assert_equal(self.as_latex(p), '$x \\mapsto 1.0 + 2.0\\,\\left(1.0 + x\\right) + 3.0\\,\\left(1.0 + x\\right)^{2}$')
```

### Step 3: Assign p = poly.Polynomial(...)

```python
p = poly.Polynomial([1, 2, 3], domain=[-2, 0])
```

**Verification:**
```python
assert_equal(self.as_latex(p), '$x \\mapsto 1.0 + 2.0\\,\\left(2.0x\\right) + 3.0\\,\\left(2.0x\\right)^{2}$')
```

### Step 4: Call assert_equal()

```python
assert_equal(self.as_latex(p), '$x \\mapsto 1.0 + 2.0\\,\\left(1.0 + x\\right) + 3.0\\,\\left(1.0 + x\\right)^{2}$')
```

**Verification:**
```python
assert_equal(self.as_latex(p), '$x \\mapsto 1.0 + 2.0\\,\\left(1.0 + 2.0x\\right) + 3.0\\,\\left(1.0 + 2.0x\\right)^{2}$')
```

### Step 5: Assign p = poly.Polynomial(...)

```python
p = poly.Polynomial([1, 2, 3], domain=[-0.5, 0.5])
```

### Step 6: Call assert_equal()

```python
assert_equal(self.as_latex(p), '$x \\mapsto 1.0 + 2.0\\,\\left(2.0x\\right) + 3.0\\,\\left(2.0x\\right)^{2}$')
```

### Step 7: Assign p = poly.Polynomial(...)

```python
p = poly.Polynomial([1, 2, 3], domain=[-1, 0])
```

### Step 8: Call assert_equal()

```python
assert_equal(self.as_latex(p), '$x \\mapsto 1.0 + 2.0\\,\\left(1.0 + 2.0x\\right) + 3.0\\,\\left(1.0 + 2.0x\\right)^{2}$')
```


## Complete Example

```python
# Workflow
p = poly.Polynomial([1, 2, 3])
assert_equal(self.as_latex(p), '$x \\mapsto 1.0 + 2.0\\,x + 3.0\\,x^{2}$')
p = poly.Polynomial([1, 2, 3], domain=[-2, 0])
assert_equal(self.as_latex(p), '$x \\mapsto 1.0 + 2.0\\,\\left(1.0 + x\\right) + 3.0\\,\\left(1.0 + x\\right)^{2}$')
p = poly.Polynomial([1, 2, 3], domain=[-0.5, 0.5])
assert_equal(self.as_latex(p), '$x \\mapsto 1.0 + 2.0\\,\\left(2.0x\\right) + 3.0\\,\\left(2.0x\\right)^{2}$')
p = poly.Polynomial([1, 2, 3], domain=[-1, 0])
assert_equal(self.as_latex(p), '$x \\mapsto 1.0 + 2.0\\,\\left(1.0 + 2.0x\\right) + 3.0\\,\\left(1.0 + 2.0x\\right)^{2}$')
```

## Next Steps


---

*Source: test_printing.py:411 | Complexity: Advanced | Last updated: 2026-06-02*