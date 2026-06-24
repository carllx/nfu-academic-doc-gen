# How To: Insertion Method On Conflict Update

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test insertion method on conflict update

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `contextlib`
- `contextlib`
- `csv`
- `datetime`
- `io`
- `pathlib`
- `sqlite3`
- `typing`
- `uuid`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.compat`
- `pandas.compat._optional`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.util.version`
- `pandas.io`
- `pandas.io.sql`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy.engine`
- `sqlalchemy`
- `sqlalchemy.engine`
- `sqlalchemy`
- `adbc_driver_postgresql`
- `adbc_driver_manager`
- `adbc_driver_manager`
- `adbc_driver_sqlite`
- `adbc_driver_manager`
- `adbc_driver_manager`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy.engine`
- `sqlalchemy.dialects.postgresql`
- `sqlalchemy.engine`
- `sqlalchemy.sql`
- `sqlalchemy.dialects.mysql`
- `sqlalchemy.engine`
- `sqlalchemy.sql`
- `sqlalchemy.engine`
- `sqlalchemy.sql`
- `sqlalchemy`
- `sqlalchemy.engine`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy.engine`
- `sqlalchemy`
- `sqlalchemy.schema`
- `sqlalchemy`
- `sqlalchemy.schema`
- `sqlalchemy`
- `sqlalchemy.schema`
- `sqlalchemy.engine`
- `sqlalchemy`
- `sqlalchemy.orm`
- `sqlalchemy`
- `sqlalchemy.orm`
- `sqlalchemy.sql`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy.engine`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `pandas.arrays`
- `sqlalchemy`

**Setup Required:**
```python
# Fixtures: conn, request
```

## Step-by-Step Guide

### Step 1: Assign conn = request.getfixturevalue(...)

```python
conn = request.getfixturevalue(conn)
```

**Verification:**
```python
assert inserted == 2
```

### Step 2: Assign create_sql = text(...)

```python
create_sql = text('\n    CREATE TABLE test_insert_conflict (\n        a INT PRIMARY KEY,\n        b FLOAT,\n        c VARCHAR(10)\n    );\n    ')
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2.1, 'a']], columns=list('abc'))
```

### Step 4: Call df.to_sql()

```python
df.to_sql(name='test_insert_conflict', con=conn, if_exists='append', index=False)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 3.2, 'b']], columns=list('abc'))
```

### Step 6: Assign inserted = expected.to_sql(...)

```python
inserted = expected.to_sql(name='test_insert_conflict', con=conn, index=False, if_exists='append', method=insert_on_conflict)
```

### Step 7: Assign result = sql.read_sql_table(...)

```python
result = sql.read_sql_table('test_insert_conflict', conn)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert inserted == 2
```

### Step 9: Assign data = value

```python
data = [dict(zip(keys, row)) for row in data_iter]
```

### Step 10: Assign stmt = insert.values(...)

```python
stmt = insert(table.table).values(data)
```

### Step 11: Assign stmt = stmt.on_duplicate_key_update(...)

```python
stmt = stmt.on_duplicate_key_update(b=stmt.inserted.b, c=stmt.inserted.c)
```

### Step 12: Assign result = conn.execute(...)

```python
result = conn.execute(stmt)
```

### Step 13: Call pandasSQL.drop_table()

```python
pandasSQL.drop_table('test_insert_conflict')
```

### Step 14: Call conn.execute()

```python
conn.execute(create_sql)
```

### Step 15: Call con.execute()

```python
con.execute(create_sql)
```


## Complete Example

```python
# Setup
# Fixtures: conn, request

# Workflow
conn = request.getfixturevalue(conn)
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.engine import Engine
from sqlalchemy.sql import text

def insert_on_conflict(table, conn, keys, data_iter):
    data = [dict(zip(keys, row)) for row in data_iter]
    stmt = insert(table.table).values(data)
    stmt = stmt.on_duplicate_key_update(b=stmt.inserted.b, c=stmt.inserted.c)
    result = conn.execute(stmt)
    return result.rowcount
create_sql = text('\n    CREATE TABLE test_insert_conflict (\n        a INT PRIMARY KEY,\n        b FLOAT,\n        c VARCHAR(10)\n    );\n    ')
if isinstance(conn, Engine):
    with conn.connect() as con:
        with con.begin():
            con.execute(create_sql)
else:
    with conn.begin():
        conn.execute(create_sql)
df = DataFrame([[1, 2.1, 'a']], columns=list('abc'))
df.to_sql(name='test_insert_conflict', con=conn, if_exists='append', index=False)
expected = DataFrame([[1, 3.2, 'b']], columns=list('abc'))
inserted = expected.to_sql(name='test_insert_conflict', con=conn, index=False, if_exists='append', method=insert_on_conflict)
result = sql.read_sql_table('test_insert_conflict', conn)
tm.assert_frame_equal(result, expected)
assert inserted == 2
with sql.SQLDatabase(conn, need_transaction=True) as pandasSQL:
    pandasSQL.drop_table('test_insert_conflict')
```

## Next Steps


---

*Source: test_sql.py:1404 | Complexity: Advanced | Last updated: 2026-06-02*