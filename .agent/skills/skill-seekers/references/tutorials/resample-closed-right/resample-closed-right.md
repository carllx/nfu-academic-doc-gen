# How To: Resample Closed Right

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resample closed right

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

### Step 1: Assign idx = pd.Index(...)

```python
idx = pd.Index([pd.Timedelta(seconds=120 + i * 30) for i in range(10)])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(range(10), index=idx)
```

### Step 3: Assign result = ser.resample.sum(...)

```python
result = ser.resample('min', closed='right', label='right').sum()
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([0, 3, 7, 11, 15, 9], index=pd.TimedeltaIndex([pd.Timedelta(seconds=120 + i * 60) for i in range(6)], freq='min'))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = pd.Index([pd.Timedelta(seconds=120 + i * 30) for i in range(10)])
ser = Series(range(10), index=idx)
result = ser.resample('min', closed='right', label='right').sum()
expected = Series([0, 3, 7, 11, 15, 9], index=pd.TimedeltaIndex([pd.Timedelta(seconds=120 + i * 60) for i in range(6)], freq='min'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_timedelta.py:200 | Complexity: Intermediate | Last updated: 2026-06-02*