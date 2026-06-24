# How To: Limit Offset In Unions From Alias

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test limit offset in unions from alias

## Prerequisites

**Required Modules:**
- `collections.abc`
- `itertools`
- `assertions`
- `assertions`
- `assertions`
- `assertsql`
- `schema`
- `schema`
- `exc`
- `exc`


## Step-by-Step Guide

### Step 1: Assign table = value

```python
table = self.tables.some_table
```

### Step 2: Assign s1 = select.where.limit.order_by(...)

```python
s1 = select(table).where(table.c.id == 2).limit(1).order_by(table.c.id)
```

### Step 3: Assign s2 = select.where.limit.order_by(...)

```python
s2 = select(table).where(table.c.id == 3).limit(1).order_by(table.c.id)
```

### Step 4: Assign u1 = union.alias(...)

```python
u1 = union(s1, s2).alias()
```

### Step 5: Call self._assert_result()

```python
self._assert_result(u1.select().limit(2).order_by(u1.c.id), [(2, 2, 3), (3, 3, 4)])
```


## Complete Example

```python
# Workflow
table = self.tables.some_table
s1 = select(table).where(table.c.id == 2).limit(1).order_by(table.c.id)
s2 = select(table).where(table.c.id == 3).limit(1).order_by(table.c.id)
u1 = union(s1, s2).alias()
self._assert_result(u1.select().limit(2).order_by(u1.c.id), [(2, 2, 3), (3, 3, 4)])
```

## Next Steps


---

*Source: test_select.py:919 | Complexity: Intermediate | Last updated: 2026-06-02*