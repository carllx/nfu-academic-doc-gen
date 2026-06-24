# How To: Dta Dti

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: dta dti

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `zoneinfo`

**Setup Required:**
```python
# Fixtures: unit, dtype
```

## Step-by-Step Guide

### Step 1: Assign tz = getattr(...)

```python
tz = getattr(dtype, 'tz', None)
```

### Step 2: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('2016-01-01', periods=55, freq='D', tz=tz)
```

### Step 3: Assign dta = DatetimeArray._simple_new(...)

```python
dta = DatetimeArray._simple_new(arr, dtype=dtype)
```

### Step 4: Assign arr = np.asarray.astype(...)

```python
arr = np.asarray(dti).astype(f'M8[{unit}]')
```

### Step 5: Assign arr = np.asarray.astype(...)

```python
arr = np.asarray(dti.tz_convert('UTC').tz_localize(None)).astype(f'M8[{unit}]')
```


## Complete Example

```python
# Setup
# Fixtures: unit, dtype

# Workflow
tz = getattr(dtype, 'tz', None)
dti = pd.date_range('2016-01-01', periods=55, freq='D', tz=tz)
if tz is None:
    arr = np.asarray(dti).astype(f'M8[{unit}]')
else:
    arr = np.asarray(dti.tz_convert('UTC').tz_localize(None)).astype(f'M8[{unit}]')
dta = DatetimeArray._simple_new(arr, dtype=dtype)
return (dta, dti)
```

## Next Steps


---

*Source: test_datetimes.py:45 | Complexity: Intermediate | Last updated: 2026-06-02*