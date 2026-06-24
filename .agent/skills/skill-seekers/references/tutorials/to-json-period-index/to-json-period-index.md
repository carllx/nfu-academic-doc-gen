# How To: To Json Period Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to json period index

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

### Step 1: Assign idx = pd.period_range(...)

```python
idx = pd.period_range('2016', freq='Q-JAN', periods=2)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign data = pd.Series(...)

```python
data = pd.Series(1, idx)
```

### Step 3: Assign result = data.to_json(...)

```python
result = data.to_json(orient='table', date_format='iso')
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
fields = [{'freq': 'QE-JAN', 'name': 'index', 'type': 'datetime'}, {'name': 'values', 'type': 'integer'}]
```

### Step 7: Assign schema = value

```python
schema = {'fields': fields, 'primaryKey': ['index']}
```

### Step 8: Assign data = value

```python
data = [OrderedDict([('index', '2015-11-01T00:00:00.000'), ('values', 1)]), OrderedDict([('index', '2016-02-01T00:00:00.000'), ('values', 1)])]
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
# Workflow
idx = pd.period_range('2016', freq='Q-JAN', periods=2)
data = pd.Series(1, idx)
result = data.to_json(orient='table', date_format='iso')
result = json.loads(result, object_pairs_hook=OrderedDict)
result['schema'].pop('pandas_version')
fields = [{'freq': 'QE-JAN', 'name': 'index', 'type': 'datetime'}, {'name': 'values', 'type': 'integer'}]
schema = {'fields': fields, 'primaryKey': ['index']}
data = [OrderedDict([('index', '2015-11-01T00:00:00.000'), ('values', 1)]), OrderedDict([('index', '2016-02-01T00:00:00.000'), ('values', 1)])]
expected = OrderedDict([('schema', schema), ('data', data)])
assert result == expected
```

## Next Steps


---

*Source: test_json_table_schema.py:399 | Complexity: Advanced | Last updated: 2026-06-02*