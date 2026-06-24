# How To: Timegrouper Apply Return Type Value

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timegrouper apply return type value

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

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
```

### Step 6: Assign expected = df.groupby.apply(...)

```python
expected = df.groupby(Grouper(key='date')).apply(sumfunc_value)
```

### Step 7: Assign result = df_dt.groupby.apply(...)

```python
result = df_dt.groupby(Grouper(freq='ME', key='date')).apply(sumfunc_value)
```


## Complete Example

```python
# Workflow
df = DataFrame({'date': ['10/10/2000', '11/10/2000'], 'value': [10, 13]})
df_dt = df.copy()
df_dt['date'] = pd.to_datetime(df_dt['date'])

def sumfunc_value(x):
    return x.value.sum()
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = df.groupby(Grouper(key='date')).apply(sumfunc_value)
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df_dt.groupby(Grouper(freq='ME', key='date')).apply(sumfunc_value)
tm.assert_series_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
```

## Next Steps


---

*Source: test_timegrouper.py:492 | Complexity: Intermediate | Last updated: 2026-06-02*