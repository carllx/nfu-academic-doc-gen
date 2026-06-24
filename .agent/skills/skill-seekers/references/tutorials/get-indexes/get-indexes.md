# How To: Get Indexes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexes

## Prerequisites

**Required Modules:**
- `contextlib`
- `operator`
- `re`
- `sqlalchemy`
- `provision`
- `provision`
- `schema`
- `schema`
- `engine`
- `engine`
- `engine`
- `exc`
- `exc`
- `schema`
- `schema`
- `sql.elements`
- `sql.schema`
- `testing`
- `testing`
- `testing`
- `testing`
- `testing`
- `testing`
- `sqlalchemy`


## Step-by-Step Guide

### Step 1: Assign insp = inspect(...)

```python
insp = inspect(connection)
```

### Step 2: Assign indexes = insp.get_indexes(...)

```python
indexes = insp.get_indexes('users', schema=schema)
```

### Step 3: Assign exp = self.exp_indexes(...)

```python
exp = self.exp_indexes(schema=schema)
```

### Step 4: Call self._check_list()

```python
self._check_list(indexes, exp[schema, 'users'], self._required_index_keys)
```

### Step 5: Assign no_cst = value

```python
no_cst = self.tables.no_constraints.name
```

### Step 6: Call self._check_list()

```python
self._check_list(insp.get_indexes(no_cst, schema=schema), exp[schema, no_cst], self._required_index_keys)
```

### Step 7: Assign schema = value

```python
schema = config.test_schema
```

### Step 8: Assign schema = None

```python
schema = None
```


## Complete Example

```python
# Workflow
if use_schema:
    schema = config.test_schema
else:
    schema = None
insp = inspect(connection)
indexes = insp.get_indexes('users', schema=schema)
exp = self.exp_indexes(schema=schema)
self._check_list(indexes, exp[schema, 'users'], self._required_index_keys)
no_cst = self.tables.no_constraints.name
self._check_list(insp.get_indexes(no_cst, schema=schema), exp[schema, no_cst], self._required_index_keys)
```

## Next Steps


---

*Source: test_reflection.py:1988 | Complexity: Advanced | Last updated: 2026-06-02*