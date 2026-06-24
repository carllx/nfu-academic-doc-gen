# How To: Simple Limit Offset

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simple limit offset

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: connection, cases
```

## Step-by-Step Guide

### Step 1: Assign table = value

```python
table = self.tables.some_table
```

**Verification:**
```python
assert_data = [(1, 1, 2), (2, 2, 3), (3, 3, 4), (4, 4, 5), (5, 4, 6)]
```

### Step 2: Assign connection = connection.execution_options(...)

```python
connection = connection.execution_options(compiled_cache={})
```

### Step 3: Assign assert_data = value

```python
assert_data = [(1, 1, 2), (2, 2, 3), (3, 3, 4), (4, 4, 5), (5, 4, 6)]
```

### Step 4: Assign expected = value

```python
expected = assert_data[offset:offset + limit]
```

### Step 5: Call self._assert_result()

```python
self._assert_result(connection, select(table).order_by(table.c.id).limit(limit).offset(offset), expected)
```


## Complete Example

```python
# Setup
# Fixtures: connection, cases

# Workflow
table = self.tables.some_table
connection = connection.execution_options(compiled_cache={})
assert_data = [(1, 1, 2), (2, 2, 3), (3, 3, 4), (4, 4, 5), (5, 4, 6)]
for limit, offset in cases:
    expected = assert_data[offset:offset + limit]
    self._assert_result(connection, select(table).order_by(table.c.id).limit(limit).offset(offset), expected)
```

## Next Steps


---

*Source: test_select.py:286 | Complexity: Intermediate | Last updated: 2026-06-02*