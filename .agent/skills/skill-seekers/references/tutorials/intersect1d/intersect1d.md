# How To: Intersect1D

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersect1d

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
assert_array_equal(c, ed)
```

### Step 3: Assign ec = np.array(...)

```python
ec = np.array([1, 2, 5])
```

**Verification:**
```python
assert_array_equal([], intersect1d([], []))
```

### Step 4: Assign c = intersect1d(...)

```python
c = intersect1d(a, b, assume_unique=True)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(c, ec)
```

### Step 6: Assign a = np.array(...)

```python
a = np.array([5, 5, 7, 1, 2])
```

### Step 7: Assign b = np.array(...)

```python
b = np.array([2, 1, 4, 3, 3, 1, 5])
```

### Step 8: Assign ed = np.array(...)

```python
ed = np.array([1, 2, 5])
```

### Step 9: Assign c = intersect1d(...)

```python
c = intersect1d(a, b)
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(c, ed)
```

### Step 11: Call assert_array_equal()

```python
assert_array_equal([], intersect1d([], []))
```


## Complete Example

```python
# Workflow
a = np.array([5, 7, 1, 2])
b = np.array([2, 4, 3, 1, 5])
ec = np.array([1, 2, 5])
c = intersect1d(a, b, assume_unique=True)
assert_array_equal(c, ec)
a = np.array([5, 5, 7, 1, 2])
b = np.array([2, 1, 4, 3, 3, 1, 5])
ed = np.array([1, 2, 5])
c = intersect1d(a, b)
assert_array_equal(c, ed)
assert_array_equal([], intersect1d([], []))
```

## Next Steps


---

*Source: test_arraysetops.py:20 | Complexity: Advanced | Last updated: 2026-06-02*