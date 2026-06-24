# How To: Special Type

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test special type

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `json`
- `re`
- `uuid`
- `assertions`
- `assertions`
- `assertions`
- `config`
- `schema`
- `schema`
- `orm`
- `orm`
- `sql`
- `sql.sqltypes`
- `sql.sqltypes`

**Setup Required:**
```python
# Fixtures: metadata, connection, string_as_int
```

## Step-by-Step Guide

### Step 1: Assign type_ = string_as_int

```python
type_ = string_as_int
```

### Step 2: Assign t = Table(...)

```python
t = Table('t', metadata, Column('x', type_))
```

### Step 3: Call t.create()

```python
t.create(connection)
```

### Step 4: Call connection.execute()

```python
connection.execute(t.insert(), [{'x': x} for x in [1, 2, 3]])
```

### Step 5: Assign result = value

```python
result = {row[0] for row in connection.execute(t.select())}
```

### Step 6: Call eq_()

```python
eq_(result, {1, 2, 3})
```

### Step 7: Assign result = value

```python
result = {row[0] for row in connection.execute(t.select().where(t.c.x == 2))}
```

### Step 8: Call eq_()

```python
eq_(result, {2})
```


## Complete Example

```python
# Setup
# Fixtures: metadata, connection, string_as_int

# Workflow
type_ = string_as_int
t = Table('t', metadata, Column('x', type_))
t.create(connection)
connection.execute(t.insert(), [{'x': x} for x in [1, 2, 3]])
result = {row[0] for row in connection.execute(t.select())}
eq_(result, {1, 2, 3})
result = {row[0] for row in connection.execute(t.select().where(t.c.x == 2))}
eq_(result, {2})
```

## Next Steps


---

*Source: test_types.py:879 | Complexity: Advanced | Last updated: 2026-06-02*