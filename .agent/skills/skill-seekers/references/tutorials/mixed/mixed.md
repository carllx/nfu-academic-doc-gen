# How To: Mixed

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mixed

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

### Step 1: Assign x = Series(...)

```python
x = Series(['A', 'A', np.nan, 'B', 3.14, np.inf])
```

### Step 2: Assign unknown = algos.factorize(...)

```python
codes, uniques = algos.factorize(x)
```

### Step 3: Assign exp = np.array(...)

```python
exp = np.array([0, 0, -1, 1, 2, 3], dtype=np.intp)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(codes, exp)
```

### Step 5: Assign exp = Index(...)

```python
exp = Index(['A', 'B', 3.14, np.inf])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(uniques, exp)
```

### Step 7: Assign unknown = algos.factorize(...)

```python
codes, uniques = algos.factorize(x, sort=True)
```

### Step 8: Assign exp = np.array(...)

```python
exp = np.array([2, 2, -1, 3, 0, 1], dtype=np.intp)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(codes, exp)
```

### Step 10: Assign exp = Index(...)

```python
exp = Index([3.14, np.inf, 'A', 'B'])
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(uniques, exp)
```


## Complete Example

```python
# Workflow
x = Series(['A', 'A', np.nan, 'B', 3.14, np.inf])
codes, uniques = algos.factorize(x)
exp = np.array([0, 0, -1, 1, 2, 3], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
exp = Index(['A', 'B', 3.14, np.inf])
tm.assert_index_equal(uniques, exp)
codes, uniques = algos.factorize(x, sort=True)
exp = np.array([2, 2, -1, 3, 0, 1], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
exp = Index([3.14, np.inf, 'A', 'B'])
tm.assert_index_equal(uniques, exp)
```

## Next Steps


---

*Source: test_algos.py:151 | Complexity: Advanced | Last updated: 2026-06-02*