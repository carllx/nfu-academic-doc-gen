# How To: Ensure Timedelta64Ns Overflows

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ensure timedelta64ns overflows

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = value

```python
arr = np.arange(10).astype('m8[Y]') * 100
```

### Step 2: Assign msg = 'Cannot convert 300 years to timedelta64\\[ns\\] without overflow'

```python
msg = 'Cannot convert 300 years to timedelta64\\[ns\\] without overflow'
```

### Step 3: Call astype_overflowsafe()

```python
astype_overflowsafe(arr, dtype=np.dtype('m8[ns]'))
```


## Complete Example

```python
# Workflow
arr = np.arange(10).astype('m8[Y]') * 100
msg = 'Cannot convert 300 years to timedelta64\\[ns\\] without overflow'
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    astype_overflowsafe(arr, dtype=np.dtype('m8[ns]'))
```

## Next Steps


---

*Source: test_conversion.py:128 | Complexity: Beginner | Last updated: 2026-06-02*