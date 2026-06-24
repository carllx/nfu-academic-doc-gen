# How To: Insert W Floats

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test #9701.

this tests insertmanyvalues as well as decimal / floating point
RETURNING types

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `uuid`
- `assertions`
- `config`
- `schema`
- `schema`
- `types`
- `types`
- `types`

**Setup Required:**
```python
# Fixtures: connection, metadata, sort_by_parameter_order, type_, value, do_rounding, multiple_rows
```

## Step-by-Step Guide

### Step 1: 'test #9701.\n\n        this tests insertmanyvalues as well as decimal / floating point\n        RETURNING types\n\n        '

```python
'test #9701.\n\n        this tests insertmanyvalues as well as decimal / floating point\n        RETURNING types\n\n        '
```

### Step 2: Assign t = Table(...)

```python
t = Table('f_t', metadata, Column('id', Integer, Identity(), primary_key=True), Column('value', type_))
```

### Step 3: Call t.create()

```python
t.create(connection)
```

### Step 4: Assign result = connection.execute(...)

```python
result = connection.execute(t.insert().returning(t.c.id, t.c.value, sort_by_parameter_order=bool(sort_by_parameter_order)), [{'value': value} for i in range(10)] if multiple_rows else {'value': value})
```

### Step 5: Assign i_range = range(...)

```python
i_range = range(1, 11)
```

### Step 6: Assign i_range = range(...)

```python
i_range = range(1, 2)
```

### Step 7: Call eq_()

```python
eq_({(id_, round(val_, 5)) for id_, val_ in result}, {(id_, round(value, 5)) for id_ in i_range})
```

### Step 8: Call eq_()

```python
eq_({round(val_, 5) for val_ in connection.scalars(select(t.c.value))}, {round(value, 5)})
```

### Step 9: Call eq_()

```python
eq_(set(result), {(id_, value) for id_ in i_range})
```

### Step 10: Call eq_()

```python
eq_(set(connection.scalars(select(t.c.value))), {value})
```


## Complete Example

```python
# Setup
# Fixtures: connection, metadata, sort_by_parameter_order, type_, value, do_rounding, multiple_rows

# Workflow
'test #9701.\n\n        this tests insertmanyvalues as well as decimal / floating point\n        RETURNING types\n\n        '
t = Table('f_t', metadata, Column('id', Integer, Identity(), primary_key=True), Column('value', type_))
t.create(connection)
result = connection.execute(t.insert().returning(t.c.id, t.c.value, sort_by_parameter_order=bool(sort_by_parameter_order)), [{'value': value} for i in range(10)] if multiple_rows else {'value': value})
if multiple_rows:
    i_range = range(1, 11)
else:
    i_range = range(1, 2)
if do_rounding:
    eq_({(id_, round(val_, 5)) for id_, val_ in result}, {(id_, round(value, 5)) for id_ in i_range})
    eq_({round(val_, 5) for val_ in connection.scalars(select(t.c.value))}, {round(value, 5)})
else:
    eq_(set(result), {(id_, value) for id_ in i_range})
    eq_(set(connection.scalars(select(t.c.value))), {value})
```

## Next Steps


---

*Source: test_insert.py:460 | Complexity: Advanced | Last updated: 2026-06-02*