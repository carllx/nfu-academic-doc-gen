# How To: Where Non Categories

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where non categories

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(['a', 'b', 'c', 'd'])
```

### Step 2: Assign mask = np.array(...)

```python
mask = np.array([True, False, True, False])
```

### Step 3: Assign result = ci.where(...)

```python
result = ci.where(mask, 2)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index(['a', 2, 'c', 2], dtype=object)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign msg = 'Cannot setitem on a Categorical with a new category'

```python
msg = 'Cannot setitem on a Categorical with a new category'
```

### Step 7: Call ci._data._where()

```python
ci._data._where(mask, 2)
```


## Complete Example

```python
# Workflow
ci = CategoricalIndex(['a', 'b', 'c', 'd'])
mask = np.array([True, False, True, False])
result = ci.where(mask, 2)
expected = Index(['a', 2, 'c', 2], dtype=object)
tm.assert_index_equal(result, expected)
msg = 'Cannot setitem on a Categorical with a new category'
with pytest.raises(TypeError, match=msg):
    ci._data._where(mask, 2)
```

## Next Steps


---

*Source: test_indexing.py:324 | Complexity: Intermediate | Last updated: 2026-06-02*