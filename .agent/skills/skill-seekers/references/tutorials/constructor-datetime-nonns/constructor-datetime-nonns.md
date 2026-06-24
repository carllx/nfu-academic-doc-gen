# How To: Constructor Datetime Nonns

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor datetime nonns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `sys`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.accessor`
- `pandas.core.base`

**Setup Required:**
```python
# Fixtures: constructor
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array(['2020-01-01T00:00:00.000000'], dtype='datetime64[us]')
```

**Verification:**
```python
assert expected.dtype == arr.dtype
```

### Step 2: Assign dta = pd.core.arrays.DatetimeArray._simple_new(...)

```python
dta = pd.core.arrays.DatetimeArray._simple_new(arr, dtype=arr.dtype)
```

### Step 3: Assign expected = constructor(...)

```python
expected = constructor(dta)
```

**Verification:**
```python
assert expected.dtype == arr.dtype
```

### Step 4: Assign result = constructor(...)

```python
result = constructor(arr)
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 6: Assign arr.flags.writeable = False

```python
arr.flags.writeable = False
```

### Step 7: Assign result = constructor(...)

```python
result = constructor(arr)
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: constructor

# Workflow
arr = np.array(['2020-01-01T00:00:00.000000'], dtype='datetime64[us]')
dta = pd.core.arrays.DatetimeArray._simple_new(arr, dtype=arr.dtype)
expected = constructor(dta)
assert expected.dtype == arr.dtype
result = constructor(arr)
tm.assert_equal(result, expected)
arr.flags.writeable = False
result = constructor(arr)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:167 | Complexity: Advanced | Last updated: 2026-06-02*