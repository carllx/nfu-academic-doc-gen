# How To: Masked All Like

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test masked all like

## Prerequisites

**Required Modules:**
- `inspect`
- `itertools`
- `pytest`
- `numpy`
- `numpy._core.numeric`
- `numpy.ma.core`
- `numpy.ma.extras`
- `numpy.ma.testutils`


## Step-by-Step Guide

### Step 1: Assign base = array(...)

```python
base = array([1, 2], dtype=float)
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 2: Assign test = masked_all_like(...)

```python
test = masked_all_like(base)
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 3: Assign control = array(...)

```python
control = array([1, 1], mask=[1, 1], dtype=float)
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 4: Call assert_equal()

```python
assert_equal(test, control)
```

### Step 5: Assign dt = np.dtype(...)

```python
dt = np.dtype({'names': ['a', 'b'], 'formats': ['f', 'f']})
```

### Step 6: Assign base = array(...)

```python
base = array([(0, 0), (0, 0)], mask=[(1, 1), (1, 1)], dtype=dt)
```

### Step 7: Assign test = masked_all_like(...)

```python
test = masked_all_like(base)
```

### Step 8: Assign control = array(...)

```python
control = array([(10, 10), (10, 10)], mask=[(1, 1), (1, 1)], dtype=dt)
```

### Step 9: Call assert_equal()

```python
assert_equal(test, control)
```

### Step 10: Assign dt = np.dtype(...)

```python
dt = np.dtype([('a', 'f'), ('b', [('ba', 'f'), ('bb', 'f')])])
```

### Step 11: Assign control = array(...)

```python
control = array([(1, (1, 1)), (1, (1, 1))], mask=[(1, (1, 1)), (1, (1, 1))], dtype=dt)
```

### Step 12: Assign test = masked_all_like(...)

```python
test = masked_all_like(control)
```

### Step 13: Call assert_equal()

```python
assert_equal(test, control)
```


## Complete Example

```python
# Workflow
base = array([1, 2], dtype=float)
test = masked_all_like(base)
control = array([1, 1], mask=[1, 1], dtype=float)
assert_equal(test, control)
dt = np.dtype({'names': ['a', 'b'], 'formats': ['f', 'f']})
base = array([(0, 0), (0, 0)], mask=[(1, 1), (1, 1)], dtype=dt)
test = masked_all_like(base)
control = array([(10, 10), (10, 10)], mask=[(1, 1), (1, 1)], dtype=dt)
assert_equal(test, control)
dt = np.dtype([('a', 'f'), ('b', [('ba', 'f'), ('bb', 'f')])])
control = array([(1, (1, 1)), (1, (1, 1))], mask=[(1, (1, 1)), (1, (1, 1))], dtype=dt)
test = masked_all_like(control)
assert_equal(test, control)
```

## Next Steps


---

*Source: test_extras.py:127 | Complexity: Advanced | Last updated: 2026-06-02*