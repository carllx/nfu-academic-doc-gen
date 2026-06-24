# How To: Testaverage3

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test testAverage3

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

### Step 1: Assign a = arange(...)

```python
a = arange(6)
```

**Verification:**
```python
assert_equal(shape(r1), shape(w1))
```

### Step 2: Assign b = value

```python
b = arange(6) * 3
```

**Verification:**
```python
assert_equal(r1.shape, w1.shape)
```

### Step 3: Assign unknown = average(...)

```python
r1, w1 = average([[a, b], [b, a]], axis=1, returned=True)
```

**Verification:**
```python
assert_equal(shape(w2), shape(r2))
```

### Step 4: Call assert_equal()

```python
assert_equal(shape(r1), shape(w1))
```

**Verification:**
```python
assert_equal(shape(w2), shape(r2))
```

### Step 5: Call assert_equal()

```python
assert_equal(r1.shape, w1.shape)
```

**Verification:**
```python
assert_equal(shape(w2), shape(r2))
```

### Step 6: Assign unknown = average(...)

```python
r2, w2 = average(ones((2, 2, 3)), axis=0, weights=[3, 1], returned=True)
```

**Verification:**
```python
assert_equal(a2da, [0.5, 3.0])
```

### Step 7: Call assert_equal()

```python
assert_equal(shape(w2), shape(r2))
```

**Verification:**
```python
assert_equal(a2dma, [1.0, 3.0])
```

### Step 8: Assign unknown = average(...)

```python
r2, w2 = average(ones((2, 2, 3)), returned=True)
```

**Verification:**
```python
assert_equal(a2dma, 7.0 / 3.0)
```

### Step 9: Call assert_equal()

```python
assert_equal(shape(w2), shape(r2))
```

**Verification:**
```python
assert_equal(a2dma, [1.5, 4.0])
```

### Step 10: Assign unknown = average(...)

```python
r2, w2 = average(ones((2, 2, 3)), weights=ones((2, 2, 3)), returned=True)
```

### Step 11: Call assert_equal()

```python
assert_equal(shape(w2), shape(r2))
```

### Step 12: Assign a2d = array(...)

```python
a2d = array([[1, 2], [0, 4]], float)
```

### Step 13: Assign a2dm = masked_array(...)

```python
a2dm = masked_array(a2d, [[False, False], [True, False]])
```

### Step 14: Assign a2da = average(...)

```python
a2da = average(a2d, axis=0)
```

### Step 15: Call assert_equal()

```python
assert_equal(a2da, [0.5, 3.0])
```

### Step 16: Assign a2dma = average(...)

```python
a2dma = average(a2dm, axis=0)
```

### Step 17: Call assert_equal()

```python
assert_equal(a2dma, [1.0, 3.0])
```

### Step 18: Assign a2dma = average(...)

```python
a2dma = average(a2dm, axis=None)
```

### Step 19: Call assert_equal()

```python
assert_equal(a2dma, 7.0 / 3.0)
```

### Step 20: Assign a2dma = average(...)

```python
a2dma = average(a2dm, axis=1)
```

### Step 21: Call assert_equal()

```python
assert_equal(a2dma, [1.5, 4.0])
```


## Complete Example

```python
# Workflow
a = arange(6)
b = arange(6) * 3
r1, w1 = average([[a, b], [b, a]], axis=1, returned=True)
assert_equal(shape(r1), shape(w1))
assert_equal(r1.shape, w1.shape)
r2, w2 = average(ones((2, 2, 3)), axis=0, weights=[3, 1], returned=True)
assert_equal(shape(w2), shape(r2))
r2, w2 = average(ones((2, 2, 3)), returned=True)
assert_equal(shape(w2), shape(r2))
r2, w2 = average(ones((2, 2, 3)), weights=ones((2, 2, 3)), returned=True)
assert_equal(shape(w2), shape(r2))
a2d = array([[1, 2], [0, 4]], float)
a2dm = masked_array(a2d, [[False, False], [True, False]])
a2da = average(a2d, axis=0)
assert_equal(a2da, [0.5, 3.0])
a2dma = average(a2dm, axis=0)
assert_equal(a2dma, [1.0, 3.0])
a2dma = average(a2dm, axis=None)
assert_equal(a2dma, 7.0 / 3.0)
a2dma = average(a2dm, axis=1)
assert_equal(a2dma, [1.5, 4.0])
```

## Next Steps


---

*Source: test_extras.py:258 | Complexity: Advanced | Last updated: 2026-06-02*