# How To: Reindex Empty With Level

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test reindex empty with level

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: values
```

## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_arrays(...)

```python
idx = MultiIndex.from_arrays(values)
```

### Step 2: Assign unknown = idx.reindex(...)

```python
result, result_indexer = idx.reindex(np.array(['b']), level=0)
```

### Step 3: Assign expected = MultiIndex(...)

```python
expected = MultiIndex(levels=[['b'], values[1]], codes=[[], []])
```

### Step 4: Assign expected_indexer = np.array(...)

```python
expected_indexer = np.array([], dtype=result_indexer.dtype)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result_indexer, expected_indexer)
```


## Complete Example

```python
# Setup
# Fixtures: values

# Workflow
idx = MultiIndex.from_arrays(values)
result, result_indexer = idx.reindex(np.array(['b']), level=0)
expected = MultiIndex(levels=[['b'], values[1]], codes=[[], []])
expected_indexer = np.array([], dtype=result_indexer.dtype)
tm.assert_index_equal(result, expected)
tm.assert_numpy_array_equal(result_indexer, expected_indexer)
```

## Next Steps


---

*Source: test_reindex.py:116 | Complexity: Intermediate | Last updated: 2026-06-02*