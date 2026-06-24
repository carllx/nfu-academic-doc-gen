# How To: Flat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test flat

## Prerequisites

**Required Modules:**
- `pickle`
- `numpy`
- `numpy.ma.core`
- `numpy.ma.extras`
- `numpy.ma.testutils`


## Step-by-Step Guide

### Step 1: Assign test = masked_array(...)

```python
test = masked_array(np.matrix([[1, 2, 3]]), mask=[0, 0, 1])
```

**Verification:**
```python
assert_equal(test.flat[1], 2)
```

### Step 2: Call assert_equal()

```python
assert_equal(test.flat[1], 2)
```

**Verification:**
```python
assert_equal(test.flat[2], masked)
```

### Step 3: Call assert_equal()

```python
assert_equal(test.flat[2], masked)
```

**Verification:**
```python
assert_(np.all(test.flat[0:2] == test[0, 0:2]))
```

### Step 4: Call assert_()

```python
assert_(np.all(test.flat[0:2] == test[0, 0:2]))
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 5: Assign test = masked_array(...)

```python
test = masked_array(np.matrix([[1, 2, 3]]), mask=[0, 0, 1])
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 6: Assign test.flat = masked_array(...)

```python
test.flat = masked_array([3, 2, 1], mask=[1, 0, 0])
```

**Verification:**
```python
assert_equal(b01.data, np.array([[1.0, 0.0]]))
```

### Step 7: Assign control = masked_array(...)

```python
control = masked_array(np.matrix([[3, 2, 1]]), mask=[1, 0, 0])
```

**Verification:**
```python
assert_equal(b01.mask, np.array([[False, False]]))
```

### Step 8: Call assert_equal()

```python
assert_equal(test, control)
```

### Step 9: Assign test = masked_array(...)

```python
test = masked_array(np.matrix([[1, 2, 3]]), mask=[0, 0, 1])
```

### Step 10: Assign testflat = value

```python
testflat = test.flat
```

### Step 11: Assign unknown = value

```python
testflat[:] = testflat[np.array([2, 1, 0])]
```

### Step 12: Call assert_equal()

```python
assert_equal(test, control)
```

### Step 13: Assign unknown = 9

```python
testflat[0] = 9
```

### Step 14: Assign a = masked_array(...)

```python
a = masked_array(np.matrix(np.eye(2)), mask=0)
```

### Step 15: Assign b = value

```python
b = a.flat
```

### Step 16: Assign b01 = value

```python
b01 = b[:2]
```

### Step 17: Call assert_equal()

```python
assert_equal(b01.data, np.array([[1.0, 0.0]]))
```

### Step 18: Call assert_equal()

```python
assert_equal(b01.mask, np.array([[False, False]]))
```


## Complete Example

```python
# Workflow
test = masked_array(np.matrix([[1, 2, 3]]), mask=[0, 0, 1])
assert_equal(test.flat[1], 2)
assert_equal(test.flat[2], masked)
assert_(np.all(test.flat[0:2] == test[0, 0:2]))
test = masked_array(np.matrix([[1, 2, 3]]), mask=[0, 0, 1])
test.flat = masked_array([3, 2, 1], mask=[1, 0, 0])
control = masked_array(np.matrix([[3, 2, 1]]), mask=[1, 0, 0])
assert_equal(test, control)
test = masked_array(np.matrix([[1, 2, 3]]), mask=[0, 0, 1])
testflat = test.flat
testflat[:] = testflat[np.array([2, 1, 0])]
assert_equal(test, control)
testflat[0] = 9
a = masked_array(np.matrix(np.eye(2)), mask=0)
b = a.flat
b01 = b[:2]
assert_equal(b01.data, np.array([[1.0, 0.0]]))
assert_equal(b01.mask, np.array([[False, False]]))
```

## Next Steps


---

*Source: test_masked_matrix.py:104 | Complexity: Advanced | Last updated: 2026-06-02*