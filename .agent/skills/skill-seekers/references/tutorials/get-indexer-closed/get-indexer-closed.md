# How To: Get Indexer Closed

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get indexer closed

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
# Fixtures: closed, leaf_size
```

## Step-by-Step Guide

### Step 1: Assign x = np.arange(...)

```python
x = np.arange(1000, dtype='float64')
```

### Step 2: Assign found = x.astype(...)

```python
found = x.astype('intp')
```

### Step 3: Assign not_found = unknown.astype(...)

```python
not_found = (-1 * np.ones(1000)).astype('intp')
```

### Step 4: Assign tree = IntervalTree(...)

```python
tree = IntervalTree(x, x + 0.5, closed=closed, leaf_size=leaf_size)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(found, tree.get_indexer(x + 0.25))
```

### Step 6: Assign expected = value

```python
expected = found if tree.closed_left else not_found
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(expected, tree.get_indexer(x + 0.0))
```

### Step 8: Assign expected = value

```python
expected = found if tree.closed_right else not_found
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(expected, tree.get_indexer(x + 0.5))
```


## Complete Example

```python
# Setup
# Fixtures: closed, leaf_size

# Workflow
x = np.arange(1000, dtype='float64')
found = x.astype('intp')
not_found = (-1 * np.ones(1000)).astype('intp')
tree = IntervalTree(x, x + 0.5, closed=closed, leaf_size=leaf_size)
tm.assert_numpy_array_equal(found, tree.get_indexer(x + 0.25))
expected = found if tree.closed_left else not_found
tm.assert_numpy_array_equal(expected, tree.get_indexer(x + 0.0))
expected = found if tree.closed_right else not_found
tm.assert_numpy_array_equal(expected, tree.get_indexer(x + 0.5))
```

## Next Steps


---

*Source: test_interval_tree.py:127 | Complexity: Advanced | Last updated: 2026-06-02*