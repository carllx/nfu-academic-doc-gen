# How To: Array Strptime Resolution All Nat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array strptime resolution all nat

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.strptime`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([NaT, np.nan], dtype=object)
```

**Verification:**
```python
assert res.dtype == 'M8[s]'
```

### Step 2: Assign fmt = '%Y-%m-%d %H:%M:%S'

```python
fmt = '%Y-%m-%d %H:%M:%S'
```

**Verification:**
```python
assert res.dtype == 'M8[s]'
```

### Step 3: Assign unknown = array_strptime(...)

```python
res, _ = array_strptime(arr, fmt=fmt, utc=False, creso=creso_infer)
```

**Verification:**
```python
assert res.dtype == 'M8[s]'
```

### Step 4: Assign unknown = array_strptime(...)

```python
res, _ = array_strptime(arr, fmt=fmt, utc=True, creso=creso_infer)
```

**Verification:**
```python
assert res.dtype == 'M8[s]'
```


## Complete Example

```python
# Workflow
arr = np.array([NaT, np.nan], dtype=object)
fmt = '%Y-%m-%d %H:%M:%S'
res, _ = array_strptime(arr, fmt=fmt, utc=False, creso=creso_infer)
assert res.dtype == 'M8[s]'
res, _ = array_strptime(arr, fmt=fmt, utc=True, creso=creso_infer)
assert res.dtype == 'M8[s]'
```

## Next Steps


---

*Source: test_strptime.py:22 | Complexity: Intermediate | Last updated: 2026-06-02*