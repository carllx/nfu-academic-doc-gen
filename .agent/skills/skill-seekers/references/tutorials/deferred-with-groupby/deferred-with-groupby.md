# How To: Deferred With Groupby

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test deferred with groupby

## Prerequisites

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `IPython.core.completer`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [['2010-01-01', 'A', 2], ['2010-01-02', 'A', 3], ['2010-01-05', 'A', 8], ['2010-01-10', 'A', 7], ['2010-01-13', 'A', 3], ['2010-01-01', 'B', 5], ['2010-01-03', 'B', 2], ['2010-01-04', 'B', 1], ['2010-01-11', 'B', 7], ['2010-01-14', 'B', 3]]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(data, columns=['date', 'id', 'score'])
```

### Step 3: Assign df.date = pd.to_datetime(...)

```python
df.date = pd.to_datetime(df.date)
```

### Step 4: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 5: Assign msg = 'DataFrameGroupBy.resample operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.resample operated on the grouping columns'
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign df = DataFrame.set_index(...)

```python
df = DataFrame({'date': date_range(start='2016-01-01', periods=4, freq='W'), 'group': [1, 1, 2, 2], 'val': [5, 6, 7, 8]}).set_index('date')
```

### Step 8: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 9: Assign msg = 'DataFrameGroupBy.resample operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.resample operated on the grouping columns'
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign expected = df.groupby.apply(...)

```python
expected = df.groupby('id').apply(f_0)
```

### Step 12: Assign result = df.set_index.groupby.resample.asfreq(...)

```python
result = df.set_index('date').groupby('id').resample('D').asfreq()
```

### Step 13: Assign expected = df.groupby.apply(...)

```python
expected = df.groupby('group').apply(f_1)
```

### Step 14: Assign result = df.groupby.resample.ffill(...)

```python
result = df.groupby('group').resample('1D').ffill()
```


## Complete Example

```python
# Workflow
data = [['2010-01-01', 'A', 2], ['2010-01-02', 'A', 3], ['2010-01-05', 'A', 8], ['2010-01-10', 'A', 7], ['2010-01-13', 'A', 3], ['2010-01-01', 'B', 5], ['2010-01-03', 'B', 2], ['2010-01-04', 'B', 1], ['2010-01-11', 'B', 7], ['2010-01-14', 'B', 3]]
df = DataFrame(data, columns=['date', 'id', 'score'])
df.date = pd.to_datetime(df.date)

def f_0(x):
    return x.set_index('date').resample('D').asfreq()
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = df.groupby('id').apply(f_0)
msg = 'DataFrameGroupBy.resample operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.set_index('date').groupby('id').resample('D').asfreq()
tm.assert_frame_equal(result, expected)
df = DataFrame({'date': date_range(start='2016-01-01', periods=4, freq='W'), 'group': [1, 1, 2, 2], 'val': [5, 6, 7, 8]}).set_index('date')

def f_1(x):
    return x.resample('1D').ffill()
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = df.groupby('group').apply(f_1)
msg = 'DataFrameGroupBy.resample operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.groupby('group').resample('1D').ffill()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_resampler_grouper.py:50 | Complexity: Advanced | Last updated: 2026-06-02*