# How To: Read View Postgres

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read view postgres

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

### Step 2: Assign table_name = value

```python
table_name = f'group_{uuid.uuid4().hex}'
```

### Step 3: Assign view_name = value

```python
view_name = f'group_view_{uuid.uuid4().hex}'
```

### Step 4: Assign sql_stmt = text(...)

```python
sql_stmt = text(f"\n    CREATE TABLE {table_name} (\n        group_id INTEGER,\n        name TEXT\n    );\n    INSERT INTO {table_name} VALUES\n        (1, 'name');\n    CREATE VIEW {view_name}\n    AS\n    SELECT * FROM {table_name};\n    ")
```

### Step 5: Assign result = read_sql_table(...)

```python
result = read_sql_table(view_name, conn)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'group_id': [1], 'name': 'name'})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Call conn.execute()

```python
conn.execute(sql_stmt)
```

### Step 9: Call con.execute()

```python
con.execute(sql_stmt)
```


## Complete Example

```python
# Setup
# Fixtures: conn, request

# Workflow
conn = request.getfixturevalue(conn)
from sqlalchemy.engine import Engine
from sqlalchemy.sql import text
table_name = f'group_{uuid.uuid4().hex}'
view_name = f'group_view_{uuid.uuid4().hex}'
sql_stmt = text(f"\n    CREATE TABLE {table_name} (\n        group_id INTEGER,\n        name TEXT\n    );\n    INSERT INTO {table_name} VALUES\n        (1, 'name');\n    CREATE VIEW {view_name}\n    AS\n    SELECT * FROM {table_name};\n    ")
if isinstance(conn, Engine):
    with conn.connect() as con:
        with con.begin():
            con.execute(sql_stmt)
else:
    with conn.begin():
        conn.execute(sql_stmt)
result = read_sql_table(view_name, conn)
expected = DataFrame({'group_id': [1], 'name': 'name'})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sql.py:1457 | Complexity: Advanced | Last updated: 2026-06-02*