# How To: Tril Indices

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tril indices

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign il1 = tril_indices(...)

```python
il1 = tril_indices(4)
```

**Verification:**
```python
assert_array_equal(a[il1], array([1, 5, 6, 9, 10, 11, 13, 14, 15, 16]))
```

### Step 2: Assign il2 = tril_indices(...)

```python
il2 = tril_indices(4, k=2)
```

**Verification:**
```python
assert_array_equal(b[il3], array([1, 6, 7, 11, 12, 13, 16, 17, 18, 19]))
```

### Step 3: Assign il3 = tril_indices(...)

```python
il3 = tril_indices(4, m=5)
```

**Verification:**
```python
assert_array_equal(a, array([[-1, 2, 3, 4], [-1, -1, 7, 8], [-1, -1, -1, 12], [-1, -1, -1, -1]]))
```

### Step 4: Assign il4 = tril_indices(...)

```python
il4 = tril_indices(4, k=2, m=5)
```

**Verification:**
```python
assert_array_equal(b, array([[-1, 2, 3, 4, 5], [-1, -1, 8, 9, 10], [-1, -1, -1, 14, 15], [-1, -1, -1, -1, 20]]))
```

### Step 5: Assign a = np.array(...)

```python
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
```

**Verification:**
```python
assert_array_equal(a, array([[-10, -10, -10, 4], [-10, -10, -10, -10], [-10, -10, -10, -10], [-10, -10, -10, -10]]))
```

### Step 6: Assign b = np.arange.reshape(...)

```python
b = np.arange(1, 21).reshape(4, 5)
```

**Verification:**
```python
assert_array_equal(b, array([[-10, -10, -10, 4, 5], [-10, -10, -10, -10, 10], [-10, -10, -10, -10, -10], [-10, -10, -10, -10, -10]]))
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(a[il1], array([1, 5, 6, 9, 10, 11, 13, 14, 15, 16]))
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(b[il3], array([1, 6, 7, 11, 12, 13, 16, 17, 18, 19]))
```

### Step 9: Assign unknown = value

```python
a[il1] = -1
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(a, array([[-1, 2, 3, 4], [-1, -1, 7, 8], [-1, -1, -1, 12], [-1, -1, -1, -1]]))
```

### Step 11: Assign unknown = value

```python
b[il3] = -1
```

### Step 12: Call assert_array_equal()

```python
assert_array_equal(b, array([[-1, 2, 3, 4, 5], [-1, -1, 8, 9, 10], [-1, -1, -1, 14, 15], [-1, -1, -1, -1, 20]]))
```

### Step 13: Assign unknown = value

```python
a[il2] = -10
```

### Step 14: Call assert_array_equal()

```python
assert_array_equal(a, array([[-10, -10, -10, 4], [-10, -10, -10, -10], [-10, -10, -10, -10], [-10, -10, -10, -10]]))
```

### Step 15: Assign unknown = value

```python
b[il4] = -10
```

### Step 16: Call assert_array_equal()

```python
assert_array_equal(b, array([[-10, -10, -10, 4, 5], [-10, -10, -10, -10, 10], [-10, -10, -10, -10, -10], [-10, -10, -10, -10, -10]]))
```


## Complete Example

```python
# Workflow
il1 = tril_indices(4)
il2 = tril_indices(4, k=2)
il3 = tril_indices(4, m=5)
il4 = tril_indices(4, k=2, m=5)
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
b = np.arange(1, 21).reshape(4, 5)
assert_array_equal(a[il1], array([1, 5, 6, 9, 10, 11, 13, 14, 15, 16]))
assert_array_equal(b[il3], array([1, 6, 7, 11, 12, 13, 16, 17, 18, 19]))
a[il1] = -1
assert_array_equal(a, array([[-1, 2, 3, 4], [-1, -1, 7, 8], [-1, -1, -1, 12], [-1, -1, -1, -1]]))
b[il3] = -1
assert_array_equal(b, array([[-1, 2, 3, 4, 5], [-1, -1, 8, 9, 10], [-1, -1, -1, 14, 15], [-1, -1, -1, -1, 20]]))
a[il2] = -10
assert_array_equal(a, array([[-10, -10, -10, 4], [-10, -10, -10, -10], [-10, -10, -10, -10], [-10, -10, -10, -10]]))
b[il4] = -10
assert_array_equal(b, array([[-10, -10, -10, 4, 5], [-10, -10, -10, -10, 10], [-10, -10, -10, -10, -10], [-10, -10, -10, -10, -10]]))
```

## Next Steps


---

*Source: test_twodim_base.py:417 | Complexity: Advanced | Last updated: 2026-06-02*