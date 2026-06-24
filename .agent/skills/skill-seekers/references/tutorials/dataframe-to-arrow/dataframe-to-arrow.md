# How To: Dataframe To Arrow

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe to arrow

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
assert table.equals(expected)
```

### Step 2: Assign table = pa.RecordBatchReader.from_stream.read_all(...)

```python
table = pa.RecordBatchReader.from_stream(df).read_all()
```

**Verification:**
```python
assert table.equals(expected)
```

### Step 3: Assign string_type = value

```python
string_type = pa.large_string() if using_infer_string else pa.string()
```

### Step 4: Assign expected = pa.table(...)

```python
expected = pa.table({'a': [1, 2, 3], 'b': pa.array(['a', 'b', 'c'], string_type)})
```

**Verification:**
```python
assert table.equals(expected)
```

### Step 5: Assign schema = pa.schema(...)

```python
schema = pa.schema([('a', pa.int8()), ('b', pa.string())])
```

### Step 6: Assign table = pa.RecordBatchReader.from_stream.read_all(...)

```python
table = pa.RecordBatchReader.from_stream(df, schema=schema).read_all()
```

### Step 7: Assign expected = expected.cast(...)

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
table = pa.RecordBatchReader.from_stream(df).read_all()
string_type = pa.large_string() if using_infer_string else pa.string()
expected = pa.table({'a': [1, 2, 3], 'b': pa.array(['a', 'b', 'c'], string_type)})
assert table.equals(expected)
schema = pa.schema([('a', pa.int8()), ('b', pa.string())])
table = pa.RecordBatchReader.from_stream(df, schema=schema).read_all()
expected = expected.cast(schema)
assert table.equals(expected)
```

## Next Steps


---

*Source: test_arrow_interface.py:36 | Complexity: Intermediate | Last updated: 2026-06-02*