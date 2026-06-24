# How To: Resample Entirely Nat Window

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test resample entirely nat window

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.indexes.datetimes`

**Setup Required:**
```python
# Fixtures: method, method_args, unit
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([0] * 2 + [np.nan] * 2, index=date_range('2017', periods=4))
```

### Step 2: Assign result = methodcaller(...)

```python
result = methodcaller(method, **method_args)(ser.resample('2d'))
```

### Step 3: Assign exp_dti = pd.DatetimeIndex(...)

```python
exp_dti = pd.DatetimeIndex(['2017-01-01', '2017-01-03'], dtype='M8[ns]', freq='2D')
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([0.0, unit], index=exp_dti)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: method, method_args, unit

# Workflow
ser = Series([0] * 2 + [np.nan] * 2, index=date_range('2017', periods=4))
result = methodcaller(method, **method_args)(ser.resample('2d'))
exp_dti = pd.DatetimeIndex(['2017-01-01', '2017-01-03'], dtype='M8[ns]', freq='2D')
expected = Series([0.0, unit], index=exp_dti)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_time_grouper.py:198 | Complexity: Intermediate | Last updated: 2026-06-02*