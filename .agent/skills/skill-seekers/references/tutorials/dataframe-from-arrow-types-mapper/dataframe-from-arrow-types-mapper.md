# How To: Dataframe From Arrow Types Mapper

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe from arrow types mapper

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.arrow._arrow_utils`


## Step-by-Step Guide

### Step 1: Assign bools_array = pa.array(...)

```python
bools_array = pa.array([True, None, False], type=pa.bool_())
```

### Step 2: Assign ints_array = pa.array(...)

```python
ints_array = pa.array([1, None, 2], type=pa.int64())
```

### Step 3: Assign small_ints_array = pa.array(...)

```python
small_ints_array = pa.array([-1, 0, 7], type=pa.int8())
```

### Step 4: Assign record_batch = pa.RecordBatch.from_arrays(...)

```python
record_batch = pa.RecordBatch.from_arrays([bools_array, ints_array, small_ints_array], ['bools', 'ints', 'small_ints'])
```

### Step 5: Assign result = record_batch.to_pandas(...)

```python
result = record_batch.to_pandas(types_mapper=types_mapper)
```

### Step 6: Assign bools = pd.Series(...)

```python
bools = pd.Series([True, None, False], dtype='boolean')
```

### Step 7: Assign ints = pd.Series(...)

```python
ints = pd.Series([1, None, 2], dtype='Int64')
```

### Step 8: Assign small_ints = pd.Series(...)

```python
small_ints = pd.Series([-1, 0, 7], dtype='Int64')
```

### Step 9: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'bools': bools, 'ints': ints, 'small_ints': small_ints})
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
def types_mapper(arrow_type):
    if pa.types.is_boolean(arrow_type):
        return pd.BooleanDtype()
    elif pa.types.is_integer(arrow_type):
        return pd.Int64Dtype()
bools_array = pa.array([True, None, False], type=pa.bool_())
ints_array = pa.array([1, None, 2], type=pa.int64())
small_ints_array = pa.array([-1, 0, 7], type=pa.int8())
record_batch = pa.RecordBatch.from_arrays([bools_array, ints_array, small_ints_array], ['bools', 'ints', 'small_ints'])
result = record_batch.to_pandas(types_mapper=types_mapper)
bools = pd.Series([True, None, False], dtype='boolean')
ints = pd.Series([1, None, 2], dtype='Int64')
small_ints = pd.Series([-1, 0, 7], dtype='Int64')
expected = pd.DataFrame({'bools': bools, 'ints': ints, 'small_ints': small_ints})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_arrow_compat.py:49 | Complexity: Advanced | Last updated: 2026-06-02*