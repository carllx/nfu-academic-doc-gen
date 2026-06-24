# How To: Insertion Method On Conflict Do Nothing

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test insertion method on conflict do nothing

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
assert inserted == 0
```

### Step 2: Assign create_sql = text(...)

```python
create_sql = text('\n    CREATE TABLE test_insert_conflict (\n        a  integer PRIMARY KEY,\n        b  numeric,\n        c  text\n    );\n    ')
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2.1, 'a']], columns=list('abc'))
```

### Step 4: Call expected.to_sql()

```python
expected.to_sql(name='test_insert_conflict', con=conn, if_exists='append', index=False)
```

### Step 5: Assign df_insert = DataFrame(...)

```python
df_insert = DataFrame([[1, 3.2, 'b']], columns=list('abc'))
```

### Step 6: Assign inserted = df_insert.to_sql(...)

```python
inserted = df_insert.to_sql(name='test_insert_conflict', con=conn, index=False, if_exists='append', method=insert_on_conflict)
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
assert inserted == 0
```

### Step 9: Assign data = value

```python
data = [dict(zip(keys, row)) for row in data_iter]
```

### Step 10: Assign stmt = insert.values.on_conflict_do_nothing(...)

```python
stmt = insert(table.table).values(data).on_conflict_do_nothing(index_elements=['a'])
```

### Step 11: Assign result = conn.execute(...)

```python
result = conn.execute(stmt)
```

### Step 12: Call pandasSQL.drop_table()

```python
pandasSQL.drop_table('test_insert_conflict')
```

### Step 13: Call conn.execute()

```python
conn.execute(create_sql)
```

### Step 14: Call con.execute()

```python
con.execute(create_sql)
```


## Complete Example

```python
# Setup
# Fixtures: conn, request

# Workflow
conn = request.getfixturevalue(conn)
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Engine
from sqlalchemy.sql import text

def insert_on_conflict(table, conn, keys, data_iter):
    data = [dict(zip(keys, row)) for row in data_iter]
    stmt = insert(table.table).values(data).on_conflict_do_nothing(index_elements=['a'])
    result = conn.execute(stmt)
    return result.rowcount
create_sql = text('\n    CREATE TABLE test_insert_conflict (\n        a  integer PRIMARY KEY,\n        b  numeric,\n        c  text\n    );\n    ')
if isinstance(conn, Engine):
    with conn.connect() as con:
        with con.begin():
            con.execute(create_sql)
else:
    with conn.begin():
        conn.execute(create_sql)
expected = DataFrame([[1, 2.1, 'a']], columns=list('abc'))
expected.to_sql(name='test_insert_conflict', con=conn, if_exists='append', index=False)
df_insert = DataFrame([[1, 3.2, 'b']], columns=list('abc'))
inserted = df_insert.to_sql(name='test_insert_conflict', con=conn, index=False, if_exists='append', method=insert_on_conflict)
result = sql.read_sql_table('test_insert_conflict', conn)
tm.assert_frame_equal(result, expected)
assert inserted == 0
with sql.SQLDatabase(conn, need_transaction=True) as pandasSQL:
    pandasSQL.drop_table('test_insert_conflict')
```

## Next Steps


---

*Source: test_sql.py:1322 | Complexity: Advanced | Last updated: 2026-06-02*