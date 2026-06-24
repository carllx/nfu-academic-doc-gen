# How To: To Json Categorical Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to json categorical index

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

### Step 1: Assign data = pd.Series(...)

```python
data = pd.Series(1, pd.CategoricalIndex(['a', 'b']))
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = data.to_json(...)

```python
result = data.to_json(orient='table', date_format='iso')
```

### Step 3: Assign result = json.loads(...)

```python
result = json.loads(result, object_pairs_hook=OrderedDict)
```

### Step 4: Call unknown.pop()

```python
result['schema'].pop('pandas_version')
```

### Step 5: Assign expected = OrderedDict(...)

```python
expected = OrderedDict([('schema', {'fields': [{'name': 'index', 'type': 'any', 'constraints': {'enum': ['a', 'b']}, 'ordered': False}, {'name': 'values', 'type': 'integer'}], 'primaryKey': ['index']}), ('data', [OrderedDict([('index', 'a'), ('values', 1)]), OrderedDict([('index', 'b'), ('values', 1)])])])
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
data = pd.Series(1, pd.CategoricalIndex(['a', 'b']))
result = data.to_json(orient='table', date_format='iso')
result = json.loads(result, object_pairs_hook=OrderedDict)
result['schema'].pop('pandas_version')
expected = OrderedDict([('schema', {'fields': [{'name': 'index', 'type': 'any', 'constraints': {'enum': ['a', 'b']}, 'ordered': False}, {'name': 'values', 'type': 'integer'}], 'primaryKey': ['index']}), ('data', [OrderedDict([('index', 'a'), ('values', 1)]), OrderedDict([('index', 'b'), ('values', 1)])])])
assert result == expected
```

## Next Steps


---

*Source: test_json_table_schema.py:420 | Complexity: Intermediate | Last updated: 2026-06-02*