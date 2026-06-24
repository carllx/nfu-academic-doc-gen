# How To: Unique Label Indices

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unique label indices

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign a = np.random.default_rng.integers.astype(...)

```python
a = np.random.default_rng(2).integers(1, 1 << 10, 1 << 15).astype(np.intp)
```

### Step 2: Assign left = ht.unique_label_indices(...)

```python
left = ht.unique_label_indices(a)
```

### Step 3: Assign right = value

```python
right = np.unique(a, return_index=True)[1]
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(left, right, check_dtype=False)
```

### Step 5: Assign unknown = value

```python
a[np.random.default_rng(2).choice(len(a), 10)] = -1
```

### Step 6: Assign left = ht.unique_label_indices(...)

```python
left = ht.unique_label_indices(a)
```

### Step 7: Assign right = value

```python
right = np.unique(a, return_index=True)[1][1:]
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(left, right, check_dtype=False)
```


## Complete Example

```python
# Workflow
a = np.random.default_rng(2).integers(1, 1 << 10, 1 << 15).astype(np.intp)
left = ht.unique_label_indices(a)
right = np.unique(a, return_index=True)[1]
tm.assert_numpy_array_equal(left, right, check_dtype=False)
a[np.random.default_rng(2).choice(len(a), 10)] = -1
left = ht.unique_label_indices(a)
right = np.unique(a, return_index=True)[1][1:]
tm.assert_numpy_array_equal(left, right, check_dtype=False)
```

## Next Steps


---

*Source: test_hashtable.py:673 | Complexity: Advanced | Last updated: 2026-06-02*