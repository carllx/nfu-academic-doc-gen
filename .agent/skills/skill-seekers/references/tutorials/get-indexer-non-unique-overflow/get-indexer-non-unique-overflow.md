# How To: Get Indexer Non Unique Overflow

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get indexer non unique overflow

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs.interval`
- `pandas.compat`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dtype, target_value, target_dtype
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
left, right = (np.array([0, 2], dtype=dtype), np.array([1, 3], dtype=dtype))
```

### Step 2: Assign tree = IntervalTree(...)

```python
tree = IntervalTree(left, right)
```

### Step 3: Assign target = np.array(...)

```python
target = np.array([target_value], dtype=target_dtype)
```

### Step 4: Assign unknown = tree.get_indexer_non_unique(...)

```python
result_indexer, result_missing = tree.get_indexer_non_unique(target)
```

### Step 5: Assign expected_indexer = np.array(...)

```python
expected_indexer = np.array([-1], dtype='intp')
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result_indexer, expected_indexer)
```

### Step 7: Assign expected_missing = np.array(...)

```python
expected_missing = np.array([0], dtype='intp')
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result_missing, expected_missing)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, target_value, target_dtype

# Workflow
left, right = (np.array([0, 2], dtype=dtype), np.array([1, 3], dtype=dtype))
tree = IntervalTree(left, right)
target = np.array([target_value], dtype=target_dtype)
result_indexer, result_missing = tree.get_indexer_non_unique(target)
expected_indexer = np.array([-1], dtype='intp')
tm.assert_numpy_array_equal(result_indexer, expected_indexer)
expected_missing = np.array([0], dtype='intp')
tm.assert_numpy_array_equal(result_missing, expected_missing)
```

## Next Steps


---

*Source: test_interval_tree.py:94 | Complexity: Advanced | Last updated: 2026-06-02*