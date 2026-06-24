# How To: Path Typed Comparison

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test path typed comparison

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `json`
- `re`
- `uuid`
- `assertions`
- `assertions`
- `assertions`
- `config`
- `schema`
- `schema`
- `orm`
- `orm`
- `sql`
- `sql.sqltypes`
- `sql.sqltypes`

**Setup Required:**
```python
# Fixtures: datatype, value
```

## Step-by-Step Guide

### Step 1: Assign data_table = value

```python
data_table = self.tables.data_table
```

### Step 2: Assign data_element = value

```python
data_element = {'key1': {'subkey1': value}}
```

### Step 3: Assign unknown = self._json_value_insert(...)

```python
datatype, compare_value, p_s = self._json_value_insert(conn, datatype, value, data_element)
```

### Step 4: Assign expr = value

```python
expr = data_table.c.data['key1', 'subkey1']
```

### Step 5: Assign row = conn.execute.first(...)

```python
row = conn.execute(select(expr).where(expr == compare_value)).first()
```

### Step 6: Call eq_()

```python
eq_(row, (compare_value,))
```

### Step 7: Assign expr = expr.as_numeric(...)

```python
expr = expr.as_numeric(*p_s)
```

### Step 8: Assign expr = getattr(...)

```python
expr = getattr(expr, 'as_%s' % datatype)()
```


## Complete Example

```python
# Setup
# Fixtures: datatype, value

# Workflow
data_table = self.tables.data_table
data_element = {'key1': {'subkey1': value}}
with config.db.begin() as conn:
    datatype, compare_value, p_s = self._json_value_insert(conn, datatype, value, data_element)
    expr = data_table.c.data['key1', 'subkey1']
    if datatype:
        if datatype == 'numeric' and p_s:
            expr = expr.as_numeric(*p_s)
        else:
            expr = getattr(expr, 'as_%s' % datatype)()
    row = conn.execute(select(expr).where(expr == compare_value)).first()
    eq_(row, (compare_value,))
```

## Next Steps


---

*Source: test_types.py:1538 | Complexity: Advanced | Last updated: 2026-06-02*