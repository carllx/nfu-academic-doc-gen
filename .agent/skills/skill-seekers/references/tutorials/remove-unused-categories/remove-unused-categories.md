# How To: Remove Unused Categories

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test remove unused categories

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

### Step 1: Assign c = Categorical(...)

```python
c = Categorical(['a', 'b', 'c', 'd', 'a'], categories=['a', 'b', 'c', 'd', 'e'])
```

**Verification:**
```python
assert out.tolist() == val
```

### Step 2: Assign exp_categories_all = Index(...)

```python
exp_categories_all = Index(['a', 'b', 'c', 'd', 'e'])
```

**Verification:**
```python
assert out.tolist() == val.tolist()
```

### Step 3: Assign exp_categories_dropped = Index(...)

```python
exp_categories_dropped = Index(['a', 'b', 'c', 'd'])
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(c.categories, exp_categories_all)
```

### Step 5: Assign res = c.remove_unused_categories(...)

```python
res = c.remove_unused_categories()
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res.categories, exp_categories_dropped)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(c.categories, exp_categories_all)
```

### Step 8: Assign c = Categorical(...)

```python
c = Categorical(['a', 'b', 'c', np.nan], categories=['a', 'b', 'c', 'd', 'e'])
```

### Step 9: Assign res = c.remove_unused_categories(...)

```python
res = c.remove_unused_categories()
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res.categories, Index(np.array(['a', 'b', 'c'])))
```

### Step 11: Assign exp_codes = np.array(...)

```python
exp_codes = np.array([0, 1, 2, -1], dtype=np.int8)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res.codes, exp_codes)
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(c.categories, exp_categories_all)
```

### Step 14: Assign val = value

```python
val = ['F', np.nan, 'D', 'B', 'D', 'F', np.nan]
```

### Step 15: Assign cat = Categorical(...)

```python
cat = Categorical(values=val, categories=list('ABCDEFG'))
```

### Step 16: Assign out = cat.remove_unused_categories(...)

```python
out = cat.remove_unused_categories()
```

### Step 17: Call tm.assert_index_equal()

```python
tm.assert_index_equal(out.categories, Index(['B', 'D', 'F']))
```

### Step 18: Assign exp_codes = np.array(...)

```python
exp_codes = np.array([2, -1, 1, 0, 1, 2, -1], dtype=np.int8)
```

### Step 19: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(out.codes, exp_codes)
```

**Verification:**
```python
assert out.tolist() == val
```

### Step 20: Assign alpha = list(...)

```python
alpha = list('abcdefghijklmnopqrstuvwxyz')
```

### Step 21: Assign val = np.random.default_rng.choice.astype(...)

```python
val = np.random.default_rng(2).choice(alpha[::2], 10000).astype('object')
```

### Step 22: Assign unknown = value

```python
val[np.random.default_rng(2).choice(len(val), 100)] = np.nan
```

### Step 23: Assign cat = Categorical(...)

```python
cat = Categorical(values=val, categories=alpha)
```

### Step 24: Assign out = cat.remove_unused_categories(...)

```python
out = cat.remove_unused_categories()
```

**Verification:**
```python
assert out.tolist() == val.tolist()
```


## Complete Example

```python
# Workflow
c = Categorical(['a', 'b', 'c', 'd', 'a'], categories=['a', 'b', 'c', 'd', 'e'])
exp_categories_all = Index(['a', 'b', 'c', 'd', 'e'])
exp_categories_dropped = Index(['a', 'b', 'c', 'd'])
tm.assert_index_equal(c.categories, exp_categories_all)
res = c.remove_unused_categories()
tm.assert_index_equal(res.categories, exp_categories_dropped)
tm.assert_index_equal(c.categories, exp_categories_all)
c = Categorical(['a', 'b', 'c', np.nan], categories=['a', 'b', 'c', 'd', 'e'])
res = c.remove_unused_categories()
tm.assert_index_equal(res.categories, Index(np.array(['a', 'b', 'c'])))
exp_codes = np.array([0, 1, 2, -1], dtype=np.int8)
tm.assert_numpy_array_equal(res.codes, exp_codes)
tm.assert_index_equal(c.categories, exp_categories_all)
val = ['F', np.nan, 'D', 'B', 'D', 'F', np.nan]
cat = Categorical(values=val, categories=list('ABCDEFG'))
out = cat.remove_unused_categories()
tm.assert_index_equal(out.categories, Index(['B', 'D', 'F']))
exp_codes = np.array([2, -1, 1, 0, 1, 2, -1], dtype=np.int8)
tm.assert_numpy_array_equal(out.codes, exp_codes)
assert out.tolist() == val
alpha = list('abcdefghijklmnopqrstuvwxyz')
val = np.random.default_rng(2).choice(alpha[::2], 10000).astype('object')
val[np.random.default_rng(2).choice(len(val), 100)] = np.nan
cat = Categorical(values=val, categories=alpha)
out = cat.remove_unused_categories()
assert out.tolist() == val.tolist()
```

## Next Steps


---

*Source: test_api.py:351 | Complexity: Advanced | Last updated: 2026-06-02*