# How To: Weight And Input Dims Different

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weight and input dims different

## Prerequisites

**Required Modules:**
- `inspect`
- `itertools`
- `pytest`
- `numpy`
- `numpy._core.numeric`
- `numpy.ma.core`
- `numpy.ma.extras`
- `numpy.ma.testutils`


## Step-by-Step Guide

### Step 1: Assign y = np.arange.reshape(...)

```python
y = np.arange(12).reshape(2, 2, 3)
```

**Verification:**
```python
assert_almost_equal(actual, desired)
```

### Step 2: Assign w = np.array.reshape(...)

```python
w = np.array([0.0, 0.0, 1.0, 0.5, 0.5, 0.0, 0.0, 0.5, 0.5, 1.0, 0.0, 0.0]).reshape(2, 2, 3)
```

**Verification:**
```python
assert_almost_equal(actual, desired)
```

### Step 3: Assign m = np.full(...)

```python
m = np.full((2, 2, 3), False)
```

**Verification:**
```python
assert_almost_equal(actual, desired)
```

### Step 4: Assign yma = np.ma.array(...)

```python
yma = np.ma.array(y, mask=m)
```

**Verification:**
```python
assert_almost_equal(actual, desired)
```

### Step 5: Assign subw0 = value

```python
subw0 = w[:, :, 0]
```

### Step 6: Assign actual = average(...)

```python
actual = average(yma, axis=(0, 1), weights=subw0)
```

### Step 7: Assign desired = masked_array(...)

```python
desired = masked_array([7.0, 8.0, 9.0], mask=[False, False, False])
```

### Step 8: Call assert_almost_equal()

```python
assert_almost_equal(actual, desired)
```

### Step 9: Assign m = np.full(...)

```python
m = np.full((2, 2, 3), False)
```

### Step 10: Assign unknown = True

```python
m[:, :, 0] = True
```

### Step 11: Assign unknown = True

```python
m[0, 0, 1] = True
```

### Step 12: Assign yma = np.ma.array(...)

```python
yma = np.ma.array(y, mask=m)
```

### Step 13: Assign actual = average(...)

```python
actual = average(yma, axis=(0, 1), weights=subw0)
```

### Step 14: Assign desired = masked_array(...)

```python
desired = masked_array([np.nan, 8.0, 9.0], mask=[True, False, False])
```

### Step 15: Call assert_almost_equal()

```python
assert_almost_equal(actual, desired)
```

### Step 16: Assign m = np.full(...)

```python
m = np.full((2, 2, 3), False)
```

### Step 17: Assign yma = np.ma.array(...)

```python
yma = np.ma.array(y, mask=m)
```

### Step 18: Assign subw1 = value

```python
subw1 = w[1, :, :]
```

### Step 19: Assign actual = average(...)

```python
actual = average(yma, axis=(1, 2), weights=subw1)
```

### Step 20: Assign desired = masked_array(...)

```python
desired = masked_array([2.25, 8.25], mask=[False, False])
```

### Step 21: Call assert_almost_equal()

```python
assert_almost_equal(actual, desired)
```

### Step 22: Assign actual = average(...)

```python
actual = average(yma, axis=(1, 0), weights=subw0)
```

### Step 23: Assign desired = average(...)

```python
desired = average(yma, axis=(0, 1), weights=subw0.T)
```

### Step 24: Call assert_almost_equal()

```python
assert_almost_equal(actual, desired)
```

### Step 25: Call average()

```python
average(yma, axis=(0, 1, 2), weights=subw0)
```

### Step 26: Call average()

```python
average(yma, axis=(0, 1), weights=subw1)
```


## Complete Example

```python
# Workflow
y = np.arange(12).reshape(2, 2, 3)
w = np.array([0.0, 0.0, 1.0, 0.5, 0.5, 0.0, 0.0, 0.5, 0.5, 1.0, 0.0, 0.0]).reshape(2, 2, 3)
m = np.full((2, 2, 3), False)
yma = np.ma.array(y, mask=m)
subw0 = w[:, :, 0]
actual = average(yma, axis=(0, 1), weights=subw0)
desired = masked_array([7.0, 8.0, 9.0], mask=[False, False, False])
assert_almost_equal(actual, desired)
m = np.full((2, 2, 3), False)
m[:, :, 0] = True
m[0, 0, 1] = True
yma = np.ma.array(y, mask=m)
actual = average(yma, axis=(0, 1), weights=subw0)
desired = masked_array([np.nan, 8.0, 9.0], mask=[True, False, False])
assert_almost_equal(actual, desired)
m = np.full((2, 2, 3), False)
yma = np.ma.array(y, mask=m)
subw1 = w[1, :, :]
actual = average(yma, axis=(1, 2), weights=subw1)
desired = masked_array([2.25, 8.25], mask=[False, False])
assert_almost_equal(actual, desired)
with pytest.raises(ValueError, match='Shape of weights must be consistent with shape of a along specified axis'):
    average(yma, axis=(0, 1, 2), weights=subw0)
with pytest.raises(ValueError, match='Shape of weights must be consistent with shape of a along specified axis'):
    average(yma, axis=(0, 1), weights=subw1)
actual = average(yma, axis=(1, 0), weights=subw0)
desired = average(yma, axis=(0, 1), weights=subw0.T)
assert_almost_equal(actual, desired)
```

## Next Steps


---

*Source: test_extras.py:291 | Complexity: Advanced | Last updated: 2026-06-02*