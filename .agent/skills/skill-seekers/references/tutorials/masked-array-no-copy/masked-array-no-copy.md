# How To: Masked Array No Copy

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test masked array no copy

## Prerequisites

**Required Modules:**
- `copy`
- `inspect`
- `itertools`
- `operator`
- `pickle`
- `sys`
- `textwrap`
- `warnings`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.fromnumeric`
- `numpy._core.umath`
- `numpy.ma.core`
- `numpy`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.ma.core`
- `numpy.ma.testutils`
- `numpy.testing`
- `numpy.testing._private.utils`
- `datetime`
- `copy`
- `io`
- `copy`
- `copy`


## Step-by-Step Guide

### Step 1: Assign a = np.ma.array(...)

```python
a = np.ma.array([1, 2, 3, 4])
```

**Verification:**
```python
assert_array_equal(a.mask, [False, False, True, False])
```

### Step 2: Assign _ = np.ma.masked_where(...)

```python
_ = np.ma.masked_where(a == 3, a, copy=False)
```

**Verification:**
```python
assert_array_equal(a.mask, [True, False, True, False])
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(a.mask, [False, False, True, False])
```

**Verification:**
```python
assert_array_equal(a.mask, [True, False, False, False, False])
```

### Step 4: Assign a = np.ma.array(...)

```python
a = np.ma.array([1, 2, 3, 4], mask=[1, 0, 0, 0])
```

### Step 5: Assign _ = np.ma.masked_where(...)

```python
_ = np.ma.masked_where(a == 3, a, copy=False)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(a.mask, [True, False, True, False])
```

### Step 7: Assign a = np.ma.array(...)

```python
a = np.ma.array([np.inf, 1, 2, 3, 4])
```

### Step 8: Assign _ = np.ma.masked_invalid(...)

```python
_ = np.ma.masked_invalid(a, copy=False)
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(a.mask, [True, False, False, False, False])
```


## Complete Example

```python
# Workflow
a = np.ma.array([1, 2, 3, 4])
_ = np.ma.masked_where(a == 3, a, copy=False)
assert_array_equal(a.mask, [False, False, True, False])
a = np.ma.array([1, 2, 3, 4], mask=[1, 0, 0, 0])
_ = np.ma.masked_where(a == 3, a, copy=False)
assert_array_equal(a.mask, [True, False, True, False])
a = np.ma.array([np.inf, 1, 2, 3, 4])
_ = np.ma.masked_invalid(a, copy=False)
assert_array_equal(a.mask, [True, False, False, False, False])
```

## Next Steps


---

*Source: test_core.py:5658 | Complexity: Advanced | Last updated: 2026-06-02*