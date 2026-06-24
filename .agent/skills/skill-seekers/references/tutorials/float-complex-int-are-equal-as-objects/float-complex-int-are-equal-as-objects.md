# How To: Float Complex Int Are Equal As Objects

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test float complex int are equal as objects

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

### Step 1: Assign values = value

```python
values = ['a', 5, 5.0, 5.0 + 0j]
```

### Step 2: Assign comps = list(...)

```python
comps = list(range(129))
```

### Step 3: Assign result = isin(...)

```python
result = isin(np.array(values, dtype=object), np.asarray(comps))
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([False, True, True, True], dtype=np.bool_)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
values = ['a', 5, 5.0, 5.0 + 0j]
comps = list(range(129))
result = isin(np.array(values, dtype=object), np.asarray(comps))
expected = np.array([False, True, True, True], dtype=np.bool_)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_hashtable.py:743 | Complexity: Intermediate | Last updated: 2026-06-02*