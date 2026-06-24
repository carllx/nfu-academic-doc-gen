# How To: Dataframe Arrow Interface

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe arrow interface

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `ctypes`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c']})
```

**Verification:**
```python
assert ctypes.pythonapi.PyCapsule_IsValid(ctypes.py_object(capsule), b'arrow_array_stream') == 1
```

### Step 2: Assign capsule = df.__arrow_c_stream__(...)

```python
capsule = df.__arrow_c_stream__()
```

**Verification:**
```python
assert table.equals(expected)
```

### Step 3: Assign table = pa.table(...)

```python
table = pa.table(df)
```

**Verification:**
```python
assert table.equals(expected)
```

### Step 4: Assign string_type = value

```python
string_type = pa.large_string() if using_infer_string else pa.string()
```

### Step 5: Assign expected = pa.table(...)

```python
expected = pa.table({'a': [1, 2, 3], 'b': pa.array(['a', 'b', 'c'], string_type)})
```

**Verification:**
```python
assert table.equals(expected)
```

### Step 6: Assign schema = pa.schema(...)

```python
schema = pa.schema([('a', pa.int8()), ('b', pa.string())])
```

### Step 7: Assign table = pa.table(...)

```python
table = pa.table(df, schema=schema)
```

### Step 8: Assign expected = expected.cast(...)

```python
expected = expected.cast(schema)
```

**Verification:**
```python
assert table.equals(expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c']})
capsule = df.__arrow_c_stream__()
assert ctypes.pythonapi.PyCapsule_IsValid(ctypes.py_object(capsule), b'arrow_array_stream') == 1
table = pa.table(df)
string_type = pa.large_string() if using_infer_string else pa.string()
expected = pa.table({'a': [1, 2, 3], 'b': pa.array(['a', 'b', 'c'], string_type)})
assert table.equals(expected)
schema = pa.schema([('a', pa.int8()), ('b', pa.string())])
table = pa.table(df, schema=schema)
expected = expected.cast(schema)
assert table.equals(expected)
```

## Next Steps


---

*Source: test_arrow_interface.py:13 | Complexity: Advanced | Last updated: 2026-06-02*