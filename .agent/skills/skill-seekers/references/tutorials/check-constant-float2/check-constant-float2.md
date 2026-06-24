# How To: Check Constant Float2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check constant float2

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.lib._arraypad_impl`
- `numpy.testing`
- `fractions`


## Step-by-Step Guide

### Step 1: Assign arr = np.arange.reshape(...)

```python
arr = np.arange(30).reshape(5, 6)
```

**Verification:**
```python
assert_allclose(test, expected)
```

### Step 2: Assign arr_float = arr.astype(...)

```python
arr_float = arr.astype(np.float64)
```

### Step 3: Assign test = np.pad(...)

```python
test = np.pad(arr_float, ((1, 2), (1, 2)), mode='constant', constant_values=1.1)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([[1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1], [1.1, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 1.1, 1.1], [1.1, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 1.1, 1.1], [1.1, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 1.1, 1.1], [1.1, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 1.1, 1.1], [1.1, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 1.1, 1.1], [1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1], [1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1]])
```

### Step 5: Call assert_allclose()

```python
assert_allclose(test, expected)
```


## Complete Example

```python
# Workflow
arr = np.arange(30).reshape(5, 6)
arr_float = arr.astype(np.float64)
test = np.pad(arr_float, ((1, 2), (1, 2)), mode='constant', constant_values=1.1)
expected = np.array([[1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1], [1.1, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 1.1, 1.1], [1.1, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 1.1, 1.1], [1.1, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 1.1, 1.1], [1.1, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 1.1, 1.1], [1.1, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 1.1, 1.1], [1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1], [1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1]])
assert_allclose(test, expected)
```

## Next Steps


---

*Source: test_arraypad.py:566 | Complexity: Intermediate | Last updated: 2026-06-02*