# How To: Non Rowcount Scenarios No Raise

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate execute: test non rowcount scenarios no raise

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
# Fixtures: connection, statement, close_first
```

## Step-by-Step Guide

### Step 1: Assign r = connection.execute(...)

```python
r = connection.execute(employees_table.insert(), [{'employee_id': 25, 'name': 'none 1', 'department': 'X'}, {'employee_id': 26, 'name': 'none 2', 'department': 'Z'}, {'employee_id': 27, 'name': 'none 3', 'department': 'Z'}])
```


## Complete Example

```python
# Setup
# Fixtures: connection, statement, close_first

# Workflow
r = connection.execute(employees_table.insert(), [{'employee_id': 25, 'name': 'none 1', 'department': 'X'}, {'employee_id': 26, 'name': 'none 2', 'department': 'Z'}, {'employee_id': 27, 'name': 'none 3', 'department': 'Z'}])
```

## Next Steps


---

*Source: test_rowcount.py:96 | Complexity: Beginner | Last updated: 2026-06-02*