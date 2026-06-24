# How To: Groupby Resample Api

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby resample api

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`

**Required Fixtures:**
- `api_client` fixture


## Step-by-Step Guide

### Step 1: Assign df = DataFrame.set_index(...)

```python
df = DataFrame({'date': date_range(start='2016-01-01', periods=4, freq='W'), 'group': [1, 1, 2, 2], 'val': [5, 6, 7, 8]}).set_index('date')
```

### Step 2: Assign i = value

```python
i = date_range('2016-01-03', periods=8).tolist() + date_range('2016-01-17', periods=8).tolist()
```

### Step 3: Assign index = pd.MultiIndex.from_arrays(...)

```python
index = pd.MultiIndex.from_arrays([[1] * 8 + [2] * 8, i], names=['group', 'date'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'val': [5] * 7 + [6] + [7] * 7 + [8]}, index=index)
```

### Step 5: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = df.groupby('group').apply(lambda x: x.resample('1D').ffill())[['val']]
```


## Complete Example

```python
# Workflow
df = DataFrame({'date': date_range(start='2016-01-01', periods=4, freq='W'), 'group': [1, 1, 2, 2], 'val': [5, 6, 7, 8]}).set_index('date')
i = date_range('2016-01-03', periods=8).tolist() + date_range('2016-01-17', periods=8).tolist()
index = pd.MultiIndex.from_arrays([[1] * 8 + [2] * 8, i], names=['group', 'date'])
expected = DataFrame({'val': [5] * 7 + [6] + [7] * 7 + [8]}, index=index)
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.groupby('group').apply(lambda x: x.resample('1D').ffill())[['val']]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_resample_api.py:61 | Complexity: Intermediate | Last updated: 2026-06-02*