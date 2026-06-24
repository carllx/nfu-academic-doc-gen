# How To: Writeable

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test writeable

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy._core._rational_tests`
- `numpy.lib._stride_tricks_impl`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.arange(...)

```python
arr = np.arange(5)
```

**Verification:**
```python
assert_(not view.flags.writeable)
```

### Step 2: Assign view = sliding_window_view(...)

```python
view = sliding_window_view(arr, 2, writeable=False)
```

**Verification:**
```python
assert_(view.flags.writeable)
```

### Step 3: Call assert_()

```python
assert_(not view.flags.writeable)
```

**Verification:**
```python
assert_array_equal(arr, np.array([0, 3, 2, 3, 4]))
```

### Step 4: Assign view = sliding_window_view(...)

```python
view = sliding_window_view(arr, 2, writeable=True)
```

### Step 5: Call assert_()

```python
assert_(view.flags.writeable)
```

### Step 6: Assign unknown = 3

```python
view[0, 1] = 3
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(arr, np.array([0, 3, 2, 3, 4]))
```

### Step 8: Assign unknown = 3

```python
view[0, 0] = 3
```


## Complete Example

```python
# Workflow
arr = np.arange(5)
view = sliding_window_view(arr, 2, writeable=False)
assert_(not view.flags.writeable)
with pytest.raises(ValueError, match='assignment destination is read-only'):
    view[0, 0] = 3
view = sliding_window_view(arr, 2, writeable=True)
assert_(view.flags.writeable)
view[0, 1] = 3
assert_array_equal(arr, np.array([0, 3, 2, 3, 4]))
```

## Next Steps


---

*Source: test_stride_tricks.py:484 | Complexity: Advanced | Last updated: 2026-06-02*