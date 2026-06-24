# How To: Read Clipboard Dtype Backend

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read clipboard dtype backend

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.clipboard`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: clipboard, string_storage, dtype_backend, engine, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign text = 'a,b,c,d,e,f,g,h,i\nx,1,4.0,x,2,4.0,,True,False\ny,2,5.0,,,,,False,'

```python
text = 'a,b,c,d,e,f,g,h,i\nx,1,4.0,x,2,4.0,,True,False\ny,2,5.0,,,,,False,'
```

### Step 2: Call clipboard.setText()

```python
clipboard.setText(text)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': Series(['x', 'y'], dtype=string_dtype), 'b': Series([1, 2], dtype='Int64'), 'c': Series([4.0, 5.0], dtype='Float64'), 'd': Series(['x', None], dtype=string_dtype), 'e': Series([2, NA], dtype='Int64'), 'f': Series([4.0, NA], dtype='Float64'), 'g': Series([NA, NA], dtype='Int64'), 'h': Series([True, False], dtype='boolean'), 'i': Series([False, NA], dtype='boolean')})
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow')
```

### Step 6: Assign string_dtype = pd.StringDtype(...)

```python
string_dtype = pd.StringDtype(string_storage)
```

### Step 7: Assign result = read_clipboard(...)

```python
result = read_clipboard(sep=',', dtype_backend=dtype_backend, engine=engine)
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame({col: ArrowExtensionArray(pa.array(expected[col], from_pandas=True)) for col in expected.columns})
```

### Step 9: Assign unknown = ArrowExtensionArray(...)

```python
expected['g'] = ArrowExtensionArray(pa.array([None, None]))
```

### Step 10: Assign expected.columns = expected.columns.astype(...)

```python
expected.columns = expected.columns.astype(pd.StringDtype(string_storage, na_value=np.nan))
```

### Step 11: Assign string_dtype = pd.ArrowDtype(...)

```python
string_dtype = pd.ArrowDtype(pa.large_string())
```

### Step 12: Assign string_dtype = pd.ArrowDtype(...)

```python
string_dtype = pd.ArrowDtype(pa.string())
```


## Complete Example

```python
# Setup
# Fixtures: clipboard, string_storage, dtype_backend, engine, using_infer_string

# Workflow
if dtype_backend == 'pyarrow':
    pa = pytest.importorskip('pyarrow')
    if engine == 'c' and string_storage == 'pyarrow':
        string_dtype = pd.ArrowDtype(pa.large_string())
    else:
        string_dtype = pd.ArrowDtype(pa.string())
else:
    string_dtype = pd.StringDtype(string_storage)
text = 'a,b,c,d,e,f,g,h,i\nx,1,4.0,x,2,4.0,,True,False\ny,2,5.0,,,,,False,'
clipboard.setText(text)
with pd.option_context('mode.string_storage', string_storage):
    result = read_clipboard(sep=',', dtype_backend=dtype_backend, engine=engine)
expected = DataFrame({'a': Series(['x', 'y'], dtype=string_dtype), 'b': Series([1, 2], dtype='Int64'), 'c': Series([4.0, 5.0], dtype='Float64'), 'd': Series(['x', None], dtype=string_dtype), 'e': Series([2, NA], dtype='Int64'), 'f': Series([4.0, NA], dtype='Float64'), 'g': Series([NA, NA], dtype='Int64'), 'h': Series([True, False], dtype='boolean'), 'i': Series([False, NA], dtype='boolean')})
if dtype_backend == 'pyarrow':
    from pandas.arrays import ArrowExtensionArray
    expected = DataFrame({col: ArrowExtensionArray(pa.array(expected[col], from_pandas=True)) for col in expected.columns})
    expected['g'] = ArrowExtensionArray(pa.array([None, None]))
if using_infer_string:
    expected.columns = expected.columns.astype(pd.StringDtype(string_storage, na_value=np.nan))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_clipboard.py:347 | Complexity: Advanced | Last updated: 2026-06-02*