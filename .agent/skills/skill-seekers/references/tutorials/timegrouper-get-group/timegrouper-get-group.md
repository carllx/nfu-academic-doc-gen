# How To: Timegrouper Get Group

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timegrouper get group

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

### Step 1: Assign df_original = DataFrame(...)

```python
df_original = DataFrame({'Buyer': 'Carl Joe Joe Carl Joe Carl'.split(), 'Quantity': [18, 3, 5, 1, 9, 3], 'Date': [datetime(2013, 9, 1, 13, 0), datetime(2013, 9, 1, 13, 5), datetime(2013, 10, 1, 20, 0), datetime(2013, 10, 3, 10, 0), datetime(2013, 12, 2, 12, 0), datetime(2013, 9, 2, 14, 0)]})
```

### Step 2: Assign df_reordered = df_original.sort_values(...)

```python
df_reordered = df_original.sort_values(by='Quantity')
```

### Step 3: Assign expected_list = value

```python
expected_list = [df_original.iloc[[0, 1, 5]], df_original.iloc[[2, 3]], df_original.iloc[[4]]]
```

### Step 4: Assign dt_list = value

```python
dt_list = ['2013-09-30', '2013-10-31', '2013-12-31']
```

### Step 5: Assign expected_list = value

```python
expected_list = [df_original.iloc[[1]], df_original.iloc[[3]], df_original.iloc[[4]]]
```

### Step 6: Assign g_list = value

```python
g_list = [('Joe', '2013-09-30'), ('Carl', '2013-10-31'), ('Joe', '2013-12-31')]
```

### Step 7: Assign df_original = df_original.set_index(...)

```python
df_original = df_original.set_index('Date')
```

### Step 8: Assign df_reordered = df_original.sort_values(...)

```python
df_reordered = df_original.sort_values(by='Quantity')
```

### Step 9: Assign expected_list = value

```python
expected_list = [df_original.iloc[[0, 1, 5]], df_original.iloc[[2, 3]], df_original.iloc[[4]]]
```

### Step 10: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(Grouper(freq='ME', key='Date'))
```

### Step 11: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(['Buyer', Grouper(freq='ME', key='Date')])
```

### Step 12: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(Grouper(freq='ME'))
```

### Step 13: Assign dt = Timestamp(...)

```python
dt = Timestamp(t)
```

### Step 14: Assign result = grouped.get_group(...)

```python
result = grouped.get_group(dt)
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 16: Assign dt = Timestamp(...)

```python
dt = Timestamp(t)
```

### Step 17: Assign result = grouped.get_group(...)

```python
result = grouped.get_group((b, dt))
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 19: Assign dt = Timestamp(...)

```python
dt = Timestamp(t)
```

### Step 20: Assign result = grouped.get_group(...)

```python
result = grouped.get_group(dt)
```

### Step 21: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df_original = DataFrame({'Buyer': 'Carl Joe Joe Carl Joe Carl'.split(), 'Quantity': [18, 3, 5, 1, 9, 3], 'Date': [datetime(2013, 9, 1, 13, 0), datetime(2013, 9, 1, 13, 5), datetime(2013, 10, 1, 20, 0), datetime(2013, 10, 3, 10, 0), datetime(2013, 12, 2, 12, 0), datetime(2013, 9, 2, 14, 0)]})
df_reordered = df_original.sort_values(by='Quantity')
expected_list = [df_original.iloc[[0, 1, 5]], df_original.iloc[[2, 3]], df_original.iloc[[4]]]
dt_list = ['2013-09-30', '2013-10-31', '2013-12-31']
for df in [df_original, df_reordered]:
    grouped = df.groupby(Grouper(freq='ME', key='Date'))
    for t, expected in zip(dt_list, expected_list):
        dt = Timestamp(t)
        result = grouped.get_group(dt)
        tm.assert_frame_equal(result, expected)
expected_list = [df_original.iloc[[1]], df_original.iloc[[3]], df_original.iloc[[4]]]
g_list = [('Joe', '2013-09-30'), ('Carl', '2013-10-31'), ('Joe', '2013-12-31')]
for df in [df_original, df_reordered]:
    grouped = df.groupby(['Buyer', Grouper(freq='ME', key='Date')])
    for (b, t), expected in zip(g_list, expected_list):
        dt = Timestamp(t)
        result = grouped.get_group((b, dt))
        tm.assert_frame_equal(result, expected)
df_original = df_original.set_index('Date')
df_reordered = df_original.sort_values(by='Quantity')
expected_list = [df_original.iloc[[0, 1, 5]], df_original.iloc[[2, 3]], df_original.iloc[[4]]]
for df in [df_original, df_reordered]:
    grouped = df.groupby(Grouper(freq='ME'))
    for t, expected in zip(dt_list, expected_list):
        dt = Timestamp(t)
        result = grouped.get_group(dt)
        tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_timegrouper.py:405 | Complexity: Advanced | Last updated: 2026-06-02*