# How To: Get Indexes Quoted Name

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test that index names with various casing are properly reflected.

## Prerequisites

**Required Modules:**
- `contextlib`
- `operator`
- `re`
- `sqlalchemy`
- `provision`
- `provision`
- `schema`
- `schema`
- `engine`
- `engine`
- `engine`
- `exc`
- `exc`
- `schema`
- `schema`
- `sql.elements`
- `sql.schema`
- `testing`
- `testing`
- `testing`
- `testing`
- `testing`
- `testing`
- `sqlalchemy`


## Step-by-Step Guide

### Step 1: 'Test that index names with various casing are properly reflected.'

```python
'Test that index names with various casing are properly reflected.'
```

**Verification:**
```python
assert idx_name in index_names, f'Expected {idx_name} in {index_names}'
```

### Step 2: Assign t = Table(...)

```python
t = Table('test_table', metadata, Column('id', Integer, primary_key=True), Column('data', String(50)))
```

### Step 3: Call Index()

```python
Index(idx_name, t.c.data)
```

### Step 4: Call metadata.create_all()

```python
metadata.create_all(connection)
```

### Step 5: Assign insp = inspect(...)

```python
insp = inspect(connection)
```

### Step 6: Assign indexes = insp.get_indexes(...)

```python
indexes = insp.get_indexes('test_table')
```

### Step 7: Assign index_names = value

```python
index_names = [idx['name'] for idx in indexes]
```

**Verification:**
```python
assert idx_name in index_names, f'Expected {idx_name} in {index_names}'
```

### Step 8: Assign matching_idx = value

```python
matching_idx = [idx for idx in indexes if idx['name'] == idx_name]
```

### Step 9: Call eq_()

```python
eq_(len(matching_idx), 1)
```

### Step 10: Call eq_()

```python
eq_(matching_idx[0]['column_names'], ['data'])
```


## Complete Example

```python
# Workflow
'Test that index names with various casing are properly reflected.'
t = Table('test_table', metadata, Column('id', Integer, primary_key=True), Column('data', String(50)))
Index(idx_name, t.c.data)
metadata.create_all(connection)
insp = inspect(connection)
indexes = insp.get_indexes('test_table')
index_names = [idx['name'] for idx in indexes]
assert idx_name in index_names, f'Expected {idx_name} in {index_names}'
matching_idx = [idx for idx in indexes if idx['name'] == idx_name]
eq_(len(matching_idx), 1)
eq_(matching_idx[0]['column_names'], ['data'])
```

## Next Steps


---

*Source: test_reflection.py:2040 | Complexity: Advanced | Last updated: 2026-06-02*