# How To: Bool Dtype Raises

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bool dtype raises

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

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([1, 2, 3], dtype='bool')
```

### Step 2: Assign depr_msg = 'DatetimeArray.__init__ is deprecated'

```python
depr_msg = 'DatetimeArray.__init__ is deprecated'
```

### Step 3: Assign msg = "Unexpected value for 'dtype': 'bool'. Must be"

```python
msg = "Unexpected value for 'dtype': 'bool'. Must be"
```

### Step 4: Assign msg = 'dtype bool cannot be converted to datetime64\\[ns\\]'

```python
msg = 'dtype bool cannot be converted to datetime64\\[ns\\]'
```

### Step 5: Call DatetimeArray._from_sequence()

```python
DatetimeArray._from_sequence(arr, dtype='M8[ns]')
```

### Step 6: Call pd.DatetimeIndex()

```python
pd.DatetimeIndex(arr)
```

### Step 7: Call pd.to_datetime()

```python
pd.to_datetime(arr)
```

### Step 8: Call DatetimeArray()

```python
DatetimeArray(arr)
```


## Complete Example

```python
# Workflow
arr = np.array([1, 2, 3], dtype='bool')
depr_msg = 'DatetimeArray.__init__ is deprecated'
msg = "Unexpected value for 'dtype': 'bool'. Must be"
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    with pytest.raises(ValueError, match=msg):
        DatetimeArray(arr)
msg = 'dtype bool cannot be converted to datetime64\\[ns\\]'
with pytest.raises(TypeError, match=msg):
    DatetimeArray._from_sequence(arr, dtype='M8[ns]')
with pytest.raises(TypeError, match=msg):
    pd.DatetimeIndex(arr)
with pytest.raises(TypeError, match=msg):
    pd.to_datetime(arr)
```

## Next Steps


---

*Source: test_constructors.py:106 | Complexity: Advanced | Last updated: 2026-06-02*