# How To: 2D Float32

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 2d float32

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._testing`
- `pandas.core.algorithms`


## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.standard_normal.astype(...)

```python
arr = np.random.default_rng(2).standard_normal((4, 3)).astype(np.float32)
```

### Step 2: Assign indexer = value

```python
indexer = [0, 2, -1, 1, -1]
```

### Step 3: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(arr, indexer, axis=0)
```

### Step 4: Assign expected = arr.take(...)

```python
expected = arr.take(indexer, axis=0)
```

### Step 5: Assign unknown = value

```python
expected[[2, 4], :] = np.nan
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 7: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(arr, indexer, axis=1)
```

### Step 8: Assign expected = arr.take(...)

```python
expected = arr.take(indexer, axis=1)
```

### Step 9: Assign unknown = value

```python
expected[:, [2, 4]] = np.nan
```

### Step 10: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).standard_normal((4, 3)).astype(np.float32)
indexer = [0, 2, -1, 1, -1]
result = algos.take_nd(arr, indexer, axis=0)
expected = arr.take(indexer, axis=0)
expected[[2, 4], :] = np.nan
tm.assert_almost_equal(result, expected)
result = algos.take_nd(arr, indexer, axis=1)
expected = arr.take(indexer, axis=1)
expected[:, [2, 4]] = np.nan
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_take.py:167 | Complexity: Advanced | Last updated: 2026-06-02*