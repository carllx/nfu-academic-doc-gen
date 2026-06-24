# How To: Round Trip None As Json Null

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test round trip none as json null

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
# Fixtures: connection, insert_type
```

## Step-by-Step Guide

### Step 1: Assign col = value

```python
col = self.tables.data_table.c['data']
```

**Verification:**
```python
assert False
```

### Step 2: Assign conn = connection

```python
conn = connection
```

### Step 3: Call conn.execute()

```python
conn.execute(stmt, params)
```

### Step 4: Call eq_()

```python
eq_(conn.scalar(select(self.tables.data_table.c.name).where(cast(col, String) == 'null')), 'r1')
```

### Step 5: Call eq_()

```python
eq_(conn.scalar(select(col)), None)
```

### Step 6: Assign unknown = value

```python
stmt, params = (self.tables.data_table.insert(), {'name': 'r1', 'data': None})
```

### Step 7: Assign unknown = value

```python
stmt, params = (self.tables.data_table.insert(), [{'name': 'r1', 'data': None}])
```

### Step 8: Assign unknown = value

```python
stmt, params = (self.tables.data_table.insert().values(name='r1', data=None), {})
```

**Verification:**
```python
assert False
```


## Complete Example

```python
# Setup
# Fixtures: connection, insert_type

# Workflow
col = self.tables.data_table.c['data']
if insert_type == 'parameters':
    stmt, params = (self.tables.data_table.insert(), {'name': 'r1', 'data': None})
elif insert_type == 'multiparameters':
    stmt, params = (self.tables.data_table.insert(), [{'name': 'r1', 'data': None}])
elif insert_type == 'values':
    stmt, params = (self.tables.data_table.insert().values(name='r1', data=None), {})
else:
    assert False
conn = connection
conn.execute(stmt, params)
eq_(conn.scalar(select(self.tables.data_table.c.name).where(cast(col, String) == 'null')), 'r1')
eq_(conn.scalar(select(col)), None)
```

## Next Steps


---

*Source: test_types.py:1698 | Complexity: Advanced | Last updated: 2026-06-02*