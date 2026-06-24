# How To: Legacy Vector Functionality

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test legacy vector functionality

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.lib._arraypad_impl`
- `numpy.testing`
- `fractions`


## Step-by-Step Guide

### Step 1: Assign a = np.arange.reshape(...)

```python
a = np.arange(6).reshape(2, 3)
```

**Verification:**
```python
assert_array_equal(a, b)
```

### Step 2: Assign a = np.pad(...)

```python
a = np.pad(a, 2, _padwithtens)
```

### Step 3: Assign b = np.array(...)

```python
b = np.array([[10, 10, 10, 10, 10, 10, 10], [10, 10, 10, 10, 10, 10, 10], [10, 10, 0, 1, 2, 10, 10], [10, 10, 3, 4, 5, 10, 10], [10, 10, 10, 10, 10, 10, 10], [10, 10, 10, 10, 10, 10, 10]])
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(a, b)
```

### Step 5: Assign unknown = 10

```python
vector[:pad_width[0]] = 10
```

### Step 6: Assign unknown = 10

```python
vector[-pad_width[1]:] = 10
```


## Complete Example

```python
# Workflow
def _padwithtens(vector, pad_width, iaxis, kwargs):
    vector[:pad_width[0]] = 10
    vector[-pad_width[1]:] = 10
a = np.arange(6).reshape(2, 3)
a = np.pad(a, 2, _padwithtens)
b = np.array([[10, 10, 10, 10, 10, 10, 10], [10, 10, 10, 10, 10, 10, 10], [10, 10, 0, 1, 2, 10, 10], [10, 10, 3, 4, 5, 10, 10], [10, 10, 10, 10, 10, 10, 10], [10, 10, 10, 10, 10, 10, 10]])
assert_array_equal(a, b)
```

## Next Steps


---

*Source: test_arraypad.py:1248 | Complexity: Intermediate | Last updated: 2026-06-02*