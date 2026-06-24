# How To: Resample With Timedeltas

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resample with timedeltas

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.timedeltas`


## Step-by-Step Guide

### Step 1: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': np.arange(1480)})
```

### Step 2: Assign expected = expected.groupby.sum(...)

```python
expected = expected.groupby(expected.index // 30).sum()
```

### Step 3: Assign expected.index = timedelta_range(...)

```python
expected.index = timedelta_range('0 days', freq='30min', periods=50)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'A': np.arange(1480)}, index=pd.to_timedelta(np.arange(1480), unit='min'))
```

### Step 5: Assign result = df.resample.sum(...)

```python
result = df.resample('30min').sum()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign s = value

```python
s = df['A']
```

### Step 8: Assign result = s.resample.sum(...)

```python
result = s.resample('30min').sum()
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected['A'])
```


## Complete Example

```python
# Workflow
expected = DataFrame({'A': np.arange(1480)})
expected = expected.groupby(expected.index // 30).sum()
expected.index = timedelta_range('0 days', freq='30min', periods=50)
df = DataFrame({'A': np.arange(1480)}, index=pd.to_timedelta(np.arange(1480), unit='min'))
result = df.resample('30min').sum()
tm.assert_frame_equal(result, expected)
s = df['A']
result = s.resample('30min').sum()
tm.assert_series_equal(result, expected['A'])
```

## Next Steps


---

*Source: test_timedelta.py:50 | Complexity: Advanced | Last updated: 2026-06-02*