# How To: Argsort

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test argsort

## Prerequisites

**Required Modules:**
- `tempfile`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy.testing`
- `pickle`


## Step-by-Step Guide

### Step 1: Assign a = self._get_array(...)

```python
a = self._get_array(1.0)
```

**Verification:**
```python
assert_array_equal(indices, [2, 1, 0])
```

### Step 2: Assign a = value

```python
a = a[::-1]
```

**Verification:**
```python
assert_array_equal(a.view(np.float64), [3.0, 2.0, 1.0])
```

### Step 3: Assign indices = np.argsort(...)

```python
indices = np.argsort(a)
```

**Verification:**
```python
assert_array_equal(indices, [1, 0])
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(indices, [2, 1, 0])
```

**Verification:**
```python
assert_array_equal(a.view(np.float64), [6.0, 2.0])
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(a.view(np.float64), [3.0, 2.0, 1.0])
```

**Verification:**
```python
assert_array_equal(indices, [2, 1, 0])
```

### Step 6: Assign a = self._get_array(...)

```python
a = self._get_array(0.5)
```

**Verification:**
```python
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```

### Step 7: Assign a = value

```python
a = a[::2][::-1]
```

**Verification:**
```python
assert_array_equal(sorted_indices, [2, 1, 0])
```

### Step 8: Assign indices = np.argsort(...)

```python
indices = np.argsort(a)
```

**Verification:**
```python
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(indices, [1, 0])
```

**Verification:**
```python
assert_array_equal(sorted_indices, [2, 1, 0])
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(a.view(np.float64), [6.0, 2.0])
```

**Verification:**
```python
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```

### Step 11: Assign a = self._get_array(...)

```python
a = self._get_array(0.5, aligned=False)
```

### Step 12: Assign a = value

```python
a = a[::-1]
```

### Step 13: Assign indices = np.argsort(...)

```python
indices = np.argsort(a)
```

### Step 14: Call assert_array_equal()

```python
assert_array_equal(indices, [2, 1, 0])
```

### Step 15: Call assert_array_equal()

```python
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```

### Step 16: Assign sorted_indices = np.argsort(...)

```python
sorted_indices = np.argsort(a, stable=True)
```

### Step 17: Call assert_array_equal()

```python
assert_array_equal(sorted_indices, [2, 1, 0])
```

### Step 18: Call assert_array_equal()

```python
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```

### Step 19: Assign sorted_indices = np.argsort(...)

```python
sorted_indices = np.argsort(a, stable=False)
```

### Step 20: Call assert_array_equal()

```python
assert_array_equal(sorted_indices, [2, 1, 0])
```

### Step 21: Call assert_array_equal()

```python
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```


## Complete Example

```python
# Workflow
a = self._get_array(1.0)
a = a[::-1]
indices = np.argsort(a)
assert_array_equal(indices, [2, 1, 0])
assert_array_equal(a.view(np.float64), [3.0, 2.0, 1.0])
a = self._get_array(0.5)
a = a[::2][::-1]
indices = np.argsort(a)
assert_array_equal(indices, [1, 0])
assert_array_equal(a.view(np.float64), [6.0, 2.0])
a = self._get_array(0.5, aligned=False)
a = a[::-1]
indices = np.argsort(a)
assert_array_equal(indices, [2, 1, 0])
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
sorted_indices = np.argsort(a, stable=True)
assert_array_equal(sorted_indices, [2, 1, 0])
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
sorted_indices = np.argsort(a, stable=False)
assert_array_equal(sorted_indices, [2, 1, 0])
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```

## Next Steps


---

*Source: test_custom_dtypes.py:273 | Complexity: Advanced | Last updated: 2026-06-02*