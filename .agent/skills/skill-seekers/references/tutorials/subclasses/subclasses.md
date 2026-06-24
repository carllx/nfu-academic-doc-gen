# How To: Subclasses

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subclasses

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy._core._rational_tests`
- `numpy.lib._stride_tricks_impl`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = VerySimpleSubClass(...)

```python
a = VerySimpleSubClass([1, 2, 3, 4])
```

**Verification:**
```python
assert_(type(a) is VerySimpleSubClass)
```

### Step 2: Call assert_()

```python
assert_(type(a) is VerySimpleSubClass)
```

**Verification:**
```python
assert_(type(a_view) is np.ndarray)
```

### Step 3: Assign a_view = as_strided(...)

```python
a_view = as_strided(a, shape=(2,), strides=(2 * a.itemsize,))
```

**Verification:**
```python
assert_(type(a_view) is VerySimpleSubClass)
```

### Step 4: Call assert_()

```python
assert_(type(a_view) is np.ndarray)
```

**Verification:**
```python
assert_(type(a_view) is SimpleSubClass)
```

### Step 5: Assign a_view = as_strided(...)

```python
a_view = as_strided(a, shape=(2,), strides=(2 * a.itemsize,), subok=True)
```

**Verification:**
```python
assert_(a_view.info == 'simple finalized')
```

### Step 6: Call assert_()

```python
assert_(type(a_view) is VerySimpleSubClass)
```

**Verification:**
```python
assert_(type(a_view) is np.ndarray)
```

### Step 7: Assign a = SimpleSubClass(...)

```python
a = SimpleSubClass([1, 2, 3, 4])
```

**Verification:**
```python
assert_(type(b_view) is np.ndarray)
```

### Step 8: Assign a_view = as_strided(...)

```python
a_view = as_strided(a, shape=(2,), strides=(2 * a.itemsize,), subok=True)
```

**Verification:**
```python
assert_(a_view.shape == b_view.shape)
```

### Step 9: Call assert_()

```python
assert_(type(a_view) is SimpleSubClass)
```

**Verification:**
```python
assert_(type(a_view) is SimpleSubClass)
```

### Step 10: Call assert_()

```python
assert_(a_view.info == 'simple finalized')
```

**Verification:**
```python
assert_(a_view.info == 'simple finalized')
```

### Step 11: Assign b = np.arange.reshape(...)

```python
b = np.arange(len(a)).reshape(-1, 1)
```

**Verification:**
```python
assert_(type(b_view) is np.ndarray)
```

### Step 12: Assign unknown = broadcast_arrays(...)

```python
a_view, b_view = broadcast_arrays(a, b)
```

**Verification:**
```python
assert_(a_view.shape == b_view.shape)
```

### Step 13: Call assert_()

```python
assert_(type(a_view) is np.ndarray)
```

**Verification:**
```python
assert_(type(a_view) is np.ndarray)
```

### Step 14: Call assert_()

```python
assert_(type(b_view) is np.ndarray)
```

**Verification:**
```python
assert_(a_view.shape == shape)
```

### Step 15: Call assert_()

```python
assert_(a_view.shape == b_view.shape)
```

**Verification:**
```python
assert_(type(a_view) is SimpleSubClass)
```

### Step 16: Assign unknown = broadcast_arrays(...)

```python
a_view, b_view = broadcast_arrays(a, b, subok=True)
```

**Verification:**
```python
assert_(a_view.info == 'simple finalized')
```

### Step 17: Call assert_()

```python
assert_(type(a_view) is SimpleSubClass)
```

**Verification:**
```python
assert_(a_view.shape == shape)
```

### Step 18: Call assert_()

```python
assert_(a_view.info == 'simple finalized')
```

### Step 19: Call assert_()

```python
assert_(type(b_view) is np.ndarray)
```

### Step 20: Call assert_()

```python
assert_(a_view.shape == b_view.shape)
```

### Step 21: Assign shape = value

```python
shape = (2, 4)
```

### Step 22: Assign a_view = broadcast_to(...)

```python
a_view = broadcast_to(a, shape)
```

### Step 23: Call assert_()

```python
assert_(type(a_view) is np.ndarray)
```

### Step 24: Call assert_()

```python
assert_(a_view.shape == shape)
```

### Step 25: Assign a_view = broadcast_to(...)

```python
a_view = broadcast_to(a, shape, subok=True)
```

### Step 26: Call assert_()

```python
assert_(type(a_view) is SimpleSubClass)
```

### Step 27: Call assert_()

```python
assert_(a_view.info == 'simple finalized')
```

### Step 28: Call assert_()

```python
assert_(a_view.shape == shape)
```


## Complete Example

```python
# Workflow
a = VerySimpleSubClass([1, 2, 3, 4])
assert_(type(a) is VerySimpleSubClass)
a_view = as_strided(a, shape=(2,), strides=(2 * a.itemsize,))
assert_(type(a_view) is np.ndarray)
a_view = as_strided(a, shape=(2,), strides=(2 * a.itemsize,), subok=True)
assert_(type(a_view) is VerySimpleSubClass)
a = SimpleSubClass([1, 2, 3, 4])
a_view = as_strided(a, shape=(2,), strides=(2 * a.itemsize,), subok=True)
assert_(type(a_view) is SimpleSubClass)
assert_(a_view.info == 'simple finalized')
b = np.arange(len(a)).reshape(-1, 1)
a_view, b_view = broadcast_arrays(a, b)
assert_(type(a_view) is np.ndarray)
assert_(type(b_view) is np.ndarray)
assert_(a_view.shape == b_view.shape)
a_view, b_view = broadcast_arrays(a, b, subok=True)
assert_(type(a_view) is SimpleSubClass)
assert_(a_view.info == 'simple finalized')
assert_(type(b_view) is np.ndarray)
assert_(a_view.shape == b_view.shape)
shape = (2, 4)
a_view = broadcast_to(a, shape)
assert_(type(a_view) is np.ndarray)
assert_(a_view.shape == shape)
a_view = broadcast_to(a, shape, subok=True)
assert_(type(a_view) is SimpleSubClass)
assert_(a_view.info == 'simple finalized')
assert_(a_view.shape == shape)
```

## Next Steps


---

*Source: test_stride_tricks.py:543 | Complexity: Advanced | Last updated: 2026-06-02*