# How To: Eig Build

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test eig build

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign rva = array(...)

```python
rva = array([103.221168 + 0j, -19.1843603 + 0j, -0.604004526 + 15.84422474j, -0.604004526 - 15.84422474j, -11.3692929 + 0j, -0.657612485 + 10.41755503j, -0.657612485 - 10.41755503j, 18.2126812 + 0j, 10.6011014 + 0j, 7.80732773 + 0j, -0.765390898 + 0j, 1.51971555e-15 + 0j, -1.51308713e-15 + 0j])
```

**Verification:**
```python
assert_array_almost_equal(va, rva)
```

### Step 2: Assign a = arange(...)

```python
a = arange(13 * 13, dtype=float64)
```

### Step 3: Assign a = a.reshape(...)

```python
a = a.reshape((13, 13))
```

### Step 4: Assign a = value

```python
a = a % 17
```

### Step 5: Assign unknown = linalg.eig(...)

```python
va, ve = linalg.eig(a)
```

### Step 6: Call va.sort()

```python
va.sort()
```

### Step 7: Call rva.sort()

```python
rva.sort()
```

### Step 8: Call assert_array_almost_equal()

```python
assert_array_almost_equal(va, rva)
```


## Complete Example

```python
# Workflow
rva = array([103.221168 + 0j, -19.1843603 + 0j, -0.604004526 + 15.84422474j, -0.604004526 - 15.84422474j, -11.3692929 + 0j, -0.657612485 + 10.41755503j, -0.657612485 - 10.41755503j, 18.2126812 + 0j, 10.6011014 + 0j, 7.80732773 + 0j, -0.765390898 + 0j, 1.51971555e-15 + 0j, -1.51308713e-15 + 0j])
a = arange(13 * 13, dtype=float64)
a = a.reshape((13, 13))
a = a % 17
va, ve = linalg.eig(a)
va.sort()
rva.sort()
assert_array_almost_equal(va, rva)
```

## Next Steps


---

*Source: test_regression.py:20 | Complexity: Advanced | Last updated: 2026-06-02*