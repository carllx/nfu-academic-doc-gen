# How To: Zip Descr

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test zip descr

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.ma`
- `numpy.lib.recfunctions`
- `numpy.ma.mrecords`
- `numpy.ma.testutils`
- `numpy.testing`
- `datetime`


## Step-by-Step Guide

### Step 1: Assign x = np.array(...)

```python
x = np.array([1, 2])
```

**Verification:**
```python
assert_equal(test, np.dtype([('', int), ('', int)]))
```

### Step 2: Assign y = np.array(...)

```python
y = np.array([10, 20, 30])
```

**Verification:**
```python
assert_equal(test, np.dtype([('', int), ('', int)]))
```

### Step 3: Assign z = np.array(...)

```python
z = np.array([('A', 1.0), ('B', 2.0)], dtype=[('A', '|S3'), ('B', float)])
```

**Verification:**
```python
assert_equal(test, np.dtype([('', int), ('A', '|S3'), ('B', float)]))
```

### Step 4: Assign w = np.array(...)

```python
w = np.array([(1, (2, 3.0)), (4, (5, 6.0))], dtype=[('a', int), ('b', [('ba', float), ('bb', int)])])
```

**Verification:**
```python
assert_equal(test, np.dtype([('', int), ('', [('A', '|S3'), ('B', float)])]))
```

### Step 5: Assign test = zip_descr(...)

```python
test = zip_descr((x, x), flatten=True)
```

**Verification:**
```python
assert_equal(test, np.dtype([('', int), ('a', int), ('ba', float), ('bb', int)]))
```

### Step 6: Call assert_equal()

```python
assert_equal(test, np.dtype([('', int), ('', int)]))
```

**Verification:**
```python
assert_equal(test, np.dtype([('', int), ('', [('a', int), ('b', [('ba', float), ('bb', int)])])]))
```

### Step 7: Assign test = zip_descr(...)

```python
test = zip_descr((x, x), flatten=False)
```

### Step 8: Call assert_equal()

```python
assert_equal(test, np.dtype([('', int), ('', int)]))
```

### Step 9: Assign test = zip_descr(...)

```python
test = zip_descr((x, z), flatten=True)
```

### Step 10: Call assert_equal()

```python
assert_equal(test, np.dtype([('', int), ('A', '|S3'), ('B', float)]))
```

### Step 11: Assign test = zip_descr(...)

```python
test = zip_descr((x, z), flatten=False)
```

### Step 12: Call assert_equal()

```python
assert_equal(test, np.dtype([('', int), ('', [('A', '|S3'), ('B', float)])]))
```

### Step 13: Assign test = zip_descr(...)

```python
test = zip_descr((x, w), flatten=True)
```

### Step 14: Call assert_equal()

```python
assert_equal(test, np.dtype([('', int), ('a', int), ('ba', float), ('bb', int)]))
```

### Step 15: Assign test = zip_descr(...)

```python
test = zip_descr((x, w), flatten=False)
```

### Step 16: Call assert_equal()

```python
assert_equal(test, np.dtype([('', int), ('', [('a', int), ('b', [('ba', float), ('bb', int)])])]))
```


## Complete Example

```python
# Workflow
x = np.array([1, 2])
y = np.array([10, 20, 30])
z = np.array([('A', 1.0), ('B', 2.0)], dtype=[('A', '|S3'), ('B', float)])
w = np.array([(1, (2, 3.0)), (4, (5, 6.0))], dtype=[('a', int), ('b', [('ba', float), ('bb', int)])])
test = zip_descr((x, x), flatten=True)
assert_equal(test, np.dtype([('', int), ('', int)]))
test = zip_descr((x, x), flatten=False)
assert_equal(test, np.dtype([('', int), ('', int)]))
test = zip_descr((x, z), flatten=True)
assert_equal(test, np.dtype([('', int), ('A', '|S3'), ('B', float)]))
test = zip_descr((x, z), flatten=False)
assert_equal(test, np.dtype([('', int), ('', [('A', '|S3'), ('B', float)])]))
test = zip_descr((x, w), flatten=True)
assert_equal(test, np.dtype([('', int), ('a', int), ('ba', float), ('bb', int)]))
test = zip_descr((x, w), flatten=False)
assert_equal(test, np.dtype([('', int), ('', [('a', int), ('b', [('ba', float), ('bb', int)])])]))
```

## Next Steps


---

*Source: test_recfunctions.py:35 | Complexity: Advanced | Last updated: 2026-06-02*