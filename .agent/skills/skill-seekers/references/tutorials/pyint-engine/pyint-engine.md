# How To: Pyint Engine

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pyint engine

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign N = 5

```python
N = 5
```

**Verification:**
```python
assert index.get_loc(key_value) == idx
```

### Step 2: Assign keys = value

```python
keys = [tuple(arr) for arr in [[0] * 10 * N, [1] * 10 * N, [2] * 10 * N, [np.nan] * N + [2] * 9 * N, [0] * N + [2] * 9 * N, [np.nan] * N + [2] * 8 * N + [0] * N]]
```

### Step 3: Assign idces = range(...)

```python
idces = range(len(keys))
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([-1] + list(idces), dtype=np.intp)
```

### Step 5: Assign missing = tuple(...)

```python
missing = tuple([0, 1] * 5 * N)
```

### Step 6: Assign result = index.get_indexer(...)

```python
result = index.get_indexer([missing] + [keys[i] for i in idces])
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 8: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(keys)
```

**Verification:**
```python
assert index.get_loc(key_value) == idx
```

### Step 9: Assign expected = np.arange(...)

```python
expected = np.arange(idx + 1, dtype=np.intp)
```

### Step 10: Assign result = index.get_indexer(...)

```python
result = index.get_indexer([keys[i] for i in expected])
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
N = 5
keys = [tuple(arr) for arr in [[0] * 10 * N, [1] * 10 * N, [2] * 10 * N, [np.nan] * N + [2] * 9 * N, [0] * N + [2] * 9 * N, [np.nan] * N + [2] * 8 * N + [0] * N]]
for idx, key_value in enumerate(keys):
    index = MultiIndex.from_tuples(keys)
    assert index.get_loc(key_value) == idx
    expected = np.arange(idx + 1, dtype=np.intp)
    result = index.get_indexer([keys[i] for i in expected])
    tm.assert_numpy_array_equal(result, expected)
idces = range(len(keys))
expected = np.array([-1] + list(idces), dtype=np.intp)
missing = tuple([0, 1] * 5 * N)
result = index.get_indexer([missing] + [keys[i] for i in idces])
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:926 | Complexity: Advanced | Last updated: 2026-06-02*