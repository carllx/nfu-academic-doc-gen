# How To: Reflect

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reflect

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy.testing`
- `sqlalchemy.testing`
- `sqlalchemy.testing.schema`
- `sqlalchemy.testing.schema`

**Setup Required:**
```python
# Fixtures: connection
```

## Step-by-Step Guide

### Step 1: Call connection.execute()

```python
connection.execute(t1.insert(), {'méil': 2, '測試': 7})
```

### Step 2: Call connection.execute()

```python
connection.execute(t2.insert(), {'a': 2, 'b': 2})
```

### Step 3: Call connection.execute()

```python
connection.execute(t3.insert(), {'測試_id': 2, 'unitable1_測試': 7, 'Unitéble2_b': 2, '測試_self': 2})
```

### Step 4: Assign meta = MetaData(...)

```python
meta = MetaData()
```

### Step 5: Assign tt1 = Table(...)

```python
tt1 = Table(t1.name, meta, autoload_with=connection)
```

### Step 6: Assign tt2 = Table(...)

```python
tt2 = Table(t2.name, meta, autoload_with=connection)
```

### Step 7: Assign tt3 = Table(...)

```python
tt3 = Table(t3.name, meta, autoload_with=connection)
```

### Step 8: Call connection.execute()

```python
connection.execute(tt1.insert(), {'méil': 1, '測試': 5})
```

### Step 9: Call connection.execute()

```python
connection.execute(tt2.insert(), {'méil': 1, '測試': 1})
```

### Step 10: Call connection.execute()

```python
connection.execute(tt3.insert(), {'測試_id': 1, 'unitable1_測試': 5, 'Unitéble2_b': 1, '測試_self': 1})
```

### Step 11: Call eq_()

```python
eq_(connection.execute(tt1.select().order_by(desc('méil'))).fetchall(), [(2, 7), (1, 5)])
```

### Step 12: Call eq_()

```python
eq_(connection.execute(tt2.select().order_by(desc('méil'))).fetchall(), [(2, 2), (1, 1)])
```

### Step 13: Call eq_()

```python
eq_(connection.execute(tt3.select().order_by(desc('測試_id'))).fetchall(), [(2, 7, 2, 2), (1, 5, 1, 1)])
```


## Complete Example

```python
# Setup
# Fixtures: connection

# Workflow
connection.execute(t1.insert(), {'méil': 2, '測試': 7})
connection.execute(t2.insert(), {'a': 2, 'b': 2})
connection.execute(t3.insert(), {'測試_id': 2, 'unitable1_測試': 7, 'Unitéble2_b': 2, '測試_self': 2})
meta = MetaData()
tt1 = Table(t1.name, meta, autoload_with=connection)
tt2 = Table(t2.name, meta, autoload_with=connection)
tt3 = Table(t3.name, meta, autoload_with=connection)
connection.execute(tt1.insert(), {'méil': 1, '測試': 5})
connection.execute(tt2.insert(), {'méil': 1, '測試': 1})
connection.execute(tt3.insert(), {'測試_id': 1, 'unitable1_測試': 5, 'Unitéble2_b': 1, '測試_self': 1})
eq_(connection.execute(tt1.select().order_by(desc('méil'))).fetchall(), [(2, 7), (1, 5)])
eq_(connection.execute(tt2.select().order_by(desc('méil'))).fetchall(), [(2, 2), (1, 1)])
eq_(connection.execute(tt3.select().order_by(desc('測試_id'))).fetchall(), [(2, 7, 2, 2), (1, 5, 1, 1)])
```

## Next Steps


---

*Source: test_unicode_ddl.py:133 | Complexity: Advanced | Last updated: 2026-06-02*