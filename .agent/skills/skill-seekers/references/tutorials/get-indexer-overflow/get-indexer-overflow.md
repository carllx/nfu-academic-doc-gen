# How To: Get Indexer Overflow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get indexer overflow

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
left, right = (np.array([0, 1], dtype=dtype), np.array([1, 2], dtype=dtype))
```

### Step 2: Assign tree = IntervalTree(...)

```python
tree = IntervalTree(left, right)
```

### Step 3: Assign result = tree.get_indexer(...)

```python
result = tree.get_indexer(np.array([target_value], dtype=target_dtype))
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([-1], dtype='intp')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, target_value, target_dtype

# Workflow
left, right = (np.array([0, 1], dtype=dtype), np.array([1, 2], dtype=dtype))
tree = IntervalTree(left, right)
result = tree.get_indexer(np.array([target_value], dtype=target_dtype))
expected = np.array([-1], dtype='intp')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_interval_tree.py:63 | Complexity: Intermediate | Last updated: 2026-06-02*