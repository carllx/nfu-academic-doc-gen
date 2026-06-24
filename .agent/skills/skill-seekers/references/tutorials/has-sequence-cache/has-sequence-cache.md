# How To: Has Sequence Cache

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test has sequence cache

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `assertions`
- `assertions`
- `config`
- `provision`
- `schema`
- `schema`

**Setup Required:**
```python
# Fixtures: connection, metadata
```

## Step-by-Step Guide

### Step 1: Assign insp = inspect(...)

```python
insp = inspect(connection)
```

### Step 2: Call eq_()

```python
eq_(insp.has_sequence('user_id_seq'), True)
```

### Step 3: Assign ss = normalize_sequence(...)

```python
ss = normalize_sequence(config, Sequence('new_seq', metadata=metadata))
```

### Step 4: Call eq_()

```python
eq_(insp.has_sequence('new_seq'), False)
```

### Step 5: Call ss.create()

```python
ss.create(connection)
```

### Step 6: Call eq_()

```python
eq_(insp.has_sequence('new_seq'), False)
```

### Step 7: Call insp.clear_cache()

```python
insp.clear_cache()
```

### Step 8: Call eq_()

```python
eq_(insp.has_sequence('new_seq'), True)
```

### Step 9: Call ss.drop()

```python
ss.drop(connection)
```


## Complete Example

```python
# Setup
# Fixtures: connection, metadata

# Workflow
insp = inspect(connection)
eq_(insp.has_sequence('user_id_seq'), True)
ss = normalize_sequence(config, Sequence('new_seq', metadata=metadata))
eq_(insp.has_sequence('new_seq'), False)
ss.create(connection)
try:
    eq_(insp.has_sequence('new_seq'), False)
    insp.clear_cache()
    eq_(insp.has_sequence('new_seq'), True)
finally:
    ss.drop(connection)
```

## Next Steps


---

*Source: test_sequence.py:231 | Complexity: Advanced | Last updated: 2026-06-02*