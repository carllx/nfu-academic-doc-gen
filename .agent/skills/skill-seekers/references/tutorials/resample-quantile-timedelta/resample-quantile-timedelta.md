# How To: Resample Quantile Timedelta

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test resample quantile timedelta

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.timedeltas`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype(f'm8[{unit}]')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'value': pd.to_timedelta(np.arange(4), unit='s').astype(dtype)}, index=pd.date_range('20200101', periods=4, tz='UTC'))
```

### Step 3: Assign result = df.resample.quantile(...)

```python
result = df.resample('2D').quantile(0.99)
```

### Step 4: Assign expected = DataFrame.astype(...)

```python
expected = DataFrame({'value': [pd.Timedelta('0 days 00:00:00.990000'), pd.Timedelta('0 days 00:00:02.990000')]}, index=pd.date_range('20200101', periods=2, tz='UTC', freq='2D')).astype(dtype)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
dtype = np.dtype(f'm8[{unit}]')
df = DataFrame({'value': pd.to_timedelta(np.arange(4), unit='s').astype(dtype)}, index=pd.date_range('20200101', periods=4, tz='UTC'))
result = df.resample('2D').quantile(0.99)
expected = DataFrame({'value': [pd.Timedelta('0 days 00:00:00.990000'), pd.Timedelta('0 days 00:00:02.990000')]}, index=pd.date_range('20200101', periods=2, tz='UTC', freq='2D')).astype(dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_timedelta.py:180 | Complexity: Intermediate | Last updated: 2026-06-02*