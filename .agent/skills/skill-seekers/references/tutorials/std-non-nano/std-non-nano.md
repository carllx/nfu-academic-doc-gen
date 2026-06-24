# How To: Std Non Nano

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test std non nano

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
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('2016-01-01', periods=55, freq='D')
```

**Verification:**
```python
assert res._creso == dta._creso
```

### Step 2: Assign arr = np.asarray.astype(...)

```python
arr = np.asarray(dti).astype(f'M8[{unit}]')
```

**Verification:**
```python
assert res == dti.std().floor(unit)
```

### Step 3: Assign dta = DatetimeArray._simple_new(...)

```python
dta = DatetimeArray._simple_new(arr, dtype=arr.dtype)
```

### Step 4: Assign res = dta.std(...)

```python
res = dta.std()
```

**Verification:**
```python
assert res._creso == dta._creso
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
dti = pd.date_range('2016-01-01', periods=55, freq='D')
arr = np.asarray(dti).astype(f'M8[{unit}]')
dta = DatetimeArray._simple_new(arr, dtype=arr.dtype)
res = dta.std()
assert res._creso == dta._creso
assert res == dti.std().floor(unit)
```

## Next Steps


---

*Source: test_datetimes.py:111 | Complexity: Intermediate | Last updated: 2026-06-02*