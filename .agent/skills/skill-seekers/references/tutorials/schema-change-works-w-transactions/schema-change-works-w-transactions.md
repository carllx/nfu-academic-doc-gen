# How To: Schema Change Works W Transactions

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test schema change works w transactions

## Prerequisites

**Required Modules:**
- `importlib`
- `assertions`
- `assertions`
- `config`
- `provision`
- `schema`
- `schema`
- `sql.compiler`
- `util`


## Step-by-Step Guide

### Step 1: Assign eng = engines.testing_engine(...)

```python
eng = engines.testing_engine()
```

### Step 2: Call eq_()

```python
eq_(eng.dialect.default_schema_name, config.test_schema)
```

### Step 3: Call set_default_schema_on_connection()

```python
set_default_schema_on_connection(config, dbapi_connection, config.test_schema)
```

### Step 4: Assign trans = conn.begin(...)

```python
trans = conn.begin()
```

### Step 5: Assign what_it_should_be = eng.dialect._get_default_schema_name(...)

```python
what_it_should_be = eng.dialect._get_default_schema_name(conn)
```

### Step 6: Call eq_()

```python
eq_(what_it_should_be, config.test_schema)
```

### Step 7: Call trans.rollback()

```python
trans.rollback()
```

### Step 8: Assign what_it_should_be = eng.dialect._get_default_schema_name(...)

```python
what_it_should_be = eng.dialect._get_default_schema_name(conn)
```

### Step 9: Call eq_()

```python
eq_(what_it_should_be, config.test_schema)
```


## Complete Example

```python
# Workflow
eng = engines.testing_engine()

@event.listens_for(eng, 'connect', insert=True)
def on_connect(dbapi_connection, *arg):
    set_default_schema_on_connection(config, dbapi_connection, config.test_schema)
with eng.connect() as conn:
    trans = conn.begin()
    what_it_should_be = eng.dialect._get_default_schema_name(conn)
    eq_(what_it_should_be, config.test_schema)
    trans.rollback()
    what_it_should_be = eng.dialect._get_default_schema_name(conn)
    eq_(what_it_should_be, config.test_schema)
eq_(eng.dialect.default_schema_name, config.test_schema)
```

## Next Steps


---

*Source: test_dialect.py:483 | Complexity: Advanced | Last updated: 2026-06-02*