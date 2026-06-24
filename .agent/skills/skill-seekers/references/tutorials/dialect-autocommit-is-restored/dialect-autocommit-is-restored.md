# How To: Dialect Autocommit Is Restored

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test #10147

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
# Fixtures: testing_engine, use_dialect_setting
```

## Step-by-Step Guide

### Step 1: 'test #10147'

```python
'test #10147'
```

### Step 2: Assign levels = requirements.get_isolation_levels(...)

```python
levels = requirements.get_isolation_levels(config)
```

### Step 3: Assign default = value

```python
default = levels['default']
```

### Step 4: Assign e = testing_engine(...)

```python
e = testing_engine(options={'isolation_level': 'AUTOCOMMIT'})
```

### Step 5: Assign e = testing_engine.execution_options(...)

```python
e = testing_engine().execution_options(isolation_level='AUTOCOMMIT')
```

### Step 6: Call self._test_conn_autocommits()

```python
self._test_conn_autocommits(conn, True)
```

### Step 7: Call conn.execution_options()

```python
conn.execution_options(isolation_level=default)
```

### Step 8: Call self._test_conn_autocommits()

```python
self._test_conn_autocommits(conn, False)
```

### Step 9: Call self._test_conn_autocommits()

```python
self._test_conn_autocommits(conn, True)
```


## Complete Example

```python
# Setup
# Fixtures: testing_engine, use_dialect_setting

# Workflow
'test #10147'
if use_dialect_setting:
    e = testing_engine(options={'isolation_level': 'AUTOCOMMIT'})
else:
    e = testing_engine().execution_options(isolation_level='AUTOCOMMIT')
levels = requirements.get_isolation_levels(config)
default = levels['default']
with e.connect() as conn:
    self._test_conn_autocommits(conn, True)
with e.connect() as conn:
    conn.execution_options(isolation_level=default)
    self._test_conn_autocommits(conn, False)
with e.connect() as conn:
    self._test_conn_autocommits(conn, True)
```

## Next Steps


---

*Source: test_dialect.py:377 | Complexity: Advanced | Last updated: 2026-06-02*