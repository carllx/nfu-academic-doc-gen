# How To: Fillna Categorical

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna categorical

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = CategoricalIndex(...)

```python
idx = CategoricalIndex([1.0, np.nan, 3.0, 1.0], name='x')
```

### Step 2: Assign exp = CategoricalIndex(...)

```python
exp = CategoricalIndex([1.0, 1.0, 3.0, 1.0], name='x')
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.fillna(1.0), exp)
```

### Step 4: Assign cat = value

```python
cat = idx._data
```

### Step 5: Assign msg = 'Cannot setitem on a Categorical with a new category'

```python
msg = 'Cannot setitem on a Categorical with a new category'
```

### Step 6: Assign result = idx.fillna(...)

```python
result = idx.fillna(2.0)
```

### Step 7: Assign expected = idx.astype.fillna(...)

```python
expected = idx.astype(object).fillna(2.0)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Call cat.fillna()

```python
cat.fillna(2.0)
```


## Complete Example

```python
# Workflow
idx = CategoricalIndex([1.0, np.nan, 3.0, 1.0], name='x')
exp = CategoricalIndex([1.0, 1.0, 3.0, 1.0], name='x')
tm.assert_index_equal(idx.fillna(1.0), exp)
cat = idx._data
msg = 'Cannot setitem on a Categorical with a new category'
with pytest.raises(TypeError, match=msg):
    cat.fillna(2.0)
result = idx.fillna(2.0)
expected = idx.astype(object).fillna(2.0)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_fillna.py:9 | Complexity: Advanced | Last updated: 2026-06-02*