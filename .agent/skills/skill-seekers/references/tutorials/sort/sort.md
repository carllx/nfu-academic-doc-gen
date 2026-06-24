# How To: Sort

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort

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
assert_array_equal(a.view(np.float64), [1.0, 2.0, 3.0])
```

### Step 2: Assign a = value

```python
a = a[::-1]
```

**Verification:**
```python
assert_array_equal(sorted_a.view(np.float64), [1.0, 2.0, 3.0])
```

### Step 3: Call a.sort()

```python
a.sort()
```

**Verification:**
```python
assert_array_equal(a.view(np.float64), [3.0, 2.0, 1.0])
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(a.view(np.float64), [1.0, 2.0, 3.0])
```

**Verification:**
```python
assert_array_equal(sorted_a.view(np.float64), [2.0, 6.0])
```

### Step 5: Assign a = self._get_array(...)

```python
a = self._get_array(1.0)
```

**Verification:**
```python
assert_array_equal(a.view(np.float64), [6.0, 2.0])
```

### Step 6: Assign a = value

```python
a = a[::-1]
```

**Verification:**
```python
assert_array_equal(sorted_a.view(np.float64), [2.0, 4.0, 6.0])
```

### Step 7: Assign sorted_a = np.sort(...)

```python
sorted_a = np.sort(a)
```

**Verification:**
```python
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(sorted_a.view(np.float64), [1.0, 2.0, 3.0])
```

**Verification:**
```python
assert_array_equal(sorted_a.view(np.float64), [2.0, 4.0, 6.0])
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(a.view(np.float64), [3.0, 2.0, 1.0])
```

**Verification:**
```python
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```

### Step 10: Assign a = self._get_array(...)

```python
a = self._get_array(0.5)
```

**Verification:**
```python
assert_array_equal(sorted_a.view(np.float64), [2.0, 4.0, 6.0])
```

### Step 11: Assign a = value

```python
a = a[::2][::-1]
```

**Verification:**
```python
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```

### Step 12: Assign sorted_a = np.sort(...)

```python
sorted_a = np.sort(a)
```

### Step 13: Call assert_array_equal()

```python
assert_array_equal(sorted_a.view(np.float64), [2.0, 6.0])
```

### Step 14: Call assert_array_equal()

```python
assert_array_equal(a.view(np.float64), [6.0, 2.0])
```

### Step 15: Assign a = self._get_array(...)

```python
a = self._get_array(0.5, aligned=False)
```

### Step 16: Assign a = value

```python
a = a[::-1]
```

### Step 17: Assign sorted_a = np.sort(...)

```python
sorted_a = np.sort(a)
```

### Step 18: Call assert_array_equal()

```python
assert_array_equal(sorted_a.view(np.float64), [2.0, 4.0, 6.0])
```

### Step 19: Call assert_array_equal()

```python
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```

### Step 20: Assign sorted_a = np.sort(...)

```python
sorted_a = np.sort(a, stable=True)
```

### Step 21: Call assert_array_equal()

```python
assert_array_equal(sorted_a.view(np.float64), [2.0, 4.0, 6.0])
```

### Step 22: Call assert_array_equal()

```python
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```

### Step 23: Assign sorted_a = np.sort(...)

```python
sorted_a = np.sort(a, stable=False)
```

### Step 24: Call assert_array_equal()

```python
assert_array_equal(sorted_a.view(np.float64), [2.0, 4.0, 6.0])
```

### Step 25: Call assert_array_equal()

```python
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```


## Complete Example

```python
# Workflow
a = self._get_array(1.0)
a = a[::-1]
a.sort()
assert_array_equal(a.view(np.float64), [1.0, 2.0, 3.0])
a = self._get_array(1.0)
a = a[::-1]
sorted_a = np.sort(a)
assert_array_equal(sorted_a.view(np.float64), [1.0, 2.0, 3.0])
assert_array_equal(a.view(np.float64), [3.0, 2.0, 1.0])
a = self._get_array(0.5)
a = a[::2][::-1]
sorted_a = np.sort(a)
assert_array_equal(sorted_a.view(np.float64), [2.0, 6.0])
assert_array_equal(a.view(np.float64), [6.0, 2.0])
a = self._get_array(0.5, aligned=False)
a = a[::-1]
sorted_a = np.sort(a)
assert_array_equal(sorted_a.view(np.float64), [2.0, 4.0, 6.0])
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
sorted_a = np.sort(a, stable=True)
assert_array_equal(sorted_a.view(np.float64), [2.0, 4.0, 6.0])
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
sorted_a = np.sort(a, stable=False)
assert_array_equal(sorted_a.view(np.float64), [2.0, 4.0, 6.0])
assert_array_equal(a.view(np.float64), [6.0, 4.0, 2.0])
```

## Next Steps


---

*Source: test_custom_dtypes.py:234 | Complexity: Advanced | Last updated: 2026-06-02*