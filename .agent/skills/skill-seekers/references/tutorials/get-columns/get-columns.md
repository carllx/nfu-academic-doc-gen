# How To: Get Columns

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get columns

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

### Step 1: Assign unknown = value

```python
users, addresses = (self.tables.users, self.tables.email_addresses)
```

**Verification:**
```python
assert cols[i]['default'] is None
```

### Step 2: Assign insp = inspect(...)

```python
insp = inspect(connection)
```

### Step 3: Assign schema = value

```python
schema = config.test_schema
```

### Step 4: Assign schema = None

```python
schema = None
```

### Step 5: Assign table_names = value

```python
table_names = ['users_v', 'email_addresses_v', 'dingalings_v']
```

### Step 6: Assign table_names = value

```python
table_names = ['users', 'email_addresses']
```

### Step 7: Assign schema_name = schema

```python
schema_name = schema
```

### Step 8: Assign cols = insp.get_columns(...)

```python
cols = insp.get_columns(table_name, schema=schema_name)
```

### Step 9: Call is_true()

```python
is_true(len(cols) > 0, len(cols))
```

### Step 10: Call eq_()

```python
eq_(col.name, cols[i]['name'])
```

### Step 11: Assign ctype = value

```python
ctype = cols[i]['type'].__class__
```

### Step 12: Assign ctype_def = value

```python
ctype_def = col.type
```

### Step 13: Call is_true()

```python
is_true(len(set(ctype.__mro__).intersection(ctype_def.__mro__).intersection([sql_types.Integer, sql_types.Numeric, sql_types.DateTime, sql_types.Date, sql_types.Time, sql_types.String, sql_types._Binary])) > 0, '%s(%s), %s(%s)' % (col.name, col.type, cols[i]['name'], ctype))
```

### Step 14: Assign ctype_def = value

```python
ctype_def = ctype_def.__class__
```

### Step 15: Assign ctype_def = value

```python
ctype_def = sql_types.Date
```

**Verification:**
```python
assert cols[i]['default'] is None
```


## Complete Example

```python
# Workflow
if use_schema:
    schema = config.test_schema
else:
    schema = None
users, addresses = (self.tables.users, self.tables.email_addresses)
if use_views:
    table_names = ['users_v', 'email_addresses_v', 'dingalings_v']
else:
    table_names = ['users', 'email_addresses']
insp = inspect(connection)
for table_name, table in zip(table_names, (users, addresses)):
    schema_name = schema
    cols = insp.get_columns(table_name, schema=schema_name)
    is_true(len(cols) > 0, len(cols))
    for i, col in enumerate(table.columns):
        eq_(col.name, cols[i]['name'])
        ctype = cols[i]['type'].__class__
        ctype_def = col.type
        if isinstance(ctype_def, sa.types.TypeEngine):
            ctype_def = ctype_def.__class__
        if testing.against('oracle') and ctype_def in (sql_types.Date, sql_types.DateTime):
            ctype_def = sql_types.Date
        is_true(len(set(ctype.__mro__).intersection(ctype_def.__mro__).intersection([sql_types.Integer, sql_types.Numeric, sql_types.DateTime, sql_types.Date, sql_types.Time, sql_types.String, sql_types._Binary])) > 0, '%s(%s), %s(%s)' % (col.name, col.type, cols[i]['name'], ctype))
        if not col.primary_key:
            assert cols[i]['default'] is None
```

## Next Steps


---

*Source: test_reflection.py:1697 | Complexity: Advanced | Last updated: 2026-06-02*