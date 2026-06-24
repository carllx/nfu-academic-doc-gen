# How To: Put Str Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test put str series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.util`

**Setup Required:**
```python
# Fixtures: setup_path, string_dtype_arguments
```

## Step-by-Step Guide

### Step 1: Assign dtype = pd.StringDtype(...)

```python
dtype = pd.StringDtype(*string_dtype_arguments)
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(['x', pd.NA, 'y'], dtype=dtype)
```

### Step 3: Call _maybe_remove()

```python
_maybe_remove(store, 'df')
```

### Step 4: Call store.put()

```python
store.put('ser', ser)
```

### Step 5: Assign expected_dtype = value

```python
expected_dtype = 'str' if dtype.na_value is np.nan else 'string'
```

### Step 6: Assign expected = ser.astype(...)

```python
expected = ser.astype(expected_dtype)
```

### Step 7: Assign result = store.get(...)

```python
result = store.get('ser')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path, string_dtype_arguments

# Workflow
dtype = pd.StringDtype(*string_dtype_arguments)
ser = Series(['x', pd.NA, 'y'], dtype=dtype)
with ensure_clean_store(setup_path) as store:
    _maybe_remove(store, 'df')
    store.put('ser', ser)
    expected_dtype = 'str' if dtype.na_value is np.nan else 'string'
    expected = ser.astype(expected_dtype)
    result = store.get('ser')
    tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_put.py:250 | Complexity: Advanced | Last updated: 2026-06-02*