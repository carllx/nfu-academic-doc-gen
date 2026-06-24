# How To: Sort Values

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'b', 'a'], ordered=False)
```

**Verification:**
```python
assert cat1._codes is orig_codes
```

### Step 2: Call cat.sort_values()

```python
cat.sort_values()
```

### Step 3: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'c', 'b', 'd'], ordered=True)
```

### Step 4: Assign res = cat.sort_values(...)

```python
res = cat.sort_values()
```

### Step 5: Assign exp = np.array(...)

```python
exp = np.array(['a', 'b', 'c', 'd'], dtype=object)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res.__array__(), exp)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res.categories, cat.categories)
```

### Step 8: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'c', 'b', 'd'], categories=['a', 'b', 'c', 'd'], ordered=True)
```

### Step 9: Assign res = cat.sort_values(...)

```python
res = cat.sort_values()
```

### Step 10: Assign exp = np.array(...)

```python
exp = np.array(['a', 'b', 'c', 'd'], dtype=object)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res.__array__(), exp)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res.categories, cat.categories)
```

### Step 13: Assign res = cat.sort_values(...)

```python
res = cat.sort_values(ascending=False)
```

### Step 14: Assign exp = np.array(...)

```python
exp = np.array(['d', 'c', 'b', 'a'], dtype=object)
```

### Step 15: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res.__array__(), exp)
```

### Step 16: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res.categories, cat.categories)
```

### Step 17: Assign cat1 = cat.copy(...)

```python
cat1 = cat.copy()
```

### Step 18: Assign orig_codes = value

```python
orig_codes = cat1._codes
```

### Step 19: Call cat1.sort_values()

```python
cat1.sort_values(inplace=True)
```

**Verification:**
```python
assert cat1._codes is orig_codes
```

### Step 20: Assign exp = np.array(...)

```python
exp = np.array(['a', 'b', 'c', 'd'], dtype=object)
```

### Step 21: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(cat1.__array__(), exp)
```

### Step 22: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res.categories, cat.categories)
```

### Step 23: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'c', 'c', 'b', 'd'], ordered=True)
```

### Step 24: Assign res = cat.sort_values(...)

```python
res = cat.sort_values(ascending=False)
```

### Step 25: Assign exp_val = np.array(...)

```python
exp_val = np.array(['d', 'c', 'c', 'b', 'a'], dtype=object)
```

### Step 26: Assign exp_categories = Index(...)

```python
exp_categories = Index(['a', 'b', 'c', 'd'])
```

### Step 27: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res.__array__(), exp_val)
```

### Step 28: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res.categories, exp_categories)
```


## Complete Example

```python
# Workflow
cat = Categorical(['a', 'b', 'b', 'a'], ordered=False)
cat.sort_values()
cat = Categorical(['a', 'c', 'b', 'd'], ordered=True)
res = cat.sort_values()
exp = np.array(['a', 'b', 'c', 'd'], dtype=object)
tm.assert_numpy_array_equal(res.__array__(), exp)
tm.assert_index_equal(res.categories, cat.categories)
cat = Categorical(['a', 'c', 'b', 'd'], categories=['a', 'b', 'c', 'd'], ordered=True)
res = cat.sort_values()
exp = np.array(['a', 'b', 'c', 'd'], dtype=object)
tm.assert_numpy_array_equal(res.__array__(), exp)
tm.assert_index_equal(res.categories, cat.categories)
res = cat.sort_values(ascending=False)
exp = np.array(['d', 'c', 'b', 'a'], dtype=object)
tm.assert_numpy_array_equal(res.__array__(), exp)
tm.assert_index_equal(res.categories, cat.categories)
cat1 = cat.copy()
orig_codes = cat1._codes
cat1.sort_values(inplace=True)
assert cat1._codes is orig_codes
exp = np.array(['a', 'b', 'c', 'd'], dtype=object)
tm.assert_numpy_array_equal(cat1.__array__(), exp)
tm.assert_index_equal(res.categories, cat.categories)
cat = Categorical(['a', 'c', 'c', 'b', 'd'], ordered=True)
res = cat.sort_values(ascending=False)
exp_val = np.array(['d', 'c', 'c', 'b', 'a'], dtype=object)
exp_categories = Index(['a', 'b', 'c', 'd'])
tm.assert_numpy_array_equal(res.__array__(), exp_val)
tm.assert_index_equal(res.categories, exp_categories)
```

## Next Steps


---

*Source: test_sorting.py:43 | Complexity: Advanced | Last updated: 2026-06-02*