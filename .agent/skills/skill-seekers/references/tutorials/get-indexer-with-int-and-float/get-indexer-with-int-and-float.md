# How To: Get Indexer With Int And Float

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get indexer with int and float

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
# Fixtures: query, expected
```

## Step-by-Step Guide

### Step 1: Assign tuples = value

```python
tuples = [(0, 1), (1, 2), (3, 4)]
```

### Step 2: Assign index = IntervalIndex.from_tuples(...)

```python
index = IntervalIndex.from_tuples(tuples, closed='right')
```

### Step 3: Assign result = index.get_indexer(...)

```python
result = index.get_indexer(query)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array(expected, dtype='intp')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: query, expected

# Workflow
tuples = [(0, 1), (1, 2), (3, 4)]
index = IntervalIndex.from_tuples(tuples, closed='right')
result = index.get_indexer(query)
expected = np.array(expected, dtype='intp')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:301 | Complexity: Intermediate | Last updated: 2026-06-02*