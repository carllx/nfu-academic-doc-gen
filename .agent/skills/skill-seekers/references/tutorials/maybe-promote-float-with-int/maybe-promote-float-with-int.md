# How To: Maybe Promote Float With Int

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test maybe promote float with int

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
# Fixtures: float_numpy_dtype, any_int_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype(float_numpy_dtype)
```

### Step 2: Assign fill_dtype = np.dtype(...)

```python
fill_dtype = np.dtype(any_int_numpy_dtype)
```

### Step 3: Assign fill_value = value

```python
fill_value = np.array([1], dtype=fill_dtype)[0]
```

### Step 4: Assign expected_dtype = dtype

```python
expected_dtype = dtype
```

### Step 5: Assign exp_val_for_scalar = value

```python
exp_val_for_scalar = np.array([fill_value], dtype=expected_dtype)[0]
```

### Step 6: Call _check_promote()

```python
_check_promote(dtype, fill_value, expected_dtype, exp_val_for_scalar)
```


## Complete Example

```python
# Setup
# Fixtures: float_numpy_dtype, any_int_numpy_dtype

# Workflow
dtype = np.dtype(float_numpy_dtype)
fill_dtype = np.dtype(any_int_numpy_dtype)
fill_value = np.array([1], dtype=fill_dtype)[0]
expected_dtype = dtype
exp_val_for_scalar = np.array([fill_value], dtype=expected_dtype)[0]
_check_promote(dtype, fill_value, expected_dtype, exp_val_for_scalar)
```

## Next Steps


---

*Source: test_promote.py:211 | Complexity: Intermediate | Last updated: 2026-06-02*