# How To: Series Factorize Use Na Sentinel False

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series factorize use na sentinel false

## Prerequisites

**Required Modules:**
- `datetime`
- `struct`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.arrays`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign values = np.array(...)

```python
values = np.array([1, 2, 1, np.nan])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(values)
```

### Step 3: Assign unknown = ser.factorize(...)

```python
codes, uniques = ser.factorize(use_na_sentinel=False)
```

### Step 4: Assign expected_codes = np.array(...)

```python
expected_codes = np.array([0, 1, 0, 2], dtype=np.intp)
```

### Step 5: Assign expected_uniques = Index(...)

```python
expected_uniques = Index([1.0, 2.0, np.nan])
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(codes, expected_codes)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(uniques, expected_uniques)
```


## Complete Example

```python
# Workflow
values = np.array([1, 2, 1, np.nan])
ser = Series(values)
codes, uniques = ser.factorize(use_na_sentinel=False)
expected_codes = np.array([0, 1, 0, 2], dtype=np.intp)
expected_uniques = Index([1.0, 2.0, np.nan])
tm.assert_numpy_array_equal(codes, expected_codes)
tm.assert_index_equal(uniques, expected_uniques)
```

## Next Steps


---

*Source: test_algos.py:100 | Complexity: Intermediate | Last updated: 2026-06-02*