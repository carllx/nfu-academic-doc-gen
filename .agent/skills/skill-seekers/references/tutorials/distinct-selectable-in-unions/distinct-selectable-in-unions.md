# How To: Distinct Selectable In Unions

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test distinct selectable in unions

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

### Step 2: Assign s1 = select.where.distinct(...)

```python
s1 = select(table).where(table.c.id == 2).distinct()
```

### Step 3: Assign s2 = select.where.distinct(...)

```python
s2 = select(table).where(table.c.id == 3).distinct()
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
s1 = select(table).where(table.c.id == 2).distinct()
s2 = select(table).where(table.c.id == 3).distinct()
u1 = union(s1, s2).limit(2)
with testing.expect_deprecated('The SelectBase.c and SelectBase.columns attributes are deprecated'):
    self._assert_result(connection, u1.order_by(u1.c.id), [(2, 2, 3), (3, 3, 4)])
```

## Next Steps


---

*Source: test_deprecations.py:113 | Complexity: Intermediate | Last updated: 2026-06-02*