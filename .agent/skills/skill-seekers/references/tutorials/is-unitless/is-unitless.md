# How To: Is Unitless

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is unitless

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.np_datetime`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dtype = np.dtype(...)

```python
dtype = np.dtype('M8[ns]')
```

**Verification:**
```python
assert not is_unitless(dtype)
```

### Step 2: Assign dtype = np.dtype(...)

```python
dtype = np.dtype('datetime64')
```

**Verification:**
```python
assert is_unitless(dtype)
```

### Step 3: Assign dtype = np.dtype(...)

```python
dtype = np.dtype('m8[ns]')
```

**Verification:**
```python
assert not is_unitless(dtype)
```

### Step 4: Assign dtype = np.dtype(...)

```python
dtype = np.dtype('timedelta64')
```

**Verification:**
```python
assert is_unitless(dtype)
```

### Step 5: Assign msg = 'dtype must be datetime64 or timedelta64'

```python
msg = 'dtype must be datetime64 or timedelta64'
```

### Step 6: Assign msg = "Argument 'dtype' has incorrect type"

```python
msg = "Argument 'dtype' has incorrect type"
```

### Step 7: Call is_unitless()

```python
is_unitless(np.dtype(np.int64))
```

### Step 8: Call is_unitless()

```python
is_unitless('foo')
```


## Complete Example

```python
# Workflow
dtype = np.dtype('M8[ns]')
assert not is_unitless(dtype)
dtype = np.dtype('datetime64')
assert is_unitless(dtype)
dtype = np.dtype('m8[ns]')
assert not is_unitless(dtype)
dtype = np.dtype('timedelta64')
assert is_unitless(dtype)
msg = 'dtype must be datetime64 or timedelta64'
with pytest.raises(ValueError, match=msg):
    is_unitless(np.dtype(np.int64))
msg = "Argument 'dtype' has incorrect type"
with pytest.raises(TypeError, match=msg):
    is_unitless('foo')
```

## Next Steps


---

*Source: test_np_datetime.py:17 | Complexity: Advanced | Last updated: 2026-06-02*