# How To: Loc Empty Multiindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc empty multiindex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [['a', 'a', 'b', 'a'], ['a', 'a', 'b', 'b']]
```

### Step 2: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays(arrays, names=('idx1', 'idx2'))
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame([1, 2, 3, 4], index=index, columns=['value'])
```

### Step 4: Assign empty_multiindex = value

```python
empty_multiindex = df.loc[df.loc[:, 'value'] == 0, :].index
```

### Step 5: Assign result = value

```python
result = df.loc[empty_multiindex, :]
```

### Step 6: Assign expected = value

```python
expected = df.loc[[False] * len(df.index), :]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign unknown = 5

```python
df.loc[df.loc[df.loc[:, 'value'] == 0].index, 'value'] = 5
```

### Step 9: Assign result = df

```python
result = df
```

### Step 10: Assign expected = DataFrame(...)

```python
expected = DataFrame([1, 2, 3, 4], index=index, columns=['value'])
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
arrays = [['a', 'a', 'b', 'a'], ['a', 'a', 'b', 'b']]
index = MultiIndex.from_arrays(arrays, names=('idx1', 'idx2'))
df = DataFrame([1, 2, 3, 4], index=index, columns=['value'])
empty_multiindex = df.loc[df.loc[:, 'value'] == 0, :].index
result = df.loc[empty_multiindex, :]
expected = df.loc[[False] * len(df.index), :]
tm.assert_frame_equal(result, expected)
df.loc[df.loc[df.loc[:, 'value'] == 0].index, 'value'] = 5
result = df
expected = DataFrame([1, 2, 3, 4], index=index, columns=['value'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:394 | Complexity: Advanced | Last updated: 2026-06-02*