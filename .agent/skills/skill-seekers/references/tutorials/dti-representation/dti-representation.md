# How To: Dti Representation

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti representation

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

### Step 1: Assign idxs = value

```python
idxs = []
```

**Verification:**
```python
assert result == expected
```

### Step 2: Call idxs.append()

```python
idxs.append(DatetimeIndex([], freq='D'))
```

**Verification:**
```python
assert result == expected
```

### Step 3: Call idxs.append()

```python
idxs.append(DatetimeIndex(['2011-01-01'], freq='D'))
```

### Step 4: Call idxs.append()

```python
idxs.append(DatetimeIndex(['2011-01-01', '2011-01-02'], freq='D'))
```

### Step 5: Call idxs.append()

```python
idxs.append(DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'], freq='D'))
```

### Step 6: Call idxs.append()

```python
idxs.append(DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], freq='h', tz='Asia/Tokyo'))
```

### Step 7: Call idxs.append()

```python
idxs.append(DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', NaT], tz='US/Eastern'))
```

### Step 8: Call idxs.append()

```python
idxs.append(DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', NaT], tz='UTC'))
```

### Step 9: Assign exp = value

```python
exp = []
```

### Step 10: Call exp.append()

```python
exp.append("DatetimeIndex([], dtype='datetime64[ns]', freq='D')")
```

### Step 11: Call exp.append()

```python
exp.append("DatetimeIndex(['2011-01-01'], dtype='datetime64[ns]', freq='D')")
```

### Step 12: Call exp.append()

```python
exp.append("DatetimeIndex(['2011-01-01', '2011-01-02'], dtype='datetime64[ns]', freq='D')")
```

### Step 13: Call exp.append()

```python
exp.append("DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'], dtype='datetime64[ns]', freq='D')")
```

### Step 14: Call exp.append()

```python
exp.append("DatetimeIndex(['2011-01-01 09:00:00+09:00', '2011-01-01 10:00:00+09:00', '2011-01-01 11:00:00+09:00'], dtype='datetime64[ns, Asia/Tokyo]', freq='h')")
```

### Step 15: Call exp.append()

```python
exp.append("DatetimeIndex(['2011-01-01 09:00:00-05:00', '2011-01-01 10:00:00-05:00', 'NaT'], dtype='datetime64[ns, US/Eastern]', freq=None)")
```

### Step 16: Call exp.append()

```python
exp.append("DatetimeIndex(['2011-01-01 09:00:00+00:00', '2011-01-01 10:00:00+00:00', 'NaT'], dtype='datetime64[ns, UTC]', freq=None)")
```

### Step 17: Assign index = index.as_unit(...)

```python
index = index.as_unit(unit)
```

### Step 18: Assign expected = expected.replace(...)

```python
expected = expected.replace('[ns', f'[{unit}')
```

### Step 19: Assign result = repr(...)

```python
result = repr(index)
```

**Verification:**
```python
assert result == expected
```

### Step 20: Assign result = str(...)

```python
result = str(index)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
idxs = []
idxs.append(DatetimeIndex([], freq='D'))
idxs.append(DatetimeIndex(['2011-01-01'], freq='D'))
idxs.append(DatetimeIndex(['2011-01-01', '2011-01-02'], freq='D'))
idxs.append(DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'], freq='D'))
idxs.append(DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], freq='h', tz='Asia/Tokyo'))
idxs.append(DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', NaT], tz='US/Eastern'))
idxs.append(DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', NaT], tz='UTC'))
exp = []
exp.append("DatetimeIndex([], dtype='datetime64[ns]', freq='D')")
exp.append("DatetimeIndex(['2011-01-01'], dtype='datetime64[ns]', freq='D')")
exp.append("DatetimeIndex(['2011-01-01', '2011-01-02'], dtype='datetime64[ns]', freq='D')")
exp.append("DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'], dtype='datetime64[ns]', freq='D')")
exp.append("DatetimeIndex(['2011-01-01 09:00:00+09:00', '2011-01-01 10:00:00+09:00', '2011-01-01 11:00:00+09:00'], dtype='datetime64[ns, Asia/Tokyo]', freq='h')")
exp.append("DatetimeIndex(['2011-01-01 09:00:00-05:00', '2011-01-01 10:00:00-05:00', 'NaT'], dtype='datetime64[ns, US/Eastern]', freq=None)")
exp.append("DatetimeIndex(['2011-01-01 09:00:00+00:00', '2011-01-01 10:00:00+00:00', 'NaT'], dtype='datetime64[ns, UTC]', freq=None)")
with pd.option_context('display.width', 300):
    for index, expected in zip(idxs, exp):
        index = index.as_unit(unit)
        expected = expected.replace('[ns', f'[{unit}')
        result = repr(index)
        assert result == expected
        result = str(index)
        assert result == expected
```

## Next Steps


---

*Source: test_formats.py:130 | Complexity: Advanced | Last updated: 2026-06-02*