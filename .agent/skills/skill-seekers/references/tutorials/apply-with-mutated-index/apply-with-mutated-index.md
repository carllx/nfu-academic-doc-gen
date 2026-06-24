# How To: Apply With Mutated Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply with mutated index

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

### Step 1: Assign index = date_range(...)

```python
index = date_range('1-1-2015', '12-31-15', freq='D')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(data={'col1': np.random.default_rng(2).random(len(index))}, index=index)
```

### Step 3: Assign expected = df.groupby.apply(...)

```python
expected = df.groupby(pd.Grouper(freq='ME')).apply(f)
```

### Step 4: Assign result = df.resample.apply(...)

```python
result = df.resample('ME').apply(f)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign expected = unknown.groupby.apply(...)

```python
expected = df['col1'].groupby(pd.Grouper(freq='ME'), group_keys=False).apply(f)
```

### Step 7: Assign result = unknown.resample.apply(...)

```python
result = df['col1'].resample('ME').apply(f)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign s = Series(...)

```python
s = Series([1, 2], index=['a', 'b'])
```


## Complete Example

```python
# Workflow
index = date_range('1-1-2015', '12-31-15', freq='D')
df = DataFrame(data={'col1': np.random.default_rng(2).random(len(index))}, index=index)

def f(x):
    s = Series([1, 2], index=['a', 'b'])
    return s
expected = df.groupby(pd.Grouper(freq='ME')).apply(f)
result = df.resample('ME').apply(f)
tm.assert_frame_equal(result, expected)
expected = df['col1'].groupby(pd.Grouper(freq='ME'), group_keys=False).apply(f)
result = df['col1'].resample('ME').apply(f)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_resampler_grouper.py:296 | Complexity: Advanced | Last updated: 2026-06-02*