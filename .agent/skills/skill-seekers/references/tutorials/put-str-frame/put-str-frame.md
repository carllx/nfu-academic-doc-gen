# How To: Put Str Frame

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test put str frame

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

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': pd.array(['x', pd.NA, 'y'], dtype=dtype)})
```

### Step 3: Call _maybe_remove()

```python
_maybe_remove(store, 'df')
```

### Step 4: Call store.put()

```python
store.put('df', df)
```

### Step 5: Assign expected_dtype = value

```python
expected_dtype = 'str' if dtype.na_value is np.nan else 'string'
```

### Step 6: Assign expected = df.astype(...)

```python
expected = df.astype(expected_dtype)
```

### Step 7: Assign result = store.get(...)

```python
result = store.get('df')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path, string_dtype_arguments

# Workflow
dtype = pd.StringDtype(*string_dtype_arguments)
df = DataFrame({'a': pd.array(['x', pd.NA, 'y'], dtype=dtype)})
with ensure_clean_store(setup_path) as store:
    _maybe_remove(store, 'df')
    store.put('df', df)
    expected_dtype = 'str' if dtype.na_value is np.nan else 'string'
    expected = df.astype(expected_dtype)
    result = store.get('df')
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_put.py:236 | Complexity: Advanced | Last updated: 2026-06-02*