# How To: Get Indexer Missing

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get indexer missing

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
# Fixtures: any_string_dtype, null, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index(['a', 'b', null], dtype=any_string_dtype)
```

### Step 2: Assign result = index.get_indexer(...)

```python
result = index.get_indexer(['a', null, 'c'])
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([0, 2, -1], dtype=np.intp)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([0, -1, -1], dtype=np.intp)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([0, 2, -1], dtype=np.intp)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype, null, using_infer_string

# Workflow
index = Index(['a', 'b', null], dtype=any_string_dtype)
result = index.get_indexer(['a', null, 'c'])
if using_infer_string:
    expected = np.array([0, 2, -1], dtype=np.intp)
elif any_string_dtype == 'string' and (not _equivalent_na(any_string_dtype, null)):
    expected = np.array([0, -1, -1], dtype=np.intp)
else:
    expected = np.array([0, 2, -1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:92 | Complexity: Intermediate | Last updated: 2026-06-02*