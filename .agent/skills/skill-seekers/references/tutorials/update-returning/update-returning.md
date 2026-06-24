# How To: Update Returning

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test update returning

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `assertions`
- `schema`
- `schema`

**Setup Required:**
```python
# Fixtures: connection, criteria
```

## Step-by-Step Guide

### Step 1: Assign t = value

```python
t = self.tables.plain_pk
```

**Verification:**
```python
assert not r.is_insert
```

### Step 2: Assign stmt = t.update.returning(...)

```python
stmt = t.update().returning(t.c.id, t.c.data)
```

**Verification:**
```python
assert r.returns_rows
```

### Step 3: Assign r = connection.execute(...)

```python
r = connection.execute(stmt, dict(data='d2_new'))
```

**Verification:**
```python
assert not r.is_insert
```

### Step 4: Call eq_()

```python
eq_(r.keys(), ['id', 'data'])
```

### Step 5: Call eq_()

```python
eq_(connection.execute(t.select().order_by(t.c.id)).fetchall(), [(1, 'd1'), (2, 'd2_new'), (3, 'd3')] if criteria.rows else [(1, 'd1'), (2, 'd2'), (3, 'd3')])
```

### Step 6: Assign stmt = stmt.where(...)

```python
stmt = stmt.where(t.c.id == 10)
```

### Step 7: Call eq_()

```python
eq_(r.all(), [(2, 'd2_new')])
```

### Step 8: Call eq_()

```python
eq_(r.all(), [])
```

### Step 9: Assign stmt = stmt.where(...)

```python
stmt = stmt.where(t.c.id == 2)
```

### Step 10: Assign stmt = stmt.where(...)

```python
stmt = stmt.where(t.c.id.in_([]))
```

### Step 11: Call criteria.fail()

```python
criteria.fail()
```


## Complete Example

```python
# Setup
# Fixtures: connection, criteria

# Workflow
t = self.tables.plain_pk
stmt = t.update().returning(t.c.id, t.c.data)
if criteria.norows:
    stmt = stmt.where(t.c.id == 10)
elif criteria.rows:
    stmt = stmt.where(t.c.id == 2)
elif criteria.emptyin:
    stmt = stmt.where(t.c.id.in_([]))
else:
    criteria.fail()
r = connection.execute(stmt, dict(data='d2_new'))
assert not r.is_insert
assert r.returns_rows
eq_(r.keys(), ['id', 'data'])
if criteria.rows:
    eq_(r.all(), [(2, 'd2_new')])
else:
    eq_(r.all(), [])
eq_(connection.execute(t.select().order_by(t.c.id)).fetchall(), [(1, 'd1'), (2, 'd2_new'), (3, 'd3')] if criteria.rows else [(1, 'd1'), (2, 'd2'), (3, 'd3')])
```

## Next Steps


---

*Source: test_update_delete.py:70 | Complexity: Advanced | Last updated: 2026-06-02*