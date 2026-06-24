# How To: Check Simple

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check simple

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.lib._arraypad_impl`
- `numpy.testing`
- `fractions`


## Step-by-Step Guide

### Step 1: Assign a = np.arange(...)

```python
a = np.arange(12)
```

**Verification:**
```python
assert_array_equal(a, b)
```

### Step 2: Assign a = np.reshape(...)

```python
a = np.reshape(a, (4, 3))
```

### Step 3: Assign a = np.pad(...)

```python
a = np.pad(a, ((2, 3), (3, 2)), 'edge')
```

### Step 4: Assign b = np.array(...)

```python
b = np.array([[0, 0, 0, 0, 1, 2, 2, 2], [0, 0, 0, 0, 1, 2, 2, 2], [0, 0, 0, 0, 1, 2, 2, 2], [3, 3, 3, 3, 4, 5, 5, 5], [6, 6, 6, 6, 7, 8, 8, 8], [9, 9, 9, 9, 10, 11, 11, 11], [9, 9, 9, 9, 10, 11, 11, 11], [9, 9, 9, 9, 10, 11, 11, 11], [9, 9, 9, 9, 10, 11, 11, 11]])
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(a, b)
```


## Complete Example

```python
# Workflow
a = np.arange(12)
a = np.reshape(a, (4, 3))
a = np.pad(a, ((2, 3), (3, 2)), 'edge')
b = np.array([[0, 0, 0, 0, 1, 2, 2, 2], [0, 0, 0, 0, 1, 2, 2, 2], [0, 0, 0, 0, 1, 2, 2, 2], [3, 3, 3, 3, 4, 5, 5, 5], [6, 6, 6, 6, 7, 8, 8, 8], [9, 9, 9, 9, 10, 11, 11, 11], [9, 9, 9, 9, 10, 11, 11, 11], [9, 9, 9, 9, 10, 11, 11, 11], [9, 9, 9, 9, 10, 11, 11, 11]])
assert_array_equal(a, b)
```

## Next Steps


---

*Source: test_arraypad.py:1197 | Complexity: Intermediate | Last updated: 2026-06-02*