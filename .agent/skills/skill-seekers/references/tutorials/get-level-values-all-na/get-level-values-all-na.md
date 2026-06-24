# How To: Get Level Values All Na

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get level values all na

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [[np.nan, np.nan, np.nan], ['a', np.nan, 1]]
```

### Step 2: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays(arrays)
```

### Step 3: Assign result = index.get_level_values(...)

```python
result = index.get_level_values(0)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([np.nan, np.nan, np.nan], dtype=np.float64)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign result = index.get_level_values(...)

```python
result = index.get_level_values(1)
```

### Step 7: Assign expected = Index(...)

```python
expected = Index(['a', np.nan, 1], dtype=object)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
arrays = [[np.nan, np.nan, np.nan], ['a', np.nan, 1]]
index = MultiIndex.from_arrays(arrays)
result = index.get_level_values(0)
expected = Index([np.nan, np.nan, np.nan], dtype=np.float64)
tm.assert_index_equal(result, expected)
result = index.get_level_values(1)
expected = Index(['a', np.nan, 1], dtype=object)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_get_level_values.py:47 | Complexity: Advanced | Last updated: 2026-06-02*