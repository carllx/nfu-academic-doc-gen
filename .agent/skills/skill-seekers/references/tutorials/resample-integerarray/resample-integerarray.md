# How To: Resample Integerarray

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resample integerarray

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

### Step 1: Assign ts = Series(...)

```python
ts = Series(range(9), index=date_range('1/1/2000', periods=9, freq='min').as_unit(unit), dtype='Int64')
```

### Step 2: Assign result = ts.resample.sum(...)

```python
result = ts.resample('3min').sum()
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([3, 12, 21], index=date_range('1/1/2000', periods=3, freq='3min').as_unit(unit), dtype='Int64')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = ts.resample.mean(...)

```python
result = ts.resample('3min').mean()
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([1, 4, 7], index=date_range('1/1/2000', periods=3, freq='3min').as_unit(unit), dtype='Float64')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
ts = Series(range(9), index=date_range('1/1/2000', periods=9, freq='min').as_unit(unit), dtype='Int64')
result = ts.resample('3min').sum()
expected = Series([3, 12, 21], index=date_range('1/1/2000', periods=3, freq='3min').as_unit(unit), dtype='Int64')
tm.assert_series_equal(result, expected)
result = ts.resample('3min').mean()
expected = Series([1, 4, 7], index=date_range('1/1/2000', periods=3, freq='3min').as_unit(unit), dtype='Float64')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime_index.py:154 | Complexity: Intermediate | Last updated: 2026-06-02*