# How To: Setxor1D Unique

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setxor1d unique

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
a = np.array([1, 8, 2, 3])
```

**Verification:**
```python
assert_array_equal(c, ec)
```

### Step 2: Assign b = np.array(...)

```python
b = np.array([6, 5, 4, 8])
```

**Verification:**
```python
assert_array_equal(c, ec)
```

### Step 3: Assign ec = np.array(...)

```python
ec = np.array([1, 2, 3, 4, 5, 6])
```

### Step 4: Assign c = setxor1d(...)

```python
c = setxor1d(a, b, assume_unique=True)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(c, ec)
```

### Step 6: Assign a = np.array(...)

```python
a = np.array([[1], [8], [2], [3]])
```

### Step 7: Assign b = np.array(...)

```python
b = np.array([[6, 5], [4, 8]])
```

### Step 8: Assign ec = np.array(...)

```python
ec = np.array([1, 2, 3, 4, 5, 6])
```

### Step 9: Assign c = setxor1d(...)

```python
c = setxor1d(a, b, assume_unique=True)
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(c, ec)
```


## Complete Example

```python
# Workflow
a = np.array([1, 8, 2, 3])
b = np.array([6, 5, 4, 8])
ec = np.array([1, 2, 3, 4, 5, 6])
c = setxor1d(a, b, assume_unique=True)
assert_array_equal(c, ec)
a = np.array([[1], [8], [2], [3]])
b = np.array([[6, 5], [4, 8]])
ec = np.array([1, 2, 3, 4, 5, 6])
c = setxor1d(a, b, assume_unique=True)
assert_array_equal(c, ec)
```

## Next Steps


---

*Source: test_arraysetops.py:113 | Complexity: Advanced | Last updated: 2026-06-02*