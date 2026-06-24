# How To: Maybe Promote Any Numpy Dtype With Datetimetz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test maybe promote any numpy dtype with datetimetz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.cast`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas.core.dtypes.missing`
- `pandas`

**Setup Required:**
```python
# Fixtures: any_numpy_dtype, tz_aware_fixture, fill_value
```

## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype(any_numpy_dtype)
```

### Step 2: Assign fill_dtype = DatetimeTZDtype(...)

```python
fill_dtype = DatetimeTZDtype(tz=tz_aware_fixture)
```

### Step 3: Assign fill_value = value

```python
fill_value = pd.Series([fill_value], dtype=fill_dtype)[0]
```

### Step 4: Assign expected_dtype = np.dtype(...)

```python
expected_dtype = np.dtype(object)
```

### Step 5: Assign exp_val_for_scalar = fill_value

```python
exp_val_for_scalar = fill_value
```

### Step 6: Call _check_promote()

```python
_check_promote(dtype, fill_value, expected_dtype, exp_val_for_scalar)
```


## Complete Example

```python
# Setup
# Fixtures: any_numpy_dtype, tz_aware_fixture, fill_value

# Workflow
dtype = np.dtype(any_numpy_dtype)
fill_dtype = DatetimeTZDtype(tz=tz_aware_fixture)
fill_value = pd.Series([fill_value], dtype=fill_dtype)[0]
expected_dtype = np.dtype(object)
exp_val_for_scalar = fill_value
_check_promote(dtype, fill_value, expected_dtype, exp_val_for_scalar)
```

## Next Steps


---

*Source: test_promote.py:375 | Complexity: Intermediate | Last updated: 2026-06-02*