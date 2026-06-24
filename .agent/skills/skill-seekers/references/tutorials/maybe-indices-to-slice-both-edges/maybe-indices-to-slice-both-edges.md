# How To: Maybe Indices To Slice Both Edges

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test maybe indices to slice both edges

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pickle`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: step
```

## Step-by-Step Guide

### Step 1: Assign target = np.arange(...)

```python
target = np.arange(10)
```

**Verification:**
```python
assert isinstance(maybe_slice, slice)
```

### Step 2: Assign indices = np.arange(...)

```python
indices = np.arange(0, 9, step, dtype=np.intp)
```

**Verification:**
```python
assert isinstance(maybe_slice, slice)
```

### Step 3: Assign maybe_slice = lib.maybe_indices_to_slice(...)

```python
maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
```

**Verification:**
```python
assert isinstance(maybe_slice, slice)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
```

### Step 5: Assign indices = value

```python
indices = indices[::-1]
```

### Step 6: Assign maybe_slice = lib.maybe_indices_to_slice(...)

```python
maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
```

**Verification:**
```python
assert isinstance(maybe_slice, slice)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
```


## Complete Example

```python
# Setup
# Fixtures: step

# Workflow
target = np.arange(10)
indices = np.arange(0, 9, step, dtype=np.intp)
maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
assert isinstance(maybe_slice, slice)
tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
indices = indices[::-1]
maybe_slice = lib.maybe_indices_to_slice(indices, len(target))
assert isinstance(maybe_slice, slice)
tm.assert_numpy_array_equal(target[indices], target[maybe_slice])
```

## Next Steps


---

*Source: test_lib.py:177 | Complexity: Intermediate | Last updated: 2026-06-02*