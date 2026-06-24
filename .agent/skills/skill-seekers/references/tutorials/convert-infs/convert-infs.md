# How To: Convert Infs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test convert infs

## Prerequisites

**Required Modules:**
- `collections`
- `collections`
- `collections.abc`
- `datetime`
- `decimal`
- `fractions`
- `io`
- `itertools`
- `numbers`
- `re`
- `sys`
- `typing`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.core.dtypes`
- `pandas.core.dtypes.cast`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array(['inf', 'inf', 'inf'], dtype='O')
```

**Verification:**
```python
assert result.dtype == np.float64
```

### Step 2: Assign unknown = lib.maybe_convert_numeric(...)

```python
result, _ = lib.maybe_convert_numeric(arr, set(), False)
```

**Verification:**
```python
assert result.dtype == np.float64
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array(['-inf', '-inf', '-inf'], dtype='O')
```

### Step 4: Assign unknown = lib.maybe_convert_numeric(...)

```python
result, _ = lib.maybe_convert_numeric(arr, set(), False)
```

**Verification:**
```python
assert result.dtype == np.float64
```


## Complete Example

```python
# Workflow
arr = np.array(['inf', 'inf', 'inf'], dtype='O')
result, _ = lib.maybe_convert_numeric(arr, set(), False)
assert result.dtype == np.float64
arr = np.array(['-inf', '-inf', '-inf'], dtype='O')
result, _ = lib.maybe_convert_numeric(arr, set(), False)
assert result.dtype == np.float64
```

## Next Steps


---

*Source: test_inference.py:603 | Complexity: Intermediate | Last updated: 2026-06-02*