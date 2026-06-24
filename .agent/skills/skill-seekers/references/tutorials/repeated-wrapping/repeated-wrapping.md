# How To: Repeated Wrapping

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Check wrapping on each side individually if the wrapped area is longer
than the original array.

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.lib._arraypad_impl`
- `numpy.testing`
- `fractions`


## Step-by-Step Guide

### Step 1: '\n        Check wrapping on each side individually if the wrapped area is longer\n        than the original array.\n        '

```python
'\n        Check wrapping on each side individually if the wrapped area is longer\n        than the original array.\n        '
```

**Verification:**
```python
assert_array_equal(np.r_[a, a, a, a][3:], b)
```

### Step 2: Assign a = np.arange(...)

```python
a = np.arange(5)
```

**Verification:**
```python
assert_array_equal(np.r_[a, a, a, a][:-3], b)
```

### Step 3: Assign b = np.pad(...)

```python
b = np.pad(a, (12, 0), mode='wrap')
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(np.r_[a, a, a, a][3:], b)
```

### Step 5: Assign a = np.arange(...)

```python
a = np.arange(5)
```

### Step 6: Assign b = np.pad(...)

```python
b = np.pad(a, (0, 12), mode='wrap')
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(np.r_[a, a, a, a][:-3], b)
```


## Complete Example

```python
# Workflow
'\n        Check wrapping on each side individually if the wrapped area is longer\n        than the original array.\n        '
a = np.arange(5)
b = np.pad(a, (12, 0), mode='wrap')
assert_array_equal(np.r_[a, a, a, a][3:], b)
a = np.arange(5)
b = np.pad(a, (0, 12), mode='wrap')
assert_array_equal(np.r_[a, a, a, a][:-3], b)
```

## Next Steps


---

*Source: test_arraypad.py:1165 | Complexity: Intermediate | Last updated: 2026-06-02*