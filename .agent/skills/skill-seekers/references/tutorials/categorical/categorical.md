# How To: Categorical

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign s = pd.Series(...)

```python
s = pd.Series(pd.Categorical(['a', 'b', 'a']))
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign s.index.name = 'idx'

```python
s.index.name = 'idx'
```

### Step 3: Assign result = s.to_json(...)

```python
result = s.to_json(orient='table', date_format='iso')
```

### Step 4: Assign result = json.loads(...)

```python
result = json.loads(result, object_pairs_hook=OrderedDict)
```

### Step 5: Call unknown.pop()

```python
result['schema'].pop('pandas_version')
```

### Step 6: Assign fields = value

```python
fields = [{'name': 'idx', 'type': 'integer'}, {'constraints': {'enum': ['a', 'b']}, 'name': 'values', 'ordered': False, 'type': 'any'}]
```

### Step 7: Assign expected = OrderedDict(...)

```python
expected = OrderedDict([('schema', {'fields': fields, 'primaryKey': ['idx']}), ('data', [OrderedDict([('idx', 0), ('values', 'a')]), OrderedDict([('idx', 1), ('values', 'b')]), OrderedDict([('idx', 2), ('values', 'a')])])])
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
s = pd.Series(pd.Categorical(['a', 'b', 'a']))
s.index.name = 'idx'
result = s.to_json(orient='table', date_format='iso')
result = json.loads(result, object_pairs_hook=OrderedDict)
result['schema'].pop('pandas_version')
fields = [{'name': 'idx', 'type': 'integer'}, {'constraints': {'enum': ['a', 'b']}, 'name': 'values', 'ordered': False, 'type': 'any'}]
expected = OrderedDict([('schema', {'fields': fields, 'primaryKey': ['idx']}), ('data', [OrderedDict([('idx', 0), ('values', 'a')]), OrderedDict([('idx', 1), ('values', 'b')]), OrderedDict([('idx', 2), ('values', 'a')])])])
assert result == expected
```

## Next Steps


---

*Source: test_json_table_schema.py:563 | Complexity: Intermediate | Last updated: 2026-06-02*