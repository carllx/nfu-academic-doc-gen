# How To: Symbol Basic

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test symbol basic

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
p = poly.Polynomial([1, 2, 3], symbol='z')
```

**Verification:**
```python
assert_equal(self.as_latex(p), '$z \\mapsto 1.0 + 2.0\\,z + 3.0\\,z^{2}$')
```

### Step 2: Call assert_equal()

```python
assert_equal(self.as_latex(p), '$z \\mapsto 1.0 + 2.0\\,z + 3.0\\,z^{2}$')
```

**Verification:**
```python
assert_equal(self.as_latex(p), '$z \\mapsto 1.0 + 2.0\\,\\left(1.0 + z\\right) + 3.0\\,\\left(1.0 + z\\right)^{2}$')
```

### Step 3: Assign p = poly.Polynomial(...)

```python
p = poly.Polynomial([1, 2, 3], domain=[-2, 0], symbol='z')
```

**Verification:**
```python
assert_equal(self.as_latex(p), '$z \\mapsto 1.0 + 2.0\\,\\left(2.0z\\right) + 3.0\\,\\left(2.0z\\right)^{2}$')
```

### Step 4: Call assert_equal()

```python
assert_equal(self.as_latex(p), '$z \\mapsto 1.0 + 2.0\\,\\left(1.0 + z\\right) + 3.0\\,\\left(1.0 + z\\right)^{2}$')
```

**Verification:**
```python
assert_equal(self.as_latex(p), '$z \\mapsto 1.0 + 2.0\\,\\left(1.0 + 2.0z\\right) + 3.0\\,\\left(1.0 + 2.0z\\right)^{2}$')
```

### Step 5: Assign p = poly.Polynomial(...)

```python
p = poly.Polynomial([1, 2, 3], domain=[-0.5, 0.5], symbol='z')
```

### Step 6: Call assert_equal()

```python
assert_equal(self.as_latex(p), '$z \\mapsto 1.0 + 2.0\\,\\left(2.0z\\right) + 3.0\\,\\left(2.0z\\right)^{2}$')
```

### Step 7: Assign p = poly.Polynomial(...)

```python
p = poly.Polynomial([1, 2, 3], domain=[-1, 0], symbol='z')
```

### Step 8: Call assert_equal()

```python
assert_equal(self.as_latex(p), '$z \\mapsto 1.0 + 2.0\\,\\left(1.0 + 2.0z\\right) + 3.0\\,\\left(1.0 + 2.0z\\right)^{2}$')
```


## Complete Example

```python
# Workflow
p = poly.Polynomial([1, 2, 3], symbol='z')
assert_equal(self.as_latex(p), '$z \\mapsto 1.0 + 2.0\\,z + 3.0\\,z^{2}$')
p = poly.Polynomial([1, 2, 3], domain=[-2, 0], symbol='z')
assert_equal(self.as_latex(p), '$z \\mapsto 1.0 + 2.0\\,\\left(1.0 + z\\right) + 3.0\\,\\left(1.0 + z\\right)^{2}$')
p = poly.Polynomial([1, 2, 3], domain=[-0.5, 0.5], symbol='z')
assert_equal(self.as_latex(p), '$z \\mapsto 1.0 + 2.0\\,\\left(2.0z\\right) + 3.0\\,\\left(2.0z\\right)^{2}$')
p = poly.Polynomial([1, 2, 3], domain=[-1, 0], symbol='z')
assert_equal(self.as_latex(p), '$z \\mapsto 1.0 + 2.0\\,\\left(1.0 + 2.0z\\right) + 3.0\\,\\left(1.0 + 2.0z\\right)^{2}$')
```

## Next Steps


---

*Source: test_printing.py:446 | Complexity: Advanced | Last updated: 2026-06-02*