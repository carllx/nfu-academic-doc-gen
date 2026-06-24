# How To: Limit Offset Selectable In Unions

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test limit offset selectable in unions

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

### Step 4: Assign u1 = union.limit(...)

```python
u1 = union(s1, s2).limit(2)
```

### Step 5: Call self._assert_result()

```python
self._assert_result(connection, u1.order_by(u1.c.id), [(2, 2, 3), (3, 3, 4)])
```


## Complete Example

```python
# Setup
# Fixtures: connection

# Workflow
table = self.tables.some_table
s1 = select(table).where(table.c.id == 2).limit(1).order_by(table.c.id)
s2 = select(table).where(table.c.id == 3).limit(1).order_by(table.c.id)
u1 = union(s1, s2).limit(2)
with testing.expect_deprecated('The SelectBase.c and SelectBase.columns attributes are deprecated'):
    self._assert_result(connection, u1.order_by(u1.c.id), [(2, 2, 3), (3, 3, 4)])
```

## Next Steps


---

*Source: test_deprecations.py:84 | Complexity: Intermediate | Last updated: 2026-06-02*