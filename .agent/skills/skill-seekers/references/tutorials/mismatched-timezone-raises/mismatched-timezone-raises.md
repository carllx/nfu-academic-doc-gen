# How To: Mismatched Timezone Raises

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mismatched timezone raises

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign depr_msg = 'DatetimeArray.__init__ is deprecated'

```python
depr_msg = 'DatetimeArray.__init__ is deprecated'
```

### Step 2: Assign dtype = DatetimeTZDtype(...)

```python
dtype = DatetimeTZDtype(tz='US/Eastern')
```

### Step 3: Assign msg = 'dtype=datetime64\\[ns.*\\] does not match data dtype datetime64\\[ns.*\\]'

```python
msg = 'dtype=datetime64\\[ns.*\\] does not match data dtype datetime64\\[ns.*\\]'
```

### Step 4: Assign arr = DatetimeArray(...)

```python
arr = DatetimeArray(np.array(['2000-01-01T06:00:00'], dtype='M8[ns]'), dtype=DatetimeTZDtype(tz='US/Central'))
```

### Step 5: Call DatetimeArray()

```python
DatetimeArray(arr, dtype=dtype)
```

### Step 6: Call DatetimeArray()

```python
DatetimeArray(arr, dtype=np.dtype('M8[ns]'))
```

### Step 7: Call DatetimeArray()

```python
DatetimeArray(arr.tz_localize(None), dtype=arr.dtype)
```


## Complete Example

```python
# Workflow
depr_msg = 'DatetimeArray.__init__ is deprecated'
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    arr = DatetimeArray(np.array(['2000-01-01T06:00:00'], dtype='M8[ns]'), dtype=DatetimeTZDtype(tz='US/Central'))
dtype = DatetimeTZDtype(tz='US/Eastern')
msg = 'dtype=datetime64\\[ns.*\\] does not match data dtype datetime64\\[ns.*\\]'
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    with pytest.raises(TypeError, match=msg):
        DatetimeArray(arr, dtype=dtype)
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    with pytest.raises(TypeError, match=msg):
        DatetimeArray(arr, dtype=np.dtype('M8[ns]'))
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    with pytest.raises(TypeError, match=msg):
        DatetimeArray(arr.tz_localize(None), dtype=arr.dtype)
```

## Next Steps


---

*Source: test_constructors.py:79 | Complexity: Intermediate | Last updated: 2026-06-02*