# How To: Maybe Promote Datetime64 With Any

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test maybe promote datetime64 with any

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
# Fixtures: datetime64_dtype, any_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype(datetime64_dtype)
```

### Step 2: Assign fill_dtype = np.dtype(...)

```python
fill_dtype = np.dtype(any_numpy_dtype)
```

### Step 3: Assign fill_value = value

```python
fill_value = np.array([1], dtype=fill_dtype)[0]
```

### Step 4: Call _check_promote()

```python
_check_promote(dtype, fill_value, expected_dtype, exp_val_for_scalar)
```

### Step 5: Assign expected_dtype = dtype

```python
expected_dtype = dtype
```

### Step 6: Assign exp_val_for_scalar = pd.Timestamp.to_datetime64(...)

```python
exp_val_for_scalar = pd.Timestamp(fill_value).to_datetime64()
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
# Fixtures: datetime64_dtype, any_numpy_dtype

# Workflow
dtype = np.dtype(datetime64_dtype)
fill_dtype = np.dtype(any_numpy_dtype)
fill_value = np.array([1], dtype=fill_dtype)[0]
if fill_dtype.kind == 'M':
    expected_dtype = dtype
    exp_val_for_scalar = pd.Timestamp(fill_value).to_datetime64()
else:
    expected_dtype = np.dtype(object)
    exp_val_for_scalar = fill_value
_check_promote(dtype, fill_value, expected_dtype, exp_val_for_scalar)
```

## Next Steps


---

*Source: test_promote.py:316 | Complexity: Advanced | Last updated: 2026-06-02*