# How To: Groupby Aggregation Mixed Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby aggregation mixed dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `functools`
- `functools`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`


## Step-by-Step Guide

### Step 1: Assign expected = DataFrame(...)

```python
expected = DataFrame({'v1': [5, 5, 7, np.nan, 3, 3, 4, 1], 'v2': [55, 55, 77, np.nan, 33, 33, 44, 11]}, index=MultiIndex.from_tuples([(1, 95), (1, 99), (2, 95), (2, 99), ('big', 'damp'), ('blue', 'dry'), ('red', 'red'), ('red', 'wet')], names=['by1', 'by2']))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'v1': [1, 3, 5, 7, 8, 3, 5, np.nan, 4, 5, 7, 9], 'v2': [11, 33, 55, 77, 88, 33, 55, np.nan, 44, 55, 77, 99], 'by1': ['red', 'blue', 1, 2, np.nan, 'big', 1, 2, 'red', 1, np.nan, 12], 'by2': ['wet', 'dry', 99, 95, np.nan, 'damp', 95, 99, 'red', 99, np.nan, np.nan]})
```

### Step 3: Assign g = df.groupby(...)

```python
g = df.groupby(['by1', 'by2'])
```

### Step 4: Assign result = unknown.mean(...)

```python
result = g[['v1', 'v2']].mean()
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
expected = DataFrame({'v1': [5, 5, 7, np.nan, 3, 3, 4, 1], 'v2': [55, 55, 77, np.nan, 33, 33, 44, 11]}, index=MultiIndex.from_tuples([(1, 95), (1, 99), (2, 95), (2, 99), ('big', 'damp'), ('blue', 'dry'), ('red', 'red'), ('red', 'wet')], names=['by1', 'by2']))
df = DataFrame({'v1': [1, 3, 5, 7, 8, 3, 5, np.nan, 4, 5, 7, 9], 'v2': [11, 33, 55, 77, 88, 33, 55, np.nan, 44, 55, 77, 99], 'by1': ['red', 'blue', 1, 2, np.nan, 'big', 1, 2, 'red', 1, np.nan, 12], 'by2': ['wet', 'dry', 99, 95, np.nan, 'damp', 95, 99, 'red', 99, np.nan, np.nan]})
g = df.groupby(['by1', 'by2'])
result = g[['v1', 'v2']].mean()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_aggregate.py:65 | Complexity: Intermediate | Last updated: 2026-06-02*