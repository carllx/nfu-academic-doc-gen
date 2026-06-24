# How To: Resample Upsampling Picked But Not Correct

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resample upsampling picked but not correct

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
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign dates = date_range.as_unit(...)

```python
dates = date_range('01-Jan-2014', '05-Jan-2014', freq='D').as_unit(unit)
```

**Verification:**
```python
assert result.index[0] == dates[0]
```

### Step 2: Assign series = Series(...)

```python
series = Series(1, index=dates)
```

### Step 3: Assign result = series.resample.mean(...)

```python
result = series.resample('D').mean()
```

**Verification:**
```python
assert result.index[0] == dates[0]
```

### Step 4: Assign s = Series(...)

```python
s = Series(np.arange(1.0, 6), index=[datetime(1975, 1, i, 12, 0) for i in range(1, 6)])
```

### Step 5: Assign s.index = s.index.as_unit(...)

```python
s.index = s.index.as_unit(unit)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(np.arange(1.0, 6), index=date_range('19750101', periods=5, freq='D').as_unit(unit))
```

### Step 7: Assign result = s.resample.count(...)

```python
result = s.resample('D').count()
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, Series(1, index=expected.index))
```

### Step 9: Assign result1 = s.resample.sum(...)

```python
result1 = s.resample('D').sum()
```

### Step 10: Assign result2 = s.resample.mean(...)

```python
result2 = s.resample('D').mean()
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result1, expected)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result2, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
dates = date_range('01-Jan-2014', '05-Jan-2014', freq='D').as_unit(unit)
series = Series(1, index=dates)
result = series.resample('D').mean()
assert result.index[0] == dates[0]
s = Series(np.arange(1.0, 6), index=[datetime(1975, 1, i, 12, 0) for i in range(1, 6)])
s.index = s.index.as_unit(unit)
expected = Series(np.arange(1.0, 6), index=date_range('19750101', periods=5, freq='D').as_unit(unit))
result = s.resample('D').count()
tm.assert_series_equal(result, Series(1, index=expected.index))
result1 = s.resample('D').sum()
result2 = s.resample('D').mean()
tm.assert_series_equal(result1, expected)
tm.assert_series_equal(result2, expected)
```

## Next Steps


---

*Source: test_datetime_index.py:407 | Complexity: Advanced | Last updated: 2026-06-02*