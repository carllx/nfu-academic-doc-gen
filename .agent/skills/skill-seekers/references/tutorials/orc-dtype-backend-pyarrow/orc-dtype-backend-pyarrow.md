# How To: Orc Dtype Backend Pyarrow

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test orc dtype backend pyarrow

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
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pyarrow`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('pyarrow')
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'string': list('abc'), 'string_with_nan': ['a', np.nan, 'c'], 'string_with_none': ['a', None, 'c'], 'bytes': [b'foo', b'bar', None], 'int': list(range(1, 4)), 'float': np.arange(4.0, 7.0, dtype='float64'), 'float_with_nan': [2.0, np.nan, 3.0], 'bool': [True, False, True], 'bool_with_na': [True, False, None], 'datetime': pd.date_range('20130101', periods=3), 'datetime_with_nat': [pd.Timestamp('20130101'), pd.NaT, pd.Timestamp('20130103')]})
```

### Step 3: Assign bytes_data = df.copy.to_orc(...)

```python
bytes_data = df.copy().to_orc()
```

### Step 4: Assign result = read_orc(...)

```python
result = read_orc(BytesIO(bytes_data), dtype_backend='pyarrow')
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({col: pd.arrays.ArrowExtensionArray(pa.array(df[col], from_pandas=True)) for col in df.columns})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign string_dtype = pd.ArrowDtype(...)

```python
string_dtype = pd.ArrowDtype(pa.string())
```

### Step 8: Assign unknown = unknown.astype(...)

```python
expected['string'] = expected['string'].astype(string_dtype)
```

### Step 9: Assign unknown = unknown.astype(...)

```python
expected['string_with_nan'] = expected['string_with_nan'].astype(string_dtype)
```

### Step 10: Assign unknown = unknown.astype(...)

```python
expected['string_with_none'] = expected['string_with_none'].astype(string_dtype)
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
pytest.importorskip('pyarrow')
df = pd.DataFrame({'string': list('abc'), 'string_with_nan': ['a', np.nan, 'c'], 'string_with_none': ['a', None, 'c'], 'bytes': [b'foo', b'bar', None], 'int': list(range(1, 4)), 'float': np.arange(4.0, 7.0, dtype='float64'), 'float_with_nan': [2.0, np.nan, 3.0], 'bool': [True, False, True], 'bool_with_na': [True, False, None], 'datetime': pd.date_range('20130101', periods=3), 'datetime_with_nat': [pd.Timestamp('20130101'), pd.NaT, pd.Timestamp('20130103')]})
bytes_data = df.copy().to_orc()
result = read_orc(BytesIO(bytes_data), dtype_backend='pyarrow')
expected = pd.DataFrame({col: pd.arrays.ArrowExtensionArray(pa.array(df[col], from_pandas=True)) for col in df.columns})
if using_infer_string:
    string_dtype = pd.ArrowDtype(pa.string())
    expected['string'] = expected['string'].astype(string_dtype)
    expected['string_with_nan'] = expected['string_with_nan'].astype(string_dtype)
    expected['string_with_none'] = expected['string_with_none'].astype(string_dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_orc.py:308 | Complexity: Advanced | Last updated: 2026-06-02*