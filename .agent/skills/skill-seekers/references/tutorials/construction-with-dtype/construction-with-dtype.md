# How To: Construction With Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construction with dtype

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(list('aabbca'), categories=list('abc'), ordered=False)
```

### Step 2: Assign result = Index(...)

```python
result = Index(np.array(ci), dtype='category')
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, ci, exact=True)
```

### Step 4: Assign result = Index(...)

```python
result = Index(np.array(ci).tolist(), dtype='category')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, ci, exact=True)
```

### Step 6: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(list('aabbca'), categories=list('cab'), ordered=False)
```

### Step 7: Assign result = Index.reorder_categories(...)

```python
result = Index(np.array(ci), dtype='category').reorder_categories(ci.categories)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, ci, exact=True)
```

### Step 9: Assign idx = Index(...)

```python
idx = Index(range(3))
```

### Step 10: Assign expected = CategoricalIndex(...)

```python
expected = CategoricalIndex([0, 1, 2], categories=idx, ordered=True)
```

### Step 11: Assign result = CategoricalIndex(...)

```python
result = CategoricalIndex(idx, categories=idx, ordered=True)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```


## Complete Example

```python
# Workflow
ci = CategoricalIndex(list('aabbca'), categories=list('abc'), ordered=False)
result = Index(np.array(ci), dtype='category')
tm.assert_index_equal(result, ci, exact=True)
result = Index(np.array(ci).tolist(), dtype='category')
tm.assert_index_equal(result, ci, exact=True)
ci = CategoricalIndex(list('aabbca'), categories=list('cab'), ordered=False)
result = Index(np.array(ci), dtype='category').reorder_categories(ci.categories)
tm.assert_index_equal(result, ci, exact=True)
idx = Index(range(3))
expected = CategoricalIndex([0, 1, 2], categories=idx, ordered=True)
result = CategoricalIndex(idx, categories=idx, ordered=True)
tm.assert_index_equal(result, expected, exact=True)
```

## Next Steps


---

*Source: test_constructors.py:94 | Complexity: Advanced | Last updated: 2026-06-02*