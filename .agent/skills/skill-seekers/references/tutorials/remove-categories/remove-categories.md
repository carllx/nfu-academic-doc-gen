# How To: Remove Categories

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test remove categories

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
new = Categorical(['a', 'b', np.nan, 'a'], categories=['a', 'b'], ordered=True)
```

### Step 4: Assign res = cat.remove_categories(...)

```python
res = cat.remove_categories('c')
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(cat, old)
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, new)
```

### Step 7: Assign res = cat.remove_categories(...)

```python
res = cat.remove_categories(['c'])
```

### Step 8: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(cat, old)
```

### Step 9: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, new)
```


## Complete Example

```python
# Workflow
cat = Categorical(['a', 'b', 'c', 'a'], ordered=True)
old = cat.copy()
new = Categorical(['a', 'b', np.nan, 'a'], categories=['a', 'b'], ordered=True)
res = cat.remove_categories('c')
tm.assert_categorical_equal(cat, old)
tm.assert_categorical_equal(res, new)
res = cat.remove_categories(['c'])
tm.assert_categorical_equal(cat, old)
tm.assert_categorical_equal(res, new)
```

## Next Steps


---

*Source: test_api.py:330 | Complexity: Advanced | Last updated: 2026-06-02*