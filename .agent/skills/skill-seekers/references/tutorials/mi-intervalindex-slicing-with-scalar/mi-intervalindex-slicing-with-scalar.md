# How To: Mi Intervalindex Slicing With Scalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mi intervalindex slicing with scalar

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ii = IntervalIndex.from_arrays(...)

```python
ii = IntervalIndex.from_arrays([0, 1, 10, 11, 0, 1, 10, 11], [1, 2, 11, 12, 1, 2, 11, 12], name='MP')
```

### Step 2: Assign idx = pd.MultiIndex.from_arrays(...)

```python
idx = pd.MultiIndex.from_arrays([pd.Index(['FC', 'FC', 'FC', 'FC', 'OWNER', 'OWNER', 'OWNER', 'OWNER']), pd.Index(['RID1', 'RID1', 'RID2', 'RID2', 'RID1', 'RID1', 'RID2', 'RID2']), ii])
```

### Step 3: Assign idx.names = value

```python
idx.names = ['Item', 'RID', 'MP']
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'value': [1, 2, 3, 4, 5, 6, 7, 8]})
```

### Step 5: Assign df.index = idx

```python
df.index = idx
```

### Step 6: Assign query_df = DataFrame(...)

```python
query_df = DataFrame({'Item': ['FC', 'OWNER', 'FC', 'OWNER', 'OWNER'], 'RID': ['RID1', 'RID1', 'RID1', 'RID2', 'RID2'], 'MP': [0.2, 1.5, 1.6, 11.1, 10.9]})
```

### Step 7: Assign query_df = query_df.sort_index(...)

```python
query_df = query_df.sort_index()
```

### Step 8: Assign idx = pd.MultiIndex.from_arrays(...)

```python
idx = pd.MultiIndex.from_arrays([query_df.Item, query_df.RID, query_df.MP])
```

### Step 9: Assign query_df.index = idx

```python
query_df.index = idx
```

### Step 10: Assign result = value

```python
result = df.value.loc[query_df.index]
```

### Step 11: Assign sliced_level = ii.take(...)

```python
sliced_level = ii.take([0, 1, 1, 3, 2])
```

### Step 12: Assign expected_index = pd.MultiIndex.from_arrays(...)

```python
expected_index = pd.MultiIndex.from_arrays([idx.get_level_values(0), idx.get_level_values(1), sliced_level])
```

### Step 13: Assign expected = Series(...)

```python
expected = Series([1, 6, 2, 8, 7], index=expected_index, name='value')
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ii = IntervalIndex.from_arrays([0, 1, 10, 11, 0, 1, 10, 11], [1, 2, 11, 12, 1, 2, 11, 12], name='MP')
idx = pd.MultiIndex.from_arrays([pd.Index(['FC', 'FC', 'FC', 'FC', 'OWNER', 'OWNER', 'OWNER', 'OWNER']), pd.Index(['RID1', 'RID1', 'RID2', 'RID2', 'RID1', 'RID1', 'RID2', 'RID2']), ii])
idx.names = ['Item', 'RID', 'MP']
df = DataFrame({'value': [1, 2, 3, 4, 5, 6, 7, 8]})
df.index = idx
query_df = DataFrame({'Item': ['FC', 'OWNER', 'FC', 'OWNER', 'OWNER'], 'RID': ['RID1', 'RID1', 'RID1', 'RID2', 'RID2'], 'MP': [0.2, 1.5, 1.6, 11.1, 10.9]})
query_df = query_df.sort_index()
idx = pd.MultiIndex.from_arrays([query_df.Item, query_df.RID, query_df.MP])
query_df.index = idx
result = df.value.loc[query_df.index]
sliced_level = ii.take([0, 1, 1, 3, 2])
expected_index = pd.MultiIndex.from_arrays([idx.get_level_values(0), idx.get_level_values(1), sliced_level])
expected = Series([1, 6, 2, 8, 7], index=expected_index, name='value')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_interval.py:169 | Complexity: Advanced | Last updated: 2026-06-02*