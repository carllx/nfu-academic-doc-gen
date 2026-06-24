# How To: Explicit Returning Pk No Autocommit

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test explicit returning pk no autocommit

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

### Step 1: Assign table = value

```python
table = self.tables.autoinc_pk
```

### Step 2: Assign r = connection.execute(...)

```python
r = connection.execute(table.insert().returning(table.c.id), dict(data='some data'))
```

### Step 3: Assign pk = value

```python
pk = r.first()[0]
```

### Step 4: Assign fetched_pk = connection.scalar(...)

```python
fetched_pk = connection.scalar(select(table.c.id))
```

### Step 5: Call eq_()

```python
eq_(fetched_pk, pk)
```


## Complete Example

```python
# Setup
# Fixtures: connection

# Workflow
table = self.tables.autoinc_pk
r = connection.execute(table.insert().returning(table.c.id), dict(data='some data'))
pk = r.first()[0]
fetched_pk = connection.scalar(select(table.c.id))
eq_(fetched_pk, pk)
```

## Next Steps


---

*Source: test_insert.py:387 | Complexity: Intermediate | Last updated: 2026-06-02*