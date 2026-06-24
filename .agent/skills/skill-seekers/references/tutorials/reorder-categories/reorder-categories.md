# How To: Reorder Categories

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reorder categories

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
new = Categorical(['a', 'b', 'c', 'a'], categories=['c', 'b', 'a'], ordered=True)
```

### Step 4: Assign res = cat.reorder_categories(...)

```python
res = cat.reorder_categories(['c', 'b', 'a'])
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(cat, old)
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, new)
```


## Complete Example

```python
# Workflow
cat = Categorical(['a', 'b', 'c', 'a'], ordered=True)
old = cat.copy()
new = Categorical(['a', 'b', 'c', 'a'], categories=['c', 'b', 'a'], ordered=True)
res = cat.reorder_categories(['c', 'b', 'a'])
tm.assert_categorical_equal(cat, old)
tm.assert_categorical_equal(res, new)
```

## Next Steps


---

*Source: test_api.py:132 | Complexity: Intermediate | Last updated: 2026-06-02*