# How To: Setitem Scalar Into Readonly Backing Data

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem scalar into readonly backing data

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `os`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign array = np.zeros(...)

```python
array = np.zeros(5)
```

**Verification:**
```python
assert array[n] == 0
```

### Step 2: Assign array.flags.writeable = False

```python
array.flags.writeable = False
```

### Step 3: Assign series = Series(...)

```python
series = Series(array, copy=False)
```

### Step 4: Assign msg = 'assignment destination is read-only'

```python
msg = 'assignment destination is read-only'
```

**Verification:**
```python
assert array[n] == 0
```

### Step 5: Assign unknown = 1

```python
series[n] = 1
```


## Complete Example

```python
# Workflow
array = np.zeros(5)
array.flags.writeable = False
series = Series(array, copy=False)
for n in series.index:
    msg = 'assignment destination is read-only'
    with pytest.raises(ValueError, match=msg):
        series[n] = 1
    assert array[n] == 0
```

## Next Steps


---

*Source: test_setitem.py:635 | Complexity: Intermediate | Last updated: 2026-06-02*