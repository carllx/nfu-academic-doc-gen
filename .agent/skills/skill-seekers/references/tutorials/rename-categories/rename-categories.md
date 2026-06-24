# How To: Rename Categories

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename categories

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.categorical`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'c', 'a'])
```

### Step 2: Assign res = cat.rename_categories(...)

```python
res = cat.rename_categories([1, 2, 3])
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res.__array__(), np.array([1, 2, 3, 1], dtype=np.int64))
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res.categories, Index([1, 2, 3]))
```

### Step 5: Assign exp_cat = np.array(...)

```python
exp_cat = np.array(['a', 'b', 'c', 'a'], dtype=np.object_)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(cat.__array__(), exp_cat)
```

### Step 7: Assign exp_cat = Index(...)

```python
exp_cat = Index(['a', 'b', 'c'])
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(cat.categories, exp_cat)
```

### Step 9: Assign result = cat.rename_categories(...)

```python
result = cat.rename_categories(lambda x: x.upper())
```

### Step 10: Assign expected = Categorical(...)

```python
expected = Categorical(['A', 'B', 'C', 'A'])
```

### Step 11: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```


## Complete Example

```python
# Workflow
cat = Categorical(['a', 'b', 'c', 'a'])
res = cat.rename_categories([1, 2, 3])
tm.assert_numpy_array_equal(res.__array__(), np.array([1, 2, 3, 1], dtype=np.int64))
tm.assert_index_equal(res.categories, Index([1, 2, 3]))
exp_cat = np.array(['a', 'b', 'c', 'a'], dtype=np.object_)
tm.assert_numpy_array_equal(cat.__array__(), exp_cat)
exp_cat = Index(['a', 'b', 'c'])
tm.assert_index_equal(cat.categories, exp_cat)
result = cat.rename_categories(lambda x: x.upper())
expected = Categorical(['A', 'B', 'C', 'A'])
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_api.py:67 | Complexity: Advanced | Last updated: 2026-06-02*