# How To: Weights

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weights

## Prerequisites

**Required Modules:**
- `decimal`
- `math`
- `operator`
- `sys`
- `warnings`
- `fractions`
- `functools`
- `hypothesis`
- `hypothesis.strategies`
- `pytest`
- `hypothesis.extra.numpy`
- `numpy`
- `numpy.lib._function_base_impl`
- `numpy`
- `numpy._core.numeric`
- `numpy.exceptions`
- `numpy.random`
- `numpy.testing`
- `random`
- `gc`


## Step-by-Step Guide

### Step 1: Assign y = np.arange(...)

```python
y = np.arange(10)
```

**Verification:**
```python
assert_almost_equal(actual, desired)
```

### Step 2: Assign w = np.arange(...)

```python
w = np.arange(10)
```

**Verification:**
```python
assert_almost_equal(actual, desired)
```

### Step 3: Assign actual = average(...)

```python
actual = average(y, weights=w)
```

**Verification:**
```python
assert_almost_equal(actual, desired)
```

### Step 4: Assign desired = value

```python
desired = (np.arange(10) ** 2).sum() * 1.0 / np.arange(10).sum()
```

**Verification:**
```python
assert_array_equal(average(y1, weights=w2, axis=1), desired)
```

### Step 5: Call assert_almost_equal()

```python
assert_almost_equal(actual, desired)
```

**Verification:**
```python
assert_equal(average(y1, weights=w2), 5.0)
```

### Step 6: Assign y1 = np.array(...)

```python
y1 = np.array([[1, 2, 3], [4, 5, 6]])
```

**Verification:**
```python
assert_(np.average(y3, weights=w3).dtype == np.result_type(y3, w3))
```

### Step 7: Assign w0 = value

```python
w0 = [1, 2]
```

**Verification:**
```python
assert_array_equal(actual, desired)
```

### Step 8: Assign actual = average(...)

```python
actual = average(y1, weights=w0, axis=0)
```

**Verification:**
```python
assert_array_equal(actual, desired)
```

### Step 9: Assign desired = np.array(...)

```python
desired = np.array([3.0, 4.0, 5.0])
```

### Step 10: Call assert_almost_equal()

```python
assert_almost_equal(actual, desired)
```

### Step 11: Assign w1 = value

```python
w1 = [0, 0, 1]
```

### Step 12: Assign actual = average(...)

```python
actual = average(y1, weights=w1, axis=1)
```

### Step 13: Assign desired = np.array(...)

```python
desired = np.array([3.0, 6.0])
```

### Step 14: Call assert_almost_equal()

```python
assert_almost_equal(actual, desired)
```

### Step 15: Assign w2 = value

```python
w2 = [[0, 0, 1], [0, 0, 2]]
```

### Step 16: Assign desired = np.array(...)

```python
desired = np.array([3.0, 6.0])
```

### Step 17: Call assert_array_equal()

```python
assert_array_equal(average(y1, weights=w2, axis=1), desired)
```

### Step 18: Call assert_equal()

```python
assert_equal(average(y1, weights=w2), 5.0)
```

### Step 19: Assign y3 = rand.astype(...)

```python
y3 = rand(5).astype(np.float32)
```

### Step 20: Assign w3 = rand.astype(...)

```python
w3 = rand(5).astype(np.float64)
```

### Step 21: Call assert_()

```python
assert_(np.average(y3, weights=w3).dtype == np.result_type(y3, w3))
```

### Step 22: Assign x = np.array.reshape(...)

```python
x = np.array([2, 3, 4]).reshape(3, 1)
```

### Step 23: Assign w = np.array.reshape(...)

```python
w = np.array([4, 5, 6]).reshape(3, 1)
```

### Step 24: Assign actual = np.average(...)

```python
actual = np.average(x, weights=w, axis=1, keepdims=False)
```

### Step 25: Assign desired = np.array(...)

```python
desired = np.array([2.0, 3.0, 4.0])
```

### Step 26: Call assert_array_equal()

```python
assert_array_equal(actual, desired)
```

### Step 27: Assign actual = np.average(...)

```python
actual = np.average(x, weights=w, axis=1, keepdims=True)
```

### Step 28: Assign desired = np.array(...)

```python
desired = np.array([[2.0], [3.0], [4.0]])
```

### Step 29: Call assert_array_equal()

```python
assert_array_equal(actual, desired)
```

### Step 30: Call average()

```python
average(y1, weights=w1)
```


## Complete Example

```python
# Workflow
y = np.arange(10)
w = np.arange(10)
actual = average(y, weights=w)
desired = (np.arange(10) ** 2).sum() * 1.0 / np.arange(10).sum()
assert_almost_equal(actual, desired)
y1 = np.array([[1, 2, 3], [4, 5, 6]])
w0 = [1, 2]
actual = average(y1, weights=w0, axis=0)
desired = np.array([3.0, 4.0, 5.0])
assert_almost_equal(actual, desired)
w1 = [0, 0, 1]
actual = average(y1, weights=w1, axis=1)
desired = np.array([3.0, 6.0])
assert_almost_equal(actual, desired)
with pytest.raises(TypeError, match='Axis must be specified when shapes of a and weights differ'):
    average(y1, weights=w1)
w2 = [[0, 0, 1], [0, 0, 2]]
desired = np.array([3.0, 6.0])
assert_array_equal(average(y1, weights=w2, axis=1), desired)
assert_equal(average(y1, weights=w2), 5.0)
y3 = rand(5).astype(np.float32)
w3 = rand(5).astype(np.float64)
assert_(np.average(y3, weights=w3).dtype == np.result_type(y3, w3))
x = np.array([2, 3, 4]).reshape(3, 1)
w = np.array([4, 5, 6]).reshape(3, 1)
actual = np.average(x, weights=w, axis=1, keepdims=False)
desired = np.array([2.0, 3.0, 4.0])
assert_array_equal(actual, desired)
actual = np.average(x, weights=w, axis=1, keepdims=True)
desired = np.array([[2.0], [3.0], [4.0]])
assert_array_equal(actual, desired)
```

## Next Steps


---

*Source: test_function_base.py:376 | Complexity: Advanced | Last updated: 2026-06-02*