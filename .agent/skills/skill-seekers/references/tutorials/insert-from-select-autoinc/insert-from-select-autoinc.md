# How To: Insert From Select Autoinc

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert from select autoinc

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
# Fixtures: connection
```

## Step-by-Step Guide

### Step 1: Assign src_table = value

```python
src_table = self.tables.manual_pk
```

### Step 2: Assign dest_table = value

```python
dest_table = self.tables.autoinc_pk
```

### Step 3: Call connection.execute()

```python
connection.execute(src_table.insert(), [dict(id=1, data='data1'), dict(id=2, data='data2'), dict(id=3, data='data3')])
```

### Step 4: Assign result = connection.execute(...)

```python
result = connection.execute(dest_table.insert().from_select(('data',), select(src_table.c.data).where(src_table.c.data.in_(['data2', 'data3']))))
```

### Step 5: Call eq_()

```python
eq_(result.inserted_primary_key, (None,))
```

### Step 6: Assign result = connection.execute(...)

```python
result = connection.execute(select(dest_table.c.data).order_by(dest_table.c.data))
```

### Step 7: Call eq_()

```python
eq_(result.fetchall(), [('data2',), ('data3',)])
```


## Complete Example

```python
# Setup
# Fixtures: connection

# Workflow
src_table = self.tables.manual_pk
dest_table = self.tables.autoinc_pk
connection.execute(src_table.insert(), [dict(id=1, data='data1'), dict(id=2, data='data2'), dict(id=3, data='data3')])
result = connection.execute(dest_table.insert().from_select(('data',), select(src_table.c.data).where(src_table.c.data.in_(['data2', 'data3']))))
eq_(result.inserted_primary_key, (None,))
result = connection.execute(select(dest_table.c.data).order_by(dest_table.c.data))
eq_(result.fetchall(), [('data2',), ('data3',)])
```

## Next Steps


---

*Source: test_insert.py:235 | Complexity: Intermediate | Last updated: 2026-06-02*