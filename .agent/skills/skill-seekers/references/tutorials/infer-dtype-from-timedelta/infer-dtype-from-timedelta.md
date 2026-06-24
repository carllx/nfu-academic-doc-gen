# How To: Infer Dtype From Timedelta

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test infer dtype from timedelta

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas.core.dtypes.common`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign td64 = np.timedelta64(...)

```python
td64 = np.timedelta64(1, 'ns')
```

**Verification:**
```python
assert dtype == 'm8[ns]'
```

### Step 2: Assign unknown = infer_dtype_from_scalar(...)

```python
dtype, val = infer_dtype_from_scalar(td64)
```

**Verification:**
```python
assert dtype == 'm8[us]'
```

### Step 3: Assign pytd = timedelta(...)

```python
pytd = timedelta(1)
```

**Verification:**
```python
assert dtype == 'm8[ns]'
```

### Step 4: Assign unknown = infer_dtype_from_scalar(...)

```python
dtype, val = infer_dtype_from_scalar(pytd)
```

**Verification:**
```python
assert dtype == 'm8[us]'
```

### Step 5: Assign td = Timedelta(...)

```python
td = Timedelta(1)
```

### Step 6: Assign unknown = infer_dtype_from_scalar(...)

```python
dtype, val = infer_dtype_from_scalar(td)
```

**Verification:**
```python
assert dtype == 'm8[ns]'
```


## Complete Example

```python
# Workflow
td64 = np.timedelta64(1, 'ns')
dtype, val = infer_dtype_from_scalar(td64)
assert dtype == 'm8[ns]'
pytd = timedelta(1)
dtype, val = infer_dtype_from_scalar(pytd)
assert dtype == 'm8[us]'
td = Timedelta(1)
dtype, val = infer_dtype_from_scalar(td)
assert dtype == 'm8[ns]'
```

## Next Steps


---

*Source: test_infer_dtype.py:78 | Complexity: Intermediate | Last updated: 2026-06-02*