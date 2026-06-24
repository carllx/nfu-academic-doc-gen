# How To: Intersect1D Indices

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersect1d indices

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.dtypes`
- `numpy.exceptions`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([1, 2, 3, 4])
```

**Verification:**
```python
assert_array_equal(c, ee)
```

### Step 2: Assign b = np.array(...)

```python
b = np.array([2, 1, 4, 6])
```

**Verification:**
```python
assert_array_equal(a[i1], ee)
```

### Step 3: Assign unknown = intersect1d(...)

```python
c, i1, i2 = intersect1d(a, b, assume_unique=True, return_indices=True)
```

**Verification:**
```python
assert_array_equal(b[i2], ee)
```

### Step 4: Assign ee = np.array(...)

```python
ee = np.array([1, 2, 4])
```

**Verification:**
```python
assert_array_equal(c, ef)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(c, ee)
```

**Verification:**
```python
assert_array_equal(a[i1], ef)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(a[i1], ee)
```

**Verification:**
```python
assert_array_equal(b[i2], ef)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(b[i2], ee)
```

**Verification:**
```python
assert_array_equal(ea, a[ui1])
```

### Step 8: Assign a = np.array(...)

```python
a = np.array([1, 2, 2, 3, 4, 3, 2])
```

**Verification:**
```python
assert_array_equal(ea, b[ui2])
```

### Step 9: Assign b = np.array(...)

```python
b = np.array([1, 8, 4, 2, 2, 3, 2, 3])
```

**Verification:**
```python
assert_array_equal(ea, a[ui1])
```

### Step 10: Assign unknown = intersect1d(...)

```python
c, i1, i2 = intersect1d(a, b, return_indices=True)
```

**Verification:**
```python
assert_array_equal(ea, b[ui2])
```

### Step 11: Assign ef = np.array(...)

```python
ef = np.array([1, 2, 3, 4])
```

### Step 12: Call assert_array_equal()

```python
assert_array_equal(c, ef)
```

### Step 13: Call assert_array_equal()

```python
assert_array_equal(a[i1], ef)
```

### Step 14: Call assert_array_equal()

```python
assert_array_equal(b[i2], ef)
```

### Step 15: Assign a = np.array(...)

```python
a = np.array([[2, 4, 5, 6], [7, 8, 1, 15]])
```

### Step 16: Assign b = np.array(...)

```python
b = np.array([[3, 2, 7, 6], [10, 12, 8, 9]])
```

### Step 17: Assign unknown = intersect1d(...)

```python
c, i1, i2 = intersect1d(a, b, assume_unique=True, return_indices=True)
```

### Step 18: Assign ui1 = np.unravel_index(...)

```python
ui1 = np.unravel_index(i1, a.shape)
```

### Step 19: Assign ui2 = np.unravel_index(...)

```python
ui2 = np.unravel_index(i2, b.shape)
```

### Step 20: Assign ea = np.array(...)

```python
ea = np.array([2, 6, 7, 8])
```

### Step 21: Call assert_array_equal()

```python
assert_array_equal(ea, a[ui1])
```

### Step 22: Call assert_array_equal()

```python
assert_array_equal(ea, b[ui2])
```

### Step 23: Assign a = np.array(...)

```python
a = np.array([[2, 4, 5, 6, 6], [4, 7, 8, 7, 2]])
```

### Step 24: Assign b = np.array(...)

```python
b = np.array([[3, 2, 7, 7], [10, 12, 8, 7]])
```

### Step 25: Assign unknown = intersect1d(...)

```python
c, i1, i2 = intersect1d(a, b, return_indices=True)
```

### Step 26: Assign ui1 = np.unravel_index(...)

```python
ui1 = np.unravel_index(i1, a.shape)
```

### Step 27: Assign ui2 = np.unravel_index(...)

```python
ui2 = np.unravel_index(i2, b.shape)
```

### Step 28: Assign ea = np.array(...)

```python
ea = np.array([2, 7, 8])
```

### Step 29: Call assert_array_equal()

```python
assert_array_equal(ea, a[ui1])
```

### Step 30: Call assert_array_equal()

```python
assert_array_equal(ea, b[ui2])
```


## Complete Example

```python
# Workflow
a = np.array([1, 2, 3, 4])
b = np.array([2, 1, 4, 6])
c, i1, i2 = intersect1d(a, b, assume_unique=True, return_indices=True)
ee = np.array([1, 2, 4])
assert_array_equal(c, ee)
assert_array_equal(a[i1], ee)
assert_array_equal(b[i2], ee)
a = np.array([1, 2, 2, 3, 4, 3, 2])
b = np.array([1, 8, 4, 2, 2, 3, 2, 3])
c, i1, i2 = intersect1d(a, b, return_indices=True)
ef = np.array([1, 2, 3, 4])
assert_array_equal(c, ef)
assert_array_equal(a[i1], ef)
assert_array_equal(b[i2], ef)
a = np.array([[2, 4, 5, 6], [7, 8, 1, 15]])
b = np.array([[3, 2, 7, 6], [10, 12, 8, 9]])
c, i1, i2 = intersect1d(a, b, assume_unique=True, return_indices=True)
ui1 = np.unravel_index(i1, a.shape)
ui2 = np.unravel_index(i2, b.shape)
ea = np.array([2, 6, 7, 8])
assert_array_equal(ea, a[ui1])
assert_array_equal(ea, b[ui2])
a = np.array([[2, 4, 5, 6, 6], [4, 7, 8, 7, 2]])
b = np.array([[3, 2, 7, 7], [10, 12, 8, 7]])
c, i1, i2 = intersect1d(a, b, return_indices=True)
ui1 = np.unravel_index(i1, a.shape)
ui2 = np.unravel_index(i2, b.shape)
ea = np.array([2, 7, 8])
assert_array_equal(ea, a[ui1])
assert_array_equal(ea, b[ui2])
```

## Next Steps


---

*Source: test_arraysetops.py:50 | Complexity: Advanced | Last updated: 2026-06-02*