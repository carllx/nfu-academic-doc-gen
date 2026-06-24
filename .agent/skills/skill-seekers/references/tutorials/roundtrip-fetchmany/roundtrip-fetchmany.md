# How To: Roundtrip Fetchmany

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test roundtrip fetchmany

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `assertions`
- `config`
- `schema`
- `schema`

**Setup Required:**
```python
# Fixtures: metadata
```

## Step-by-Step Guide

### Step 1: Assign md = value

```python
md = self.metadata
```

### Step 2: Assign engine = self._fixture(...)

```python
engine = self._fixture(True)
```

### Step 3: Assign test_table = Table(...)

```python
test_table = Table('test_table', md, Column('id', Integer, primary_key=True, test_needs_autoincrement=True), Column('data', String(50)))
```

### Step 4: Call test_table.create()

```python
test_table.create(connection, checkfirst=True)
```

### Step 5: Call connection.execute()

```python
connection.execute(test_table.insert(), [dict(data='data%d' % i) for i in range(1, 20)])
```

### Step 6: Assign result = connection.execute(...)

```python
result = connection.execute(test_table.select().order_by(test_table.c.id))
```

### Step 7: Call eq_()

```python
eq_(result.fetchmany(5), [(i, 'data%d' % i) for i in range(1, 6)])
```

### Step 8: Call eq_()

```python
eq_(result.fetchmany(10), [(i, 'data%d' % i) for i in range(6, 16)])
```

### Step 9: Call eq_()

```python
eq_(result.fetchall(), [(i, 'data%d' % i) for i in range(16, 20)])
```


## Complete Example

```python
# Setup
# Fixtures: metadata

# Workflow
md = self.metadata
engine = self._fixture(True)
test_table = Table('test_table', md, Column('id', Integer, primary_key=True, test_needs_autoincrement=True), Column('data', String(50)))
with engine.begin() as connection:
    test_table.create(connection, checkfirst=True)
    connection.execute(test_table.insert(), [dict(data='data%d' % i) for i in range(1, 20)])
    result = connection.execute(test_table.select().order_by(test_table.c.id))
    eq_(result.fetchmany(5), [(i, 'data%d' % i) for i in range(1, 6)])
    eq_(result.fetchmany(10), [(i, 'data%d' % i) for i in range(6, 16)])
    eq_(result.fetchall(), [(i, 'data%d' % i) for i in range(16, 20)])
```

## Next Steps


---

*Source: test_results.py:472 | Complexity: Advanced | Last updated: 2026-06-02*