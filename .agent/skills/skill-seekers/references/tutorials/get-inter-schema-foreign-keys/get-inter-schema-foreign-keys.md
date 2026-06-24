# How To: Get Inter Schema Foreign Keys

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get inter schema foreign keys

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

### Step 1: Assign unknown = self.tables(...)

```python
local_table, remote_table, remote_table_2 = self.tables('%s.local_table' % connection.dialect.default_schema_name, '%s.remote_table' % testing.config.test_schema, '%s.remote_table_2' % testing.config.test_schema)
```

### Step 2: Assign insp = inspect(...)

```python
insp = inspect(connection)
```

### Step 3: Assign local_fkeys = insp.get_foreign_keys(...)

```python
local_fkeys = insp.get_foreign_keys(local_table.name)
```

### Step 4: Call eq_()

```python
eq_(len(local_fkeys), 1)
```

### Step 5: Assign fkey1 = value

```python
fkey1 = local_fkeys[0]
```

### Step 6: Call eq_()

```python
eq_(fkey1['referred_schema'], testing.config.test_schema)
```

### Step 7: Call eq_()

```python
eq_(fkey1['referred_table'], remote_table_2.name)
```

### Step 8: Call eq_()

```python
eq_(fkey1['referred_columns'], ['id'])
```

### Step 9: Call eq_()

```python
eq_(fkey1['constrained_columns'], ['remote_id'])
```

### Step 10: Assign remote_fkeys = insp.get_foreign_keys(...)

```python
remote_fkeys = insp.get_foreign_keys(remote_table.name, schema=testing.config.test_schema)
```

### Step 11: Call eq_()

```python
eq_(len(remote_fkeys), 1)
```

### Step 12: Assign fkey2 = value

```python
fkey2 = remote_fkeys[0]
```

### Step 13: Call is_true()

```python
is_true(fkey2['referred_schema'] in (None, connection.dialect.default_schema_name))
```

### Step 14: Call eq_()

```python
eq_(fkey2['referred_table'], local_table.name)
```

### Step 15: Call eq_()

```python
eq_(fkey2['referred_columns'], ['id'])
```

### Step 16: Call eq_()

```python
eq_(fkey2['constrained_columns'], ['local_id'])
```


## Complete Example

```python
# Workflow
local_table, remote_table, remote_table_2 = self.tables('%s.local_table' % connection.dialect.default_schema_name, '%s.remote_table' % testing.config.test_schema, '%s.remote_table_2' % testing.config.test_schema)
insp = inspect(connection)
local_fkeys = insp.get_foreign_keys(local_table.name)
eq_(len(local_fkeys), 1)
fkey1 = local_fkeys[0]
eq_(fkey1['referred_schema'], testing.config.test_schema)
eq_(fkey1['referred_table'], remote_table_2.name)
eq_(fkey1['referred_columns'], ['id'])
eq_(fkey1['constrained_columns'], ['remote_id'])
remote_fkeys = insp.get_foreign_keys(remote_table.name, schema=testing.config.test_schema)
eq_(len(remote_fkeys), 1)
fkey2 = remote_fkeys[0]
is_true(fkey2['referred_schema'] in (None, connection.dialect.default_schema_name))
eq_(fkey2['referred_table'], local_table.name)
eq_(fkey2['referred_columns'], ['id'])
eq_(fkey2['constrained_columns'], ['local_id'])
```

## Next Steps


---

*Source: test_reflection.py:1948 | Complexity: Advanced | Last updated: 2026-06-02*