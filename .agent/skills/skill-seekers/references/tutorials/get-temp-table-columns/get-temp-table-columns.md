# How To: Get Temp Table Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get temp table columns

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

### Step 1: Assign table_name = self.temp_table_name(...)

```python
table_name = self.temp_table_name()
```

### Step 2: Assign user_tmp = value

```python
user_tmp = self.tables[table_name]
```

### Step 3: Assign insp = inspect(...)

```python
insp = inspect(connection)
```

### Step 4: Assign cols = insp.get_columns(...)

```python
cols = insp.get_columns(table_name)
```

### Step 5: Call is_true()

```python
is_true(len(cols) > 0, len(cols))
```

### Step 6: Call eq_()

```python
eq_(col.name, cols[i]['name'])
```


## Complete Example

```python
# Workflow
table_name = self.temp_table_name()
user_tmp = self.tables[table_name]
insp = inspect(connection)
cols = insp.get_columns(table_name)
is_true(len(cols) > 0, len(cols))
for i, col in enumerate(user_tmp.columns):
    eq_(col.name, cols[i]['name'])
```

## Next Steps


---

*Source: test_reflection.py:1775 | Complexity: Intermediate | Last updated: 2026-06-02*