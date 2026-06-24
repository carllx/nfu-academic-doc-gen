# How To: Update Delete Rowcount Return Defaults

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: note this test should succeed for all RETURNING backends
as of 2.0.  In
Idf28379f8705e403a3c6a937f6a798a042ef2540 we changed rowcount to use
len(rows) when we have implicit returning

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy`
- `sqlalchemy.testing`
- `sqlalchemy.testing`

**Setup Required:**
```python
# Fixtures: connection, implicit_returning, dml
```

## Step-by-Step Guide

### Step 1: 'note this test should succeed for all RETURNING backends\n        as of 2.0.  In\n        Idf28379f8705e403a3c6a937f6a798a042ef2540 we changed rowcount to use\n        len(rows) when we have implicit returning\n\n        '

```python
'note this test should succeed for all RETURNING backends\n        as of 2.0.  In\n        Idf28379f8705e403a3c6a937f6a798a042ef2540 we changed rowcount to use\n        len(rows) when we have implicit returning\n\n        '
```

### Step 2: Assign department = value

```python
department = employees_table.c.department
```

### Step 3: Assign r = connection.execute(...)

```python
r = connection.execute(stmt)
```

### Step 4: Call eq_()

```python
eq_(r.rowcount, 3)
```

### Step 5: Assign employees_table = value

```python
employees_table = self.tables.employees
```

### Step 6: Assign employees_table = Table(...)

```python
employees_table = Table('employees', MetaData(), Column('employee_id', Integer, autoincrement=False, primary_key=True), Column('name', String(50)), Column('department', String(1)), implicit_returning=False)
```

### Step 7: Assign stmt = employees_table.update.where.values.return_defaults(...)

```python
stmt = employees_table.update().where(department == 'C').values(name=employees_table.c.department + 'Z').return_defaults()
```

### Step 8: Assign stmt = employees_table.delete.where.return_defaults(...)

```python
stmt = employees_table.delete().where(department == 'C').return_defaults()
```

### Step 9: Call dml.fail()

```python
dml.fail()
```


## Complete Example

```python
# Setup
# Fixtures: connection, implicit_returning, dml

# Workflow
'note this test should succeed for all RETURNING backends\n        as of 2.0.  In\n        Idf28379f8705e403a3c6a937f6a798a042ef2540 we changed rowcount to use\n        len(rows) when we have implicit returning\n\n        '
if implicit_returning:
    employees_table = self.tables.employees
else:
    employees_table = Table('employees', MetaData(), Column('employee_id', Integer, autoincrement=False, primary_key=True), Column('name', String(50)), Column('department', String(1)), implicit_returning=False)
department = employees_table.c.department
if dml.update:
    stmt = employees_table.update().where(department == 'C').values(name=employees_table.c.department + 'Z').return_defaults()
elif dml.delete:
    stmt = employees_table.delete().where(department == 'C').return_defaults()
else:
    dml.fail()
r = connection.execute(stmt)
eq_(r.rowcount, 3)
```

## Next Steps


---

*Source: test_rowcount.py:149 | Complexity: Advanced | Last updated: 2026-06-02*