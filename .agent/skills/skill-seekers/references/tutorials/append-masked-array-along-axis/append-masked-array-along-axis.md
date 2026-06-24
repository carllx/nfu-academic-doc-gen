# How To: Append Masked Array Along Axis

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append masked array along axis

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

### Step 1: Assign a = np.ma.masked_equal(...)

```python
a = np.ma.masked_equal([1, 2, 3], value=2)
```

**Verification:**
```python
assert_raises(ValueError, np.ma.append, a, b, axis=0)
```

### Step 2: Assign b = np.ma.masked_values(...)

```python
b = np.ma.masked_values([[4, 5, 6], [7, 8, 9]], 7)
```

**Verification:**
```python
assert_array_equal(result.data, expected.data)
```

### Step 3: Call assert_raises()

```python
assert_raises(ValueError, np.ma.append, a, b, axis=0)
```

**Verification:**
```python
assert_array_equal(result.mask, expected.mask)
```

### Step 4: Assign result = np.ma.append(...)

```python
result = np.ma.append(a[np.newaxis, :], b, axis=0)
```

### Step 5: Assign expected = np.ma.arange(...)

```python
expected = np.ma.arange(1, 10)
```

### Step 6: Assign unknown = value

```python
expected[[1, 6]] = np.ma.masked
```

### Step 7: Assign expected = expected.reshape(...)

```python
expected = expected.reshape((3, 3))
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(result.data, expected.data)
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(result.mask, expected.mask)
```


## Complete Example

```python
# Workflow
a = np.ma.masked_equal([1, 2, 3], value=2)
b = np.ma.masked_values([[4, 5, 6], [7, 8, 9]], 7)
assert_raises(ValueError, np.ma.append, a, b, axis=0)
result = np.ma.append(a[np.newaxis, :], b, axis=0)
expected = np.ma.arange(1, 10)
expected[[1, 6]] = np.ma.masked
expected = expected.reshape((3, 3))
assert_array_equal(result.data, expected.data)
assert_array_equal(result.mask, expected.mask)
```

## Next Steps


---

*Source: test_core.py:5697 | Complexity: Advanced | Last updated: 2026-06-02*