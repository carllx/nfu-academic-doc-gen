# How To: Complex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complex

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

### Step 1: Assign y = geomspace(...)

```python
y = geomspace(1j, 16j, num=5)
```

**Verification:**
```python
assert_allclose(y, [1j, 2j, 4j, 8j, 16j])
```

### Step 2: Call assert_allclose()

```python
assert_allclose(y, [1j, 2j, 4j, 8j, 16j])
```

**Verification:**
```python
assert_array_equal(y.real, 0)
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(y.real, 0)
```

**Verification:**
```python
assert_allclose(y, [-4j, -12j, -36j, -108j, -324j])
```

### Step 4: Assign y = geomspace(...)

```python
y = geomspace(-4j, -324j, num=5)
```

**Verification:**
```python
assert_array_equal(y.real, 0)
```

### Step 5: Call assert_allclose()

```python
assert_allclose(y, [-4j, -12j, -36j, -108j, -324j])
```

**Verification:**
```python
assert_allclose(y, [1 + 1j, 10 + 10j, 100 + 100j, 1000 + 1000j])
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(y.real, 0)
```

**Verification:**
```python
assert_allclose(y, [-1 + 1j, -10 + 10j, -100 + 100j, -1000 + 1000j])
```

### Step 7: Assign y = geomspace(...)

```python
y = geomspace(1 + 1j, 1000 + 1000j, num=4)
```

**Verification:**
```python
assert_allclose(y, [-1, 1j, +1])
```

### Step 8: Call assert_allclose()

```python
assert_allclose(y, [1 + 1j, 10 + 10j, 100 + 100j, 1000 + 1000j])
```

**Verification:**
```python
assert_allclose(y, [0 + 3j, -3 / sqrt(2) + 3j / sqrt(2), -3 + 0j])
```

### Step 9: Assign y = geomspace(...)

```python
y = geomspace(-1 + 1j, -1000 + 1000j, num=4)
```

**Verification:**
```python
assert_allclose(y, [0 + 3j, 3 / sqrt(2) + 3j / sqrt(2), 3 + 0j])
```

### Step 10: Call assert_allclose()

```python
assert_allclose(y, [-1 + 1j, -10 + 10j, -100 + 100j, -1000 + 1000j])
```

**Verification:**
```python
assert_allclose(y, [-3 + 0j, -3 / sqrt(2) - 3j / sqrt(2), 0 - 3j])
```

### Step 11: Assign y = geomspace(...)

```python
y = geomspace(-1, 1, num=3, dtype=complex)
```

**Verification:**
```python
assert_allclose(y, [0 + 3j, -3 / sqrt(2) + 3j / sqrt(2), -3 + 0j])
```

### Step 12: Call assert_allclose()

```python
assert_allclose(y, [-1, 1j, +1])
```

**Verification:**
```python
assert_allclose(y, [-2 - 3j, -0.29058977 - 4.15771027j, 2.08885354 - 4.34146838j, 4.58345529 - 3.16355218j, 6.41401745 - 0.55233457j, 6.75707386 + 3.11795092j, 5 + 7j])
```

### Step 13: Assign y = geomspace(...)

```python
y = geomspace(0 + 3j, -3 + 0j, 3)
```

**Verification:**
```python
assert_allclose(y, [3j, -5])
```

### Step 14: Call assert_allclose()

```python
assert_allclose(y, [0 + 3j, -3 / sqrt(2) + 3j / sqrt(2), -3 + 0j])
```

**Verification:**
```python
assert_allclose(y, [-5, 3j])
```

### Step 15: Assign y = geomspace(...)

```python
y = geomspace(0 + 3j, 3 + 0j, 3)
```

### Step 16: Call assert_allclose()

```python
assert_allclose(y, [0 + 3j, 3 / sqrt(2) + 3j / sqrt(2), 3 + 0j])
```

### Step 17: Assign y = geomspace(...)

```python
y = geomspace(-3 + 0j, 0 - 3j, 3)
```

### Step 18: Call assert_allclose()

```python
assert_allclose(y, [-3 + 0j, -3 / sqrt(2) - 3j / sqrt(2), 0 - 3j])
```

### Step 19: Assign y = geomspace(...)

```python
y = geomspace(0 + 3j, -3 + 0j, 3)
```

### Step 20: Call assert_allclose()

```python
assert_allclose(y, [0 + 3j, -3 / sqrt(2) + 3j / sqrt(2), -3 + 0j])
```

### Step 21: Assign y = geomspace(...)

```python
y = geomspace(-2 - 3j, 5 + 7j, 7)
```

### Step 22: Call assert_allclose()

```python
assert_allclose(y, [-2 - 3j, -0.29058977 - 4.15771027j, 2.08885354 - 4.34146838j, 4.58345529 - 3.16355218j, 6.41401745 - 0.55233457j, 6.75707386 + 3.11795092j, 5 + 7j])
```

### Step 23: Assign y = geomspace(...)

```python
y = geomspace(3j, -5, 2)
```

### Step 24: Call assert_allclose()

```python
assert_allclose(y, [3j, -5])
```

### Step 25: Assign y = geomspace(...)

```python
y = geomspace(-5, 3j, 2)
```

### Step 26: Call assert_allclose()

```python
assert_allclose(y, [-5, 3j])
```


## Complete Example

```python
# Workflow
y = geomspace(1j, 16j, num=5)
assert_allclose(y, [1j, 2j, 4j, 8j, 16j])
assert_array_equal(y.real, 0)
y = geomspace(-4j, -324j, num=5)
assert_allclose(y, [-4j, -12j, -36j, -108j, -324j])
assert_array_equal(y.real, 0)
y = geomspace(1 + 1j, 1000 + 1000j, num=4)
assert_allclose(y, [1 + 1j, 10 + 10j, 100 + 100j, 1000 + 1000j])
y = geomspace(-1 + 1j, -1000 + 1000j, num=4)
assert_allclose(y, [-1 + 1j, -10 + 10j, -100 + 100j, -1000 + 1000j])
y = geomspace(-1, 1, num=3, dtype=complex)
assert_allclose(y, [-1, 1j, +1])
y = geomspace(0 + 3j, -3 + 0j, 3)
assert_allclose(y, [0 + 3j, -3 / sqrt(2) + 3j / sqrt(2), -3 + 0j])
y = geomspace(0 + 3j, 3 + 0j, 3)
assert_allclose(y, [0 + 3j, 3 / sqrt(2) + 3j / sqrt(2), 3 + 0j])
y = geomspace(-3 + 0j, 0 - 3j, 3)
assert_allclose(y, [-3 + 0j, -3 / sqrt(2) - 3j / sqrt(2), 0 - 3j])
y = geomspace(0 + 3j, -3 + 0j, 3)
assert_allclose(y, [0 + 3j, -3 / sqrt(2) + 3j / sqrt(2), -3 + 0j])
y = geomspace(-2 - 3j, 5 + 7j, 7)
assert_allclose(y, [-2 - 3j, -0.29058977 - 4.15771027j, 2.08885354 - 4.34146838j, 4.58345529 - 3.16355218j, 6.41401745 - 0.55233457j, 6.75707386 + 3.11795092j, 5 + 7j])
y = geomspace(3j, -5, 2)
assert_allclose(y, [3j, -5])
y = geomspace(-5, 3j, 2)
assert_allclose(y, [-5, 3j])
```

## Next Steps


---

*Source: test_function_base.py:205 | Complexity: Advanced | Last updated: 2026-06-02*