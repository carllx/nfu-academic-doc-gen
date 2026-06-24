# How To: Isin Char Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin char array

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
a = np.array(['a', 'b', 'c', 'd', 'e', 'c', 'e', 'b'])
```

**Verification:**
```python
assert_array_equal(c, ec)
```

### Step 2: Assign b = np.array(...)

```python
b = np.array(['a', 'c'])
```

### Step 3: Assign ec = np.array(...)

```python
ec = np.array([True, False, True, False, False, True, False, False])
```

### Step 4: Assign c = isin(...)

```python
c = isin(a, b)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(c, ec)
```


## Complete Example

```python
# Workflow
a = np.array(['a', 'b', 'c', 'd', 'e', 'c', 'e', 'b'])
b = np.array(['a', 'c'])
ec = np.array([True, False, True, False, False, True, False, False])
c = isin(a, b)
assert_array_equal(c, ec)
```

## Next Steps


---

*Source: test_arraysetops.py:337 | Complexity: Intermediate | Last updated: 2026-06-02*