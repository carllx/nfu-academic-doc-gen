# How To: Integer Array Min Max

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test integer array min max

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: skipna, method, any_int_ea_dtype
```

## Step-by-Step Guide

### Step 1: Assign dtype = any_int_ea_dtype

```python
dtype = any_int_ea_dtype
```

**Verification:**
```python
assert result == (0 if method == 'min' else 1)
```

### Step 2: Assign arr = pd.array(...)

```python
arr = pd.array([0, 1, None], dtype=dtype)
```

**Verification:**
```python
assert result is pd.NA
```

### Step 3: Assign func = getattr(...)

```python
func = getattr(arr, method)
```

### Step 4: Assign result = func(...)

```python
result = func(skipna=skipna)
```

**Verification:**
```python
assert result == (0 if method == 'min' else 1)
```


## Complete Example

```python
# Setup
# Fixtures: skipna, method, any_int_ea_dtype

# Workflow
dtype = any_int_ea_dtype
arr = pd.array([0, 1, None], dtype=dtype)
func = getattr(arr, method)
result = func(skipna=skipna)
if skipna:
    assert result == (0 if method == 'min' else 1)
else:
    assert result is pd.NA
```

## Next Steps


---

*Source: test_function.py:158 | Complexity: Intermediate | Last updated: 2026-06-02*