# How To: Row W Scalar Select

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test that a scalar select as a column is returned as such
and that type conversion works OK.

(this is half a SQLAlchemy Core test and half to catch database
backends that may have unusual behavior with scalar selects.)

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `assertions`
- `config`
- `schema`
- `schema`

**Setup Required:**
```python
# Fixtures: connection
```

## Step-by-Step Guide

### Step 1: 'test that a scalar select as a column is returned as such\n        and that type conversion works OK.\n\n        (this is half a SQLAlchemy Core test and half to catch database\n        backends that may have unusual behavior with scalar selects.)\n\n        '

```python
'test that a scalar select as a column is returned as such\n        and that type conversion works OK.\n\n        (this is half a SQLAlchemy Core test and half to catch database\n        backends that may have unusual behavior with scalar selects.)\n\n        '
```

### Step 2: Assign datetable = value

```python
datetable = self.tables.has_dates
```

### Step 3: Assign s = select.scalar_subquery(...)

```python
s = select(datetable.alias('x').c.today).scalar_subquery()
```

### Step 4: Assign s2 = select(...)

```python
s2 = select(datetable.c.id, s.label('somelabel'))
```

### Step 5: Assign row = connection.execute.first(...)

```python
row = connection.execute(s2).first()
```

### Step 6: Call eq_()

```python
eq_(row.somelabel, datetime.datetime(2006, 5, 12, 12, 0, 0))
```


## Complete Example

```python
# Setup
# Fixtures: connection

# Workflow
'test that a scalar select as a column is returned as such\n        and that type conversion works OK.\n\n        (this is half a SQLAlchemy Core test and half to catch database\n        backends that may have unusual behavior with scalar selects.)\n\n        '
datetable = self.tables.has_dates
s = select(datetable.alias('x').c.today).scalar_subquery()
s2 = select(datetable.c.id, s.label('somelabel'))
row = connection.execute(s2).first()
eq_(row.somelabel, datetime.datetime(2006, 5, 12, 12, 0, 0))
```

## Next Steps


---

*Source: test_results.py:106 | Complexity: Intermediate | Last updated: 2026-06-02*