# How To: Get Foreign Keys

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get foreign keys

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

### Step 2: Assign insp = inspect(...)

```python
insp = inspect(connection)
```

### Step 3: Assign expected_schema = schema

```python
expected_schema = schema
```

### Step 4: Assign addr_fkeys = insp.get_foreign_keys(...)

```python
addr_fkeys = insp.get_foreign_keys(addresses.name, schema=schema)
```

### Step 5: Assign fkey1 = value

```python
fkey1 = addr_fkeys[0]
```

### Step 6: Call eq_()

```python
eq_(fkey1['referred_schema'], expected_schema)
```

### Step 7: Call eq_()

```python
eq_(fkey1['referred_table'], users.name)
```

### Step 8: Call eq_()

```python
eq_(fkey1['referred_columns'], ['user_id'])
```

### Step 9: Call eq_()

```python
eq_(fkey1['constrained_columns'], ['remote_user_id'])
```

### Step 10: Assign no_cst = value

```python
no_cst = self.tables.no_constraints.name
```

### Step 11: Call eq_()

```python
eq_(insp.get_foreign_keys(no_cst, schema=schema), [])
```

### Step 12: Assign schema = value

```python
schema = config.test_schema
```

### Step 13: Assign schema = None

```python
schema = None
```

### Step 14: Assign users_fkeys = insp.get_foreign_keys(...)

```python
users_fkeys = insp.get_foreign_keys(users.name, schema=schema)
```

### Step 15: Assign fkey1 = value

```python
fkey1 = users_fkeys[0]
```

### Step 16: Call eq_()

```python
eq_(fkey1['referred_schema'], expected_schema)
```

### Step 17: Call eq_()

```python
eq_(fkey1['referred_table'], users.name)
```

### Step 18: Call eq_()

```python
eq_(fkey1['referred_columns'], ['user_id'])
```

### Step 19: Call eq_()

```python
eq_(fkey1['constrained_columns'], ['parent_user_id'])
```

### Step 20: Call is_true()

```python
is_true(fkey1['name'] is not None)
```

### Step 21: Call eq_()

```python
eq_(fkey1['name'], 'user_id_fk')
```


## Complete Example

```python
# Workflow
if use_schema:
    schema = config.test_schema
else:
    schema = None
users, addresses = (self.tables.users, self.tables.email_addresses)
insp = inspect(connection)
expected_schema = schema
if testing.requires.self_referential_foreign_keys.enabled:
    users_fkeys = insp.get_foreign_keys(users.name, schema=schema)
    fkey1 = users_fkeys[0]
    with testing.requires.named_constraints.fail_if():
        eq_(fkey1['name'], 'user_id_fk')
    eq_(fkey1['referred_schema'], expected_schema)
    eq_(fkey1['referred_table'], users.name)
    eq_(fkey1['referred_columns'], ['user_id'])
    eq_(fkey1['constrained_columns'], ['parent_user_id'])
addr_fkeys = insp.get_foreign_keys(addresses.name, schema=schema)
fkey1 = addr_fkeys[0]
with testing.requires.implicitly_named_constraints.fail_if():
    is_true(fkey1['name'] is not None)
eq_(fkey1['referred_schema'], expected_schema)
eq_(fkey1['referred_table'], users.name)
eq_(fkey1['referred_columns'], ['user_id'])
eq_(fkey1['constrained_columns'], ['remote_user_id'])
no_cst = self.tables.no_constraints.name
eq_(insp.get_foreign_keys(no_cst, schema=schema), [])
```

## Next Steps


---

*Source: test_reflection.py:1861 | Complexity: Advanced | Last updated: 2026-06-02*