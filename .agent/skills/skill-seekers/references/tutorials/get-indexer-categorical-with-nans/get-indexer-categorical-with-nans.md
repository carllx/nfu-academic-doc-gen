# How To: Get Indexer Categorical With Nans

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get indexer categorical with nans

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ii = IntervalIndex.from_breaks(...)

```python
ii = IntervalIndex.from_breaks(range(5))
```

### Step 2: Assign ii2 = ii.append(...)

```python
ii2 = ii.append(IntervalIndex([np.nan]))
```

### Step 3: Assign ci2 = CategoricalIndex(...)

```python
ci2 = CategoricalIndex(ii2)
```

### Step 4: Assign result = ii2.get_indexer(...)

```python
result = ii2.get_indexer(ci2)
```

### Step 5: Assign expected = np.arange(...)

```python
expected = np.arange(5, dtype=np.intp)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Assign result = unknown.get_indexer(...)

```python
result = ii2[1:].get_indexer(ci2[::-1])
```

### Step 8: Assign expected = np.array(...)

```python
expected = np.array([3, 2, 1, 0, -1], dtype=np.intp)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 10: Assign result = ii2.get_indexer(...)

```python
result = ii2.get_indexer(ci2.append(ci2))
```

### Step 11: Assign expected = np.array(...)

```python
expected = np.array([0, 1, 2, 3, 4, 0, 1, 2, 3, 4], dtype=np.intp)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
ii = IntervalIndex.from_breaks(range(5))
ii2 = ii.append(IntervalIndex([np.nan]))
ci2 = CategoricalIndex(ii2)
result = ii2.get_indexer(ci2)
expected = np.arange(5, dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
result = ii2[1:].get_indexer(ci2[::-1])
expected = np.array([3, 2, 1, 0, -1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
result = ii2.get_indexer(ci2.append(ci2))
expected = np.array([0, 1, 2, 3, 4, 0, 1, 2, 3, 4], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:347 | Complexity: Advanced | Last updated: 2026-06-02*