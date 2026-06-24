# How To: Imv Returning Datatypes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test #9739, #9808 (similar to #9701).

this tests insertmanyvalues in conjunction with various datatypes.

These tests are particularly for the asyncpg driver which needs
most types to be explicitly cast for the new IMV format

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `uuid`
- `assertions`
- `config`
- `schema`
- `schema`
- `types`
- `types`
- `types`

**Setup Required:**
```python
# Fixtures: connection, metadata, sort_by_parameter_order, type_, value, multiple_rows
```

## Step-by-Step Guide

### Step 1: 'test #9739, #9808 (similar to #9701).\n\n        this tests insertmanyvalues in conjunction with various datatypes.\n\n        These tests are particularly for the asyncpg driver which needs\n        most types to be explicitly cast for the new IMV format\n\n        '

```python
'test #9739, #9808 (similar to #9701).\n\n        this tests insertmanyvalues in conjunction with various datatypes.\n\n        These tests are particularly for the asyncpg driver which needs\n        most types to be explicitly cast for the new IMV format\n\n        '
```

### Step 2: Assign t = Table(...)

```python
t = Table('d_t', metadata, Column('id', Integer, Identity(), primary_key=True), Column('value', type_))
```

### Step 3: Call t.create()

```python
t.create(connection)
```

### Step 4: Assign result = connection.execute(...)

```python
result = connection.execute(t.insert().returning(t.c.id, t.c.value, sort_by_parameter_order=bool(sort_by_parameter_order)), [{'value': value} for i in range(10)] if multiple_rows else {'value': value})
```

### Step 5: Call eq_()

```python
eq_(set(result), {(id_, value) for id_ in i_range})
```

### Step 6: Call eq_()

```python
eq_(set(connection.scalars(select(t.c.value))), {value})
```

### Step 7: Assign i_range = range(...)

```python
i_range = range(1, 11)
```

### Step 8: Assign i_range = range(...)

```python
i_range = range(1, 2)
```


## Complete Example

```python
# Setup
# Fixtures: connection, metadata, sort_by_parameter_order, type_, value, multiple_rows

# Workflow
'test #9739, #9808 (similar to #9701).\n\n        this tests insertmanyvalues in conjunction with various datatypes.\n\n        These tests are particularly for the asyncpg driver which needs\n        most types to be explicitly cast for the new IMV format\n\n        '
t = Table('d_t', metadata, Column('id', Integer, Identity(), primary_key=True), Column('value', type_))
t.create(connection)
result = connection.execute(t.insert().returning(t.c.id, t.c.value, sort_by_parameter_order=bool(sort_by_parameter_order)), [{'value': value} for i in range(10)] if multiple_rows else {'value': value})
if multiple_rows:
    i_range = range(1, 11)
else:
    i_range = range(1, 2)
eq_(set(result), {(id_, value) for id_ in i_range})
eq_(set(connection.scalars(select(t.c.value))), {value})
```

## Next Steps


---

*Source: test_insert.py:575 | Complexity: Advanced | Last updated: 2026-06-02*