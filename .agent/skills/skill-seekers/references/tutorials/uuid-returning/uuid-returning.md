# How To: Uuid Returning

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test uuid returning

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
# Fixtures: connection
```

## Step-by-Step Guide

### Step 1: Assign data = uuid.uuid4(...)

```python
data = uuid.uuid4()
```

### Step 2: Assign str_data = str(...)

```python
str_data = str(data)
```

### Step 3: Assign uuid_table = value

```python
uuid_table = self.tables.uuid_table
```

### Step 4: Assign result = connection.execute(...)

```python
result = connection.execute(uuid_table.insert().returning(uuid_table.c.uuid_data, uuid_table.c.uuid_text_data, uuid_table.c.uuid_data_nonnative, uuid_table.c.uuid_text_data_nonnative), {'id': 1, 'uuid_data': data, 'uuid_text_data': str_data, 'uuid_data_nonnative': data, 'uuid_text_data_nonnative': str_data})
```

### Step 5: Assign row = result.first(...)

```python
row = result.first()
```

### Step 6: Call eq_()

```python
eq_(row, (data, str_data, data, str_data))
```


## Complete Example

```python
# Setup
# Fixtures: connection

# Workflow
data = uuid.uuid4()
str_data = str(data)
uuid_table = self.tables.uuid_table
result = connection.execute(uuid_table.insert().returning(uuid_table.c.uuid_data, uuid_table.c.uuid_text_data, uuid_table.c.uuid_data_nonnative, uuid_table.c.uuid_text_data_nonnative), {'id': 1, 'uuid_data': data, 'uuid_text_data': str_data, 'uuid_data_nonnative': data, 'uuid_text_data_nonnative': str_data})
row = result.first()
eq_(row, (data, str_data, data, str_data))
```

## Next Steps


---

*Source: test_types.py:2086 | Complexity: Intermediate | Last updated: 2026-06-02*