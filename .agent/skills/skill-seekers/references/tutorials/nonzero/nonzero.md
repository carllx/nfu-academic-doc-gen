# How To: Nonzero

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nonzero

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
# Fixtures: strings, na_object
```

## Step-by-Step Guide

### Step 1: Assign dtype = get_dtype(...)

```python
dtype = get_dtype(na_object)
```

**Verification:**
```python
assert_array_equal(arr.nonzero()[0], is_nonzero)
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array(strings, dtype=dtype)
```

**Verification:**
```python
assert strings_with_na.nonzero()[0][-1] == 4
```

### Step 3: Assign is_nonzero = np.array(...)

```python
is_nonzero = np.array([i for i, item in enumerate(strings) if len(item) != 0])
```

**Verification:**
```python
assert strings_with_na.nonzero()[0][-1] == 3
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(arr.nonzero()[0], is_nonzero)
```

**Verification:**
```python
assert_array_equal(strings_with_na[strings_with_na.nonzero()], strings_with_na[strings_with_na.astype(bool)])
```

### Step 5: Assign strings_with_na = np.array(...)

```python
strings_with_na = np.array(strings + [na_object], dtype=dtype)
```

### Step 6: Assign is_nan = value

```python
is_nan = np.isnan(np.array([dtype.na_object], dtype=dtype))[0]
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(strings_with_na[strings_with_na.nonzero()], strings_with_na[strings_with_na.astype(bool)])
```

**Verification:**
```python
assert strings_with_na.nonzero()[0][-1] == 4
```


## Complete Example

```python
# Setup
# Fixtures: strings, na_object

# Workflow
dtype = get_dtype(na_object)
arr = np.array(strings, dtype=dtype)
is_nonzero = np.array([i for i, item in enumerate(strings) if len(item) != 0])
assert_array_equal(arr.nonzero()[0], is_nonzero)
if na_object is not pd_NA and na_object == 'unset':
    return
strings_with_na = np.array(strings + [na_object], dtype=dtype)
is_nan = np.isnan(np.array([dtype.na_object], dtype=dtype))[0]
if is_nan:
    assert strings_with_na.nonzero()[0][-1] == 4
else:
    assert strings_with_na.nonzero()[0][-1] == 3
assert_array_equal(strings_with_na[strings_with_na.nonzero()], strings_with_na[strings_with_na.astype(bool)])
```

## Next Steps


---

*Source: test_stringdtype.py:502 | Complexity: Intermediate | Last updated: 2026-06-02*