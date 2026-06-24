# How To: Simple Stat Length

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simple stat length

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
a = np.arange(30)
```

**Verification:**
```python
assert_array_equal(a, b)
```

### Step 2: Assign a = np.reshape(...)

```python
a = np.reshape(a, (6, 5))
```

### Step 3: Assign a = np.pad(...)

```python
a = np.pad(a, ((2, 3), (3, 2)), mode='mean', stat_length=(3,))
```

### Step 4: Assign b = np.array(...)

```python
b = np.array([[6, 6, 6, 5, 6, 7, 8, 9, 8, 8], [6, 6, 6, 5, 6, 7, 8, 9, 8, 8], [1, 1, 1, 0, 1, 2, 3, 4, 3, 3], [6, 6, 6, 5, 6, 7, 8, 9, 8, 8], [11, 11, 11, 10, 11, 12, 13, 14, 13, 13], [16, 16, 16, 15, 16, 17, 18, 19, 18, 18], [21, 21, 21, 20, 21, 22, 23, 24, 23, 23], [26, 26, 26, 25, 26, 27, 28, 29, 28, 28], [21, 21, 21, 20, 21, 22, 23, 24, 23, 23], [21, 21, 21, 20, 21, 22, 23, 24, 23, 23], [21, 21, 21, 20, 21, 22, 23, 24, 23, 23]])
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(a, b)
```


## Complete Example

```python
# Workflow
a = np.arange(30)
a = np.reshape(a, (6, 5))
a = np.pad(a, ((2, 3), (3, 2)), mode='mean', stat_length=(3,))
b = np.array([[6, 6, 6, 5, 6, 7, 8, 9, 8, 8], [6, 6, 6, 5, 6, 7, 8, 9, 8, 8], [1, 1, 1, 0, 1, 2, 3, 4, 3, 3], [6, 6, 6, 5, 6, 7, 8, 9, 8, 8], [11, 11, 11, 10, 11, 12, 13, 14, 13, 13], [16, 16, 16, 15, 16, 17, 18, 19, 18, 18], [21, 21, 21, 20, 21, 22, 23, 24, 23, 23], [26, 26, 26, 25, 26, 27, 28, 29, 28, 28], [21, 21, 21, 20, 21, 22, 23, 24, 23, 23], [21, 21, 21, 20, 21, 22, 23, 24, 23, 23], [21, 21, 21, 20, 21, 22, 23, 24, 23, 23]])
assert_array_equal(a, b)
```

## Next Steps


---

*Source: test_arraypad.py:453 | Complexity: Intermediate | Last updated: 2026-06-02*