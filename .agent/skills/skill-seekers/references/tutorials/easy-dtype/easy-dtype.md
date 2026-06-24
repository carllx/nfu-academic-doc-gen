# How To: Easy Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test ndtype on dtypes

## Prerequisites

**Required Modules:**
- `time`
- `datetime`
- `pytest`
- `numpy`
- `numpy.lib._iotools`
- `numpy.testing`
- `numpy._core.numeric`


## Step-by-Step Guide

### Step 1: 'Test ndtype on dtypes'

```python
'Test ndtype on dtypes'
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype), np.dtype(float))
```

### Step 2: Assign ndtype = float

```python
ndtype = float
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype), np.dtype([('f0', 'i4'), ('f1', 'f8')]))
```

### Step 3: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype), np.dtype(float))
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype, defaultfmt='field_%03i'), np.dtype([('field_000', 'i4'), ('field_001', 'f8')]))
```

### Step 4: Assign ndtype = 'i4, f8'

```python
ndtype = 'i4, f8'
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype, names='a, b'), np.dtype([('a', 'i4'), ('b', 'f8')]))
```

### Step 5: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype), np.dtype([('f0', 'i4'), ('f1', 'f8')]))
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype, names='a, b, c'), np.dtype([('a', 'i4'), ('b', 'f8')]))
```

### Step 6: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype, defaultfmt='field_%03i'), np.dtype([('field_000', 'i4'), ('field_001', 'f8')]))
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype, names=', b'), np.dtype([('f0', 'i4'), ('b', 'f8')]))
```

### Step 7: Assign ndtype = 'i4, f8'

```python
ndtype = 'i4, f8'
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype, names='a', defaultfmt='f%02i'), np.dtype([('a', 'i4'), ('f00', 'f8')]))
```

### Step 8: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype, names='a, b'), np.dtype([('a', 'i4'), ('b', 'f8')]))
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype), np.dtype([('A', int), ('B', float)]))
```

### Step 9: Assign ndtype = 'i4, f8'

```python
ndtype = 'i4, f8'
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype, names='a,b'), np.dtype([('a', int), ('b', float)]))
```

### Step 10: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype, names='a, b, c'), np.dtype([('a', 'i4'), ('b', 'f8')]))
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype, names='a'), np.dtype([('a', int), ('f0', float)]))
```

### Step 11: Assign ndtype = 'i4, f8'

```python
ndtype = 'i4, f8'
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype, names='a,b,c'), np.dtype([('a', int), ('b', float)]))
```

### Step 12: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype, names=', b'), np.dtype([('f0', 'i4'), ('b', 'f8')]))
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype), np.dtype([('f0', int), ('f1', float), ('f2', float)]))
```

### Step 13: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype, names='a', defaultfmt='f%02i'), np.dtype([('a', 'i4'), ('f00', 'f8')]))
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype, names='a, b, c'), np.dtype([('a', int), ('b', float), ('c', float)]))
```

### Step 14: Assign ndtype = value

```python
ndtype = [('A', int), ('B', float)]
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype, names='a, b, c'), np.dtype([(_, float) for _ in ('a', 'b', 'c')]))
```

### Step 15: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype), np.dtype([('A', int), ('B', float)]))
```

**Verification:**
```python
assert_equal(easy_dtype(ndtype, names=['', '', ''], defaultfmt='f%02i'), np.dtype([(_, float) for _ in ('f00', 'f01', 'f02')]))
```

### Step 16: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype, names='a,b'), np.dtype([('a', int), ('b', float)]))
```

### Step 17: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype, names='a'), np.dtype([('a', int), ('f0', float)]))
```

### Step 18: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype, names='a,b,c'), np.dtype([('a', int), ('b', float)]))
```

### Step 19: Assign ndtype = value

```python
ndtype = (int, float, float)
```

### Step 20: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype), np.dtype([('f0', int), ('f1', float), ('f2', float)]))
```

### Step 21: Assign ndtype = value

```python
ndtype = (int, float, float)
```

### Step 22: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype, names='a, b, c'), np.dtype([('a', int), ('b', float), ('c', float)]))
```

### Step 23: Assign ndtype = np.dtype(...)

```python
ndtype = np.dtype(float)
```

### Step 24: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype, names='a, b, c'), np.dtype([(_, float) for _ in ('a', 'b', 'c')]))
```

### Step 25: Assign ndtype = np.dtype(...)

```python
ndtype = np.dtype(float)
```

### Step 26: Call assert_equal()

```python
assert_equal(easy_dtype(ndtype, names=['', '', ''], defaultfmt='f%02i'), np.dtype([(_, float) for _ in ('f00', 'f01', 'f02')]))
```


## Complete Example

```python
# Workflow
'Test ndtype on dtypes'
ndtype = float
assert_equal(easy_dtype(ndtype), np.dtype(float))
ndtype = 'i4, f8'
assert_equal(easy_dtype(ndtype), np.dtype([('f0', 'i4'), ('f1', 'f8')]))
assert_equal(easy_dtype(ndtype, defaultfmt='field_%03i'), np.dtype([('field_000', 'i4'), ('field_001', 'f8')]))
ndtype = 'i4, f8'
assert_equal(easy_dtype(ndtype, names='a, b'), np.dtype([('a', 'i4'), ('b', 'f8')]))
ndtype = 'i4, f8'
assert_equal(easy_dtype(ndtype, names='a, b, c'), np.dtype([('a', 'i4'), ('b', 'f8')]))
ndtype = 'i4, f8'
assert_equal(easy_dtype(ndtype, names=', b'), np.dtype([('f0', 'i4'), ('b', 'f8')]))
assert_equal(easy_dtype(ndtype, names='a', defaultfmt='f%02i'), np.dtype([('a', 'i4'), ('f00', 'f8')]))
ndtype = [('A', int), ('B', float)]
assert_equal(easy_dtype(ndtype), np.dtype([('A', int), ('B', float)]))
assert_equal(easy_dtype(ndtype, names='a,b'), np.dtype([('a', int), ('b', float)]))
assert_equal(easy_dtype(ndtype, names='a'), np.dtype([('a', int), ('f0', float)]))
assert_equal(easy_dtype(ndtype, names='a,b,c'), np.dtype([('a', int), ('b', float)]))
ndtype = (int, float, float)
assert_equal(easy_dtype(ndtype), np.dtype([('f0', int), ('f1', float), ('f2', float)]))
ndtype = (int, float, float)
assert_equal(easy_dtype(ndtype, names='a, b, c'), np.dtype([('a', int), ('b', float), ('c', float)]))
ndtype = np.dtype(float)
assert_equal(easy_dtype(ndtype, names='a, b, c'), np.dtype([(_, float) for _ in ('a', 'b', 'c')]))
ndtype = np.dtype(float)
assert_equal(easy_dtype(ndtype, names=['', '', ''], defaultfmt='f%02i'), np.dtype([(_, float) for _ in ('f00', 'f01', 'f02')]))
```

## Next Steps


---

*Source: test__iotools.py:282 | Complexity: Advanced | Last updated: 2026-06-02*