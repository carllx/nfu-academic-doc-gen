# How To: Groupby Groups Datetimeindex2

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby groups datetimeindex2

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

### Step 1: Assign index = date_range(...)

```python
index = date_range('2015/01/01', periods=5, name='date')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [5, 6, 7, 8, 9], 'B': [1, 2, 3, 4, 5]}, index=index)
```

### Step 3: Assign result = value

```python
result = df.groupby(level='date').groups
```

### Step 4: Assign dates = value

```python
dates = ['2015-01-05', '2015-01-04', '2015-01-03', '2015-01-02', '2015-01-01']
```

### Step 5: Assign expected = value

```python
expected = {Timestamp(date): DatetimeIndex([date], name='date') for date in dates}
```

### Step 6: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(result, expected)
```

### Step 7: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(level='date')
```

### Step 8: Assign result = grouped.get_group(...)

```python
result = grouped.get_group(date)
```

### Step 9: Assign data = value

```python
data = [[df.loc[date, 'A'], df.loc[date, 'B']]]
```

### Step 10: Assign expected_index = DatetimeIndex(...)

```python
expected_index = DatetimeIndex([date], name='date', freq='D', dtype=index.dtype)
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame(data, columns=list('AB'), index=expected_index)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
index = date_range('2015/01/01', periods=5, name='date')
df = DataFrame({'A': [5, 6, 7, 8, 9], 'B': [1, 2, 3, 4, 5]}, index=index)
result = df.groupby(level='date').groups
dates = ['2015-01-05', '2015-01-04', '2015-01-03', '2015-01-02', '2015-01-01']
expected = {Timestamp(date): DatetimeIndex([date], name='date') for date in dates}
tm.assert_dict_equal(result, expected)
grouped = df.groupby(level='date')
for date in dates:
    result = grouped.get_group(date)
    data = [[df.loc[date, 'A'], df.loc[date, 'B']]]
    expected_index = DatetimeIndex([date], name='date', freq='D', dtype=index.dtype)
    expected = DataFrame(data, columns=list('AB'), index=expected_index)
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_timegrouper.py:525 | Complexity: Advanced | Last updated: 2026-06-02*