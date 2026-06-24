# How To: Isin Hit Alternate Algorithm

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Hit the standard isin code with integers

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.dtypes`
- `numpy.exceptions`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: 'Hit the standard isin code with integers'

```python
'Hit the standard isin code with integers'
```

**Verification:**
```python
assert_array_equal(expected, isin(a, b))
```

### Step 2: Assign a = np.array(...)

```python
a = np.array([5, 4, 5, 3, 4, 4, 1000000000.0], dtype=np.int64)
```

**Verification:**
```python
assert_array_equal(np.invert(expected), isin(a, b, invert=True))
```

### Step 3: Assign b = np.array(...)

```python
b = np.array([2, 3, 4, 1000000000.0], dtype=np.int64)
```

**Verification:**
```python
assert_array_equal(c, ec)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([0, 1, 0, 1, 1, 1, 1], dtype=bool)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(expected, isin(a, b))
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(np.invert(expected), isin(a, b, invert=True))
```

### Step 7: Assign a = np.array(...)

```python
a = np.array([5, 7, 1, 2], dtype=np.int64)
```

### Step 8: Assign b = np.array(...)

```python
b = np.array([2, 4, 3, 1, 5, 1000000000.0], dtype=np.int64)
```

### Step 9: Assign ec = np.array(...)

```python
ec = np.array([True, False, True, True])
```

### Step 10: Assign c = isin(...)

```python
c = isin(a, b, assume_unique=True)
```

### Step 11: Call assert_array_equal()

```python
assert_array_equal(c, ec)
```


## Complete Example

```python
# Workflow
'Hit the standard isin code with integers'
a = np.array([5, 4, 5, 3, 4, 4, 1000000000.0], dtype=np.int64)
b = np.array([2, 3, 4, 1000000000.0], dtype=np.int64)
expected = np.array([0, 1, 0, 1, 1, 1, 1], dtype=bool)
assert_array_equal(expected, isin(a, b))
assert_array_equal(np.invert(expected), isin(a, b, invert=True))
a = np.array([5, 7, 1, 2], dtype=np.int64)
b = np.array([2, 4, 3, 1, 5, 1000000000.0], dtype=np.int64)
ec = np.array([True, False, True, True])
c = isin(a, b, assume_unique=True)
assert_array_equal(c, ec)
```

## Next Steps


---

*Source: test_arraysetops.py:367 | Complexity: Advanced | Last updated: 2026-06-02*