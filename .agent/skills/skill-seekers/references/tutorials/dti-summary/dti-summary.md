# How To: Dti Summary

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti summary

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = DatetimeIndex(...)

```python
idx1 = DatetimeIndex([], freq='D')
```

**Verification:**
```python
assert result == expected
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

### Step 7: Assign exp1 = 'DatetimeIndex: 0 entries\nFreq: D'

```python
exp1 = 'DatetimeIndex: 0 entries\nFreq: D'
```

### Step 8: Assign exp2 = 'DatetimeIndex: 1 entries, 2011-01-01 to 2011-01-01\nFreq: D'

```python
exp2 = 'DatetimeIndex: 1 entries, 2011-01-01 to 2011-01-01\nFreq: D'
```

### Step 9: Assign exp3 = 'DatetimeIndex: 2 entries, 2011-01-01 to 2011-01-02\nFreq: D'

```python
exp3 = 'DatetimeIndex: 2 entries, 2011-01-01 to 2011-01-02\nFreq: D'
```

### Step 10: Assign exp4 = 'DatetimeIndex: 3 entries, 2011-01-01 to 2011-01-03\nFreq: D'

```python
exp4 = 'DatetimeIndex: 3 entries, 2011-01-01 to 2011-01-03\nFreq: D'
```

### Step 11: Assign exp5 = 'DatetimeIndex: 3 entries, 2011-01-01 09:00:00+09:00 to 2011-01-01 11:00:00+09:00\nFreq: h'

```python
exp5 = 'DatetimeIndex: 3 entries, 2011-01-01 09:00:00+09:00 to 2011-01-01 11:00:00+09:00\nFreq: h'
```

### Step 12: Assign exp6 = 'DatetimeIndex: 3 entries, 2011-01-01 09:00:00-05:00 to NaT'

```python
exp6 = 'DatetimeIndex: 3 entries, 2011-01-01 09:00:00-05:00 to NaT'
```

### Step 13: Assign result = idx._summary(...)

```python
result = idx._summary()
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
idx1 = DatetimeIndex([], freq='D')
idx2 = DatetimeIndex(['2011-01-01'], freq='D')
idx3 = DatetimeIndex(['2011-01-01', '2011-01-02'], freq='D')
idx4 = DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'], freq='D')
idx5 = DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], freq='h', tz='Asia/Tokyo')
idx6 = DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', NaT], tz='US/Eastern')
exp1 = 'DatetimeIndex: 0 entries\nFreq: D'
exp2 = 'DatetimeIndex: 1 entries, 2011-01-01 to 2011-01-01\nFreq: D'
exp3 = 'DatetimeIndex: 2 entries, 2011-01-01 to 2011-01-02\nFreq: D'
exp4 = 'DatetimeIndex: 3 entries, 2011-01-01 to 2011-01-03\nFreq: D'
exp5 = 'DatetimeIndex: 3 entries, 2011-01-01 09:00:00+09:00 to 2011-01-01 11:00:00+09:00\nFreq: h'
exp6 = 'DatetimeIndex: 3 entries, 2011-01-01 09:00:00-05:00 to NaT'
for idx, expected in zip([idx1, idx2, idx3, idx4, idx5, idx6], [exp1, exp2, exp3, exp4, exp5, exp6]):
    result = idx._summary()
    assert result == expected
```

## Next Steps


---

*Source: test_formats.py:247 | Complexity: Advanced | Last updated: 2026-06-02*