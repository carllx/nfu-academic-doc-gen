# How To: Nullable Support

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nullable support

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `bz2`
- `datetime`
- `datetime`
- `gzip`
- `io`
- `os`
- `struct`
- `tarfile`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.frame`
- `pandas.io.parsers`
- `pandas.io.stata`

**Setup Required:**
```python
# Fixtures: dtype, version
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': Series([1.0, 2.0, 3.0]), 'b': Series([1, pd.NA, pd.NA], dtype=dtype.name), 'c': Series(['a', 'b', None])})
```

### Step 2: Assign dtype_name = value

```python
dtype_name = df.b.dtype.numpy_dtype.name
```

### Step 3: Assign dtype_name = dtype_name.replace(...)

```python
dtype_name = dtype_name.replace('u', '')
```

### Step 4: Assign value = value

```python
value = StataMissingValue.BASE_MISSING_VALUES[dtype_name]
```

### Step 5: Assign smv = StataMissingValue(...)

```python
smv = StataMissingValue(value)
```

### Step 6: Assign expected_b = Series(...)

```python
expected_b = Series([1, smv, smv], dtype=object, name='b')
```

### Step 7: Assign expected_c = Series(...)

```python
expected_c = Series(['a', 'b', ''], name='c')
```

### Step 8: Assign dtype_name = 'int32'

```python
dtype_name = 'int32'
```

### Step 9: Call df.to_stata()

```python
df.to_stata(path, write_index=False, version=version)
```

### Step 10: Assign reread = read_stata(...)

```python
reread = read_stata(path, convert_missing=True)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df.a, reread.a)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(reread.b, expected_b)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(reread.c, expected_c)
```

### Step 14: Assign dtype_name = 'int8'

```python
dtype_name = 'int8'
```


## Complete Example

```python
# Setup
# Fixtures: dtype, version

# Workflow
df = DataFrame({'a': Series([1.0, 2.0, 3.0]), 'b': Series([1, pd.NA, pd.NA], dtype=dtype.name), 'c': Series(['a', 'b', None])})
dtype_name = df.b.dtype.numpy_dtype.name
dtype_name = dtype_name.replace('u', '')
if dtype_name == 'int64':
    dtype_name = 'int32'
elif dtype_name == 'bool':
    dtype_name = 'int8'
value = StataMissingValue.BASE_MISSING_VALUES[dtype_name]
smv = StataMissingValue(value)
expected_b = Series([1, smv, smv], dtype=object, name='b')
expected_c = Series(['a', 'b', ''], name='c')
with tm.ensure_clean() as path:
    df.to_stata(path, write_index=False, version=version)
    reread = read_stata(path, convert_missing=True)
    tm.assert_series_equal(df.a, reread.a)
    tm.assert_series_equal(reread.b, expected_b)
    tm.assert_series_equal(reread.c, expected_c)
```

## Next Steps


---

*Source: test_stata.py:2356 | Complexity: Advanced | Last updated: 2026-06-02*