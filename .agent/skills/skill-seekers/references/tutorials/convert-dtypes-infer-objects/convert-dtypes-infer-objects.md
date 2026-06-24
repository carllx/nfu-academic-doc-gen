# How To: Convert Dtypes Infer Objects

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test convert dtypes infer objects

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pickle`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.pyarrow`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(['a', 'b', 'c'])
```

**Verification:**
```python
assert tm.shares_memory(get_array(ser), get_array(result))
```

### Step 2: Assign ser_orig = ser.copy(...)

```python
ser_orig = ser.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(ser), get_array(result))
```

### Step 3: Assign result = ser.convert_dtypes(...)

```python
result = ser.convert_dtypes(convert_integer=False, convert_boolean=False, convert_floating=False, convert_string=False)
```

### Step 4: Assign unknown = 'x'

```python
result.iloc[0] = 'x'
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, ser_orig)
```

**Verification:**
```python
assert tm.shares_memory(get_array(ser), get_array(result))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
ser = Series(['a', 'b', 'c'])
ser_orig = ser.copy()
result = ser.convert_dtypes(convert_integer=False, convert_boolean=False, convert_floating=False, convert_string=False)
if using_copy_on_write:
    assert tm.shares_memory(get_array(ser), get_array(result))
else:
    assert not np.shares_memory(get_array(ser), get_array(result))
result.iloc[0] = 'x'
tm.assert_series_equal(ser, ser_orig)
```

## Next Steps


---

*Source: test_astype.py:245 | Complexity: Intermediate | Last updated: 2026-06-02*