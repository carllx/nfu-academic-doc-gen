# How To: Day Attribute Non Nano Beyond Int32

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test day attribute non nano beyond int32

## Prerequisites

**Required Modules:**
- `calendar`
- `datetime`
- `locale`
- `unicodedata`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.timezones`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.indexes.accessors`


## Step-by-Step Guide

### Step 1: Assign data = np.array(...)

```python
data = np.array([136457654736252, 134736784364431, 245345345545332, 223432411, 2343241, 3634548734, 23234], dtype='timedelta64[s]')
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(data)
```

### Step 3: Assign result = value

```python
result = ser.dt.days
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1579371003, 1559453522, 2839645203, 2586, 27, 42066, 0])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = np.array([136457654736252, 134736784364431, 245345345545332, 223432411, 2343241, 3634548734, 23234], dtype='timedelta64[s]')
ser = Series(data)
result = ser.dt.days
expected = Series([1579371003, 1559453522, 2839645203, 2586, 27, 42066, 0])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_dt_accessor.py:826 | Complexity: Intermediate | Last updated: 2026-06-02*