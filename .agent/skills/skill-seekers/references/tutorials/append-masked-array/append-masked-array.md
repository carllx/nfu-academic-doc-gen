# How To: Append Masked Array

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append masked array

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
assert_array_equal(result.data, expected_data)
```

### Step 2: Assign b = np.ma.masked_equal(...)

```python
b = np.ma.masked_equal([4, 3, 2], value=2)
```

**Verification:**
```python
assert_array_equal(result.mask, expected_mask)
```

### Step 3: Assign result = np.ma.append(...)

```python
result = np.ma.append(a, b)
```

**Verification:**
```python
assert_array_equal(result.data[-3], expected_data)
```

### Step 4: Assign expected_data = value

```python
expected_data = [1, 2, 3, 4, 3, 2]
```

**Verification:**
```python
assert_array_equal(result.mask, expected_mask)
```

### Step 5: Assign expected_mask = value

```python
expected_mask = [False, True, False, False, False, True]
```

**Verification:**
```python
assert_array_equal(result.data[-3], expected_data)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(result.data, expected_data)
```

**Verification:**
```python
assert_array_equal(result.mask, expected_mask)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(result.mask, expected_mask)
```

### Step 8: Assign a = np.ma.masked_all(...)

```python
a = np.ma.masked_all((2, 2))
```

### Step 9: Assign b = np.ma.ones(...)

```python
b = np.ma.ones((3, 1))
```

### Step 10: Assign result = np.ma.append(...)

```python
result = np.ma.append(a, b)
```

### Step 11: Assign expected_data = value

```python
expected_data = [1] * 3
```

### Step 12: Assign expected_mask = value

```python
expected_mask = [True] * 4 + [False] * 3
```

### Step 13: Call assert_array_equal()

```python
assert_array_equal(result.data[-3], expected_data)
```

### Step 14: Call assert_array_equal()

```python
assert_array_equal(result.mask, expected_mask)
```

### Step 15: Assign result = np.ma.append(...)

```python
result = np.ma.append(a, b, axis=None)
```

### Step 16: Call assert_array_equal()

```python
assert_array_equal(result.data[-3], expected_data)
```

### Step 17: Call assert_array_equal()

```python
assert_array_equal(result.mask, expected_mask)
```


## Complete Example

```python
# Workflow
a = np.ma.masked_equal([1, 2, 3], value=2)
b = np.ma.masked_equal([4, 3, 2], value=2)
result = np.ma.append(a, b)
expected_data = [1, 2, 3, 4, 3, 2]
expected_mask = [False, True, False, False, False, True]
assert_array_equal(result.data, expected_data)
assert_array_equal(result.mask, expected_mask)
a = np.ma.masked_all((2, 2))
b = np.ma.ones((3, 1))
result = np.ma.append(a, b)
expected_data = [1] * 3
expected_mask = [True] * 4 + [False] * 3
assert_array_equal(result.data[-3], expected_data)
assert_array_equal(result.mask, expected_mask)
result = np.ma.append(a, b, axis=None)
assert_array_equal(result.data[-3], expected_data)
assert_array_equal(result.mask, expected_mask)
```

## Next Steps


---

*Source: test_core.py:5673 | Complexity: Advanced | Last updated: 2026-06-02*