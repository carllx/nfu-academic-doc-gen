# How To: Get Indexer Non Unique

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get indexer non unique

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: idx_values, key_values, key_class, dtype
```

## Step-by-Step Guide

### Step 1: Assign key = key_class(...)

```python
key = key_class(key_values, categories=range(1, 5))
```

### Step 2: Assign idx = Index(...)

```python
idx = Index(idx_values, dtype=dtype)
```

### Step 3: Assign unknown = idx.get_indexer_non_unique(...)

```python
expected, exp_miss = idx.get_indexer_non_unique(key_values)
```

### Step 4: Assign unknown = idx.get_indexer_non_unique(...)

```python
result, res_miss = idx.get_indexer_non_unique(key)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(expected, result)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(exp_miss, res_miss)
```

### Step 7: Assign exp_unique = idx.unique.get_indexer(...)

```python
exp_unique = idx.unique().get_indexer(key_values)
```

### Step 8: Assign res_unique = idx.unique.get_indexer(...)

```python
res_unique = idx.unique().get_indexer(key)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res_unique, exp_unique)
```

### Step 10: Assign dtype = value

```python
dtype = key.dtype
```


## Complete Example

```python
# Setup
# Fixtures: idx_values, key_values, key_class, dtype

# Workflow
key = key_class(key_values, categories=range(1, 5))
if dtype == 'key':
    dtype = key.dtype
idx = Index(idx_values, dtype=dtype)
expected, exp_miss = idx.get_indexer_non_unique(key_values)
result, res_miss = idx.get_indexer_non_unique(key)
tm.assert_numpy_array_equal(expected, result)
tm.assert_numpy_array_equal(exp_miss, res_miss)
exp_unique = idx.unique().get_indexer(key_values)
res_unique = idx.unique().get_indexer(key)
tm.assert_numpy_array_equal(res_unique, exp_unique)
```

## Next Steps


---

*Source: test_indexing.py:226 | Complexity: Advanced | Last updated: 2026-06-02*