# How To: Timegrouper Apply Return Type Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timegrouper apply return type series

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.groupby.ops`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'date': ['10/10/2000', '11/10/2000'], 'value': [10, 13]})
```

### Step 2: Assign df_dt = df.copy(...)

```python
df_dt = df.copy()
```

### Step 3: Assign unknown = pd.to_datetime(...)

```python
df_dt['date'] = pd.to_datetime(df_dt['date'])
```

### Step 4: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 5: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
```

### Step 7: Assign expected = df.groupby.apply(...)

```python
expected = df.groupby(Grouper(key='date')).apply(sumfunc_series)
```

### Step 8: Assign result = df_dt.groupby.apply(...)

```python
result = df_dt.groupby(Grouper(freq='ME', key='date')).apply(sumfunc_series)
```


## Complete Example

```python
# Workflow
df = DataFrame({'date': ['10/10/2000', '11/10/2000'], 'value': [10, 13]})
df_dt = df.copy()
df_dt['date'] = pd.to_datetime(df_dt['date'])

def sumfunc_series(x):
    return Series([x['value'].sum()], ('sum',))
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = df.groupby(Grouper(key='date')).apply(sumfunc_series)
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df_dt.groupby(Grouper(freq='ME', key='date')).apply(sumfunc_series)
tm.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
```

## Next Steps


---

*Source: test_timegrouper.py:471 | Complexity: Advanced | Last updated: 2026-06-02*