# How To: Tostring C

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tostring c

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy.f2py.symbolic`


## Step-by-Step Guide

### Step 1: Assign language = value

```python
language = Language.C
```

**Verification:**
```python
assert Expr(Op.FACTORS, {x: 2}).tostring(language=language) == 'x * x'
```

### Step 2: Assign x = as_symbol(...)

```python
x = as_symbol('x')
```

**Verification:**
```python
assert Expr(Op.FACTORS, {x + y: 2}).tostring(language=language) == '(x + y) * (x + y)'
```

### Step 3: Assign y = as_symbol(...)

```python
y = as_symbol('y')
```

**Verification:**
```python
assert Expr(Op.FACTORS, {x: 12}).tostring(language=language) == 'pow(x, 12)'
```

### Step 4: Assign z = as_symbol(...)

```python
z = as_symbol('z')
```

**Verification:**
```python
assert as_apply(ArithOp.DIV, x, y).tostring(language=language) == 'x / y'
```

### Step 5: Assign n = as_number(...)

```python
n = as_number(123)
```

**Verification:**
```python
assert as_apply(ArithOp.DIV, x, x + y).tostring(language=language) == 'x / (x + y)'
```


## Complete Example

```python
# Workflow
language = Language.C
x = as_symbol('x')
y = as_symbol('y')
z = as_symbol('z')
n = as_number(123)
assert Expr(Op.FACTORS, {x: 2}).tostring(language=language) == 'x * x'
assert Expr(Op.FACTORS, {x + y: 2}).tostring(language=language) == '(x + y) * (x + y)'
assert Expr(Op.FACTORS, {x: 12}).tostring(language=language) == 'pow(x, 12)'
assert as_apply(ArithOp.DIV, x, y).tostring(language=language) == 'x / y'
assert as_apply(ArithOp.DIV, x, x + y).tostring(language=language) == 'x / (x + y)'
assert as_apply(ArithOp.DIV, x - y, x + y).tostring(language=language) == '(x - y) / (x + y)'
assert (x + (x - y) / (x + y) + n).tostring(language=language) == '123 + x + (x - y) / (x + y)'
assert as_ternary(x, y, z).tostring(language=language) == '(x?y:z)'
assert as_eq(x, y).tostring(language=language) == 'x == y'
assert as_ne(x, y).tostring(language=language) == 'x != y'
assert as_lt(x, y).tostring(language=language) == 'x < y'
assert as_le(x, y).tostring(language=language) == 'x <= y'
assert as_gt(x, y).tostring(language=language) == 'x > y'
assert as_ge(x, y).tostring(language=language) == 'x >= y'
```

## Next Steps


---

*Source: test_symbolic.py:181 | Complexity: Intermediate | Last updated: 2026-06-02*