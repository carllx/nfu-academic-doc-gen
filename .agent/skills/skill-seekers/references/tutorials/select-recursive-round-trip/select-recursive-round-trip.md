# How To: Select Recursive Round Trip

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test select recursive round trip

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `assertions`
- `schema`
- `schema`

**Setup Required:**
```python
# Fixtures: connection
```

## Step-by-Step Guide

### Step 1: Assign some_table = value

```python
some_table = self.tables.some_table
```

### Step 2: Assign cte = select.where.cte(...)

```python
cte = select(some_table).where(some_table.c.data.in_(['d2', 'd3', 'd4'])).cte('some_cte', recursive=True)
```

### Step 3: Assign cte_alias = cte.alias(...)

```python
cte_alias = cte.alias('c1')
```

### Step 4: Assign st1 = some_table.alias(...)

```python
st1 = some_table.alias()
```

### Step 5: Assign cte = cte.union_all(...)

```python
cte = cte.union_all(select(st1).where(st1.c.id == cte_alias.c.parent_id))
```

### Step 6: Assign result = connection.execute(...)

```python
result = connection.execute(select(cte.c.data).where(cte.c.data != 'd2').order_by(cte.c.data.desc()))
```

### Step 7: Call eq_()

```python
eq_(result.fetchall(), [('d4',), ('d3',), ('d3',), ('d1',), ('d1',), ('d1',)])
```


## Complete Example

```python
# Setup
# Fixtures: connection

# Workflow
some_table = self.tables.some_table
cte = select(some_table).where(some_table.c.data.in_(['d2', 'd3', 'd4'])).cte('some_cte', recursive=True)
cte_alias = cte.alias('c1')
st1 = some_table.alias()
cte = cte.union_all(select(st1).where(st1.c.id == cte_alias.c.parent_id))
result = connection.execute(select(cte.c.data).where(cte.c.data != 'd2').order_by(cte.c.data.desc()))
eq_(result.fetchall(), [('d4',), ('d3',), ('d3',), ('d1',), ('d1',), ('d1',)])
```

## Next Steps


---

*Source: test_cte.py:73 | Complexity: Intermediate | Last updated: 2026-06-02*