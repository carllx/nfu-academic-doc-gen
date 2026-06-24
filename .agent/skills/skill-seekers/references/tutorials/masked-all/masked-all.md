# How To: Masked All

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test masked all

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

### Step 1: Assign test = masked_all(...)

```python
test = masked_all((2,), dtype=float)
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 2: Assign control = array(...)

```python
control = array([1, 1], mask=[1, 1], dtype=float)
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 3: Call assert_equal()

```python
assert_equal(test, control)
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 4: Assign dt = np.dtype(...)

```python
dt = np.dtype({'names': ['a', 'b'], 'formats': ['f', 'f']})
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 5: Assign test = masked_all(...)

```python
test = masked_all((2,), dtype=dt)
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 6: Assign control = array(...)

```python
control = array([(0, 0), (0, 0)], mask=[(1, 1), (1, 1)], dtype=dt)
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 7: Call assert_equal()

```python
assert_equal(test, control)
```

### Step 8: Assign test = masked_all(...)

```python
test = masked_all((2, 2), dtype=dt)
```

### Step 9: Assign control = array(...)

```python
control = array([[(0, 0), (0, 0)], [(0, 0), (0, 0)]], mask=[[(1, 1), (1, 1)], [(1, 1), (1, 1)]], dtype=dt)
```

### Step 10: Call assert_equal()

```python
assert_equal(test, control)
```

### Step 11: Assign dt = np.dtype(...)

```python
dt = np.dtype([('a', 'f'), ('b', [('ba', 'f'), ('bb', 'f')])])
```

### Step 12: Assign test = masked_all(...)

```python
test = masked_all((2,), dtype=dt)
```

### Step 13: Assign control = array(...)

```python
control = array([(1, (1, 1)), (1, (1, 1))], mask=[(1, (1, 1)), (1, (1, 1))], dtype=dt)
```

### Step 14: Call assert_equal()

```python
assert_equal(test, control)
```

### Step 15: Assign test = masked_all(...)

```python
test = masked_all((2,), dtype=dt)
```

### Step 16: Assign control = array(...)

```python
control = array([(1, (1, 1)), (1, (1, 1))], mask=[(1, (1, 1)), (1, (1, 1))], dtype=dt)
```

### Step 17: Call assert_equal()

```python
assert_equal(test, control)
```

### Step 18: Assign test = masked_all(...)

```python
test = masked_all((1, 1), dtype=dt)
```

### Step 19: Assign control = array(...)

```python
control = array([[(1, (1, 1))]], mask=[[(1, (1, 1))]], dtype=dt)
```

### Step 20: Call assert_equal()

```python
assert_equal(test, control)
```


## Complete Example

```python
# Workflow
test = masked_all((2,), dtype=float)
control = array([1, 1], mask=[1, 1], dtype=float)
assert_equal(test, control)
dt = np.dtype({'names': ['a', 'b'], 'formats': ['f', 'f']})
test = masked_all((2,), dtype=dt)
control = array([(0, 0), (0, 0)], mask=[(1, 1), (1, 1)], dtype=dt)
assert_equal(test, control)
test = masked_all((2, 2), dtype=dt)
control = array([[(0, 0), (0, 0)], [(0, 0), (0, 0)]], mask=[[(1, 1), (1, 1)], [(1, 1), (1, 1)]], dtype=dt)
assert_equal(test, control)
dt = np.dtype([('a', 'f'), ('b', [('ba', 'f'), ('bb', 'f')])])
test = masked_all((2,), dtype=dt)
control = array([(1, (1, 1)), (1, (1, 1))], mask=[(1, (1, 1)), (1, (1, 1))], dtype=dt)
assert_equal(test, control)
test = masked_all((2,), dtype=dt)
control = array([(1, (1, 1)), (1, (1, 1))], mask=[(1, (1, 1)), (1, (1, 1))], dtype=dt)
assert_equal(test, control)
test = masked_all((1, 1), dtype=dt)
control = array([[(1, (1, 1))]], mask=[[(1, (1, 1))]], dtype=dt)
assert_equal(test, control)
```

## Next Steps


---

*Source: test_extras.py:75 | Complexity: Advanced | Last updated: 2026-06-02*