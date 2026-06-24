# How To: Read Iris Query Chunksize

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read iris query chunksize

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
assert iris_frame.shape == (0, 5)
```

### Step 2: Assign iris_frame = concat(...)

```python
iris_frame = concat(read_sql_query('SELECT * FROM iris', conn, chunksize=7))
```

**Verification:**
```python
assert 'SepalWidth' in iris_frame.columns
```

### Step 3: Call check_iris_frame()

```python
check_iris_frame(iris_frame)
```

### Step 4: Assign iris_frame = concat(...)

```python
iris_frame = concat(pd.read_sql('SELECT * FROM iris', conn, chunksize=7))
```

### Step 5: Call check_iris_frame()

```python
check_iris_frame(iris_frame)
```

### Step 6: Assign iris_frame = concat(...)

```python
iris_frame = concat(pd.read_sql('SELECT * FROM iris where 0=1', conn, chunksize=7))
```

**Verification:**
```python
assert iris_frame.shape == (0, 5)
```

### Step 7: Call request.node.add_marker()

```python
request.node.add_marker(pytest.mark.xfail(reason="'chunksize' not implemented for ADBC drivers", strict=True))
```


## Complete Example

```python
# Setup
# Fixtures: conn, request

# Workflow
if 'adbc' in conn:
    request.node.add_marker(pytest.mark.xfail(reason="'chunksize' not implemented for ADBC drivers", strict=True))
conn = request.getfixturevalue(conn)
iris_frame = concat(read_sql_query('SELECT * FROM iris', conn, chunksize=7))
check_iris_frame(iris_frame)
iris_frame = concat(pd.read_sql('SELECT * FROM iris', conn, chunksize=7))
check_iris_frame(iris_frame)
iris_frame = concat(pd.read_sql('SELECT * FROM iris where 0=1', conn, chunksize=7))
assert iris_frame.shape == (0, 5)
assert 'SepalWidth' in iris_frame.columns
```

## Next Steps


---

*Source: test_sql.py:1106 | Complexity: Intermediate | Last updated: 2026-06-02*