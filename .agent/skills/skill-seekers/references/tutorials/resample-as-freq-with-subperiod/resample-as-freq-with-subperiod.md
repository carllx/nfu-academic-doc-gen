# How To: Resample As Freq With Subperiod

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resample as freq with subperiod

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

### Step 1: Assign index = timedelta_range(...)

```python
index = timedelta_range('00:00:00', '00:10:00', freq='5min')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(data={'value': [1, 5, 10]}, index=index)
```

### Step 3: Assign result = df.resample.asfreq(...)

```python
result = df.resample('2min').asfreq()
```

### Step 4: Assign expected_data = value

```python
expected_data = {'value': [1, np.nan, np.nan, np.nan, np.nan, 10]}
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(data=expected_data, index=timedelta_range('00:00:00', '00:10:00', freq='2min'))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
index = timedelta_range('00:00:00', '00:10:00', freq='5min')
df = DataFrame(data={'value': [1, 5, 10]}, index=index)
result = df.resample('2min').asfreq()
expected_data = {'value': [1, np.nan, np.nan, np.nan, np.nan, 10]}
expected = DataFrame(data=expected_data, index=timedelta_range('00:00:00', '00:10:00', freq='2min'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_timedelta.py:38 | Complexity: Intermediate | Last updated: 2026-06-02*