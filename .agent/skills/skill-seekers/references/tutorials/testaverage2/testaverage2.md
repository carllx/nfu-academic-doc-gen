# How To: Testaverage2

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test testAverage2

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

### Step 1: Assign w1 = value

```python
w1 = [0, 1, 1, 1, 1, 0]
```

**Verification:**
```python
assert_equal(average(x, axis=0), 2.5)
```

### Step 2: Assign w2 = value

```python
w2 = [[0, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1]]
```

**Verification:**
```python
assert_equal(average(x, axis=0, weights=w1), 2.5)
```

### Step 3: Assign x = arange(...)

```python
x = arange(6, dtype=np.float64)
```

**Verification:**
```python
assert_equal(average(y, None), np.add.reduce(np.arange(6)) * 3.0 / 12.0)
```

### Step 4: Call assert_equal()

```python
assert_equal(average(x, axis=0), 2.5)
```

**Verification:**
```python
assert_equal(average(y, axis=0), np.arange(6) * 3.0 / 2.0)
```

### Step 5: Call assert_equal()

```python
assert_equal(average(x, axis=0, weights=w1), 2.5)
```

**Verification:**
```python
assert_equal(average(y, axis=1), [average(x, axis=0), average(x, axis=0) * 2.0])
```

### Step 6: Assign y = array(...)

```python
y = array([arange(6, dtype=np.float64), 2.0 * arange(6)])
```

**Verification:**
```python
assert_equal(average(y, None, weights=w2), 20.0 / 6.0)
```

### Step 7: Call assert_equal()

```python
assert_equal(average(y, None), np.add.reduce(np.arange(6)) * 3.0 / 12.0)
```

**Verification:**
```python
assert_equal(average(y, axis=0, weights=w2), [0.0, 1.0, 2.0, 3.0, 4.0, 10.0])
```

### Step 8: Call assert_equal()

```python
assert_equal(average(y, axis=0), np.arange(6) * 3.0 / 2.0)
```

**Verification:**
```python
assert_equal(average(y, axis=1), [average(x, axis=0), average(x, axis=0) * 2.0])
```

### Step 9: Call assert_equal()

```python
assert_equal(average(y, axis=1), [average(x, axis=0), average(x, axis=0) * 2.0])
```

**Verification:**
```python
assert_equal(average(masked_array(x, m1), axis=0), 2.5)
```

### Step 10: Call assert_equal()

```python
assert_equal(average(y, None, weights=w2), 20.0 / 6.0)
```

**Verification:**
```python
assert_equal(average(masked_array(x, m2), axis=0), 2.5)
```

### Step 11: Call assert_equal()

```python
assert_equal(average(y, axis=0, weights=w2), [0.0, 1.0, 2.0, 3.0, 4.0, 10.0])
```

**Verification:**
```python
assert_equal(average(masked_array(x, m4), axis=0).mask, [True])
```

### Step 12: Call assert_equal()

```python
assert_equal(average(y, axis=1), [average(x, axis=0), average(x, axis=0) * 2.0])
```

**Verification:**
```python
assert_equal(average(masked_array(x, m5), axis=0), 0.0)
```

### Step 13: Assign m1 = zeros(...)

```python
m1 = zeros(6)
```

**Verification:**
```python
assert_equal(count(average(masked_array(x, m4), axis=0)), 0)
```

### Step 14: Assign m2 = value

```python
m2 = [0, 0, 1, 1, 0, 0]
```

**Verification:**
```python
assert_equal(average(z, None), 20.0 / 6.0)
```

### Step 15: Assign m3 = value

```python
m3 = [[0, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0]]
```

**Verification:**
```python
assert_equal(average(z, axis=0), [0.0, 1.0, 99.0, 99.0, 4.0, 7.5])
```

### Step 16: Assign m4 = ones(...)

```python
m4 = ones(6)
```

**Verification:**
```python
assert_equal(average(z, axis=1), [2.5, 5.0])
```

### Step 17: Assign m5 = value

```python
m5 = [0, 1, 1, 1, 1, 1]
```

**Verification:**
```python
assert_equal(average(z, axis=0, weights=w2), [0.0, 1.0, 99.0, 99.0, 4.0, 10.0])
```

### Step 18: Call assert_equal()

```python
assert_equal(average(masked_array(x, m1), axis=0), 2.5)
```

### Step 19: Call assert_equal()

```python
assert_equal(average(masked_array(x, m2), axis=0), 2.5)
```

### Step 20: Call assert_equal()

```python
assert_equal(average(masked_array(x, m4), axis=0).mask, [True])
```

### Step 21: Call assert_equal()

```python
assert_equal(average(masked_array(x, m5), axis=0), 0.0)
```

### Step 22: Call assert_equal()

```python
assert_equal(count(average(masked_array(x, m4), axis=0)), 0)
```

### Step 23: Assign z = masked_array(...)

```python
z = masked_array(y, m3)
```

### Step 24: Call assert_equal()

```python
assert_equal(average(z, None), 20.0 / 6.0)
```

### Step 25: Call assert_equal()

```python
assert_equal(average(z, axis=0), [0.0, 1.0, 99.0, 99.0, 4.0, 7.5])
```

### Step 26: Call assert_equal()

```python
assert_equal(average(z, axis=1), [2.5, 5.0])
```

### Step 27: Call assert_equal()

```python
assert_equal(average(z, axis=0, weights=w2), [0.0, 1.0, 99.0, 99.0, 4.0, 10.0])
```


## Complete Example

```python
# Workflow
w1 = [0, 1, 1, 1, 1, 0]
w2 = [[0, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1]]
x = arange(6, dtype=np.float64)
assert_equal(average(x, axis=0), 2.5)
assert_equal(average(x, axis=0, weights=w1), 2.5)
y = array([arange(6, dtype=np.float64), 2.0 * arange(6)])
assert_equal(average(y, None), np.add.reduce(np.arange(6)) * 3.0 / 12.0)
assert_equal(average(y, axis=0), np.arange(6) * 3.0 / 2.0)
assert_equal(average(y, axis=1), [average(x, axis=0), average(x, axis=0) * 2.0])
assert_equal(average(y, None, weights=w2), 20.0 / 6.0)
assert_equal(average(y, axis=0, weights=w2), [0.0, 1.0, 2.0, 3.0, 4.0, 10.0])
assert_equal(average(y, axis=1), [average(x, axis=0), average(x, axis=0) * 2.0])
m1 = zeros(6)
m2 = [0, 0, 1, 1, 0, 0]
m3 = [[0, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0]]
m4 = ones(6)
m5 = [0, 1, 1, 1, 1, 1]
assert_equal(average(masked_array(x, m1), axis=0), 2.5)
assert_equal(average(masked_array(x, m2), axis=0), 2.5)
assert_equal(average(masked_array(x, m4), axis=0).mask, [True])
assert_equal(average(masked_array(x, m5), axis=0), 0.0)
assert_equal(count(average(masked_array(x, m4), axis=0)), 0)
z = masked_array(y, m3)
assert_equal(average(z, None), 20.0 / 6.0)
assert_equal(average(z, axis=0), [0.0, 1.0, 99.0, 99.0, 4.0, 7.5])
assert_equal(average(z, axis=1), [2.5, 5.0])
assert_equal(average(z, axis=0, weights=w2), [0.0, 1.0, 99.0, 99.0, 4.0, 10.0])
```

## Next Steps


---

*Source: test_extras.py:224 | Complexity: Advanced | Last updated: 2026-06-02*