# How To: Arithmetic Operation Table Interval And Literal Interval

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arithmetic operation table interval and literal interval

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
# Fixtures: connection, arithmetic_table_fixture
```

## Step-by-Step Guide

### Step 1: Assign interval_table = arithmetic_table_fixture

```python
interval_table = arithmetic_table_fixture
```

### Step 2: Assign data = datetime.timedelta(...)

```python
data = datetime.timedelta(days=2, seconds=5)
```

### Step 3: Call connection.execute()

```python
connection.execute(interval_table.insert(), {'id': 1, 'interval_data': data})
```

### Step 4: Assign value = connection.execute.scalar(...)

```python
value = connection.execute(select(interval_table.c.interval_data - literal(self.data))).scalar()
```

### Step 5: Call eq_()

```python
eq_(value, data - self.data)
```

### Step 6: Assign value = connection.execute.scalar(...)

```python
value = connection.execute(select(interval_table.c.interval_data + literal(self.data))).scalar()
```

### Step 7: Call eq_()

```python
eq_(value, data + self.data)
```


## Complete Example

```python
# Setup
# Fixtures: connection, arithmetic_table_fixture

# Workflow
interval_table = arithmetic_table_fixture
data = datetime.timedelta(days=2, seconds=5)
connection.execute(interval_table.insert(), {'id': 1, 'interval_data': data})
value = connection.execute(select(interval_table.c.interval_data - literal(self.data))).scalar()
eq_(value, data - self.data)
value = connection.execute(select(interval_table.c.interval_data + literal(self.data))).scalar()
eq_(value, data + self.data)
```

## Next Steps


---

*Source: test_types.py:522 | Complexity: Intermediate | Last updated: 2026-06-02*