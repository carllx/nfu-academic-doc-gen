# How To: Astype Timedelta64

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype timedelta64

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign idx = TimedeltaIndex(...)

```python
idx = TimedeltaIndex([100000000000000.0, 'NaT', NaT, np.nan])
```

**Verification:**
```python
assert result is not idx
```

### Step 2: Assign msg = "Cannot convert from timedelta64\\[ns\\] to timedelta64. Supported resolutions are 's', 'ms', 'us', 'ns'"

```python
msg = "Cannot convert from timedelta64\\[ns\\] to timedelta64. Supported resolutions are 's', 'ms', 'us', 'ns'"
```

**Verification:**
```python
assert result is idx
```

### Step 3: Assign result = idx.astype(...)

```python
result = idx.astype('timedelta64[ns]')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx)
```

**Verification:**
```python
assert result is not idx
```

### Step 5: Assign result = idx.astype(...)

```python
result = idx.astype('timedelta64[ns]', copy=False)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx)
```

**Verification:**
```python
assert result is idx
```

### Step 7: Call idx.astype()

```python
idx.astype('timedelta64')
```


## Complete Example

```python
# Workflow
idx = TimedeltaIndex([100000000000000.0, 'NaT', NaT, np.nan])
msg = "Cannot convert from timedelta64\\[ns\\] to timedelta64. Supported resolutions are 's', 'ms', 'us', 'ns'"
with pytest.raises(ValueError, match=msg):
    idx.astype('timedelta64')
result = idx.astype('timedelta64[ns]')
tm.assert_index_equal(result, idx)
assert result is not idx
result = idx.astype('timedelta64[ns]', copy=False)
tm.assert_index_equal(result, idx)
assert result is idx
```

## Next Steps


---

*Source: test_astype.py:85 | Complexity: Intermediate | Last updated: 2026-06-02*