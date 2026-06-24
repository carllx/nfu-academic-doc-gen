# How To: Get Level Values Na

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get level values na

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
expected = Index([np.nan, np.nan, np.nan])
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
expected = Index(['a', np.nan, 1])
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign arrays = value

```python
arrays = [['a', 'b', 'b'], pd.DatetimeIndex([0, 1, pd.NaT])]
```

### Step 10: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays(arrays)
```

### Step 11: Assign result = index.get_level_values(...)

```python
result = index.get_level_values(1)
```

### Step 12: Assign expected = pd.DatetimeIndex(...)

```python
expected = pd.DatetimeIndex([0, 1, pd.NaT])
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 14: Assign arrays = value

```python
arrays = [[], []]
```

### Step 15: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays(arrays)
```

### Step 16: Assign result = index.get_level_values(...)

```python
result = index.get_level_values(0)
```

### Step 17: Assign expected = Index(...)

```python
expected = Index([], dtype=object)
```

### Step 18: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
arrays = [[np.nan, np.nan, np.nan], ['a', np.nan, 1]]
index = MultiIndex.from_arrays(arrays)
result = index.get_level_values(0)
expected = Index([np.nan, np.nan, np.nan])
tm.assert_index_equal(result, expected)
result = index.get_level_values(1)
expected = Index(['a', np.nan, 1])
tm.assert_index_equal(result, expected)
arrays = [['a', 'b', 'b'], pd.DatetimeIndex([0, 1, pd.NaT])]
index = MultiIndex.from_arrays(arrays)
result = index.get_level_values(1)
expected = pd.DatetimeIndex([0, 1, pd.NaT])
tm.assert_index_equal(result, expected)
arrays = [[], []]
index = MultiIndex.from_arrays(arrays)
result = index.get_level_values(0)
expected = Index([], dtype=object)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_get_level_values.py:75 | Complexity: Advanced | Last updated: 2026-06-02*