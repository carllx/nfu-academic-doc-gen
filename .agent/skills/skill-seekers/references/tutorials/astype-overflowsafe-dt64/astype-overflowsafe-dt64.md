# How To: Astype Overflowsafe Dt64

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype overflowsafe dt64

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
assert not (wrong == roundtrip).all()
```

### Step 2: Assign dt = np.datetime64(...)

```python
dt = np.datetime64('2262-04-05', 'D')
```

### Step 3: Assign arr = value

```python
arr = dt + np.arange(10, dtype='m8[D]')
```

### Step 4: Assign wrong = arr.astype(...)

```python
wrong = arr.astype(dtype)
```

### Step 5: Assign roundtrip = wrong.astype(...)

```python
roundtrip = wrong.astype(arr.dtype)
```

**Verification:**
```python
assert not (wrong == roundtrip).all()
```

### Step 6: Assign msg = 'Out of bounds nanosecond timestamp'

```python
msg = 'Out of bounds nanosecond timestamp'
```

### Step 7: Assign dtype2 = np.dtype(...)

```python
dtype2 = np.dtype('M8[us]')
```

### Step 8: Assign result = astype_overflowsafe(...)

```python
result = astype_overflowsafe(arr, dtype2)
```

### Step 9: Assign expected = arr.astype(...)

```python
expected = arr.astype(dtype2)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 11: Call astype_overflowsafe()

```python
astype_overflowsafe(arr, dtype)
```


## Complete Example

```python
# Workflow
dtype = np.dtype('M8[ns]')
dt = np.datetime64('2262-04-05', 'D')
arr = dt + np.arange(10, dtype='m8[D]')
wrong = arr.astype(dtype)
roundtrip = wrong.astype(arr.dtype)
assert not (wrong == roundtrip).all()
msg = 'Out of bounds nanosecond timestamp'
with pytest.raises(OutOfBoundsDatetime, match=msg):
    astype_overflowsafe(arr, dtype)
dtype2 = np.dtype('M8[us]')
result = astype_overflowsafe(arr, dtype2)
expected = arr.astype(dtype2)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_np_datetime.py:169 | Complexity: Advanced | Last updated: 2026-06-02*