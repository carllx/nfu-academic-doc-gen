# How To: Maybe Promote Any With Datetime64

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test maybe promote any with datetime64

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
# Fixtures: any_numpy_dtype, fill_value
```

## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype(any_numpy_dtype)
```

### Step 2: Call _check_promote()

```python
_check_promote(dtype, fill_value, expected_dtype, exp_val_for_scalar)
```

### Step 3: Assign expected_dtype = dtype

```python
expected_dtype = dtype
```

### Step 4: Assign exp_val_for_scalar = pd.Timestamp.to_datetime64(...)

```python
exp_val_for_scalar = pd.Timestamp(fill_value).to_datetime64()
```

### Step 5: Assign expected_dtype = np.dtype(...)

```python
expected_dtype = np.dtype(object)
```

### Step 6: Assign exp_val_for_scalar = fill_value

```python
exp_val_for_scalar = fill_value
```

### Step 7: Assign expected_dtype = np.dtype(...)

```python
expected_dtype = np.dtype(object)
```

### Step 8: Assign exp_val_for_scalar = fill_value

```python
exp_val_for_scalar = fill_value
```


## Complete Example

```python
# Setup
# Fixtures: any_numpy_dtype, fill_value

# Workflow
dtype = np.dtype(any_numpy_dtype)
if dtype.kind == 'M':
    expected_dtype = dtype
    exp_val_for_scalar = pd.Timestamp(fill_value).to_datetime64()
else:
    expected_dtype = np.dtype(object)
    exp_val_for_scalar = fill_value
if type(fill_value) is datetime.date and dtype.kind == 'M':
    expected_dtype = np.dtype(object)
    exp_val_for_scalar = fill_value
_check_promote(dtype, fill_value, expected_dtype, exp_val_for_scalar)
```

## Next Steps


---

*Source: test_promote.py:345 | Complexity: Advanced | Last updated: 2026-06-02*