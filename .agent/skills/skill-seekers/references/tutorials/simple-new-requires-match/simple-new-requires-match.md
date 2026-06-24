# How To: Simple New Requires Match

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simple new requires match

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

### Step 1: Assign arr = np.arange.view(...)

```python
arr = np.arange(5, dtype=np.int64).view(f'M8[{unit}]')
```

**Verification:**
```python
assert dta.dtype == dtype
```

### Step 2: Assign dtype = DatetimeTZDtype(...)

```python
dtype = DatetimeTZDtype(unit, 'UTC')
```

### Step 3: Assign dta = DatetimeArray._simple_new(...)

```python
dta = DatetimeArray._simple_new(arr, dtype=dtype)
```

**Verification:**
```python
assert dta.dtype == dtype
```

### Step 4: Assign wrong = DatetimeTZDtype(...)

```python
wrong = DatetimeTZDtype('ns', 'UTC')
```

### Step 5: Call DatetimeArray._simple_new()

```python
DatetimeArray._simple_new(arr, dtype=wrong)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
arr = np.arange(5, dtype=np.int64).view(f'M8[{unit}]')
dtype = DatetimeTZDtype(unit, 'UTC')
dta = DatetimeArray._simple_new(arr, dtype=dtype)
assert dta.dtype == dtype
wrong = DatetimeTZDtype('ns', 'UTC')
with pytest.raises(AssertionError, match=''):
    DatetimeArray._simple_new(arr, dtype=wrong)
```

## Next Steps


---

*Source: test_datetimes.py:100 | Complexity: Intermediate | Last updated: 2026-06-02*