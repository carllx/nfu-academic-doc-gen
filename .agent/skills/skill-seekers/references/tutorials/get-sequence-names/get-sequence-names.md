# How To: Get Sequence Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get sequence names

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
# Fixtures: connection
```

## Step-by-Step Guide

### Step 1: Assign exp = value

```python
exp = {'other_seq', 'user_id_seq'}
```

### Step 2: Assign res = set(...)

```python
res = set(inspect(connection).get_sequence_names())
```

### Step 3: Call is_true()

```python
is_true(res.intersection(exp) == exp)
```

### Step 4: Call is_true()

```python
is_true('schema_seq' not in res)
```


## Complete Example

```python
# Setup
# Fixtures: connection

# Workflow
exp = {'other_seq', 'user_id_seq'}
res = set(inspect(connection).get_sequence_names())
is_true(res.intersection(exp) == exp)
is_true('schema_seq' not in res)
```

## Next Steps


---

*Source: test_sequence.py:281 | Complexity: Intermediate | Last updated: 2026-06-02*