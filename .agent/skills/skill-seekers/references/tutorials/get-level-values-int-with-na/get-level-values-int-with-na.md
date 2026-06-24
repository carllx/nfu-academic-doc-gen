# How To: Get Level Values Int With Na

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get level values int with na

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
arrays = [['a', 'b', 'b'], [1, np.nan, 2]]
```

### Step 2: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays(arrays)
```

### Step 3: Assign result = index.get_level_values(...)

```python
result = index.get_level_values(1)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([1, np.nan, 2])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign arrays = value

```python
arrays = [['a', 'b', 'b'], [np.nan, np.nan, 2]]
```

### Step 7: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays(arrays)
```

### Step 8: Assign result = index.get_level_values(...)

```python
result = index.get_level_values(1)
```

### Step 9: Assign expected = Index(...)

```python
expected = Index([np.nan, np.nan, 2])
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
arrays = [['a', 'b', 'b'], [1, np.nan, 2]]
index = MultiIndex.from_arrays(arrays)
result = index.get_level_values(1)
expected = Index([1, np.nan, 2])
tm.assert_index_equal(result, expected)
arrays = [['a', 'b', 'b'], [np.nan, np.nan, 2]]
index = MultiIndex.from_arrays(arrays)
result = index.get_level_values(1)
expected = Index([np.nan, np.nan, 2])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_get_level_values.py:60 | Complexity: Advanced | Last updated: 2026-06-02*