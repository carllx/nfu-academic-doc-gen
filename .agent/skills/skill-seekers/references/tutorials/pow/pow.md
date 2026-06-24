# How To: Pow

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test raising a matrix to an integer power works as expected.

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

### Step 1: 'Test raising a matrix to an integer power works as expected.'

```python
'Test raising a matrix to an integer power works as expected.'
```

**Verification:**
```python
assert_array_almost_equal(m2, m ** 2)
```

### Step 2: Assign m = matrix(...)

```python
m = matrix('1. 2.; 3. 4.')
```

**Verification:**
```python
assert_array_almost_equal(m4, np.dot(m2, m2))
```

### Step 3: Assign m2 = m.copy(...)

```python
m2 = m.copy()
```

**Verification:**
```python
assert_array_almost_equal(np.dot(mi, m), np.eye(2))
```

### Step 4: Assign mi = m.copy(...)

```python
mi = m.copy()
```

### Step 5: Assign m4 = m2.copy(...)

```python
m4 = m2.copy()
```

### Step 6: Call assert_array_almost_equal()

```python
assert_array_almost_equal(m2, m ** 2)
```

### Step 7: Call assert_array_almost_equal()

```python
assert_array_almost_equal(m4, np.dot(m2, m2))
```

### Step 8: Call assert_array_almost_equal()

```python
assert_array_almost_equal(np.dot(mi, m), np.eye(2))
```


## Complete Example

```python
# Workflow
'Test raising a matrix to an integer power works as expected.'
m = matrix('1. 2.; 3. 4.')
m2 = m.copy()
m2 **= 2
mi = m.copy()
mi **= -1
m4 = m2.copy()
m4 **= 2
assert_array_almost_equal(m2, m ** 2)
assert_array_almost_equal(m4, np.dot(m2, m2))
assert_array_almost_equal(np.dot(mi, m), np.eye(2))
```

## Next Steps


---

*Source: test_defmatrix.py:242 | Complexity: Advanced | Last updated: 2026-06-02*