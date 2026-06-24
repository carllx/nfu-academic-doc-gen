# How To: Mismatched Values Dtype Units

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mismatched values dtype units

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([1, 2, 3], dtype='m8[s]')
```

### Step 2: Assign dtype = np.dtype(...)

```python
dtype = np.dtype('m8[ns]')
```

### Step 3: Assign msg = 'Values resolution does not match dtype'

```python
msg = 'Values resolution does not match dtype'
```

### Step 4: Assign depr_msg = 'TimedeltaArray.__init__ is deprecated'

```python
depr_msg = 'TimedeltaArray.__init__ is deprecated'
```

### Step 5: Call TimedeltaArray()

```python
TimedeltaArray(arr, dtype=dtype)
```


## Complete Example

```python
# Workflow
arr = np.array([1, 2, 3], dtype='m8[s]')
dtype = np.dtype('m8[ns]')
msg = 'Values resolution does not match dtype'
depr_msg = 'TimedeltaArray.__init__ is deprecated'
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    with pytest.raises(ValueError, match=msg):
        TimedeltaArray(arr, dtype=dtype)
```

## Next Steps


---

*Source: test_constructors.py:81 | Complexity: Intermediate | Last updated: 2026-06-02*