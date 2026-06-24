# How To: Astype Datetime64

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype datetime64

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = DatetimeIndex(...)

```python
idx = DatetimeIndex(['2016-05-16', 'NaT', NaT, np.nan], dtype='M8[ns]', name='idx')
```

**Verification:**
```python
assert result is not idx
```

### Step 2: Assign result = idx.astype(...)

```python
result = idx.astype('datetime64[ns]')
```

**Verification:**
```python
assert result is idx
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx)
```

**Verification:**
```python
assert result is not idx
```

### Step 4: Assign result = idx.astype(...)

```python
result = idx.astype('datetime64[ns]', copy=False)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx)
```

**Verification:**
```python
assert result is idx
```

### Step 6: Assign idx_tz = DatetimeIndex(...)

```python
idx_tz = DatetimeIndex(['2016-05-16', 'NaT', NaT, np.nan], tz='EST', name='idx')
```

### Step 7: Assign msg = 'Cannot use .astype to convert from timezone-aware'

```python
msg = 'Cannot use .astype to convert from timezone-aware'
```

### Step 8: Assign result = idx_tz.astype(...)

```python
result = idx_tz.astype('datetime64[ns]')
```


## Complete Example

```python
# Workflow
idx = DatetimeIndex(['2016-05-16', 'NaT', NaT, np.nan], dtype='M8[ns]', name='idx')
result = idx.astype('datetime64[ns]')
tm.assert_index_equal(result, idx)
assert result is not idx
result = idx.astype('datetime64[ns]', copy=False)
tm.assert_index_equal(result, idx)
assert result is idx
idx_tz = DatetimeIndex(['2016-05-16', 'NaT', NaT, np.nan], tz='EST', name='idx')
msg = 'Cannot use .astype to convert from timezone-aware'
with pytest.raises(TypeError, match=msg):
    result = idx_tz.astype('datetime64[ns]')
```

## Next Steps


---

*Source: test_astype.py:167 | Complexity: Advanced | Last updated: 2026-06-02*