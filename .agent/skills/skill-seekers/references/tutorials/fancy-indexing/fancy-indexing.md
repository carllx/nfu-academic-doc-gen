# How To: Fancy Indexing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fancy indexing

## Prerequisites

**Required Modules:**
- `collections.abc`
- `numpy`
- `numpy`
- `numpy.linalg`
- `numpy.testing`
- `numpy.linalg`
- `numpy.linalg`


## Step-by-Step Guide

### Step 1: Assign a = value

```python
a = self.a
```

**Verification:**
```python
assert_(isinstance(x, matrix))
```

### Step 2: Assign x = value

```python
x = a[1, [0, 1, 0]]
```

**Verification:**
```python
assert_equal(x, matrix([[3, 4, 3]]))
```

### Step 3: Call assert_()

```python
assert_(isinstance(x, matrix))
```

**Verification:**
```python
assert_(isinstance(x, matrix))
```

### Step 4: Call assert_equal()

```python
assert_equal(x, matrix([[3, 4, 3]]))
```

**Verification:**
```python
assert_equal(x, matrix([[3, 4], [1, 2]]))
```

### Step 5: Assign x = value

```python
x = a[[1, 0]]
```

**Verification:**
```python
assert_(isinstance(x, matrix))
```

### Step 6: Call assert_()

```python
assert_(isinstance(x, matrix))
```

**Verification:**
```python
assert_equal(x, matrix([[4, 3], [1, 2]]))
```

### Step 7: Call assert_equal()

```python
assert_equal(x, matrix([[3, 4], [1, 2]]))
```

### Step 8: Assign x = value

```python
x = a[[[1], [0]], [[1, 0], [0, 1]]]
```

### Step 9: Call assert_()

```python
assert_(isinstance(x, matrix))
```

### Step 10: Call assert_equal()

```python
assert_equal(x, matrix([[4, 3], [1, 2]]))
```


## Complete Example

```python
# Workflow
a = self.a
x = a[1, [0, 1, 0]]
assert_(isinstance(x, matrix))
assert_equal(x, matrix([[3, 4, 3]]))
x = a[[1, 0]]
assert_(isinstance(x, matrix))
assert_equal(x, matrix([[3, 4], [1, 2]]))
x = a[[[1], [0]], [[1, 0], [0, 1]]]
assert_(isinstance(x, matrix))
assert_equal(x, matrix([[4, 3], [1, 2]]))
```

## Next Steps


---

*Source: test_defmatrix.py:340 | Complexity: Advanced | Last updated: 2026-06-02*