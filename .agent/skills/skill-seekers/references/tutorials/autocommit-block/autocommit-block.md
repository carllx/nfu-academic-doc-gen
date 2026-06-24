# How To: Autocommit Block

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test autocommit block

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `importlib`
- `assertions`
- `assertions`
- `config`
- `provision`
- `schema`
- `schema`
- `sql.compiler`
- `util`

**Setup Required:**
```python
# Fixtures: testing_engine, autocommit_setting, block_rollback
```

## Step-by-Step Guide

### Step 1: Assign kw = value

```python
kw = {}
```

### Step 2: Assign engine = testing_engine(...)

```python
engine = testing_engine(options=kw)
```

### Step 3: Assign conn = engine.connect(...)

```python
conn = engine.connect()
```

### Step 4: Call self._test_conn_autocommits()

```python
self._test_conn_autocommits(conn, autocommit_setting.engine or autocommit_setting.option, ensure_table=True)
```

### Step 5: Assign unknown = True

```python
kw['skip_autocommit_rollback'] = True
```

### Step 6: Assign unknown = 'AUTOCOMMIT'

```python
kw['isolation_level'] = 'AUTOCOMMIT'
```

### Step 7: Call conn.execution_options()

```python
conn.execution_options(isolation_level='AUTOCOMMIT')
```

### Step 8: Call conn.close()

```python
conn.close()
```

### Step 9: Call eq_()

```python
eq_(check_rollback.mock_calls, [mock.call()])
```

### Step 10: Call eq_()

```python
eq_(check_rollback.mock_calls, [])
```


## Complete Example

```python
# Setup
# Fixtures: testing_engine, autocommit_setting, block_rollback

# Workflow
kw = {}
if bool(block_rollback):
    kw['skip_autocommit_rollback'] = True
if autocommit_setting.engine:
    kw['isolation_level'] = 'AUTOCOMMIT'
engine = testing_engine(options=kw)
conn = engine.connect()
if autocommit_setting.option:
    conn.execution_options(isolation_level='AUTOCOMMIT')
self._test_conn_autocommits(conn, autocommit_setting.engine or autocommit_setting.option, ensure_table=True)
with mock.patch.object(conn.connection, 'rollback', wraps=conn.connection.rollback) as check_rollback:
    conn.close()
if autocommit_setting.false or not block_rollback:
    eq_(check_rollback.mock_calls, [mock.call()])
else:
    eq_(check_rollback.mock_calls, [])
```

## Next Steps


---

*Source: test_dialect.py:347 | Complexity: Advanced | Last updated: 2026-06-02*