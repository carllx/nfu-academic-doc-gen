# How To: Sqlite Adbc Types

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: sqlite adbc types

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
# Fixtures: sqlite_adbc_conn, types_data
```

## Step-by-Step Guide

### Step 1: Assign conn = sqlite_adbc_conn

```python
conn = sqlite_adbc_conn
```

### Step 2: yield conn

```python
yield conn
```

### Step 3: Call conn.adbc_get_table_schema()

```python
conn.adbc_get_table_schema('types')
```

### Step 4: Call conn.rollback()

```python
conn.rollback()
```

### Step 5: Assign new_data = value

```python
new_data = []
```

### Step 6: Call create_and_load_types_sqlite3()

```python
create_and_load_types_sqlite3(conn, new_data)
```

### Step 7: Call conn.commit()

```python
conn.commit()
```

### Step 8: Assign unknown = int(...)

```python
entry['BoolCol'] = int(entry['BoolCol'])
```

### Step 9: Call new_data.append()

```python
new_data.append(tuple(entry.values()))
```

### Step 10: Assign unknown = int(...)

```python
entry['BoolColWithNull'] = int(entry['BoolColWithNull'])
```


## Complete Example

```python
# Setup
# Fixtures: sqlite_adbc_conn, types_data

# Workflow
import adbc_driver_manager as mgr
conn = sqlite_adbc_conn
try:
    conn.adbc_get_table_schema('types')
except mgr.ProgrammingError:
    conn.rollback()
    new_data = []
    for entry in types_data:
        entry['BoolCol'] = int(entry['BoolCol'])
        if entry['BoolColWithNull'] is not None:
            entry['BoolColWithNull'] = int(entry['BoolColWithNull'])
        new_data.append(tuple(entry.values()))
    create_and_load_types_sqlite3(conn, new_data)
    conn.commit()
yield conn
```

## Next Steps


---

*Source: test_sql.py:855 | Complexity: Advanced | Last updated: 2026-06-02*