# How To: Resample How

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test resample how

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
# Fixtures: series, downsample_method, unit
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

### Step 8: Assign expected = s.groupby.agg(...)

```python
expected = s.groupby(grouplist).agg(downsample_method)
```

### Step 9: Assign expected.index = date_range.as_unit(...)

```python
expected.index = date_range('1/1/2000', periods=4, freq='5min', name='index').as_unit(unit)
```

### Step 10: Assign result = getattr(...)

```python
result = getattr(s.resample('5min', closed='right', label='right'), downsample_method)()
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Call pytest.skip()

```python
pytest.skip('covered by test_resample_how_ohlc')
```


## Complete Example

```python
# Setup
# Fixtures: series, downsample_method, unit

# Workflow
if downsample_method == 'ohlc':
    pytest.skip('covered by test_resample_how_ohlc')
s = series
s.index = s.index.as_unit(unit)
grouplist = np.ones_like(s)
grouplist[0] = 0
grouplist[1:6] = 1
grouplist[6:11] = 2
grouplist[11:] = 3
expected = s.groupby(grouplist).agg(downsample_method)
expected.index = date_range('1/1/2000', periods=4, freq='5min', name='index').as_unit(unit)
result = getattr(s.resample('5min', closed='right', label='right'), downsample_method)()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime_index.py:208 | Complexity: Advanced | Last updated: 2026-06-02*