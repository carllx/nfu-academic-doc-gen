# How To: Substitute

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test substitute

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy.f2py.symbolic`


## Step-by-Step Guide

### Step 1: Assign x = as_symbol(...)

```python
x = as_symbol('x')
```

**Verification:**
```python
assert x.substitute({x: y}) == y
```

### Step 2: Assign y = as_symbol(...)

```python
y = as_symbol('y')
```

**Verification:**
```python
assert (x + y).substitute({x: z}) == y + z
```

### Step 3: Assign z = as_symbol(...)

```python
z = as_symbol('z')
```

**Verification:**
```python
assert (x * y).substitute({x: z}) == y * z
```

### Step 4: Assign a = as_array(...)

```python
a = as_array((x, y))
```

**Verification:**
```python
assert (x ** 4).substitute({x: z}) == z ** 4
```


## Complete Example

```python
# Workflow
x = as_symbol('x')
y = as_symbol('y')
z = as_symbol('z')
a = as_array((x, y))
assert x.substitute({x: y}) == y
assert (x + y).substitute({x: z}) == y + z
assert (x * y).substitute({x: z}) == y * z
assert (x ** 4).substitute({x: z}) == z ** 4
assert (x / y).substitute({x: z}) == z / y
assert x.substitute({x: y + z}) == y + z
assert a.substitute({x: y + z}) == as_array((y + z, y))
assert as_ternary(x, y, z).substitute({x: y + z}) == as_ternary(y + z, y, z)
assert as_eq(x, y).substitute({x: y + z}) == as_eq(y + z, y)
```

## Next Steps


---

*Source: test_symbolic.py:277 | Complexity: Intermediate | Last updated: 2026-06-02*