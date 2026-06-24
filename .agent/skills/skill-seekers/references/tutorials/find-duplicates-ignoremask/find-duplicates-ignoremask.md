# How To: Find Duplicates Ignoremask

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test find duplicates ignoremask

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

### Step 1: Assign ndtype = value

```python
ndtype = [('a', int)]
```

**Verification:**
```python
assert_equal(sorted(test[-1]), control)
```

### Step 2: Assign a = ma.array.view(...)

```python
a = ma.array([1, 1, 1, 2, 2, 3, 3], mask=[0, 0, 1, 0, 0, 0, 1]).view(ndtype)
```

**Verification:**
```python
assert_equal(test[0], a[test[-1]])
```

### Step 3: Assign test = find_duplicates(...)

```python
test = find_duplicates(a, ignoremask=True, return_index=True)
```

**Verification:**
```python
assert_equal(sorted(test[-1]), control)
```

### Step 4: Assign control = value

```python
control = [0, 1, 3, 4]
```

**Verification:**
```python
assert_equal(test[0], a[test[-1]])
```

### Step 5: Call assert_equal()

```python
assert_equal(sorted(test[-1]), control)
```

### Step 6: Call assert_equal()

```python
assert_equal(test[0], a[test[-1]])
```

### Step 7: Assign test = find_duplicates(...)

```python
test = find_duplicates(a, ignoremask=False, return_index=True)
```

### Step 8: Assign control = value

```python
control = [0, 1, 2, 3, 4, 6]
```

### Step 9: Call assert_equal()

```python
assert_equal(sorted(test[-1]), control)
```

### Step 10: Call assert_equal()

```python
assert_equal(test[0], a[test[-1]])
```


## Complete Example

```python
# Workflow
ndtype = [('a', int)]
a = ma.array([1, 1, 1, 2, 2, 3, 3], mask=[0, 0, 1, 0, 0, 0, 1]).view(ndtype)
test = find_duplicates(a, ignoremask=True, return_index=True)
control = [0, 1, 3, 4]
assert_equal(sorted(test[-1]), control)
assert_equal(test[0], a[test[-1]])
test = find_duplicates(a, ignoremask=False, return_index=True)
control = [0, 1, 2, 3, 4, 6]
assert_equal(sorted(test[-1]), control)
assert_equal(test[0], a[test[-1]])
```

## Next Steps


---

*Source: test_recfunctions.py:212 | Complexity: Advanced | Last updated: 2026-06-02*