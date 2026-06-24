# How To: Get Table Names

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get table names

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

### Step 1: Assign _ignore_tables = value

```python
_ignore_tables = {'comment_test', 'noncol_idx_test_pk', 'noncol_idx_test_nopk', 'local_table', 'remote_table', 'remote_table_2', 'no_constraints'}
```

### Step 2: Assign insp = inspect(...)

```python
insp = inspect(connection)
```

### Step 3: Assign table_names = value

```python
table_names = [t for t in tables if t not in _ignore_tables]
```

### Step 4: Assign schema = value

```python
schema = config.test_schema
```

### Step 5: Assign schema = None

```python
schema = None
```

### Step 6: Assign tables = value

```python
tables = [rec[0] for rec in insp.get_sorted_table_and_fkc_names(schema) if rec[0]]
```

### Step 7: Assign tables = insp.get_table_names(...)

```python
tables = insp.get_table_names(schema)
```

### Step 8: Assign answer = value

```python
answer = ['users', 'email_addresses', 'dingalings']
```

### Step 9: Call eq_()

```python
eq_(table_names, answer)
```

### Step 10: Assign answer = value

```python
answer = ['dingalings', 'email_addresses', 'users']
```

### Step 11: Call eq_()

```python
eq_(sorted(table_names), answer)
```


## Complete Example

```python
# Workflow
if use_schema:
    schema = config.test_schema
else:
    schema = None
_ignore_tables = {'comment_test', 'noncol_idx_test_pk', 'noncol_idx_test_nopk', 'local_table', 'remote_table', 'remote_table_2', 'no_constraints'}
insp = inspect(connection)
if order_by:
    tables = [rec[0] for rec in insp.get_sorted_table_and_fkc_names(schema) if rec[0]]
else:
    tables = insp.get_table_names(schema)
table_names = [t for t in tables if t not in _ignore_tables]
if order_by == 'foreign_key':
    answer = ['users', 'email_addresses', 'dingalings']
    eq_(table_names, answer)
else:
    answer = ['dingalings', 'email_addresses', 'users']
    eq_(sorted(table_names), answer)
```

## Next Steps


---

*Source: test_reflection.py:1588 | Complexity: Advanced | Last updated: 2026-06-02*