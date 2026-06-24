# How To: Resample Timedelta Values

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resample timedelta values

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

### Step 1: Assign times = timedelta_range(...)

```python
times = timedelta_range('1 day', '6 day', freq='4D')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'time': times}, index=times)
```

### Step 3: Assign times2 = timedelta_range(...)

```python
times2 = timedelta_range('1 day', '6 day', freq='2D')
```

### Step 4: Assign exp = Series(...)

```python
exp = Series(times2, index=times2, name='time')
```

### Step 5: Assign unknown = value

```python
exp.iloc[1] = pd.NaT
```

### Step 6: Assign res = value

```python
res = df.resample('2D').first()['time']
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 8: Assign res = unknown.resample.first(...)

```python
res = df['time'].resample('2D').first()
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```


## Complete Example

```python
# Workflow
times = timedelta_range('1 day', '6 day', freq='4D')
df = DataFrame({'time': times}, index=times)
times2 = timedelta_range('1 day', '6 day', freq='2D')
exp = Series(times2, index=times2, name='time')
exp.iloc[1] = pd.NaT
res = df.resample('2D').first()['time']
tm.assert_series_equal(res, exp)
res = df['time'].resample('2D').first()
tm.assert_series_equal(res, exp)
```

## Next Steps


---

*Source: test_timedelta.py:115 | Complexity: Advanced | Last updated: 2026-06-02*