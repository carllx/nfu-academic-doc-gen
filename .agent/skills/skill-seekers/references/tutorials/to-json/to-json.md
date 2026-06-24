# How To: To Json

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to json

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `decimal`
- `io`
- `json`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.integer`
- `pandas.core.arrays.string_`
- `pandas.core.series`
- `pandas.tests.extension.date`
- `pandas.tests.extension.decimal.array`
- `pandas.io.json._table_schema`

**Setup Required:**
```python
# Fixtures: df
```

## Step-by-Step Guide

### Step 1: Assign df = df.copy(...)

```python
df = df.copy()
```

**Verification:**
```python
assert 'pandas_version' in result['schema']
```

### Step 2: Assign df.index.name = 'idx'

```python
df.index.name = 'idx'
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = df.to_json(...)

```python
result = df.to_json(orient='table', date_format='iso')
```

### Step 4: Assign result = json.loads(...)

```python
result = json.loads(result, object_pairs_hook=OrderedDict)
```

**Verification:**
```python
assert 'pandas_version' in result['schema']
```

### Step 5: Call unknown.pop()

```python
result['schema'].pop('pandas_version')
```

### Step 6: Assign fields = value

```python
fields = [OrderedDict({'name': 'idx', 'type': 'integer'}), OrderedDict({'name': 'A', 'type': 'any', 'extDtype': 'DateDtype'}), OrderedDict({'name': 'B', 'type': 'number', 'extDtype': 'decimal'}), OrderedDict({'name': 'C', 'type': 'string', 'extDtype': 'string'}), OrderedDict({'name': 'D', 'type': 'integer', 'extDtype': 'Int64'})]
```

### Step 7: Assign schema = OrderedDict(...)

```python
schema = OrderedDict({'fields': fields, 'primaryKey': ['idx']})
```

### Step 8: Assign data = value

```python
data = [OrderedDict([('idx', 0), ('A', '2021-10-10T00:00:00.000'), ('B', 10.0), ('C', 'pandas'), ('D', 10)])]
```

### Step 9: Assign expected = OrderedDict(...)

```python
expected = OrderedDict([('schema', schema), ('data', data)])
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: df

# Workflow
df = df.copy()
df.index.name = 'idx'
result = df.to_json(orient='table', date_format='iso')
result = json.loads(result, object_pairs_hook=OrderedDict)
assert 'pandas_version' in result['schema']
result['schema'].pop('pandas_version')
fields = [OrderedDict({'name': 'idx', 'type': 'integer'}), OrderedDict({'name': 'A', 'type': 'any', 'extDtype': 'DateDtype'}), OrderedDict({'name': 'B', 'type': 'number', 'extDtype': 'decimal'}), OrderedDict({'name': 'C', 'type': 'string', 'extDtype': 'string'}), OrderedDict({'name': 'D', 'type': 'integer', 'extDtype': 'Int64'})]
schema = OrderedDict({'fields': fields, 'primaryKey': ['idx']})
data = [OrderedDict([('idx', 0), ('A', '2021-10-10T00:00:00.000'), ('B', 10.0), ('C', 'pandas'), ('D', 10)])]
expected = OrderedDict([('schema', schema), ('data', data)])
assert result == expected
```

## Next Steps


---

*Source: test_json_table_schema_ext_dtype.py:246 | Complexity: Advanced | Last updated: 2026-06-02*