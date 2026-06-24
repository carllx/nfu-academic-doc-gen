# How To: Method Delegation

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test method delegation

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.arrays`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.api`


## Step-by-Step Guide

### Step 1: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(list('aabbca'), categories=list('cabdef'))
```

### Step 2: Assign result = ci.set_categories(...)

```python
result = ci.set_categories(list('cab'))
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, CategoricalIndex(list('aabbca'), categories=list('cab')))
```

### Step 4: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(list('aabbca'), categories=list('cab'))
```

### Step 5: Assign result = ci.rename_categories(...)

```python
result = ci.rename_categories(list('efg'))
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, CategoricalIndex(list('ffggef'), categories=list('efg')))
```

### Step 7: Assign result = ci.rename_categories(...)

```python
result = ci.rename_categories(lambda x: x.upper())
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, CategoricalIndex(list('AABBCA'), categories=list('CAB')))
```

### Step 9: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(list('aabbca'), categories=list('cab'))
```

### Step 10: Assign result = ci.add_categories(...)

```python
result = ci.add_categories(['d'])
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, CategoricalIndex(list('aabbca'), categories=list('cabd')))
```

### Step 12: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(list('aabbca'), categories=list('cab'))
```

### Step 13: Assign result = ci.remove_categories(...)

```python
result = ci.remove_categories(['c'])
```

### Step 14: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, CategoricalIndex(list('aabb') + [np.nan] + ['a'], categories=list('ab')))
```

### Step 15: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(list('aabbca'), categories=list('cabdef'))
```

### Step 16: Assign result = ci.as_unordered(...)

```python
result = ci.as_unordered()
```

### Step 17: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, ci)
```

### Step 18: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(list('aabbca'), categories=list('cabdef'))
```

### Step 19: Assign result = ci.as_ordered(...)

```python
result = ci.as_ordered()
```

### Step 20: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, CategoricalIndex(list('aabbca'), categories=list('cabdef'), ordered=True))
```

### Step 21: Assign msg = 'cannot use inplace with CategoricalIndex'

```python
msg = 'cannot use inplace with CategoricalIndex'
```

### Step 22: Call ci.set_categories()

```python
ci.set_categories(list('cab'), inplace=True)
```


## Complete Example

```python
# Workflow
ci = CategoricalIndex(list('aabbca'), categories=list('cabdef'))
result = ci.set_categories(list('cab'))
tm.assert_index_equal(result, CategoricalIndex(list('aabbca'), categories=list('cab')))
ci = CategoricalIndex(list('aabbca'), categories=list('cab'))
result = ci.rename_categories(list('efg'))
tm.assert_index_equal(result, CategoricalIndex(list('ffggef'), categories=list('efg')))
result = ci.rename_categories(lambda x: x.upper())
tm.assert_index_equal(result, CategoricalIndex(list('AABBCA'), categories=list('CAB')))
ci = CategoricalIndex(list('aabbca'), categories=list('cab'))
result = ci.add_categories(['d'])
tm.assert_index_equal(result, CategoricalIndex(list('aabbca'), categories=list('cabd')))
ci = CategoricalIndex(list('aabbca'), categories=list('cab'))
result = ci.remove_categories(['c'])
tm.assert_index_equal(result, CategoricalIndex(list('aabb') + [np.nan] + ['a'], categories=list('ab')))
ci = CategoricalIndex(list('aabbca'), categories=list('cabdef'))
result = ci.as_unordered()
tm.assert_index_equal(result, ci)
ci = CategoricalIndex(list('aabbca'), categories=list('cabdef'))
result = ci.as_ordered()
tm.assert_index_equal(result, CategoricalIndex(list('aabbca'), categories=list('cabdef'), ordered=True))
msg = 'cannot use inplace with CategoricalIndex'
with pytest.raises(ValueError, match=msg):
    ci.set_categories(list('cab'), inplace=True)
```

## Next Steps


---

*Source: test_category.py:330 | Complexity: Advanced | Last updated: 2026-06-02*