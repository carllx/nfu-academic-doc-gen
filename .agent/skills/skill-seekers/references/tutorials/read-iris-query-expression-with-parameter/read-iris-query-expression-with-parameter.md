# How To: Read Iris Query Expression With Parameter

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read iris query expression with parameter

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

### Step 2: Assign metadata = MetaData(...)

```python
metadata = MetaData()
```

### Step 3: Assign autoload_con = value

```python
autoload_con = create_engine(conn) if isinstance(conn, str) else conn
```

### Step 4: Assign iris = Table(...)

```python
iris = Table('iris', metadata, autoload_with=autoload_con)
```

### Step 5: Assign iris_frame = read_sql_query(...)

```python
iris_frame = read_sql_query(select(iris), conn, params={'name': 'Iris-setosa', 'length': 5.1})
```

### Step 6: Call check_iris_frame()

```python
check_iris_frame(iris_frame)
```

### Step 7: Call request.node.add_marker()

```python
request.node.add_marker(pytest.mark.xfail(reason="'chunksize' not implemented for ADBC drivers", strict=True))
```

### Step 8: Call autoload_con.dispose()

```python
autoload_con.dispose()
```


## Complete Example

```python
# Setup
# Fixtures: conn, request

# Workflow
if 'adbc' in conn:
    request.node.add_marker(pytest.mark.xfail(reason="'chunksize' not implemented for ADBC drivers", strict=True))
conn = request.getfixturevalue(conn)
from sqlalchemy import MetaData, Table, create_engine, select
metadata = MetaData()
autoload_con = create_engine(conn) if isinstance(conn, str) else conn
iris = Table('iris', metadata, autoload_with=autoload_con)
iris_frame = read_sql_query(select(iris), conn, params={'name': 'Iris-setosa', 'length': 5.1})
check_iris_frame(iris_frame)
if isinstance(conn, str):
    autoload_con.dispose()
```

## Next Steps


---

*Source: test_sql.py:1125 | Complexity: Advanced | Last updated: 2026-06-02*