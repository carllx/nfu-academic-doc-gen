# How To: Self Casts

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test self casts

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `itertools`
- `os`
- `pickle`
- `string`
- `sys`
- `tempfile`
- `pytest`
- `numpy`
- `numpy._core.tests._natype`
- `numpy.dtypes`
- `numpy.testing`
- `numpy.lib._stride_tricks_impl`

**Setup Required:**
```python
# Fixtures: dtype, dtype2, strings
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array(strings, dtype=dtype)
```

**Verification:**
```python
assert newarr[-1] == str(dtype.na_object)
```

### Step 2: Assign newarr = arr.astype(...)

```python
newarr = arr.astype(dtype2)
```

**Verification:**
```python
assert newarr[-1] is dtype2.na_object
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(arr[:-1], newarr[:-1])
```

**Verification:**
```python
assert newarr[-1] == ''
```

### Step 4: Assign strings = value

```python
strings = strings + [dtype.na_object]
```

**Verification:**
```python
assert_array_equal(arr[:-1], newarr[:-1])
```

### Step 5: Assign na1 = value

```python
na1 = dtype.na_object
```

### Step 6: Assign na2 = value

```python
na2 = dtype2.na_object
```

### Step 7: Assign strings = value

```python
strings = strings + ['']
```

### Step 8: Call arr.astype()

```python
arr.astype(dtype2, casting='safe')
```

**Verification:**
```python
assert newarr[-1] is dtype2.na_object
```

### Step 9: Call arr.astype()

```python
arr.astype(dtype2, casting='safe')
```

**Verification:**
```python
assert newarr[-1] == ''
```

### Step 10: Call arr.astype()

```python
arr.astype(dtype2, casting='safe')
```

### Step 11: Call arr.astype()

```python
arr.astype(dtype2, casting='safe')
```

### Step 12: arr[:-1] == newarr[:-1]

```python
arr[:-1] == newarr[:-1]
```


## Complete Example

```python
# Setup
# Fixtures: dtype, dtype2, strings

# Workflow
if hasattr(dtype, 'na_object'):
    strings = strings + [dtype.na_object]
elif hasattr(dtype2, 'na_object'):
    strings = strings + ['']
arr = np.array(strings, dtype=dtype)
newarr = arr.astype(dtype2)
if hasattr(dtype, 'na_object') and (not hasattr(dtype2, 'na_object')):
    assert newarr[-1] == str(dtype.na_object)
    with pytest.raises(TypeError):
        arr.astype(dtype2, casting='safe')
elif hasattr(dtype, 'na_object') and hasattr(dtype2, 'na_object'):
    assert newarr[-1] is dtype2.na_object
    arr.astype(dtype2, casting='safe')
elif hasattr(dtype2, 'na_object'):
    assert newarr[-1] == ''
    arr.astype(dtype2, casting='safe')
else:
    arr.astype(dtype2, casting='safe')
if hasattr(dtype, 'na_object') and hasattr(dtype2, 'na_object'):
    na1 = dtype.na_object
    na2 = dtype2.na_object
    if na1 is not na2 and ((na1 is pd_NA or na2 is pd_NA) or (na1 != na2 and (not (na1 != na1 and na2 != na2)))):
        with pytest.raises(TypeError):
            arr[:-1] == newarr[:-1]
        return
assert_array_equal(arr[:-1], newarr[:-1])
```

## Next Steps


---

*Source: test_stringdtype.py:221 | Complexity: Advanced | Last updated: 2026-06-02*