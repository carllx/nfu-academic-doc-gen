# How To: Add Categories

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add categories

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
cat = Categorical(['a', 'b', 'c', 'a'], ordered=True)
```

### Step 2: Assign old = cat.copy(...)

```python
old = cat.copy()
```

### Step 3: Assign new = Categorical(...)

```python
new = Categorical(['a', 'b', 'c', 'a'], categories=['a', 'b', 'c', 'd'], ordered=True)
```

### Step 4: Assign res = cat.add_categories(...)

```python
res = cat.add_categories('d')
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(cat, old)
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, new)
```

### Step 7: Assign res = cat.add_categories(...)

```python
res = cat.add_categories(['d'])
```

### Step 8: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(cat, old)
```

### Step 9: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, new)
```

### Step 10: Assign cat = Categorical(...)

```python
cat = Categorical(list('abc'), ordered=True)
```

### Step 11: Assign expected = Categorical(...)

```python
expected = Categorical(list('abc'), categories=list('abcde'), ordered=True)
```

### Step 12: Assign res = cat.add_categories(...)

```python
res = cat.add_categories(Series(['d', 'e']))
```

### Step 13: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, expected)
```

### Step 14: Assign res = cat.add_categories(...)

```python
res = cat.add_categories(np.array(['d', 'e']))
```

### Step 15: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, expected)
```

### Step 16: Assign res = cat.add_categories(...)

```python
res = cat.add_categories(Index(['d', 'e']))
```

### Step 17: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, expected)
```

### Step 18: Assign res = cat.add_categories(...)

```python
res = cat.add_categories(['d', 'e'])
```

### Step 19: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, expected)
```


## Complete Example

```python
# Workflow
cat = Categorical(['a', 'b', 'c', 'a'], ordered=True)
old = cat.copy()
new = Categorical(['a', 'b', 'c', 'a'], categories=['a', 'b', 'c', 'd'], ordered=True)
res = cat.add_categories('d')
tm.assert_categorical_equal(cat, old)
tm.assert_categorical_equal(res, new)
res = cat.add_categories(['d'])
tm.assert_categorical_equal(cat, old)
tm.assert_categorical_equal(res, new)
cat = Categorical(list('abc'), ordered=True)
expected = Categorical(list('abc'), categories=list('abcde'), ordered=True)
res = cat.add_categories(Series(['d', 'e']))
tm.assert_categorical_equal(res, expected)
res = cat.add_categories(np.array(['d', 'e']))
tm.assert_categorical_equal(res, expected)
res = cat.add_categories(Index(['d', 'e']))
tm.assert_categorical_equal(res, expected)
res = cat.add_categories(['d', 'e'])
tm.assert_categorical_equal(res, expected)
```

## Next Steps


---

*Source: test_api.py:159 | Complexity: Advanced | Last updated: 2026-06-02*