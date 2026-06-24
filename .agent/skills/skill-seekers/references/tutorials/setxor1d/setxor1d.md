# How To: Setxor1D

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setxor1d

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
a = np.array([5, 7, 1, 2])
```

**Verification:**
```python
assert_array_equal(c, ec)
```

### Step 2: Assign b = np.array(...)

```python
b = np.array([2, 4, 3, 1, 5])
```

**Verification:**
```python
assert_array_equal(c, ec)
```

### Step 3: Assign ec = np.array(...)

```python
ec = np.array([3, 4, 7])
```

**Verification:**
```python
assert_array_equal(c, ec)
```

### Step 4: Assign c = setxor1d(...)

```python
c = setxor1d(a, b)
```

**Verification:**
```python
assert_array_equal([], setxor1d([], []))
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(c, ec)
```

### Step 6: Assign a = np.array(...)

```python
a = np.array([1, 2, 3])
```

### Step 7: Assign b = np.array(...)

```python
b = np.array([6, 5, 4])
```

### Step 8: Assign ec = np.array(...)

```python
ec = np.array([1, 2, 3, 4, 5, 6])
```

### Step 9: Assign c = setxor1d(...)

```python
c = setxor1d(a, b)
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(c, ec)
```

### Step 11: Assign a = np.array(...)

```python
a = np.array([1, 8, 2, 3])
```

### Step 12: Assign b = np.array(...)

```python
b = np.array([6, 5, 4, 8])
```

### Step 13: Assign ec = np.array(...)

```python
ec = np.array([1, 2, 3, 4, 5, 6])
```

### Step 14: Assign c = setxor1d(...)

```python
c = setxor1d(a, b)
```

### Step 15: Call assert_array_equal()

```python
assert_array_equal(c, ec)
```

### Step 16: Call assert_array_equal()

```python
assert_array_equal([], setxor1d([], []))
```


## Complete Example

```python
# Workflow
a = np.array([5, 7, 1, 2])
b = np.array([2, 4, 3, 1, 5])
ec = np.array([3, 4, 7])
c = setxor1d(a, b)
assert_array_equal(c, ec)
a = np.array([1, 2, 3])
b = np.array([6, 5, 4])
ec = np.array([1, 2, 3, 4, 5, 6])
c = setxor1d(a, b)
assert_array_equal(c, ec)
a = np.array([1, 8, 2, 3])
b = np.array([6, 5, 4, 8])
ec = np.array([1, 2, 3, 4, 5, 6])
c = setxor1d(a, b)
assert_array_equal(c, ec)
assert_array_equal([], setxor1d([], []))
```

## Next Steps


---

*Source: test_arraysetops.py:89 | Complexity: Advanced | Last updated: 2026-06-02*