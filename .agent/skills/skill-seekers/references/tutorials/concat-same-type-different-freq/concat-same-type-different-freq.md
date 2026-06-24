# How To: Concat Same Type Different Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat same type different freq

## Prerequisites

**Required Modules:**
- `__future__`
- `re`
- `warnings`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs.dtypes`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign a = value

```python
a = pd.date_range('2000', periods=2, freq='D', tz='US/Central', unit=unit)._data
```

### Step 2: Assign b = value

```python
b = pd.date_range('2000', periods=2, freq='h', tz='US/Central', unit=unit)._data
```

### Step 3: Assign result = DatetimeArray._concat_same_type(...)

```python
result = DatetimeArray._concat_same_type([a, b])
```

### Step 4: Assign expected = value

```python
expected = pd.to_datetime(['2000-01-01 00:00:00', '2000-01-02 00:00:00', '2000-01-01 00:00:00', '2000-01-01 01:00:00']).tz_localize('US/Central').as_unit(unit)._data
```

### Step 5: Call tm.assert_datetime_array_equal()

```python
tm.assert_datetime_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = pd.date_range('2000', periods=2, freq='D', tz='US/Central', unit=unit)._data
b = pd.date_range('2000', periods=2, freq='h', tz='US/Central', unit=unit)._data
result = DatetimeArray._concat_same_type([a, b])
expected = pd.to_datetime(['2000-01-01 00:00:00', '2000-01-02 00:00:00', '2000-01-01 00:00:00', '2000-01-01 01:00:00']).tz_localize('US/Central').as_unit(unit)._data
tm.assert_datetime_array_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimelike.py:868 | Complexity: Intermediate | Last updated: 2026-06-02*