# How To: Orc Dtype Backend Numpy Nullable

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test orc dtype backend numpy nullable

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('pyarrow')
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'string': list('abc'), 'string_with_nan': ['a', np.nan, 'c'], 'string_with_none': ['a', None, 'c'], 'int': list(range(1, 4)), 'int_with_nan': pd.Series([1, pd.NA, 3], dtype='Int64'), 'na_only': pd.Series([pd.NA, pd.NA, pd.NA], dtype='Int64'), 'float': np.arange(4.0, 7.0, dtype='float64'), 'float_with_nan': [2.0, np.nan, 3.0], 'bool': [True, False, True], 'bool_with_na': [True, False, None]})
```

### Step 3: Assign bytes_data = df.copy.to_orc(...)

```python
bytes_data = df.copy().to_orc()
```

### Step 4: Assign result = read_orc(...)

```python
result = read_orc(BytesIO(bytes_data), dtype_backend='numpy_nullable')
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'string': StringArray(np.array(['a', 'b', 'c'], dtype=np.object_)), 'string_with_nan': StringArray(np.array(['a', pd.NA, 'c'], dtype=np.object_)), 'string_with_none': StringArray(np.array(['a', pd.NA, 'c'], dtype=np.object_)), 'int': pd.Series([1, 2, 3], dtype='Int64'), 'int_with_nan': pd.Series([1, pd.NA, 3], dtype='Int64'), 'na_only': pd.Series([pd.NA, pd.NA, pd.NA], dtype='Int64'), 'float': pd.Series([4.0, 5.0, 6.0], dtype='Float64'), 'float_with_nan': pd.Series([2.0, pd.NA, 3.0], dtype='Float64'), 'bool': pd.Series([True, False, True], dtype='boolean'), 'bool_with_na': pd.Series([True, False, pd.NA], dtype='boolean')})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
pytest.importorskip('pyarrow')
df = pd.DataFrame({'string': list('abc'), 'string_with_nan': ['a', np.nan, 'c'], 'string_with_none': ['a', None, 'c'], 'int': list(range(1, 4)), 'int_with_nan': pd.Series([1, pd.NA, 3], dtype='Int64'), 'na_only': pd.Series([pd.NA, pd.NA, pd.NA], dtype='Int64'), 'float': np.arange(4.0, 7.0, dtype='float64'), 'float_with_nan': [2.0, np.nan, 3.0], 'bool': [True, False, True], 'bool_with_na': [True, False, None]})
bytes_data = df.copy().to_orc()
result = read_orc(BytesIO(bytes_data), dtype_backend='numpy_nullable')
expected = pd.DataFrame({'string': StringArray(np.array(['a', 'b', 'c'], dtype=np.object_)), 'string_with_nan': StringArray(np.array(['a', pd.NA, 'c'], dtype=np.object_)), 'string_with_none': StringArray(np.array(['a', pd.NA, 'c'], dtype=np.object_)), 'int': pd.Series([1, 2, 3], dtype='Int64'), 'int_with_nan': pd.Series([1, pd.NA, 3], dtype='Int64'), 'na_only': pd.Series([pd.NA, pd.NA, pd.NA], dtype='Int64'), 'float': pd.Series([4.0, 5.0, 6.0], dtype='Float64'), 'float_with_nan': pd.Series([2.0, pd.NA, 3.0], dtype='Float64'), 'bool': pd.Series([True, False, True], dtype='boolean'), 'bool_with_na': pd.Series([True, False, pd.NA], dtype='boolean')})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_orc.py:350 | Complexity: Intermediate | Last updated: 2026-06-02*