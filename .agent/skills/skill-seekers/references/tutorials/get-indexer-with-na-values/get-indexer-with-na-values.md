# How To: Get Indexer With Na Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer with NA values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `numpy`
- `pytest`
- `pandas._libs.missing`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: unique_nulls_fixture, unique_nulls_fixture2
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([unique_nulls_fixture, unique_nulls_fixture2], dtype=object)
```

### Step 2: Assign index = Index(...)

```python
index = Index(arr, dtype=object)
```

### Step 3: Assign result = index.get_indexer(...)

```python
result = index.get_indexer(Index([unique_nulls_fixture, unique_nulls_fixture2, 'Unknown'], dtype=object))
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([0, 1, -1], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unique_nulls_fixture, unique_nulls_fixture2

# Workflow
if unique_nulls_fixture is unique_nulls_fixture2:
    return
arr = np.array([unique_nulls_fixture, unique_nulls_fixture2], dtype=object)
index = Index(arr, dtype=object)
result = index.get_indexer(Index([unique_nulls_fixture, unique_nulls_fixture2, 'Unknown'], dtype=object))
expected = np.array([0, 1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:47 | Complexity: Intermediate | Last updated: 2026-06-02*