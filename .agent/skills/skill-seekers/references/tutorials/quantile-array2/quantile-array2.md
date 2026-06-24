# How To: Quantile Array2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quantile array2

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.integers(...)

```python
arr = np.random.default_rng(2).integers(0, 5, size=(10, 3), dtype=np.int64)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(arr, columns=list('ABC'))
```

### Step 3: Assign result = df.groupby.quantile(...)

```python
result = df.groupby('A').quantile([0.3, 0.7])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'B': [2.0, 2.0, 2.3, 2.7, 0.3, 0.7, 3.2, 4.0, 0.3, 0.7], 'C': [1.0, 1.0, 1.9, 3.0999999999999996, 0.3, 0.7, 2.6, 3.0, 1.2, 2.8]}, index=pd.MultiIndex.from_product([[0, 1, 2, 3, 4], [0.3, 0.7]], names=['A', None]))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).integers(0, 5, size=(10, 3), dtype=np.int64)
df = DataFrame(arr, columns=list('ABC'))
result = df.groupby('A').quantile([0.3, 0.7])
expected = DataFrame({'B': [2.0, 2.0, 2.3, 2.7, 0.3, 0.7, 3.2, 4.0, 0.3, 0.7], 'C': [1.0, 1.0, 1.9, 3.0999999999999996, 0.3, 0.7, 2.6, 3.0, 1.2, 2.8]}, index=pd.MultiIndex.from_product([[0, 1, 2, 3, 4], [0.3, 0.7]], names=['A', None]))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_quantile.py:94 | Complexity: Intermediate | Last updated: 2026-06-02*