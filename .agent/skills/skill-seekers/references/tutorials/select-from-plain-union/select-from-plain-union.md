# How To: Select From Plain Union

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test select from plain union

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

### Step 2: Assign s1 = select.where(...)

```python
s1 = select(table).where(table.c.id == 2)
```

### Step 3: Assign s2 = select.where(...)

```python
s2 = select(table).where(table.c.id == 3)
```

### Step 4: Assign u1 = union.alias.select(...)

```python
u1 = union(s1, s2).alias().select()
```

### Step 5: Call self._assert_result()

```python
self._assert_result(u1.order_by(u1.selected_columns.id), [(2, 2, 3), (3, 3, 4)])
```


## Complete Example

```python
# Workflow
table = self.tables.some_table
s1 = select(table).where(table.c.id == 2)
s2 = select(table).where(table.c.id == 3)
u1 = union(s1, s2).alias().select()
self._assert_result(u1.order_by(u1.selected_columns.id), [(2, 2, 3), (3, 3, 4)])
```

## Next Steps


---

*Source: test_select.py:875 | Complexity: Intermediate | Last updated: 2026-06-02*