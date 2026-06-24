# How To: Set Categories Private

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set categories private

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
cat = Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c', 'd'])
```

### Step 2: Call cat._set_categories()

```python
cat._set_categories(['a', 'c', 'd', 'e'])
```

### Step 3: Assign expected = Categorical(...)

```python
expected = Categorical(['a', 'c', 'd'], categories=list('acde'))
```

### Step 4: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(cat, expected)
```

### Step 5: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c', 'd'])
```

### Step 6: Call cat._set_categories()

```python
cat._set_categories(['a', 'c', 'd', 'e'], fastpath=True)
```

### Step 7: Assign expected = Categorical(...)

```python
expected = Categorical(['a', 'c', 'd'], categories=list('acde'))
```

### Step 8: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(cat, expected)
```


## Complete Example

```python
# Workflow
cat = Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c', 'd'])
cat._set_categories(['a', 'c', 'd', 'e'])
expected = Categorical(['a', 'c', 'd'], categories=list('acde'))
tm.assert_categorical_equal(cat, expected)
cat = Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c', 'd'])
cat._set_categories(['a', 'c', 'd', 'e'], fastpath=True)
expected = Categorical(['a', 'c', 'd'], categories=list('acde'))
tm.assert_categorical_equal(cat, expected)
```

## Next Steps


---

*Source: test_api.py:318 | Complexity: Advanced | Last updated: 2026-06-02*