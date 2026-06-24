# How To: Resample How Ohlc

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test resample how ohlc

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._typing`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.resample`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: series, unit
```

## Step-by-Step Guide

### Step 1: Assign s = series

```python
s = series
```

### Step 2: Assign s.index = s.index.as_unit(...)

```python
s.index = s.index.as_unit(unit)
```

### Step 3: Assign grouplist = np.ones_like(...)

```python
grouplist = np.ones_like(s)
```

### Step 4: Assign unknown = 0

```python
grouplist[0] = 0
```

### Step 5: Assign unknown = 1

```python
grouplist[1:6] = 1
```

### Step 6: Assign unknown = 2

```python
grouplist[6:11] = 2
```

### Step 7: Assign unknown = 3

```python
grouplist[11:] = 3
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame(s.groupby(grouplist).agg(_ohlc).values.tolist(), index=date_range('1/1/2000', periods=4, freq='5min', name='index').as_unit(unit), columns=['open', 'high', 'low', 'close'])
```

### Step 9: Assign result = s.resample.ohlc(...)

```python
result = s.resample('5min', closed='right', label='right').ohlc()
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: series, unit

# Workflow
s = series
s.index = s.index.as_unit(unit)
grouplist = np.ones_like(s)
grouplist[0] = 0
grouplist[1:6] = 1
grouplist[6:11] = 2
grouplist[11:] = 3

def _ohlc(group):
    if isna(group).all():
        return np.repeat(np.nan, 4)
    return [group.iloc[0], group.max(), group.min(), group.iloc[-1]]
expected = DataFrame(s.groupby(grouplist).agg(_ohlc).values.tolist(), index=date_range('1/1/2000', periods=4, freq='5min', name='index').as_unit(unit), columns=['open', 'high', 'low', 'close'])
result = s.resample('5min', closed='right', label='right').ohlc()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime_index.py:234 | Complexity: Advanced | Last updated: 2026-06-02*