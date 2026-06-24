# How To: Get Indexer Categorical

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get indexer categorical

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: target, ordered
```

## Step-by-Step Guide

### Step 1: Assign index = IntervalIndex.from_tuples(...)

```python
index = IntervalIndex.from_tuples([(0, 1), (1, 2), (3, 4)])
```

### Step 2: Assign categorical_target = CategoricalIndex(...)

```python
categorical_target = CategoricalIndex(target, ordered=ordered)
```

### Step 3: Assign result = index.get_indexer(...)

```python
result = index.get_indexer(categorical_target)
```

### Step 4: Assign expected = index.get_indexer(...)

```python
expected = index.get_indexer(target)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: target, ordered

# Workflow
index = IntervalIndex.from_tuples([(0, 1), (1, 2), (3, 4)])
categorical_target = CategoricalIndex(target, ordered=ordered)
result = index.get_indexer(categorical_target)
expected = index.get_indexer(target)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:335 | Complexity: Intermediate | Last updated: 2026-06-02*