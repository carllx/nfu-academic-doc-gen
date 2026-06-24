# How To: Array Astype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array astype

## Prerequisites

**Required Modules:**
- `textwrap`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.matrix(...)

```python
a = np.matrix([[0, 1, 2], [3, 4, 5]], dtype='f4')
```

**Verification:**
```python
assert_(a is b)
```

### Step 2: Assign b = a.astype(...)

```python
b = a.astype('f4', subok=True, copy=False)
```

**Verification:**
```python
assert_equal(a, b)
```

### Step 3: Call assert_()

```python
assert_(a is b)
```

**Verification:**
```python
assert_equal(type(b), np.matrix)
```

### Step 4: Assign b = a.astype(...)

```python
b = a.astype('i4', copy=False)
```

**Verification:**
```python
assert_equal(a, b)
```

### Step 5: Call assert_equal()

```python
assert_equal(a, b)
```

**Verification:**
```python
assert_(not a is b)
```

### Step 6: Call assert_equal()

```python
assert_equal(type(b), np.matrix)
```

**Verification:**
```python
assert_(type(b) is not np.matrix)
```

### Step 7: Assign b = a.astype(...)

```python
b = a.astype('f4', subok=False, copy=False)
```

### Step 8: Call assert_equal()

```python
assert_equal(a, b)
```

### Step 9: Call assert_()

```python
assert_(not a is b)
```

### Step 10: Call assert_()

```python
assert_(type(b) is not np.matrix)
```


## Complete Example

```python
# Workflow
a = np.matrix([[0, 1, 2], [3, 4, 5]], dtype='f4')
b = a.astype('f4', subok=True, copy=False)
assert_(a is b)
b = a.astype('i4', copy=False)
assert_equal(a, b)
assert_equal(type(b), np.matrix)
b = a.astype('f4', subok=False, copy=False)
assert_equal(a, b)
assert_(not a is b)
assert_(type(b) is not np.matrix)
```

## Next Steps


---

*Source: test_interaction.py:132 | Complexity: Advanced | Last updated: 2026-06-02*