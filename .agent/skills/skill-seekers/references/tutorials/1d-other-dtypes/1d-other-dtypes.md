# How To: 1D Other Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 1d other dtypes

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
arr = np.random.default_rng(2).standard_normal(10).astype(np.float32)
```

### Step 2: Assign indexer = value

```python
indexer = [1, 2, 3, -1]
```

### Step 3: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(arr, indexer)
```

### Step 4: Assign expected = arr.take(...)

```python
expected = arr.take(indexer)
```

### Step 5: Assign unknown = value

```python
expected[-1] = np.nan
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).standard_normal(10).astype(np.float32)
indexer = [1, 2, 3, -1]
result = algos.take_nd(arr, indexer)
expected = arr.take(indexer)
expected[-1] = np.nan
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_take.py:117 | Complexity: Intermediate | Last updated: 2026-06-02*