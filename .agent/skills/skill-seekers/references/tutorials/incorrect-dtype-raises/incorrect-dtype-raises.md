# How To: Incorrect Dtype Raises

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test incorrect dtype raises

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign msg = "dtype 'category' is invalid, should be np.timedelta64 dtype"

```python
msg = "dtype 'category' is invalid, should be np.timedelta64 dtype"
```

### Step 2: Assign msg = "dtype 'int64' is invalid, should be np.timedelta64 dtype"

```python
msg = "dtype 'int64' is invalid, should be np.timedelta64 dtype"
```

### Step 3: Assign msg = "dtype 'datetime64\\[ns\\]' is invalid, should be np.timedelta64 dtype"

```python
msg = "dtype 'datetime64\\[ns\\]' is invalid, should be np.timedelta64 dtype"
```

### Step 4: Assign msg = "dtype 'datetime64\\[us, UTC\\]' is invalid, should be np.timedelta64 dtype"

```python
msg = "dtype 'datetime64\\[us, UTC\\]' is invalid, should be np.timedelta64 dtype"
```

### Step 5: Assign msg = "Supported timedelta64 resolutions are 's', 'ms', 'us', 'ns'"

```python
msg = "Supported timedelta64 resolutions are 's', 'ms', 'us', 'ns'"
```

### Step 6: Call TimedeltaArray._from_sequence()

```python
TimedeltaArray._from_sequence(np.array([1, 2, 3], dtype='i8'), dtype='category')
```

### Step 7: Call TimedeltaArray._from_sequence()

```python
TimedeltaArray._from_sequence(np.array([1, 2, 3], dtype='i8'), dtype=np.dtype('int64'))
```

### Step 8: Call TimedeltaArray._from_sequence()

```python
TimedeltaArray._from_sequence(np.array([1, 2, 3], dtype='i8'), dtype=np.dtype('M8[ns]'))
```

### Step 9: Call TimedeltaArray._from_sequence()

```python
TimedeltaArray._from_sequence(np.array([1, 2, 3], dtype='i8'), dtype='M8[us, UTC]')
```

### Step 10: Call TimedeltaArray._from_sequence()

```python
TimedeltaArray._from_sequence(np.array([1, 2, 3], dtype='i8'), dtype=np.dtype('m8[Y]'))
```


## Complete Example

```python
# Workflow
msg = "dtype 'category' is invalid, should be np.timedelta64 dtype"
with pytest.raises(ValueError, match=msg):
    TimedeltaArray._from_sequence(np.array([1, 2, 3], dtype='i8'), dtype='category')
msg = "dtype 'int64' is invalid, should be np.timedelta64 dtype"
with pytest.raises(ValueError, match=msg):
    TimedeltaArray._from_sequence(np.array([1, 2, 3], dtype='i8'), dtype=np.dtype('int64'))
msg = "dtype 'datetime64\\[ns\\]' is invalid, should be np.timedelta64 dtype"
with pytest.raises(ValueError, match=msg):
    TimedeltaArray._from_sequence(np.array([1, 2, 3], dtype='i8'), dtype=np.dtype('M8[ns]'))
msg = "dtype 'datetime64\\[us, UTC\\]' is invalid, should be np.timedelta64 dtype"
with pytest.raises(ValueError, match=msg):
    TimedeltaArray._from_sequence(np.array([1, 2, 3], dtype='i8'), dtype='M8[us, UTC]')
msg = "Supported timedelta64 resolutions are 's', 'ms', 'us', 'ns'"
with pytest.raises(ValueError, match=msg):
    TimedeltaArray._from_sequence(np.array([1, 2, 3], dtype='i8'), dtype=np.dtype('m8[Y]'))
```

## Next Steps


---

*Source: test_constructors.py:48 | Complexity: Advanced | Last updated: 2026-06-02*