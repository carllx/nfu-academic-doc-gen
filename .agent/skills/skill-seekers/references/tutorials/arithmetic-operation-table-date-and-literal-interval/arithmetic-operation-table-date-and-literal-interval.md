# How To: Arithmetic Operation Table Date And Literal Interval

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arithmetic operation table date and literal interval

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

### Step 2: Assign now = datetime.datetime.now.replace(...)

```python
now = datetime.datetime.now().replace(microsecond=0)
```

### Step 3: Call connection.execute()

```python
connection.execute(interval_table.insert(), {'id': 1, 'date_data': now})
```

### Step 4: Assign value = connection.execute.scalar(...)

```python
value = connection.execute(select(interval_table.c.date_data - literal(self.data))).scalar()
```

### Step 5: Call eq_()

```python
eq_(value, now - self.data)
```

### Step 6: Assign value = connection.execute.scalar(...)

```python
value = connection.execute(select(interval_table.c.date_data + literal(self.data))).scalar()
```

### Step 7: Call eq_()

```python
eq_(value, now + self.data)
```


## Complete Example

```python
# Setup
# Fixtures: connection, arithmetic_table_fixture

# Workflow
interval_table = arithmetic_table_fixture
now = datetime.datetime.now().replace(microsecond=0)
connection.execute(interval_table.insert(), {'id': 1, 'date_data': now})
value = connection.execute(select(interval_table.c.date_data - literal(self.data))).scalar()
eq_(value, now - self.data)
value = connection.execute(select(interval_table.c.date_data + literal(self.data))).scalar()
eq_(value, now + self.data)
```

## Next Steps


---

*Source: test_types.py:542 | Complexity: Intermediate | Last updated: 2026-06-02*