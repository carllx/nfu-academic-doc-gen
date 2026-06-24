# How To: Get Names Flat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get names flat

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

### Step 1: Assign ndtype = np.dtype(...)

```python
ndtype = np.dtype([('A', '|S3'), ('B', float)])
```

**Verification:**
```python
assert_equal(test, ('A', 'B'))
```

### Step 2: Assign test = get_names_flat(...)

```python
test = get_names_flat(ndtype)
```

**Verification:**
```python
assert_equal(test, ('a', 'b', 'ba', 'bb'))
```

### Step 3: Call assert_equal()

```python
assert_equal(test, ('A', 'B'))
```

**Verification:**
```python
assert_equal(test, ('a', 'b'))
```

### Step 4: Assign ndtype = np.dtype(...)

```python
ndtype = np.dtype([('a', int), ('b', [('ba', float), ('bb', int)])])
```

**Verification:**
```python
assert_equal(test, ())
```

### Step 5: Assign test = get_names_flat(...)

```python
test = get_names_flat(ndtype)
```

### Step 6: Call assert_equal()

```python
assert_equal(test, ('a', 'b', 'ba', 'bb'))
```

### Step 7: Assign ndtype = np.dtype(...)

```python
ndtype = np.dtype([('a', int), ('b', [])])
```

### Step 8: Assign test = get_names_flat(...)

```python
test = get_names_flat(ndtype)
```

### Step 9: Call assert_equal()

```python
assert_equal(test, ('a', 'b'))
```

### Step 10: Assign ndtype = np.dtype(...)

```python
ndtype = np.dtype([])
```

### Step 11: Assign test = get_names_flat(...)

```python
test = get_names_flat(ndtype)
```

### Step 12: Call assert_equal()

```python
assert_equal(test, ())
```


## Complete Example

```python
# Workflow
ndtype = np.dtype([('A', '|S3'), ('B', float)])
test = get_names_flat(ndtype)
assert_equal(test, ('A', 'B'))
ndtype = np.dtype([('a', int), ('b', [('ba', float), ('bb', int)])])
test = get_names_flat(ndtype)
assert_equal(test, ('a', 'b', 'ba', 'bb'))
ndtype = np.dtype([('a', int), ('b', [])])
test = get_names_flat(ndtype)
assert_equal(test, ('a', 'b'))
ndtype = np.dtype([])
test = get_names_flat(ndtype)
assert_equal(test, ())
```

## Next Steps


---

*Source: test_recfunctions.py:134 | Complexity: Advanced | Last updated: 2026-06-02*