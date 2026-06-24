# How To: Agg Dict Parameter Cast Result Dtypes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg dict parameter cast result dtypes

## Prerequisites

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.printing`
- `pandas.tests.extension.decimal.array`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'class': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'], 'time': date_range('1/1/2011', periods=8, freq='h')})
```

### Step 2: Assign unknown = None

```python
df.loc[[0, 1, 2, 5], 'time'] = None
```

### Step 3: Assign exp = unknown.set_index(...)

```python
exp = df.loc[[0, 3, 4, 6]].set_index('class')
```

### Step 4: Assign grouped = df.groupby(...)

```python
grouped = df.groupby('class')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.first(), exp)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.agg('first'), exp)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.agg({'time': 'first'}), exp)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.time.first(), exp['time'])
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.time.agg('first'), exp['time'])
```

### Step 10: Assign exp = unknown.set_index(...)

```python
exp = df.loc[[0, 3, 4, 7]].set_index('class')
```

### Step 11: Assign grouped = df.groupby(...)

```python
grouped = df.groupby('class')
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.last(), exp)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.agg('last'), exp)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(grouped.agg({'time': 'last'}), exp)
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.time.last(), exp['time'])
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.time.agg('last'), exp['time'])
```

### Step 17: Assign exp = Series(...)

```python
exp = Series([2, 2, 2, 2], index=Index(list('ABCD'), name='class'), name='time')
```

### Step 18: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.time.agg(len), exp)
```

### Step 19: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.time.size(), exp)
```

### Step 20: Assign exp = Series(...)

```python
exp = Series([0, 1, 1, 2], index=Index(list('ABCD'), name='class'), name='time')
```

### Step 21: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grouped.time.count(), exp)
```


## Complete Example

```python
# Workflow
df = DataFrame({'class': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'], 'time': date_range('1/1/2011', periods=8, freq='h')})
df.loc[[0, 1, 2, 5], 'time'] = None
exp = df.loc[[0, 3, 4, 6]].set_index('class')
grouped = df.groupby('class')
tm.assert_frame_equal(grouped.first(), exp)
tm.assert_frame_equal(grouped.agg('first'), exp)
tm.assert_frame_equal(grouped.agg({'time': 'first'}), exp)
tm.assert_series_equal(grouped.time.first(), exp['time'])
tm.assert_series_equal(grouped.time.agg('first'), exp['time'])
exp = df.loc[[0, 3, 4, 7]].set_index('class')
grouped = df.groupby('class')
tm.assert_frame_equal(grouped.last(), exp)
tm.assert_frame_equal(grouped.agg('last'), exp)
tm.assert_frame_equal(grouped.agg({'time': 'last'}), exp)
tm.assert_series_equal(grouped.time.last(), exp['time'])
tm.assert_series_equal(grouped.time.agg('last'), exp['time'])
exp = Series([2, 2, 2, 2], index=Index(list('ABCD'), name='class'), name='time')
tm.assert_series_equal(grouped.time.agg(len), exp)
tm.assert_series_equal(grouped.time.size(), exp)
exp = Series([0, 1, 1, 2], index=Index(list('ABCD'), name='class'), name='time')
tm.assert_series_equal(grouped.time.count(), exp)
```

## Next Steps


---

*Source: test_other.py:103 | Complexity: Advanced | Last updated: 2026-06-02*