# How To: Dialect User Setting Is Restored

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dialect user setting is restored

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
# Fixtures: testing_engine
```

## Step-by-Step Guide

### Step 1: Assign levels = requirements.get_isolation_levels(...)

```python
levels = requirements.get_isolation_levels(config)
```

### Step 2: Assign default = value

```python
default = levels['default']
```

### Step 3: Assign supported = value

```python
supported = sorted(set(levels['supported']).difference([default, 'AUTOCOMMIT']))[0]
```

### Step 4: Assign e = testing_engine(...)

```python
e = testing_engine(options={'isolation_level': supported})
```

### Step 5: Call eq_()

```python
eq_(conn.get_isolation_level(), supported)
```

### Step 6: Call conn.execution_options()

```python
conn.execution_options(isolation_level=default)
```

### Step 7: Call eq_()

```python
eq_(conn.get_isolation_level(), default)
```

### Step 8: Call eq_()

```python
eq_(conn.get_isolation_level(), supported)
```


## Complete Example

```python
# Setup
# Fixtures: testing_engine

# Workflow
levels = requirements.get_isolation_levels(config)
default = levels['default']
supported = sorted(set(levels['supported']).difference([default, 'AUTOCOMMIT']))[0]
e = testing_engine(options={'isolation_level': supported})
with e.connect() as conn:
    eq_(conn.get_isolation_level(), supported)
with e.connect() as conn:
    conn.execution_options(isolation_level=default)
    eq_(conn.get_isolation_level(), default)
with e.connect() as conn:
    eq_(conn.get_isolation_level(), supported)
```

## Next Steps


---

*Source: test_dialect.py:258 | Complexity: Advanced | Last updated: 2026-06-02*