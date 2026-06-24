# How To: Build Table Schema

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test build table schema

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': DateArray([dt.date(2021, 10, 10)]), 'B': DecimalArray([decimal.Decimal(10)]), 'C': array(['pandas'], dtype='string'), 'D': array([10], dtype='Int64')})
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = build_table_schema(...)

```python
result = build_table_schema(df, version=False)
```

**Verification:**
```python
assert 'pandas_version' in result
```

### Step 3: Assign expected = value

```python
expected = {'fields': [{'name': 'index', 'type': 'integer'}, {'name': 'A', 'type': 'any', 'extDtype': 'DateDtype'}, {'name': 'B', 'type': 'number', 'extDtype': 'decimal'}, {'name': 'C', 'type': 'string', 'extDtype': 'string'}, {'name': 'D', 'type': 'integer', 'extDtype': 'Int64'}], 'primaryKey': ['index']}
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign result = build_table_schema(...)

```python
result = build_table_schema(df)
```

**Verification:**
```python
assert 'pandas_version' in result
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': DateArray([dt.date(2021, 10, 10)]), 'B': DecimalArray([decimal.Decimal(10)]), 'C': array(['pandas'], dtype='string'), 'D': array([10], dtype='Int64')})
result = build_table_schema(df, version=False)
expected = {'fields': [{'name': 'index', 'type': 'integer'}, {'name': 'A', 'type': 'any', 'extDtype': 'DateDtype'}, {'name': 'B', 'type': 'number', 'extDtype': 'decimal'}, {'name': 'C', 'type': 'string', 'extDtype': 'string'}, {'name': 'D', 'type': 'integer', 'extDtype': 'Int64'}], 'primaryKey': ['index']}
assert result == expected
result = build_table_schema(df)
assert 'pandas_version' in result
```

## Next Steps


---

*Source: test_json_table_schema_ext_dtype.py:38 | Complexity: Intermediate | Last updated: 2026-06-02*