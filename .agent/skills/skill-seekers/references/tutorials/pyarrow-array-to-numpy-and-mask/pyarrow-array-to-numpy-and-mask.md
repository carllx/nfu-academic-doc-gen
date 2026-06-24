# How To: Pyarrow Array To Numpy And Mask

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test conversion from pyarrow array to numpy array.

Modifies the pyarrow buffer to contain padding and offset, which are
considered valid buffers by pyarrow.

Also tests empty pyarrow arrays with non empty buffers.
See https://github.com/pandas-dev/pandas/issues/40896

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.arrow._arrow_utils`

**Setup Required:**
```python
# Fixtures: np_dtype_to_arrays
```

## Step-by-Step Guide

### Step 1: '\n    Test conversion from pyarrow array to numpy array.\n\n    Modifies the pyarrow buffer to contain padding and offset, which are\n    considered valid buffers by pyarrow.\n\n    Also tests empty pyarrow arrays with non empty buffers.\n    See https://github.com/pandas-dev/pandas/issues/40896\n    '

```python
'\n    Test conversion from pyarrow array to numpy array.\n\n    Modifies the pyarrow buffer to contain padding and offset, which are\n    considered valid buffers by pyarrow.\n\n    Also tests empty pyarrow arrays with non empty buffers.\n    See https://github.com/pandas-dev/pandas/issues/40896\n    '
```

### Step 2: Assign unknown = np_dtype_to_arrays

```python
np_dtype, pa_array, np_expected, mask_expected = np_dtype_to_arrays
```

### Step 3: Assign unknown = pyarrow_array_to_numpy_and_mask(...)

```python
data, mask = pyarrow_array_to_numpy_and_mask(pa_array, np_dtype)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(data[:3], np_expected)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(mask, mask_expected)
```

### Step 6: Assign mask_buffer = value

```python
mask_buffer = pa_array.buffers()[0]
```

### Step 7: Assign data_buffer = value

```python
data_buffer = pa_array.buffers()[1]
```

### Step 8: Assign data_buffer_bytes = unknown.to_pybytes(...)

```python
data_buffer_bytes = pa_array.buffers()[1].to_pybytes()
```

### Step 9: Assign data_buffer_trail = pa.py_buffer(...)

```python
data_buffer_trail = pa.py_buffer(data_buffer_bytes + b'\x00')
```

### Step 10: Assign pa_array_trail = pa.Array.from_buffers(...)

```python
pa_array_trail = pa.Array.from_buffers(type=pa_array.type, length=len(pa_array), buffers=[mask_buffer, data_buffer_trail], offset=pa_array.offset)
```

### Step 11: Call pa_array_trail.validate()

```python
pa_array_trail.validate()
```

### Step 12: Assign unknown = pyarrow_array_to_numpy_and_mask(...)

```python
data, mask = pyarrow_array_to_numpy_and_mask(pa_array_trail, np_dtype)
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(data[:3], np_expected)
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(mask, mask_expected)
```

### Step 15: Assign offset = value

```python
offset = b'\x00' * (pa_array.type.bit_width // 8)
```

### Step 16: Assign data_buffer_offset = pa.py_buffer(...)

```python
data_buffer_offset = pa.py_buffer(offset + data_buffer_bytes)
```

### Step 17: Assign mask_buffer_offset = pa.py_buffer(...)

```python
mask_buffer_offset = pa.py_buffer(b'\x0e')
```

### Step 18: Assign pa_array_offset = pa.Array.from_buffers(...)

```python
pa_array_offset = pa.Array.from_buffers(type=pa_array.type, length=len(pa_array), buffers=[mask_buffer_offset, data_buffer_offset], offset=pa_array.offset + 1)
```

### Step 19: Call pa_array_offset.validate()

```python
pa_array_offset.validate()
```

### Step 20: Assign unknown = pyarrow_array_to_numpy_and_mask(...)

```python
data, mask = pyarrow_array_to_numpy_and_mask(pa_array_offset, np_dtype)
```

### Step 21: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(data[:3], np_expected)
```

### Step 22: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(mask, mask_expected)
```

### Step 23: Assign np_expected_empty = np.array(...)

```python
np_expected_empty = np.array([], dtype=np_dtype)
```

### Step 24: Assign mask_expected_empty = np.array(...)

```python
mask_expected_empty = np.array([], dtype=np.bool_)
```

### Step 25: Assign pa_array_offset = pa.Array.from_buffers(...)

```python
pa_array_offset = pa.Array.from_buffers(type=pa_array.type, length=0, buffers=[mask_buffer, data_buffer], offset=pa_array.offset)
```

### Step 26: Call pa_array_offset.validate()

```python
pa_array_offset.validate()
```

### Step 27: Assign unknown = pyarrow_array_to_numpy_and_mask(...)

```python
data, mask = pyarrow_array_to_numpy_and_mask(pa_array_offset, np_dtype)
```

### Step 28: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(data[:3], np_expected_empty)
```

### Step 29: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(mask, mask_expected_empty)
```


## Complete Example

```python
# Setup
# Fixtures: np_dtype_to_arrays

# Workflow
'\n    Test conversion from pyarrow array to numpy array.\n\n    Modifies the pyarrow buffer to contain padding and offset, which are\n    considered valid buffers by pyarrow.\n\n    Also tests empty pyarrow arrays with non empty buffers.\n    See https://github.com/pandas-dev/pandas/issues/40896\n    '
np_dtype, pa_array, np_expected, mask_expected = np_dtype_to_arrays
data, mask = pyarrow_array_to_numpy_and_mask(pa_array, np_dtype)
tm.assert_numpy_array_equal(data[:3], np_expected)
tm.assert_numpy_array_equal(mask, mask_expected)
mask_buffer = pa_array.buffers()[0]
data_buffer = pa_array.buffers()[1]
data_buffer_bytes = pa_array.buffers()[1].to_pybytes()
data_buffer_trail = pa.py_buffer(data_buffer_bytes + b'\x00')
pa_array_trail = pa.Array.from_buffers(type=pa_array.type, length=len(pa_array), buffers=[mask_buffer, data_buffer_trail], offset=pa_array.offset)
pa_array_trail.validate()
data, mask = pyarrow_array_to_numpy_and_mask(pa_array_trail, np_dtype)
tm.assert_numpy_array_equal(data[:3], np_expected)
tm.assert_numpy_array_equal(mask, mask_expected)
offset = b'\x00' * (pa_array.type.bit_width // 8)
data_buffer_offset = pa.py_buffer(offset + data_buffer_bytes)
mask_buffer_offset = pa.py_buffer(b'\x0e')
pa_array_offset = pa.Array.from_buffers(type=pa_array.type, length=len(pa_array), buffers=[mask_buffer_offset, data_buffer_offset], offset=pa_array.offset + 1)
pa_array_offset.validate()
data, mask = pyarrow_array_to_numpy_and_mask(pa_array_offset, np_dtype)
tm.assert_numpy_array_equal(data[:3], np_expected)
tm.assert_numpy_array_equal(mask, mask_expected)
np_expected_empty = np.array([], dtype=np_dtype)
mask_expected_empty = np.array([], dtype=np.bool_)
pa_array_offset = pa.Array.from_buffers(type=pa_array.type, length=0, buffers=[mask_buffer, data_buffer], offset=pa_array.offset)
pa_array_offset.validate()
data, mask = pyarrow_array_to_numpy_and_mask(pa_array_offset, np_dtype)
tm.assert_numpy_array_equal(data[:3], np_expected_empty)
tm.assert_numpy_array_equal(mask, mask_expected_empty)
```

## Next Steps


---

*Source: test_arrow_compat.py:130 | Complexity: Advanced | Last updated: 2026-06-02*