# How To: Fetch Offset Nobinds

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test that 'literal binds' mode works - no bound params.

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

### Step 1: "test that 'literal binds' mode works - no bound params."

```python
"test that 'literal binds' mode works - no bound params."
```

### Step 2: Assign table = value

```python
table = self.tables.some_table
```

### Step 3: Assign stmt = select.order_by.fetch.offset(...)

```python
stmt = select(table).order_by(table.c.id).fetch(2).offset(1)
```

### Step 4: Assign sql = stmt.compile(...)

```python
sql = stmt.compile(dialect=config.db.dialect, compile_kwargs={'literal_binds': True})
```

### Step 5: Assign sql = str(...)

```python
sql = str(sql)
```

### Step 6: Call self._assert_result_str()

```python
self._assert_result_str(sql, [(2, 2, 3), (3, 3, 4)])
```


## Complete Example

```python
# Workflow
"test that 'literal binds' mode works - no bound params."
table = self.tables.some_table
stmt = select(table).order_by(table.c.id).fetch(2).offset(1)
sql = stmt.compile(dialect=config.db.dialect, compile_kwargs={'literal_binds': True})
sql = str(sql)
self._assert_result_str(sql, [(2, 2, 3), (3, 3, 4)])
```

## Next Steps


---

*Source: test_select.py:354 | Complexity: Intermediate | Last updated: 2026-06-02*