# How To: Inf

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test inf

## Prerequisites

**Required Modules:**
- `itertools`
- `os`
- `re`
- `sys`
- `warnings`
- `weakref`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy.testing`
- `datetime`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([[1.0, 2.0], [3.0, 4.0]])
```

**Verification:**
```python
assert_raises(AssertionError, lambda: self._assert_func(a, b))
```

### Step 2: Assign b = a.copy(...)

```python
b = a.copy()
```

**Verification:**
```python
assert_raises(AssertionError, lambda: self._assert_func(a, b))
```

### Step 3: Assign unknown = value

```python
a[0, 0] = np.inf
```

### Step 4: Call assert_raises()

```python
assert_raises(AssertionError, lambda: self._assert_func(a, b))
```

### Step 5: Assign unknown = value

```python
b[0, 0] = -np.inf
```

### Step 6: Call assert_raises()

```python
assert_raises(AssertionError, lambda: self._assert_func(a, b))
```


## Complete Example

```python
# Workflow
a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = a.copy()
a[0, 0] = np.inf
assert_raises(AssertionError, lambda: self._assert_func(a, b))
b[0, 0] = -np.inf
assert_raises(AssertionError, lambda: self._assert_func(a, b))
```

## Next Steps


---

*Source: test_utils.py:608 | Complexity: Intermediate | Last updated: 2026-06-02*