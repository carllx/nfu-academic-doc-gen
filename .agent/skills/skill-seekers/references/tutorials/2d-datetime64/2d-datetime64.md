# How To: 2D Datetime64

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 2d datetime64

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._testing`
- `pandas.core.algorithms`


## Step-by-Step Guide

### Step 1: Assign arr = value

```python
arr = np.random.default_rng(2).integers(11045376, 11360736, (5, 3)) * 100000000000
```

### Step 2: Assign arr = arr.view(...)

```python
arr = arr.view(dtype='datetime64[ns]')
```

### Step 3: Assign indexer = value

```python
indexer = [0, 2, -1, 1, -1]
```

### Step 4: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(arr, indexer, axis=0)
```

### Step 5: Assign expected = arr.take(...)

```python
expected = arr.take(indexer, axis=0)
```

### Step 6: Assign unknown = iNaT

```python
expected.view(np.int64)[[2, 4], :] = iNaT
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 8: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(arr, indexer, axis=0, fill_value=datetime(2007, 1, 1))
```

### Step 9: Assign expected = arr.take(...)

```python
expected = arr.take(indexer, axis=0)
```

### Step 10: Assign unknown = datetime(...)

```python
expected[[2, 4], :] = datetime(2007, 1, 1)
```

### Step 11: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 12: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(arr, indexer, axis=1)
```

### Step 13: Assign expected = arr.take(...)

```python
expected = arr.take(indexer, axis=1)
```

### Step 14: Assign unknown = iNaT

```python
expected.view(np.int64)[:, [2, 4]] = iNaT
```

### Step 15: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 16: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(arr, indexer, axis=1, fill_value=datetime(2007, 1, 1))
```

### Step 17: Assign expected = arr.take(...)

```python
expected = arr.take(indexer, axis=1)
```

### Step 18: Assign unknown = datetime(...)

```python
expected[:, [2, 4]] = datetime(2007, 1, 1)
```

### Step 19: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).integers(11045376, 11360736, (5, 3)) * 100000000000
arr = arr.view(dtype='datetime64[ns]')
indexer = [0, 2, -1, 1, -1]
result = algos.take_nd(arr, indexer, axis=0)
expected = arr.take(indexer, axis=0)
expected.view(np.int64)[[2, 4], :] = iNaT
tm.assert_almost_equal(result, expected)
result = algos.take_nd(arr, indexer, axis=0, fill_value=datetime(2007, 1, 1))
expected = arr.take(indexer, axis=0)
expected[[2, 4], :] = datetime(2007, 1, 1)
tm.assert_almost_equal(result, expected)
result = algos.take_nd(arr, indexer, axis=1)
expected = arr.take(indexer, axis=1)
expected.view(np.int64)[:, [2, 4]] = iNaT
tm.assert_almost_equal(result, expected)
result = algos.take_nd(arr, indexer, axis=1, fill_value=datetime(2007, 1, 1))
expected = arr.take(indexer, axis=1)
expected[:, [2, 4]] = datetime(2007, 1, 1)
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_take.py:184 | Complexity: Advanced | Last updated: 2026-06-02*