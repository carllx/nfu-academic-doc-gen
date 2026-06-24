# How To: Dataframe To Sql Arrow Dtypes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dataframe to sql arrow dtypes

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

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('pyarrow')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'int': pd.array([1], dtype='int8[pyarrow]'), 'datetime': pd.array([datetime(2023, 1, 1)], dtype='timestamp[ns][pyarrow]'), 'date': pd.array([date(2023, 1, 1)], dtype='date32[day][pyarrow]'), 'timedelta': pd.array([timedelta(1)], dtype='duration[ns][pyarrow]'), 'string': pd.array(['a'], dtype='string[pyarrow]')})
```

### Step 3: Assign conn = request.getfixturevalue(...)

```python
conn = request.getfixturevalue(conn)
```

### Step 4: Assign exp_warning = UserWarning

```python
exp_warning = UserWarning
```

### Step 5: Assign msg = "the 'timedelta'"

```python
msg = "the 'timedelta'"
```

### Step 6: Call df.to_sql()

```python
df.to_sql(name='test_arrow', con=conn, if_exists='replace', index=False)
```

### Step 7: Assign df = df.drop(...)

```python
df = df.drop(columns=['timedelta'])
```

### Step 8: Assign exp_warning = DeprecationWarning

```python
exp_warning = DeprecationWarning
```

### Step 9: Assign msg = 'is_sparse is deprecated'

```python
msg = 'is_sparse is deprecated'
```

### Step 10: Assign exp_warning = None

```python
exp_warning = None
```

### Step 11: Assign msg = ''

```python
msg = ''
```


## Complete Example

```python
# Setup
# Fixtures: conn, request

# Workflow
pytest.importorskip('pyarrow')
df = DataFrame({'int': pd.array([1], dtype='int8[pyarrow]'), 'datetime': pd.array([datetime(2023, 1, 1)], dtype='timestamp[ns][pyarrow]'), 'date': pd.array([date(2023, 1, 1)], dtype='date32[day][pyarrow]'), 'timedelta': pd.array([timedelta(1)], dtype='duration[ns][pyarrow]'), 'string': pd.array(['a'], dtype='string[pyarrow]')})
if 'adbc' in conn:
    if conn == 'sqlite_adbc_conn':
        df = df.drop(columns=['timedelta'])
    if pa_version_under14p1:
        exp_warning = DeprecationWarning
        msg = 'is_sparse is deprecated'
    else:
        exp_warning = None
        msg = ''
else:
    exp_warning = UserWarning
    msg = "the 'timedelta'"
conn = request.getfixturevalue(conn)
with tm.assert_produces_warning(exp_warning, match=msg, check_stacklevel=False):
    df.to_sql(name='test_arrow', con=conn, if_exists='replace', index=False)
```

## Next Steps


---

*Source: test_sql.py:1005 | Complexity: Advanced | Last updated: 2026-06-02*