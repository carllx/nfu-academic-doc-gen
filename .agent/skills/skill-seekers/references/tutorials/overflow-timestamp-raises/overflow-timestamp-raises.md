# How To: Overflow Timestamp Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test overflow timestamp raises

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign msg = 'Result is too large'

```python
msg = 'Result is too large'
```

**Verification:**
```python
assert a - b.to_pydatetime() == a.to_pydatetime() - b
```

### Step 2: Assign a = Timestamp.as_unit(...)

```python
a = Timestamp('2101-01-01 00:00:00').as_unit('ns')
```

### Step 3: Assign b = Timestamp.as_unit(...)

```python
b = Timestamp('1688-01-01 00:00:00').as_unit('ns')
```

**Verification:**
```python
assert a - b.to_pydatetime() == a.to_pydatetime() - b
```

### Step 4: a - b

```python
a - b
```


## Complete Example

```python
# Workflow
msg = 'Result is too large'
a = Timestamp('2101-01-01 00:00:00').as_unit('ns')
b = Timestamp('1688-01-01 00:00:00').as_unit('ns')
with pytest.raises(OutOfBoundsDatetime, match=msg):
    a - b
assert a - b.to_pydatetime() == a.to_pydatetime() - b
```

## Next Steps


---

*Source: test_arithmetic.py:74 | Complexity: Intermediate | Last updated: 2026-06-02*