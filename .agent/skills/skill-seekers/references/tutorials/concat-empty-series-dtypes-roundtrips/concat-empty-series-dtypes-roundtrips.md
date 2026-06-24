# How To: Concat Empty Series Dtypes Roundtrips

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat empty series dtypes roundtrips

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dtype, dtype2
```

## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype(dtype)
```

**Verification:**
```python
assert result.kind == expected
```

### Step 2: Assign dtype2 = np.dtype(...)

```python
dtype2 = np.dtype(dtype2)
```

### Step 3: Assign expected = get_result_type(...)

```python
expected = get_result_type(dtype, dtype2)
```

### Step 4: Assign result = value

```python
result = concat([Series(dtype=dtype), Series(dtype=dtype2)]).dtype
```

**Verification:**
```python
assert result.kind == expected
```

### Step 5: Call pytest.skip()

```python
pytest.skip('same dtype is not applicable for test')
```

### Step 6: Assign typs = value

```python
typs = {dtype.kind, dtype2.kind}
```

### Step 7: Assign typs = value

```python
typs = {dtype.kind, dtype2.kind}
```

### Step 8: Assign result = float_result_type(...)

```python
result = float_result_type(dtype, dtype2)
```

### Step 9: Assign result = int_result_type(...)

```python
result = int_result_type(dtype, dtype2)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, dtype2

# Workflow
if dtype == dtype2:
    pytest.skip('same dtype is not applicable for test')

def int_result_type(dtype, dtype2):
    typs = {dtype.kind, dtype2.kind}
    if not len(typs - {'i', 'u', 'b'}) and (dtype.kind == 'i' or dtype2.kind == 'i'):
        return 'i'
    elif not len(typs - {'u', 'b'}) and (dtype.kind == 'u' or dtype2.kind == 'u'):
        return 'u'
    return None

def float_result_type(dtype, dtype2):
    typs = {dtype.kind, dtype2.kind}
    if not len(typs - {'f', 'i', 'u'}) and (dtype.kind == 'f' or dtype2.kind == 'f'):
        return 'f'
    return None

def get_result_type(dtype, dtype2):
    result = float_result_type(dtype, dtype2)
    if result is not None:
        return result
    result = int_result_type(dtype, dtype2)
    if result is not None:
        return result
    return 'O'
dtype = np.dtype(dtype)
dtype2 = np.dtype(dtype2)
expected = get_result_type(dtype, dtype2)
result = concat([Series(dtype=dtype), Series(dtype=dtype2)]).dtype
assert result.kind == expected
```

## Next Steps


---

*Source: test_empty.py:141 | Complexity: Advanced | Last updated: 2026-06-02*