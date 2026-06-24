# How To: Loc Datetime Mask Slicing

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc datetime mask slicing

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dt_idx = pd.to_datetime(...)

```python
dt_idx = pd.to_datetime(['2017-05-04', '2017-05-05'])
```

### Step 2: Assign m_idx = MultiIndex.from_product(...)

```python
m_idx = MultiIndex.from_product([dt_idx, dt_idx], names=['Idx1', 'Idx2'])
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(data=[[1, 2], [3, 4], [5, 6], [7, 6]], index=m_idx, columns=['C1', 'C2'])
```

### Step 4: Assign result = value

```python
result = df.loc[(dt_idx[0], df.index.get_level_values(1) > '2017-05-04'), 'C1']
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([3], name='C1', index=MultiIndex.from_tuples([(pd.Timestamp('2017-05-04'), pd.Timestamp('2017-05-05'))], names=['Idx1', 'Idx2']))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
dt_idx = pd.to_datetime(['2017-05-04', '2017-05-05'])
m_idx = MultiIndex.from_product([dt_idx, dt_idx], names=['Idx1', 'Idx2'])
df = DataFrame(data=[[1, 2], [3, 4], [5, 6], [7, 6]], index=m_idx, columns=['C1', 'C2'])
result = df.loc[(dt_idx[0], df.index.get_level_values(1) > '2017-05-04'), 'C1']
expected = Series([3], name='C1', index=MultiIndex.from_tuples([(pd.Timestamp('2017-05-04'), pd.Timestamp('2017-05-05'))], names=['Idx1', 'Idx2']))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_loc.py:639 | Complexity: Intermediate | Last updated: 2026-06-02*