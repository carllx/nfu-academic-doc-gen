# How To: Subclass

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subclass

## Prerequisites

**Required Modules:**
- `platform`
- `sys`
- `pytest`
- `numpy`
- `numpy`
- `numpy._core`
- `numpy._core.function_base`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = array.view(...)

```python
a = array(1).view(PhysicalQuantity2)
```

**Verification:**
```python
assert type(ls) is PhysicalQuantity2
```

### Step 2: Assign b = array.view(...)

```python
b = array(7).view(PhysicalQuantity2)
```

**Verification:**
```python
assert_equal(ls, logspace(1.0, 7.0))
```

### Step 3: Assign ls = logspace(...)

```python
ls = logspace(a, b)
```

**Verification:**
```python
assert type(ls) is PhysicalQuantity2
```

### Step 4: Call assert_equal()

```python
assert_equal(ls, logspace(1.0, 7.0))
```

**Verification:**
```python
assert_equal(ls, logspace(1.0, 7.0, 1))
```

### Step 5: Assign ls = logspace(...)

```python
ls = logspace(a, b, 1)
```

**Verification:**
```python
assert type(ls) is PhysicalQuantity2
```

### Step 6: Call assert_equal()

```python
assert_equal(ls, logspace(1.0, 7.0, 1))
```


## Complete Example

```python
# Workflow
a = array(1).view(PhysicalQuantity2)
b = array(7).view(PhysicalQuantity2)
ls = logspace(a, b)
assert type(ls) is PhysicalQuantity2
assert_equal(ls, logspace(1.0, 7.0))
ls = logspace(a, b, 1)
assert type(ls) is PhysicalQuantity2
assert_equal(ls, logspace(1.0, 7.0, 1))
```

## Next Steps


---

*Source: test_function_base.py:136 | Complexity: Intermediate | Last updated: 2026-06-02*