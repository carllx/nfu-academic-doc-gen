# How To: Latin Encoding

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test latin encoding

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.io`
- `pandas.io.pytables`

**Setup Required:**
```python
# Fixtures: tmp_path, setup_path, dtype, val
```

## Step-by-Step Guide

### Step 1: Assign enc = 'latin-1'

```python
enc = 'latin-1'
```

### Step 2: Assign nan_rep = ''

```python
nan_rep = ''
```

### Step 3: Assign key = 'data'

```python
key = 'data'
```

### Step 4: Assign val = value

```python
val = [x.decode(enc) if isinstance(x, bytes) else x for x in val]
```

### Step 5: Assign ser = Series(...)

```python
ser = Series(val, dtype=dtype)
```

### Step 6: Assign store = value

```python
store = tmp_path / setup_path
```

### Step 7: Call ser.to_hdf()

```python
ser.to_hdf(store, key=key, format='table', encoding=enc, nan_rep=nan_rep)
```

### Step 8: Assign retr = read_hdf(...)

```python
retr = read_hdf(store, key)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s_nan, retr)
```

### Step 10: Assign s_nan = ser.replace(...)

```python
s_nan = ser.replace(nan_rep, np.nan)
```

### Step 11: Assign s_nan = ser.cat.remove_categories(...)

```python
s_nan = ser.cat.remove_categories([nan_rep])
```

### Step 12: Assign s_nan = ser

```python
s_nan = ser
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path, dtype, val

# Workflow
enc = 'latin-1'
nan_rep = ''
key = 'data'
val = [x.decode(enc) if isinstance(x, bytes) else x for x in val]
ser = Series(val, dtype=dtype)
store = tmp_path / setup_path
ser.to_hdf(store, key=key, format='table', encoding=enc, nan_rep=nan_rep)
retr = read_hdf(store, key)
if dtype == 'category':
    if nan_rep in ser.cat.categories:
        s_nan = ser.cat.remove_categories([nan_rep])
    else:
        s_nan = ser
else:
    s_nan = ser.replace(nan_rep, np.nan)
tm.assert_series_equal(s_nan, retr)
```

## Next Steps


---

*Source: test_file_handling.py:354 | Complexity: Advanced | Last updated: 2026-06-02*