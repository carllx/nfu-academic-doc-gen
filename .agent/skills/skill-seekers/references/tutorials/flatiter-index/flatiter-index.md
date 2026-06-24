# How To: Flatiter Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test flatiter index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `tempfile`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy.testing`
- `pickle`

**Setup Required:**
```python
# Fixtures: index
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([1.0, 2.0, 3.0], dtype=SF(1.0))
```

### Step 2: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(arr[index].view(np.float64), arr.flat[index].view(np.float64))
```

### Step 3: Assign arr2 = arr.copy(...)

```python
arr2 = arr.copy()
```

### Step 4: Assign unknown = 5.0

```python
arr[index] = 5.0
```

### Step 5: Assign unknown = 5.0

```python
arr2.flat[index] = 5.0
```

### Step 6: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(arr.view(np.float64), arr2.view(np.float64))
```


## Complete Example

```python
# Setup
# Fixtures: index

# Workflow
arr = np.array([1.0, 2.0, 3.0], dtype=SF(1.0))
np.testing.assert_array_equal(arr[index].view(np.float64), arr.flat[index].view(np.float64))
arr2 = arr.copy()
arr[index] = 5.0
arr2.flat[index] = 5.0
np.testing.assert_array_equal(arr.view(np.float64), arr2.view(np.float64))
```

## Next Steps


---

*Source: test_custom_dtypes.py:365 | Complexity: Intermediate | Last updated: 2026-06-02*