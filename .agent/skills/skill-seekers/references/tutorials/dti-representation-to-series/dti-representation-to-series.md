# How To: Dti Representation To Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti representation to series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign idx1 = DatetimeIndex(...)

```python
idx1 = DatetimeIndex([], freq='D')
```

**Verification:**
```python
assert result == expected.replace('[ns', f'[{unit}')
```

### Step 2: Assign idx2 = DatetimeIndex(...)

```python
idx2 = DatetimeIndex(['2011-01-01'], freq='D')
```

### Step 3: Assign idx3 = DatetimeIndex(...)

```python
idx3 = DatetimeIndex(['2011-01-01', '2011-01-02'], freq='D')
```

### Step 4: Assign idx4 = DatetimeIndex(...)

```python
idx4 = DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'], freq='D')
```

### Step 5: Assign idx5 = DatetimeIndex(...)

```python
idx5 = DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], freq='h', tz='Asia/Tokyo')
```

### Step 6: Assign idx6 = DatetimeIndex(...)

```python
idx6 = DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', NaT], tz='US/Eastern')
```

### Step 7: Assign idx7 = DatetimeIndex(...)

```python
idx7 = DatetimeIndex(['2011-01-01 09:00', '2011-01-02 10:15'])
```

### Step 8: Assign exp1 = 'Series([], dtype: datetime64[ns])'

```python
exp1 = 'Series([], dtype: datetime64[ns])'
```

### Step 9: Assign exp2 = '0   2011-01-01\ndtype: datetime64[ns]'

```python
exp2 = '0   2011-01-01\ndtype: datetime64[ns]'
```

### Step 10: Assign exp3 = '0   2011-01-01\n1   2011-01-02\ndtype: datetime64[ns]'

```python
exp3 = '0   2011-01-01\n1   2011-01-02\ndtype: datetime64[ns]'
```

### Step 11: Assign exp4 = '0   2011-01-01\n1   2011-01-02\n2   2011-01-03\ndtype: datetime64[ns]'

```python
exp4 = '0   2011-01-01\n1   2011-01-02\n2   2011-01-03\ndtype: datetime64[ns]'
```

### Step 12: Assign exp5 = '0   2011-01-01 09:00:00+09:00\n1   2011-01-01 10:00:00+09:00\n2   2011-01-01 11:00:00+09:00\ndtype: datetime64[ns, Asia/Tokyo]'

```python
exp5 = '0   2011-01-01 09:00:00+09:00\n1   2011-01-01 10:00:00+09:00\n2   2011-01-01 11:00:00+09:00\ndtype: datetime64[ns, Asia/Tokyo]'
```

### Step 13: Assign exp6 = '0   2011-01-01 09:00:00-05:00\n1   2011-01-01 10:00:00-05:00\n2                         NaT\ndtype: datetime64[ns, US/Eastern]'

```python
exp6 = '0   2011-01-01 09:00:00-05:00\n1   2011-01-01 10:00:00-05:00\n2                         NaT\ndtype: datetime64[ns, US/Eastern]'
```

### Step 14: Assign exp7 = '0   2011-01-01 09:00:00\n1   2011-01-02 10:15:00\ndtype: datetime64[ns]'

```python
exp7 = '0   2011-01-01 09:00:00\n1   2011-01-02 10:15:00\ndtype: datetime64[ns]'
```

### Step 15: Assign ser = Series(...)

```python
ser = Series(idx.as_unit(unit))
```

### Step 16: Assign result = repr(...)

```python
result = repr(ser)
```

**Verification:**
```python
assert result == expected.replace('[ns', f'[{unit}')
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
idx1 = DatetimeIndex([], freq='D')
idx2 = DatetimeIndex(['2011-01-01'], freq='D')
idx3 = DatetimeIndex(['2011-01-01', '2011-01-02'], freq='D')
idx4 = DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'], freq='D')
idx5 = DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], freq='h', tz='Asia/Tokyo')
idx6 = DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', NaT], tz='US/Eastern')
idx7 = DatetimeIndex(['2011-01-01 09:00', '2011-01-02 10:15'])
exp1 = 'Series([], dtype: datetime64[ns])'
exp2 = '0   2011-01-01\ndtype: datetime64[ns]'
exp3 = '0   2011-01-01\n1   2011-01-02\ndtype: datetime64[ns]'
exp4 = '0   2011-01-01\n1   2011-01-02\n2   2011-01-03\ndtype: datetime64[ns]'
exp5 = '0   2011-01-01 09:00:00+09:00\n1   2011-01-01 10:00:00+09:00\n2   2011-01-01 11:00:00+09:00\ndtype: datetime64[ns, Asia/Tokyo]'
exp6 = '0   2011-01-01 09:00:00-05:00\n1   2011-01-01 10:00:00-05:00\n2                         NaT\ndtype: datetime64[ns, US/Eastern]'
exp7 = '0   2011-01-01 09:00:00\n1   2011-01-02 10:15:00\ndtype: datetime64[ns]'
with pd.option_context('display.width', 300):
    for idx, expected in zip([idx1, idx2, idx3, idx4, idx5, idx6, idx7], [exp1, exp2, exp3, exp4, exp5, exp6, exp7]):
        ser = Series(idx.as_unit(unit))
        result = repr(ser)
        assert result == expected.replace('[ns', f'[{unit}')
```

## Next Steps


---

*Source: test_formats.py:190 | Complexity: Advanced | Last updated: 2026-06-02*