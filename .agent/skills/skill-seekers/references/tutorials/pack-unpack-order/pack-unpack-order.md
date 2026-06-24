# How To: Pack Unpack Order

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pack unpack order

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([[2], [7], [23]], dtype=np.uint8)
```

**Verification:**
```python
assert_equal(b.dtype, np.uint8)
```

### Step 2: Assign b = np.unpackbits(...)

```python
b = np.unpackbits(a, axis=1)
```

**Verification:**
```python
assert_array_equal(b, b_big)
```

### Step 3: Call assert_equal()

```python
assert_equal(b.dtype, np.uint8)
```

**Verification:**
```python
assert_array_equal(a, np.packbits(b_little, axis=1, bitorder='little'))
```

### Step 4: Assign b_little = np.unpackbits(...)

```python
b_little = np.unpackbits(a, axis=1, bitorder='little')
```

**Verification:**
```python
assert_array_equal(b[:, ::-1], b_little)
```

### Step 5: Assign b_big = np.unpackbits(...)

```python
b_big = np.unpackbits(a, axis=1, bitorder='big')
```

**Verification:**
```python
assert_array_equal(a, np.packbits(b_big, axis=1, bitorder='big'))
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(b, b_big)
```

**Verification:**
```python
assert_raises(ValueError, np.unpackbits, a, bitorder='r')
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(a, np.packbits(b_little, axis=1, bitorder='little'))
```

**Verification:**
```python
assert_raises(TypeError, np.unpackbits, a, bitorder=10)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(b[:, ::-1], b_little)
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(a, np.packbits(b_big, axis=1, bitorder='big'))
```

### Step 10: Call assert_raises()

```python
assert_raises(ValueError, np.unpackbits, a, bitorder='r')
```

### Step 11: Call assert_raises()

```python
assert_raises(TypeError, np.unpackbits, a, bitorder=10)
```


## Complete Example

```python
# Workflow
a = np.array([[2], [7], [23]], dtype=np.uint8)
b = np.unpackbits(a, axis=1)
assert_equal(b.dtype, np.uint8)
b_little = np.unpackbits(a, axis=1, bitorder='little')
b_big = np.unpackbits(a, axis=1, bitorder='big')
assert_array_equal(b, b_big)
assert_array_equal(a, np.packbits(b_little, axis=1, bitorder='little'))
assert_array_equal(b[:, ::-1], b_little)
assert_array_equal(a, np.packbits(b_big, axis=1, bitorder='big'))
assert_raises(ValueError, np.unpackbits, a, bitorder='r')
assert_raises(TypeError, np.unpackbits, a, bitorder=10)
```

## Next Steps


---

*Source: test_packbits.py:233 | Complexity: Advanced | Last updated: 2026-06-02*