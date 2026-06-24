# How To: Shift Months

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test shift months

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.conversion`
- `pandas._libs.tslibs.offsets`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: years, months, unit
```

## Step-by-Step Guide

### Step 1: Assign dti = DatetimeIndex.as_unit(...)

```python
dti = DatetimeIndex([Timestamp('2000-01-05 00:15:00'), Timestamp('2000-01-31 00:23:00'), Timestamp('2000-01-01'), Timestamp('2000-02-29'), Timestamp('2000-12-31')]).as_unit(unit)
```

### Step 2: Assign shifted = shift_months(...)

```python
shifted = shift_months(dti.asi8, years * 12 + months, reso=dti._data._creso)
```

### Step 3: Assign shifted_dt64 = shifted.view(...)

```python
shifted_dt64 = shifted.view(f'M8[{dti.unit}]')
```

### Step 4: Assign actual = DatetimeIndex(...)

```python
actual = DatetimeIndex(shifted_dt64)
```

### Step 5: Assign raw = value

```python
raw = [x + pd.offsets.DateOffset(years=years, months=months) for x in dti]
```

### Step 6: Assign expected = DatetimeIndex.as_unit(...)

```python
expected = DatetimeIndex(raw).as_unit(dti.unit)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(actual, expected)
```


## Complete Example

```python
# Setup
# Fixtures: years, months, unit

# Workflow
dti = DatetimeIndex([Timestamp('2000-01-05 00:15:00'), Timestamp('2000-01-31 00:23:00'), Timestamp('2000-01-01'), Timestamp('2000-02-29'), Timestamp('2000-12-31')]).as_unit(unit)
shifted = shift_months(dti.asi8, years * 12 + months, reso=dti._data._creso)
shifted_dt64 = shifted.view(f'M8[{dti.unit}]')
actual = DatetimeIndex(shifted_dt64)
raw = [x + pd.offsets.DateOffset(years=years, months=months) for x in dti]
expected = DatetimeIndex(raw).as_unit(dti.unit)
tm.assert_index_equal(actual, expected)
```

## Next Steps


---

*Source: test_datetime64.py:2392 | Complexity: Intermediate | Last updated: 2026-06-02*