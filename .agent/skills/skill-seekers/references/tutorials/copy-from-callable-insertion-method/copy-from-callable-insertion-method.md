# How To: Copy From Callable Insertion Method

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test copy from callable insertion method

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
# Fixtures: conn, expected_count, request
```

## Step-by-Step Guide

### Step 1: Assign conn = request.getfixturevalue(...)

```python
conn = request.getfixturevalue(conn)
```

**Verification:**
```python
assert result_count is None
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'col1': [1, 2], 'col2': [0.1, 0.2], 'col3': ['a', 'n']})
```

**Verification:**
```python
assert result_count == expected_count
```

### Step 3: Assign result_count = expected.to_sql(...)

```python
result_count = expected.to_sql(name='test_frame', con=conn, index=False, method=psql_insert_copy)
```

### Step 4: Assign result = sql.read_sql_table(...)

```python
result = sql.read_sql_table('test_frame', conn)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign dbapi_conn = value

```python
dbapi_conn = conn.connection
```

**Verification:**
```python
assert result_count is None
```

### Step 7: Assign s_buf = StringIO(...)

```python
s_buf = StringIO()
```

### Step 8: Assign writer = csv.writer(...)

```python
writer = csv.writer(s_buf)
```

### Step 9: Call writer.writerows()

```python
writer.writerows(data_iter)
```

### Step 10: Call s_buf.seek()

```python
s_buf.seek(0)
```

### Step 11: Assign columns = unknown.join(...)

```python
columns = ', '.join([f'"{k}"' for k in keys])
```

### Step 12: Assign sql_query = value

```python
sql_query = f'COPY {table_name} ({columns}) FROM STDIN WITH CSV'
```

### Step 13: Call cur.copy_expert()

```python
cur.copy_expert(sql=sql_query, file=s_buf)
```

### Step 14: Assign table_name = value

```python
table_name = f'{table.schema}.{table.name}'
```

### Step 15: Assign table_name = value

```python
table_name = table.name
```


## Complete Example

```python
# Setup
# Fixtures: conn, expected_count, request

# Workflow
def psql_insert_copy(table, conn, keys, data_iter):
    dbapi_conn = conn.connection
    with dbapi_conn.cursor() as cur:
        s_buf = StringIO()
        writer = csv.writer(s_buf)
        writer.writerows(data_iter)
        s_buf.seek(0)
        columns = ', '.join([f'"{k}"' for k in keys])
        if table.schema:
            table_name = f'{table.schema}.{table.name}'
        else:
            table_name = table.name
        sql_query = f'COPY {table_name} ({columns}) FROM STDIN WITH CSV'
        cur.copy_expert(sql=sql_query, file=s_buf)
    return expected_count
conn = request.getfixturevalue(conn)
expected = DataFrame({'col1': [1, 2], 'col2': [0.1, 0.2], 'col3': ['a', 'n']})
result_count = expected.to_sql(name='test_frame', con=conn, index=False, method=psql_insert_copy)
if expected_count is None:
    assert result_count is None
else:
    assert result_count == expected_count
result = sql.read_sql_table('test_frame', conn)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sql.py:1284 | Complexity: Advanced | Last updated: 2026-06-02*