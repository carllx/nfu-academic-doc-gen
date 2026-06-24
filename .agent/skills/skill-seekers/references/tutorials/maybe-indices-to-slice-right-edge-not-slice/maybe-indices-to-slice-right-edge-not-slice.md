# How To: Maybe Indices To Slice Right Edge Not Slice

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test maybe indices to slice right edge not slice

## Prerequisites

**Required Modules:**
- `pickle`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign target = np.arange(...)

```python
target = np.arange(100)
```

**Verification:**
```python
assert not isinstance(maybe_slice, slice)
```

### Step 2: Assign indices = np.array(...)

```python
indices = np.array([97, 98, 99, 100], dtype=np.intp)
```

**Verification:**
```python
assert not isinstance(maybe_slice, slice)
```

### Step 3: Assign maybe_slice = lib.maybe_indices_to_slice(...)

```python
maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
```

**Verification:**
```python
assert not isinstance(maybe_slice, slice)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(maybe_slice, indices)
```

### Step 5: Assign msg = 'index 100 is out of bounds for axis (0|1) with size 100'

```python
msg = 'index 100 is out of bounds for axis (0|1) with size 100'
```

### Step 6: Assign indices = np.array(...)

```python
indices = np.array([100, 99, 98, 97], dtype=np.intp)
```

### Step 7: Assign maybe_slice = lib.maybe_indices_to_slice(...)

```python
maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
```

**Verification:**
```python
assert not isinstance(maybe_slice, slice)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(maybe_slice, indices)
```

### Step 9: target[indices]

```python
target[indices]
```

### Step 10: target[maybe_slice]

```python
target[maybe_slice]
```

### Step 11: target[indices]

```python
target[indices]
```

### Step 12: target[maybe_slice]

```python
target[maybe_slice]
```


## Complete Example

```python
# Workflow
target = np.arange(100)
indices = np.array([97, 98, 99, 100], dtype=np.intp)
maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
assert not isinstance(maybe_slice, slice)
tm.assert_numpy_array_equal(maybe_slice, indices)
msg = 'index 100 is out of bounds for axis (0|1) with size 100'
with pytest.raises(IndexError, match=msg):
    target[indices]
with pytest.raises(IndexError, match=msg):
    target[maybe_slice]
indices = np.array([100, 99, 98, 97], dtype=np.intp)
maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
assert not isinstance(maybe_slice, slice)
tm.assert_numpy_array_equal(maybe_slice, indices)
with pytest.raises(IndexError, match=msg):
    target[indices]
with pytest.raises(IndexError, match=msg):
    target[maybe_slice]
```

## Next Steps


---

*Source: test_lib.py:137 | Complexity: Advanced | Last updated: 2026-06-02*