# How To: Unique Label Indices Intp

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unique label indices intp

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections.abc`
- `contextlib`
- `re`
- `struct`
- `tracemalloc`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`

**Setup Required:**
```python
# Fixtures: writable
```

## Step-by-Step Guide

### Step 1: Assign keys = np.array(...)

```python
keys = np.array([1, 2, 2, 2, 1, 3], dtype=np.intp)
```

### Step 2: Assign keys.flags.writeable = writable

```python
keys.flags.writeable = writable
```

### Step 3: Assign result = ht.unique_label_indices(...)

```python
result = ht.unique_label_indices(keys)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([0, 1, 5], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: writable

# Workflow
keys = np.array([1, 2, 2, 2, 1, 3], dtype=np.intp)
keys.flags.writeable = writable
result = ht.unique_label_indices(keys)
expected = np.array([0, 1, 5], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_hashtable.py:665 | Complexity: Intermediate | Last updated: 2026-06-02*