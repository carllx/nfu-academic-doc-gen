# How To: Aliases And Ss

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test aliases and ss

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `assertions`
- `config`
- `schema`
- `schema`


## Step-by-Step Guide

### Step 1: Assign engine = self._fixture(...)

```python
engine = self._fixture(False)
```

**Verification:**
```python
assert not self._is_server_side(result.cursor)
```

### Step 2: Assign s1 = select.execution_options.subquery(...)

```python
s1 = select(sql.literal_column('1').label('x')).execution_options(stream_results=True).subquery()
```

**Verification:**
```python
assert not self._is_server_side(result.cursor)
```

### Step 3: Assign s2 = select.select_from(...)

```python
s2 = select(1).select_from(s1)
```

### Step 4: Assign result = conn.execute(...)

```python
result = conn.execute(s1.select())
```

**Verification:**
```python
assert not self._is_server_side(result.cursor)
```

### Step 5: Call result.close()

```python
result.close()
```

### Step 6: Assign result = conn.execute(...)

```python
result = conn.execute(s2)
```

**Verification:**
```python
assert not self._is_server_side(result.cursor)
```

### Step 7: Call result.close()

```python
result.close()
```


## Complete Example

```python
# Workflow
engine = self._fixture(False)
s1 = select(sql.literal_column('1').label('x')).execution_options(stream_results=True).subquery()
with engine.begin() as conn:
    result = conn.execute(s1.select())
    assert not self._is_server_side(result.cursor)
    result.close()
s2 = select(1).select_from(s1)
with engine.begin() as conn:
    result = conn.execute(s2)
    assert not self._is_server_side(result.cursor)
    result.close()
```

## Next Steps


---

*Source: test_results.py:410 | Complexity: Intermediate | Last updated: 2026-06-02*