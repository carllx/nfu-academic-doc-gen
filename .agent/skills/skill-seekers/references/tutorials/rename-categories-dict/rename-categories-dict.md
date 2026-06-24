# How To: Rename Categories Dict

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename categories dict

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
cat = Categorical(['a', 'b', 'c', 'd'])
```

### Step 2: Assign res = cat.rename_categories(...)

```python
res = cat.rename_categories({'a': 4, 'b': 3, 'c': 2, 'd': 1})
```

### Step 3: Assign expected = Index(...)

```python
expected = Index([4, 3, 2, 1])
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res.categories, expected)
```

### Step 5: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'c', 'd'])
```

### Step 6: Assign res = cat.rename_categories(...)

```python
res = cat.rename_categories({'a': 1, 'c': 3})
```

### Step 7: Assign expected = Index(...)

```python
expected = Index([1, 'b', 3, 'd'])
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res.categories, expected)
```

### Step 9: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'c', 'd'])
```

### Step 10: Assign res = cat.rename_categories(...)

```python
res = cat.rename_categories({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})
```

### Step 11: Assign expected = Index(...)

```python
expected = Index([1, 2, 3, 4])
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res.categories, expected)
```

### Step 13: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'c', 'd'])
```

### Step 14: Assign res = cat.rename_categories(...)

```python
res = cat.rename_categories({'f': 1, 'g': 3})
```

### Step 15: Assign expected = Index(...)

```python
expected = Index(['a', 'b', 'c', 'd'])
```

### Step 16: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res.categories, expected)
```


## Complete Example

```python
# Workflow
cat = Categorical(['a', 'b', 'c', 'd'])
res = cat.rename_categories({'a': 4, 'b': 3, 'c': 2, 'd': 1})
expected = Index([4, 3, 2, 1])
tm.assert_index_equal(res.categories, expected)
cat = Categorical(['a', 'b', 'c', 'd'])
res = cat.rename_categories({'a': 1, 'c': 3})
expected = Index([1, 'b', 3, 'd'])
tm.assert_index_equal(res.categories, expected)
cat = Categorical(['a', 'b', 'c', 'd'])
res = cat.rename_categories({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})
expected = Index([1, 2, 3, 4])
tm.assert_index_equal(res.categories, expected)
cat = Categorical(['a', 'b', 'c', 'd'])
res = cat.rename_categories({'f': 1, 'g': 3})
expected = Index(['a', 'b', 'c', 'd'])
tm.assert_index_equal(res.categories, expected)
```

## Next Steps


---

*Source: test_api.py:105 | Complexity: Advanced | Last updated: 2026-06-02*