# How To: Merge Asof Pyarrow Td Tolerance

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge asof pyarrow td tolerance

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series([datetime.datetime(2023, 1, 1)], dtype='timestamp[us, UTC][pyarrow]')
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'timestamp': ser, 'value': [1]})
```

### Step 3: Assign result = merge_asof(...)

```python
result = merge_asof(df, df, on='timestamp', tolerance=Timedelta('1s'))
```

### Step 4: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'timestamp': ser, 'value_x': [1], 'value_y': [1]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = pd.Series([datetime.datetime(2023, 1, 1)], dtype='timestamp[us, UTC][pyarrow]')
df = pd.DataFrame({'timestamp': ser, 'value': [1]})
result = merge_asof(df, df, on='timestamp', tolerance=Timedelta('1s'))
expected = pd.DataFrame({'timestamp': ser, 'value_x': [1], 'value_y': [1]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge_asof.py:3585 | Complexity: Intermediate | Last updated: 2026-06-02*