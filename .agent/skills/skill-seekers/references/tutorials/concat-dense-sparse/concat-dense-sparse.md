# How To: Concat Dense Sparse

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat dense sparse

## Prerequisites

**Required Modules:**
- `collections`
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.extension.decimal`


## Step-by-Step Guide

### Step 1: Assign dtype = pd.SparseDtype(...)

```python
dtype = pd.SparseDtype(np.float64, None)
```

### Step 2: Assign a = Series(...)

```python
a = Series(pd.arrays.SparseArray([1, None]), dtype=dtype)
```

### Step 3: Assign b = Series(...)

```python
b = Series([1], dtype=float)
```

### Step 4: Assign expected = Series.astype(...)

```python
expected = Series(data=[1, None, 1], index=[0, 1, 0]).astype(dtype)
```

### Step 5: Assign result = concat(...)

```python
result = concat([a, b], axis=0)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
dtype = pd.SparseDtype(np.float64, None)
a = Series(pd.arrays.SparseArray([1, None]), dtype=dtype)
b = Series([1], dtype=float)
expected = Series(data=[1, None, 1], index=[0, 1, 0]).astype(dtype)
result = concat([a, b], axis=0)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_concat.py:590 | Complexity: Intermediate | Last updated: 2026-06-02*