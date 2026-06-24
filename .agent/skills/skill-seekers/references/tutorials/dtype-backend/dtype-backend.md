# How To: Dtype Backend

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dtype backend

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `io`
- `os`
- `pathlib`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._config.config`
- `pandas.compat`
- `pandas.compat.pyarrow`
- `pandas`
- `pandas._testing`
- `pandas.util.version`
- `pandas.io.parquet`
- `pyarrow`
- `fastparquet`
- `pyarrow.dataset`
- `pandas.compat._optional`
- `pyarrow`
- `pyarrow`
- `pyarrow`
- `pyarrow`
- `pyarrow`
- `pyarrow.parquet`
- `fastparquet`
- `fastparquet`
- `fastparquet`
- `fastparquet`
- `fastparquet`
- `pytz`

**Setup Required:**
```python
# Fixtures: engine, request
```

## Step-by-Step Guide

### Step 1: Assign pq = pytest.importorskip(...)

```python
pq = pytest.importorskip('pyarrow.parquet')
```

**Verification:**
```python
assert result1['a'].dtype == np.dtype('float64')
```

### Step 2: Assign table = pyarrow.table(...)

```python
table = pyarrow.table({'a': pyarrow.array([1, 2, 3, None], 'int64'), 'b': pyarrow.array([1, 2, 3, None], 'uint8'), 'c': pyarrow.array(['a', 'b', 'c', None]), 'd': pyarrow.array([True, False, True, None]), 'e': pyarrow.array([1, 2, 3, 4], 'int64'), 'f': pyarrow.array([1.0, 2.0, 3.0, None], 'float32'), 'g': pyarrow.array([1.0, 2.0, 3.0, None], 'float64')})
```

**Verification:**
```python
assert result1['a'].dtype == np.dtype('float64')
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': pd.array([1, 2, 3, None], dtype='Int64'), 'b': pd.array([1, 2, 3, None], dtype='UInt8'), 'c': pd.array(['a', 'b', 'c', None], dtype='string'), 'd': pd.array([True, False, True, None], dtype='boolean'), 'e': pd.array([1, 2, 3, 4], dtype='Int64'), 'f': pd.array([1.0, 2.0, 3.0, None], dtype='Float32'), 'g': pd.array([1.0, 2.0, 3.0, None], dtype='Float64')})
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result2, expected)
```

### Step 5: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='Fastparquet nullable dtype support is disabled')
```

### Step 6: Call request.applymarker()

```python
request.applymarker(mark)
```

### Step 7: Call pq.write_table()

```python
pq.write_table(table, path)
```

### Step 8: Assign result1 = read_parquet(...)

```python
result1 = read_parquet(path, engine=engine)
```

### Step 9: Assign result2 = read_parquet(...)

```python
result2 = read_parquet(path, engine=engine, dtype_backend='numpy_nullable')
```

### Step 10: Assign result2 = result2.drop(...)

```python
result2 = result2.drop('c', axis=1)
```

### Step 11: Assign expected = expected.drop(...)

```python
expected = expected.drop('c', axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: engine, request

# Workflow
pq = pytest.importorskip('pyarrow.parquet')
if engine == 'fastparquet':
    mark = pytest.mark.xfail(reason='Fastparquet nullable dtype support is disabled')
    request.applymarker(mark)
table = pyarrow.table({'a': pyarrow.array([1, 2, 3, None], 'int64'), 'b': pyarrow.array([1, 2, 3, None], 'uint8'), 'c': pyarrow.array(['a', 'b', 'c', None]), 'd': pyarrow.array([True, False, True, None]), 'e': pyarrow.array([1, 2, 3, 4], 'int64'), 'f': pyarrow.array([1.0, 2.0, 3.0, None], 'float32'), 'g': pyarrow.array([1.0, 2.0, 3.0, None], 'float64')})
with tm.ensure_clean() as path:
    pq.write_table(table, path)
    result1 = read_parquet(path, engine=engine)
    result2 = read_parquet(path, engine=engine, dtype_backend='numpy_nullable')
assert result1['a'].dtype == np.dtype('float64')
expected = pd.DataFrame({'a': pd.array([1, 2, 3, None], dtype='Int64'), 'b': pd.array([1, 2, 3, None], dtype='UInt8'), 'c': pd.array(['a', 'b', 'c', None], dtype='string'), 'd': pd.array([True, False, True, None], dtype='boolean'), 'e': pd.array([1, 2, 3, 4], dtype='Int64'), 'f': pd.array([1.0, 2.0, 3.0, None], dtype='Float32'), 'g': pd.array([1.0, 2.0, 3.0, None], dtype='Float64')})
if engine == 'fastparquet':
    result2 = result2.drop('c', axis=1)
    expected = expected.drop('c', axis=1)
tm.assert_frame_equal(result2, expected)
```

## Next Steps


---

*Source: test_parquet.py:621 | Complexity: Advanced | Last updated: 2026-06-02*