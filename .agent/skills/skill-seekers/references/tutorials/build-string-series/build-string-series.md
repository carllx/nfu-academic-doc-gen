# How To: Build String Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test build string series

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
# Fixtures: sa
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(sa, name='a')
```

**Verification:**
```python
assert 'pandas_version' in result['schema']
```

### Step 2: Assign s.index.name = 'id'

```python
s.index.name = 'id'
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = s.to_json(...)

```python
result = s.to_json(orient='table', date_format='iso')
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
fields = [{'name': 'id', 'type': 'integer'}, {'name': 'a', 'type': 'string', 'extDtype': 'string'}]
```

### Step 7: Assign schema = value

```python
schema = {'fields': fields, 'primaryKey': ['id']}
```

### Step 8: Assign expected = OrderedDict(...)

```python
expected = OrderedDict([('schema', schema), ('data', [OrderedDict([('id', 0), ('a', 'pandas')])])])
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: sa

# Workflow
s = Series(sa, name='a')
s.index.name = 'id'
result = s.to_json(orient='table', date_format='iso')
result = json.loads(result, object_pairs_hook=OrderedDict)
assert 'pandas_version' in result['schema']
result['schema'].pop('pandas_version')
fields = [{'name': 'id', 'type': 'integer'}, {'name': 'a', 'type': 'string', 'extDtype': 'string'}]
schema = {'fields': fields, 'primaryKey': ['id']}
expected = OrderedDict([('schema', schema), ('data', [OrderedDict([('id', 0), ('a', 'pandas')])])])
assert result == expected
```

## Next Steps


---

*Source: test_json_table_schema_ext_dtype.py:196 | Complexity: Advanced | Last updated: 2026-06-02*