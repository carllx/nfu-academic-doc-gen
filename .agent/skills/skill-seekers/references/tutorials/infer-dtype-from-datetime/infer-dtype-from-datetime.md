# How To: Infer Dtype From Datetime

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test infer dtype from datetime

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas.core.dtypes.common`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign dt64 = np.datetime64(...)

```python
dt64 = np.datetime64(1, 'ns')
```

**Verification:**
```python
assert dtype == 'M8[ns]'
```

### Step 2: Assign unknown = infer_dtype_from_scalar(...)

```python
dtype, val = infer_dtype_from_scalar(dt64)
```

**Verification:**
```python
assert dtype == 'M8[ns]'
```

### Step 3: Assign ts = Timestamp(...)

```python
ts = Timestamp(1)
```

**Verification:**
```python
assert dtype == 'M8[us]'
```

### Step 4: Assign unknown = infer_dtype_from_scalar(...)

```python
dtype, val = infer_dtype_from_scalar(ts)
```

**Verification:**
```python
assert dtype == 'M8[ns]'
```

### Step 5: Assign dt = datetime(...)

```python
dt = datetime(2000, 1, 1, 0, 0)
```

### Step 6: Assign unknown = infer_dtype_from_scalar(...)

```python
dtype, val = infer_dtype_from_scalar(dt)
```

**Verification:**
```python
assert dtype == 'M8[us]'
```


## Complete Example

```python
# Workflow
dt64 = np.datetime64(1, 'ns')
dtype, val = infer_dtype_from_scalar(dt64)
assert dtype == 'M8[ns]'
ts = Timestamp(1)
dtype, val = infer_dtype_from_scalar(ts)
assert dtype == 'M8[ns]'
dt = datetime(2000, 1, 1, 0, 0)
dtype, val = infer_dtype_from_scalar(dt)
assert dtype == 'M8[us]'
```

## Next Steps


---

*Source: test_infer_dtype.py:64 | Complexity: Intermediate | Last updated: 2026-06-02*