# How To: Get View Names

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get view names

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

### Step 2: Assign table_names = insp.get_view_names(...)

```python
table_names = insp.get_view_names(schema)
```

### Step 3: Assign schema = value

```python
schema = config.test_schema
```

### Step 4: Assign schema = None

```python
schema = None
```

### Step 5: Call eq_()

```python
eq_(sorted(table_names), ['email_addresses_v', 'users_v'])
```

### Step 6: Call eq_()

```python
eq_(insp.get_materialized_view_names(schema), ['dingalings_v'])
```

### Step 7: Assign answer = value

```python
answer = ['dingalings_v', 'email_addresses_v', 'users_v']
```

### Step 8: Call eq_()

```python
eq_(sorted(table_names), answer)
```


## Complete Example

```python
# Workflow
insp = inspect(connection)
if use_schema:
    schema = config.test_schema
else:
    schema = None
table_names = insp.get_view_names(schema)
if testing.requires.materialized_views.enabled:
    eq_(sorted(table_names), ['email_addresses_v', 'users_v'])
    eq_(insp.get_materialized_view_names(schema), ['dingalings_v'])
else:
    answer = ['dingalings_v', 'email_addresses_v', 'users_v']
    eq_(sorted(table_names), answer)
```

## Next Steps


---

*Source: test_reflection.py:1626 | Complexity: Advanced | Last updated: 2026-06-02*