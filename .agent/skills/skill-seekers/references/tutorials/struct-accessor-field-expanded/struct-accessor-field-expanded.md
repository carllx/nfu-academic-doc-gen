# How To: Struct Accessor Field Expanded

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test struct accessor field expanded

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `pytest`
- `pandas.compat.pyarrow`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: indices, name
```

## Step-by-Step Guide

### Step 1: Assign arrow_type = pa.struct(...)

```python
arrow_type = pa.struct([('int_col', pa.int64()), ('struct_col', pa.struct([('int_col', pa.int64()), ('float_col', pa.float64()), ('str_col', pa.string())])), (b'string_col', pa.string())])
```

**Verification:**
```python
assert result.name == name
```

### Step 2: Assign data = pa.array(...)

```python
data = pa.array([], type=arrow_type)
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(data, dtype=ArrowDtype(arrow_type))
```

### Step 4: Assign expected = pc.struct_field(...)

```python
expected = pc.struct_field(data, indices)
```

### Step 5: Assign result = ser.struct.field(...)

```python
result = ser.struct.field(indices)
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result.array._pa_array.combine_chunks(), expected)
```

**Verification:**
```python
assert result.name == name
```


## Complete Example

```python
# Setup
# Fixtures: indices, name

# Workflow
arrow_type = pa.struct([('int_col', pa.int64()), ('struct_col', pa.struct([('int_col', pa.int64()), ('float_col', pa.float64()), ('str_col', pa.string())])), (b'string_col', pa.string())])
data = pa.array([], type=arrow_type)
ser = Series(data, dtype=ArrowDtype(arrow_type))
expected = pc.struct_field(data, indices)
result = ser.struct.field(indices)
tm.assert_equal(result.array._pa_array.combine_chunks(), expected)
assert result.name == name
```

## Next Steps


---

*Source: test_struct_accessor.py:173 | Complexity: Intermediate | Last updated: 2026-06-02*