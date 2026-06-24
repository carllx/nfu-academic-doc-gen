# How To: Get Indexer Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer array

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([Timestamp('1999-12-31 00:00:00'), Timestamp('2000-12-31 00:00:00')], dtype=object)
```

### Step 2: Assign cats = value

```python
cats = [Timestamp('1999-12-31 00:00:00'), Timestamp('2000-12-31 00:00:00')]
```

### Step 3: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(cats, categories=cats, ordered=False, dtype='category')
```

### Step 4: Assign result = ci.get_indexer(...)

```python
result = ci.get_indexer(arr)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([0, 1], dtype='intp')
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.array([Timestamp('1999-12-31 00:00:00'), Timestamp('2000-12-31 00:00:00')], dtype=object)
cats = [Timestamp('1999-12-31 00:00:00'), Timestamp('2000-12-31 00:00:00')]
ci = CategoricalIndex(cats, categories=cats, ordered=False, dtype='category')
result = ci.get_indexer(arr)
expected = np.array([0, 1], dtype='intp')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:270 | Complexity: Intermediate | Last updated: 2026-06-02*