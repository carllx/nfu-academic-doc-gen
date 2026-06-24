# How To: Read Procedure

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read procedure

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

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [0.1, 0.2, 0.3]})
```

### Step 3: Call df.to_sql()

```python
df.to_sql(name='test_frame', con=conn, index=False)
```

### Step 4: Assign proc = 'DROP PROCEDURE IF EXISTS get_testdb;\n\n    CREATE PROCEDURE get_testdb ()\n\n    BEGIN\n        SELECT * FROM test_frame;\n    END'

```python
proc = 'DROP PROCEDURE IF EXISTS get_testdb;\n\n    CREATE PROCEDURE get_testdb ()\n\n    BEGIN\n        SELECT * FROM test_frame;\n    END'
```

### Step 5: Assign proc = text(...)

```python
proc = text(proc)
```

### Step 6: Assign res1 = sql.read_sql_query(...)

```python
res1 = sql.read_sql_query('CALL get_testdb();', conn)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, res1)
```

### Step 8: Assign res2 = sql.read_sql(...)

```python
res2 = sql.read_sql('CALL get_testdb();', conn)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, res2)
```

### Step 10: Call conn.execute()

```python
conn.execute(proc)
```

### Step 11: Call engine_conn.execute()

```python
engine_conn.execute(proc)
```


## Complete Example

```python
# Setup
# Fixtures: conn, request

# Workflow
conn = request.getfixturevalue(conn)
from sqlalchemy import text
from sqlalchemy.engine import Engine
df = DataFrame({'a': [1, 2, 3], 'b': [0.1, 0.2, 0.3]})
df.to_sql(name='test_frame', con=conn, index=False)
proc = 'DROP PROCEDURE IF EXISTS get_testdb;\n\n    CREATE PROCEDURE get_testdb ()\n\n    BEGIN\n        SELECT * FROM test_frame;\n    END'
proc = text(proc)
if isinstance(conn, Engine):
    with conn.connect() as engine_conn:
        with engine_conn.begin():
            engine_conn.execute(proc)
else:
    with conn.begin():
        conn.execute(proc)
res1 = sql.read_sql_query('CALL get_testdb();', conn)
tm.assert_frame_equal(df, res1)
res2 = sql.read_sql('CALL get_testdb();', conn)
tm.assert_frame_equal(df, res2)
```

## Next Steps


---

*Source: test_sql.py:1246 | Complexity: Advanced | Last updated: 2026-06-02*