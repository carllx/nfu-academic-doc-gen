# How To: Returned

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test returned

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

### Step 1: Assign y = np.array(...)

```python
y = np.array([[1, 2, 3], [4, 5, 6]])
```

**Verification:**
```python
assert_equal(scl, 6.0)
```

### Step 2: Assign unknown = average(...)

```python
avg, scl = average(y, returned=True)
```

**Verification:**
```python
assert_array_equal(scl, np.array([2.0, 2.0, 2.0]))
```

### Step 3: Call assert_equal()

```python
assert_equal(scl, 6.0)
```

**Verification:**
```python
assert_array_equal(scl, np.array([3.0, 3.0]))
```

### Step 4: Assign unknown = average(...)

```python
avg, scl = average(y, 0, returned=True)
```

**Verification:**
```python
assert_array_equal(scl, np.array([3.0, 3.0, 3.0]))
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(scl, np.array([2.0, 2.0, 2.0]))
```

**Verification:**
```python
assert_array_equal(scl, np.array([6.0, 6.0]))
```

### Step 6: Assign unknown = average(...)

```python
avg, scl = average(y, 1, returned=True)
```

**Verification:**
```python
assert_array_equal(scl, np.array([1.0, 6.0]))
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(scl, np.array([3.0, 3.0]))
```

### Step 8: Assign w0 = value

```python
w0 = [1, 2]
```

### Step 9: Assign unknown = average(...)

```python
avg, scl = average(y, weights=w0, axis=0, returned=True)
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(scl, np.array([3.0, 3.0, 3.0]))
```

### Step 11: Assign w1 = value

```python
w1 = [1, 2, 3]
```

### Step 12: Assign unknown = average(...)

```python
avg, scl = average(y, weights=w1, axis=1, returned=True)
```

### Step 13: Call assert_array_equal()

```python
assert_array_equal(scl, np.array([6.0, 6.0]))
```

### Step 14: Assign w2 = value

```python
w2 = [[0, 0, 1], [1, 2, 3]]
```

### Step 15: Assign unknown = average(...)

```python
avg, scl = average(y, weights=w2, axis=1, returned=True)
```

### Step 16: Call assert_array_equal()

```python
assert_array_equal(scl, np.array([1.0, 6.0]))
```


## Complete Example

```python
# Workflow
y = np.array([[1, 2, 3], [4, 5, 6]])
avg, scl = average(y, returned=True)
assert_equal(scl, 6.0)
avg, scl = average(y, 0, returned=True)
assert_array_equal(scl, np.array([2.0, 2.0, 2.0]))
avg, scl = average(y, 1, returned=True)
assert_array_equal(scl, np.array([3.0, 3.0]))
w0 = [1, 2]
avg, scl = average(y, weights=w0, axis=0, returned=True)
assert_array_equal(scl, np.array([3.0, 3.0, 3.0]))
w1 = [1, 2, 3]
avg, scl = average(y, weights=w1, axis=1, returned=True)
assert_array_equal(scl, np.array([6.0, 6.0]))
w2 = [[0, 0, 1], [1, 2, 3]]
avg, scl = average(y, weights=w2, axis=1, returned=True)
assert_array_equal(scl, np.array([1.0, 6.0]))
```

## Next Steps


---

*Source: test_function_base.py:466 | Complexity: Advanced | Last updated: 2026-06-02*