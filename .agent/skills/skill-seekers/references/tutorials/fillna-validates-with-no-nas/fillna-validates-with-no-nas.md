# How To: Fillna Validates With No Nas

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna validates with no nas

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex([2, 3, 3])
```

### Step 2: Assign cat = value

```python
cat = ci._data
```

### Step 3: Assign msg = 'Cannot setitem on a Categorical with a new category'

```python
msg = 'Cannot setitem on a Categorical with a new category'
```

### Step 4: Assign res = ci.fillna(...)

```python
res = ci.fillna(False)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, ci)
```

### Step 6: Call cat.fillna()

```python
cat.fillna(False)
```


## Complete Example

```python
# Workflow
ci = CategoricalIndex([2, 3, 3])
cat = ci._data
msg = 'Cannot setitem on a Categorical with a new category'
res = ci.fillna(False)
tm.assert_index_equal(res, ci)
with pytest.raises(TypeError, match=msg):
    cat.fillna(False)
```

## Next Steps


---

*Source: test_fillna.py:42 | Complexity: Intermediate | Last updated: 2026-06-02*