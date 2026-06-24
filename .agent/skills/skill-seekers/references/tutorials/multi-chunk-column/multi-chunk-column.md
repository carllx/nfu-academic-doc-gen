# How To: Multi Chunk Column

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multi chunk column

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.core.interchange.column`
- `pandas.core.interchange.dataframe_protocol`
- `pandas.core.interchange.from_dataframe`
- `pandas.core.interchange.utils`
- `pyarrow.interchange`
- `pyarrow.compute`
- `pyarrow.interchange`
- `pyarrow.interchange`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('pyarrow', '11.0.0')
```

**Verification:**
```python
assert len(df['a'].array._pa_array.chunks) == 2
```

### Step 2: Assign ser = pd.Series(...)

```python
ser = pd.Series([1, 2, None], dtype='Int64[pyarrow]')
```

**Verification:**
```python
assert len(df_orig['a'].array._pa_array.chunks) == 2
```

### Step 3: Assign df = pd.concat.to_frame(...)

```python
df = pd.concat([ser, ser], ignore_index=True).to_frame('a')
```

### Step 4: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

### Step 5: Assign result = pd.api.interchange.from_dataframe(...)

```python
result = pd.api.interchange.from_dataframe(df.__dataframe__(allow_copy=True))
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': [1.0, 2.0, None, 1.0, 2.0, None]}, dtype='float64')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

**Verification:**
```python
assert len(df['a'].array._pa_array.chunks) == 2
```

### Step 9: Call pd.api.interchange.from_dataframe()

```python
pd.api.interchange.from_dataframe(df.__dataframe__(allow_copy=False))
```


## Complete Example

```python
# Workflow
pytest.importorskip('pyarrow', '11.0.0')
ser = pd.Series([1, 2, None], dtype='Int64[pyarrow]')
df = pd.concat([ser, ser], ignore_index=True).to_frame('a')
df_orig = df.copy()
with pytest.raises(RuntimeError, match='Found multi-chunk pyarrow array, but `allow_copy` is False'):
    pd.api.interchange.from_dataframe(df.__dataframe__(allow_copy=False))
result = pd.api.interchange.from_dataframe(df.__dataframe__(allow_copy=True))
expected = pd.DataFrame({'a': [1.0, 2.0, None, 1.0, 2.0, None]}, dtype='float64')
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(df, df_orig)
assert len(df['a'].array._pa_array.chunks) == 2
assert len(df_orig['a'].array._pa_array.chunks) == 2
```

## Next Steps


---

*Source: test_impl.py:306 | Complexity: Advanced | Last updated: 2026-06-02*