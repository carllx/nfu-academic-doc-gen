# How To: Pyarrow Dtype Backend From Pandas Nullable

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pyarrow dtype backend from pandas nullable

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign pa = pytest.importorskip(...)

```python
pa = pytest.importorskip('pyarrow')
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'a': pd.Series([1, 2, None], dtype='Int32'), 'b': pd.Series(['x', 'y', None], dtype='string[python]'), 'c': pd.Series([True, False, None], dtype='boolean'), 'd': pd.Series([None, 100.5, 200], dtype='Float64')})
```

### Step 3: Assign result = df.convert_dtypes(...)

```python
result = df.convert_dtypes(dtype_backend='pyarrow')
```

### Step 4: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': pd.arrays.ArrowExtensionArray(pa.array([1, 2, None], type=pa.int32())), 'b': pd.arrays.ArrowExtensionArray(pa.array(['x', 'y', None])), 'c': pd.arrays.ArrowExtensionArray(pa.array([True, False, None])), 'd': pd.arrays.ArrowExtensionArray(pa.array([None, 100.5, 200.0]))})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
pa = pytest.importorskip('pyarrow')
df = pd.DataFrame({'a': pd.Series([1, 2, None], dtype='Int32'), 'b': pd.Series(['x', 'y', None], dtype='string[python]'), 'c': pd.Series([True, False, None], dtype='boolean'), 'd': pd.Series([None, 100.5, 200], dtype='Float64')})
result = df.convert_dtypes(dtype_backend='pyarrow')
expected = pd.DataFrame({'a': pd.arrays.ArrowExtensionArray(pa.array([1, 2, None], type=pa.int32())), 'b': pd.arrays.ArrowExtensionArray(pa.array(['x', 'y', None])), 'c': pd.arrays.ArrowExtensionArray(pa.array([True, False, None])), 'd': pd.arrays.ArrowExtensionArray(pa.array([None, 100.5, 200.0]))})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_convert_dtypes.py:109 | Complexity: Intermediate | Last updated: 2026-06-02*