# How To: Roll Date Object

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test roll date object

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas.tests.tseries.offsets.common`


## Step-by-Step Guide

### Step 1: Assign offset = BusinessHour(...)

```python
offset = BusinessHour()
```

**Verification:**
```python
assert result == datetime(2014, 7, 4, 17)
```

### Step 2: Assign dt = datetime(...)

```python
dt = datetime(2014, 7, 6, 15, 0)
```

**Verification:**
```python
assert result == datetime(2014, 7, 7, 9)
```

### Step 3: Assign result = offset.rollback(...)

```python
result = offset.rollback(dt)
```

**Verification:**
```python
assert result == datetime(2014, 7, 4, 17)
```

### Step 4: Assign result = offset.rollforward(...)

```python
result = offset.rollforward(dt)
```

**Verification:**
```python
assert result == datetime(2014, 7, 7, 9)
```


## Complete Example

```python
# Workflow
offset = BusinessHour()
dt = datetime(2014, 7, 6, 15, 0)
result = offset.rollback(dt)
assert result == datetime(2014, 7, 4, 17)
result = offset.rollforward(dt)
assert result == datetime(2014, 7, 7, 9)
```

## Next Steps


---

*Source: test_business_hour.py:340 | Complexity: Intermediate | Last updated: 2026-06-02*