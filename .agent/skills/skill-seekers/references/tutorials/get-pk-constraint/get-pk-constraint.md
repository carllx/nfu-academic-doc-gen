# How To: Get Pk Constraint

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get pk constraint

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

### Step 3: Assign exp = self.exp_pks(...)

```python
exp = self.exp_pks(schema=schema)
```

### Step 4: Assign users_cons = insp.get_pk_constraint(...)

```python
users_cons = insp.get_pk_constraint(users.name, schema=schema)
```

### Step 5: Call self._check_list()

```python
self._check_list([users_cons], [exp[schema, users.name]], self._required_pk_keys)
```

### Step 6: Assign addr_cons = insp.get_pk_constraint(...)

```python
addr_cons = insp.get_pk_constraint(addresses.name, schema=schema)
```

### Step 7: Assign exp_cols = value

```python
exp_cols = exp[schema, addresses.name]['constrained_columns']
```

### Step 8: Call eq_()

```python
eq_(addr_cons['constrained_columns'], exp_cols)
```

### Step 9: Assign no_cst = value

```python
no_cst = self.tables.no_constraints.name
```

### Step 10: Call self._check_list()

```python
self._check_list([insp.get_pk_constraint(no_cst, schema=schema)], [exp[schema, no_cst]], self._required_pk_keys)
```

### Step 11: Assign schema = value

```python
schema = testing.config.test_schema
```

### Step 12: Assign schema = None

```python
schema = None
```

### Step 13: Call eq_()

```python
eq_(addr_cons['name'], 'email_ad_pk')
```


## Complete Example

```python
# Workflow
if use_schema:
    schema = testing.config.test_schema
else:
    schema = None
users, addresses = (self.tables.users, self.tables.email_addresses)
insp = inspect(connection)
exp = self.exp_pks(schema=schema)
users_cons = insp.get_pk_constraint(users.name, schema=schema)
self._check_list([users_cons], [exp[schema, users.name]], self._required_pk_keys)
addr_cons = insp.get_pk_constraint(addresses.name, schema=schema)
exp_cols = exp[schema, addresses.name]['constrained_columns']
eq_(addr_cons['constrained_columns'], exp_cols)
with testing.requires.reflects_pk_names.fail_if():
    eq_(addr_cons['name'], 'email_ad_pk')
no_cst = self.tables.no_constraints.name
self._check_list([insp.get_pk_constraint(no_cst, schema=schema)], [exp[schema, no_cst]], self._required_pk_keys)
```

## Next Steps


---

*Source: test_reflection.py:1797 | Complexity: Advanced | Last updated: 2026-06-02*