# How To: Get Indexer For Multiindex With Nans

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer for multiindex with nans

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: nulls_fixture
```

## Step-by-Step Guide

### Step 1: Assign idx1 = MultiIndex.from_product(...)

```python
idx1 = MultiIndex.from_product([['A'], [1.0, 2.0]], names=['id1', 'id2'])
```

### Step 2: Assign idx2 = MultiIndex.from_product(...)

```python
idx2 = MultiIndex.from_product([['A'], [nulls_fixture, 2.0]], names=['id1', 'id2'])
```

### Step 3: Assign result = idx2.get_indexer(...)

```python
result = idx2.get_indexer(idx1)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([-1, 1], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign result = idx1.get_indexer(...)

```python
result = idx1.get_indexer(idx2)
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array([-1, 1], dtype=np.intp)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: nulls_fixture

# Workflow
idx1 = MultiIndex.from_product([['A'], [1.0, 2.0]], names=['id1', 'id2'])
idx2 = MultiIndex.from_product([['A'], [nulls_fixture, 2.0]], names=['id1', 'id2'])
result = idx2.get_indexer(idx1)
expected = np.array([-1, 1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
result = idx1.get_indexer(idx2)
expected = np.array([-1, 1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:990 | Complexity: Advanced | Last updated: 2026-06-02*