# How To: Multiindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `io`
- `json`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.json._table_schema`

**Setup Required:**
```python
# Fixtures: df_schema, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df = df_schema

```python
df = df_schema
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign idx = pd.MultiIndex.from_product(...)

```python
idx = pd.MultiIndex.from_product([('a', 'b'), (1, 2)])
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign df.index = idx

```python
df.index = idx
```

### Step 4: Assign result = build_table_schema(...)

```python
result = build_table_schema(df, version=False)
```

### Step 5: Assign expected = value

```python
expected = {'fields': [{'name': 'level_0', 'type': 'string'}, {'name': 'level_1', 'type': 'integer'}, {'name': 'A', 'type': 'integer'}, {'name': 'B', 'type': 'string'}, {'name': 'C', 'type': 'datetime'}, {'name': 'D', 'type': 'duration'}], 'primaryKey': ['level_0', 'level_1']}
```

**Verification:**
```python
assert result == expected
```

### Step 6: Assign df.index.names = value

```python
df.index.names = ['idx0', None]
```

### Step 7: Assign unknown = 'idx0'

```python
expected['fields'][0]['name'] = 'idx0'
```

### Step 8: Assign unknown = value

```python
expected['primaryKey'] = ['idx0', 'level_1']
```

### Step 9: Assign result = build_table_schema(...)

```python
result = build_table_schema(df, version=False)
```

**Verification:**
```python
assert result == expected
```

### Step 10: Assign unknown = value

```python
expected['fields'][0] = {'name': 'level_0', 'type': 'string', 'extDtype': 'str'}
```

### Step 11: Assign unknown = value

```python
expected['fields'][3] = {'name': 'B', 'type': 'string', 'extDtype': 'str'}
```


## Complete Example

```python
# Setup
# Fixtures: df_schema, using_infer_string

# Workflow
df = df_schema
idx = pd.MultiIndex.from_product([('a', 'b'), (1, 2)])
df.index = idx
result = build_table_schema(df, version=False)
expected = {'fields': [{'name': 'level_0', 'type': 'string'}, {'name': 'level_1', 'type': 'integer'}, {'name': 'A', 'type': 'integer'}, {'name': 'B', 'type': 'string'}, {'name': 'C', 'type': 'datetime'}, {'name': 'D', 'type': 'duration'}], 'primaryKey': ['level_0', 'level_1']}
if using_infer_string:
    expected['fields'][0] = {'name': 'level_0', 'type': 'string', 'extDtype': 'str'}
    expected['fields'][3] = {'name': 'B', 'type': 'string', 'extDtype': 'str'}
assert result == expected
df.index.names = ['idx0', None]
expected['fields'][0]['name'] = 'idx0'
expected['primaryKey'] = ['idx0', 'level_1']
result = build_table_schema(df, version=False)
assert result == expected
```

## Next Steps


---

*Source: test_json_table_schema.py:102 | Complexity: Advanced | Last updated: 2026-06-02*