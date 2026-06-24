# How To: Round Trip Same Named Column

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test round trip same named column

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: paramname, connection, metadata
```

## Step-by-Step Guide

### Step 1: Assign name = paramname

```python
name = paramname
```

### Step 2: Assign t = Table(...)

```python
t = Table('t', metadata, Column('id', Integer, primary_key=True), Column(name, String(50), nullable=False))
```

### Step 3: Call t.create()

```python
t.create(connection)
```

### Step 4: Call connection.execute()

```python
connection.execute(t.insert().values({'id': 1, name: 'some name'}))
```

### Step 5: Assign stmt = select.where(...)

```python
stmt = select(t.c[name]).where(t.c[name] == 'some name')
```

### Step 6: Call eq_()

```python
eq_(connection.scalar(stmt), 'some name')
```

### Step 7: Assign stmt = select.where(...)

```python
stmt = select(t.c[name]).where(t.c[name] == bindparam(name))
```

### Step 8: Assign row = connection.execute.first(...)

```python
row = connection.execute(stmt, {name: 'some name'}).first()
```

### Step 9: Call eq_()

```python
eq_(row._mapping[name], 'some name')
```

### Step 10: Assign stmt = select.where(...)

```python
stmt = select(t.c[name]).where(t.c[name].in_(['some name', 'some other_name']))
```

### Step 11: Call connection.execute.first()

```python
connection.execute(stmt).first()
```


## Complete Example

```python
# Setup
# Fixtures: paramname, connection, metadata

# Workflow
name = paramname
t = Table('t', metadata, Column('id', Integer, primary_key=True), Column(name, String(50), nullable=False))
t.create(connection)
connection.execute(t.insert().values({'id': 1, name: 'some name'}))
stmt = select(t.c[name]).where(t.c[name] == 'some name')
eq_(connection.scalar(stmt), 'some name')
stmt = select(t.c[name]).where(t.c[name] == bindparam(name))
row = connection.execute(stmt, {name: 'some name'}).first()
eq_(row._mapping[name], 'some name')
stmt = select(t.c[name]).where(t.c[name].in_(['some name', 'some other_name']))
connection.execute(stmt).first()
```

## Next Steps


---

*Source: test_dialect.py:540 | Complexity: Advanced | Last updated: 2026-06-02*