# How To: No Results For Non Returning Insert

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test another INSERT issue found during #10453

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
# Fixtures: connection, style, executemany
```

## Step-by-Step Guide

### Step 1: 'test another INSERT issue found during #10453'

```python
'test another INSERT issue found during #10453'
```

**Verification:**
```python
assert not r.returns_rows
```

### Step 2: Assign table = value

```python
table = self.tables.no_implicit_returning
```

### Step 3: Assign stmt = table.insert(...)

```python
stmt = table.insert()
```

### Step 4: Assign r = connection.execute(...)

```python
r = connection.execute(stmt, data)
```

**Verification:**
```python
assert not r.returns_rows
```

### Step 5: Assign stmt = stmt.return_defaults(...)

```python
stmt = stmt.return_defaults()
```

### Step 6: Assign data = value

```python
data = [{'data': 'd1'}, {'data': 'd2'}, {'data': 'd3'}, {'data': 'd4'}, {'data': 'd5'}]
```

### Step 7: Assign data = value

```python
data = {'data': 'd1'}
```


## Complete Example

```python
# Setup
# Fixtures: connection, style, executemany

# Workflow
'test another INSERT issue found during #10453'
table = self.tables.no_implicit_returning
stmt = table.insert()
if style.return_defaults:
    stmt = stmt.return_defaults()
if executemany:
    data = [{'data': 'd1'}, {'data': 'd2'}, {'data': 'd3'}, {'data': 'd4'}, {'data': 'd5'}]
else:
    data = {'data': 'd1'}
r = connection.execute(stmt, data)
assert not r.returns_rows
```

## Next Steps


---

*Source: test_insert.py:138 | Complexity: Intermediate | Last updated: 2026-06-02*