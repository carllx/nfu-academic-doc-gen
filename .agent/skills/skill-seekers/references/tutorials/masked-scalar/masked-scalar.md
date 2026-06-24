# How To: Masked Scalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test masked scalar

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
a = np.ma.MaskedArray(a_val, mask=True)
```

### Step 2: Assign b = value

```python
b = np.ma.MaskedArray(b_val, mask=True) if b_masked else np.array(b_val)
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
a = np.ma.MaskedArray(a_val, mask=True)
```

### Step 6: Assign b = np.array(...)

```python
b = np.array(b_val)
```

### Step 7: Call self._test_equal()

```python
self._test_equal(a, b)
```

### Step 8: Call self._test_equal()

```python
self._test_equal(b, a)
```

### Step 9: Assign a = np.ma.MaskedArray(...)

```python
a = np.ma.MaskedArray(a_val, mask=True)
```

### Step 10: Assign b = np.ma.MaskedArray(...)

```python
b = np.ma.MaskedArray(b_val, mask=b_mask)
```

### Step 11: Call self._test_equal()

```python
self._test_equal(a, b)
```

### Step 12: Call self._test_equal()

```python
self._test_equal(b, a)
```


## Complete Example

```python
# Workflow
for a_val, b_val, b_masked in itertools.product([3.0, np.nan, np.inf], [3.0, 4.0, np.nan, np.inf, -np.inf], [False, True]):
    a = np.ma.MaskedArray(a_val, mask=True)
    b = np.ma.MaskedArray(b_val, mask=True) if b_masked else np.array(b_val)
    self._test_equal(a, b)
    self._test_equal(b, a)
for a_val, b_val in itertools.product([3.0, np.nan, -np.inf], itertools.product([3.0, 4.0, np.nan, np.inf, -np.inf], repeat=2)):
    a = np.ma.MaskedArray(a_val, mask=True)
    b = np.array(b_val)
    self._test_equal(a, b)
    self._test_equal(b, a)
for a_val, b_val, b_mask in itertools.product([3.0, np.nan, np.inf], itertools.product([3.0, 4.0, np.nan, np.inf, -np.inf], repeat=2), itertools.product([False, True], repeat=2)):
    a = np.ma.MaskedArray(a_val, mask=True)
    b = np.ma.MaskedArray(b_val, mask=b_mask)
    self._test_equal(a, b)
    self._test_equal(b, a)
```

## Next Steps


---

*Source: test_utils.py:204 | Complexity: Advanced | Last updated: 2026-06-02*