# How To: Get Indexer Non Unique Wrong Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get indexer non unique wrong dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: ldtype, rdtype
```

## Step-by-Step Guide

### Step 1: Assign vals = np.tile(...)

```python
vals = np.tile(3600 * 10 ** 9 * np.arange(3, dtype=np.int64), 2)
```

### Step 2: Assign left = construct(...)

```python
left = construct(ldtype)
```

### Step 3: Assign right = construct(...)

```python
right = construct(rdtype)
```

### Step 4: Assign result = left.get_indexer_non_unique(...)

```python
result = left.get_indexer_non_unique(right)
```

### Step 5: Assign ex1 = np.array(...)

```python
ex1 = np.array([0, 3, 1, 4, 2, 5] * 2, dtype=np.intp)
```

### Step 6: Assign ex2 = np.array(...)

```python
ex2 = np.array([], dtype=np.intp)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result[0], ex1)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result[1], ex2)
```

### Step 9: Assign no_matches = np.array(...)

```python
no_matches = np.array([-1] * 6, dtype=np.intp)
```

### Step 10: Assign missing = np.arange(...)

```python
missing = np.arange(6, dtype=np.intp)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result[0], no_matches)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result[1], missing)
```


## Complete Example

```python
# Setup
# Fixtures: ldtype, rdtype

# Workflow
vals = np.tile(3600 * 10 ** 9 * np.arange(3, dtype=np.int64), 2)

def construct(dtype):
    if dtype is dtlike_dtypes[-1]:
        return DatetimeIndex(vals).astype(dtype)
    return Index(vals, dtype=dtype)
left = construct(ldtype)
right = construct(rdtype)
result = left.get_indexer_non_unique(right)
if ldtype is rdtype:
    ex1 = np.array([0, 3, 1, 4, 2, 5] * 2, dtype=np.intp)
    ex2 = np.array([], dtype=np.intp)
    tm.assert_numpy_array_equal(result[0], ex1)
    tm.assert_numpy_array_equal(result[1], ex2)
else:
    no_matches = np.array([-1] * 6, dtype=np.intp)
    missing = np.arange(6, dtype=np.intp)
    tm.assert_numpy_array_equal(result[0], no_matches)
    tm.assert_numpy_array_equal(result[1], missing)
```

## Next Steps


---

*Source: test_indexing.py:21 | Complexity: Advanced | Last updated: 2026-06-02*