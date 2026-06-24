# How To: Masked Nan Inf

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test masked nan inf

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

### Step 1: Assign a = np.ma.MaskedArray(...)

```python
a = np.ma.MaskedArray([3.0, 4.0, 6.5], mask=[False, True, False])
```

### Step 2: Assign b = np.array(...)

```python
b = np.array([3.0, np.nan, 6.5])
```

### Step 3: Call self._test_equal()

```python
self._test_equal(a, b)
```

### Step 4: Call self._test_equal()

```python
self._test_equal(b, a)
```

### Step 5: Assign a = np.ma.MaskedArray(...)

```python
a = np.ma.MaskedArray([3.0, 4.0, 6.5], mask=[True, False, False])
```

### Step 6: Assign b = np.array(...)

```python
b = np.array([np.inf, 4.0, 6.5])
```

### Step 7: Call self._test_equal()

```python
self._test_equal(a, b)
```

### Step 8: Call self._test_equal()

```python
self._test_equal(b, a)
```


## Complete Example

```python
# Workflow
a = np.ma.MaskedArray([3.0, 4.0, 6.5], mask=[False, True, False])
b = np.array([3.0, np.nan, 6.5])
self._test_equal(a, b)
self._test_equal(b, a)
a = np.ma.MaskedArray([3.0, 4.0, 6.5], mask=[True, False, False])
b = np.array([np.inf, 4.0, 6.5])
self._test_equal(a, b)
self._test_equal(b, a)
```

## Next Steps


---

*Source: test_utils.py:192 | Complexity: Advanced | Last updated: 2026-06-02*