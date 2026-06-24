# How To: Td Add Datetimelike Scalar

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test td add datetimelike scalar

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: op
```

## Step-by-Step Guide

### Step 1: Assign td = Timedelta(...)

```python
td = Timedelta(10, unit='d')
```

**Verification:**
```python
assert isinstance(result, Timestamp)
```

### Step 2: Assign result = op(...)

```python
result = op(td, datetime(2016, 1, 1))
```

**Verification:**
```python
assert result == Timestamp(2016, 1, 11)
```

### Step 3: Assign result = op(...)

```python
result = op(td, Timestamp('2018-01-12 18:09'))
```

**Verification:**
```python
assert isinstance(result, Timestamp)
```

### Step 4: Assign result = op(...)

```python
result = op(td, np.datetime64('2018-01-12'))
```

**Verification:**
```python
assert result == Timestamp('2018-01-22 18:09')
```

### Step 5: Assign result = op(...)

```python
result = op(td, NaT)
```

**Verification:**
```python
assert isinstance(result, Timestamp)
```


## Complete Example

```python
# Setup
# Fixtures: op

# Workflow
td = Timedelta(10, unit='d')
result = op(td, datetime(2016, 1, 1))
if op is operator.add:
    assert isinstance(result, Timestamp)
assert result == Timestamp(2016, 1, 11)
result = op(td, Timestamp('2018-01-12 18:09'))
assert isinstance(result, Timestamp)
assert result == Timestamp('2018-01-22 18:09')
result = op(td, np.datetime64('2018-01-12'))
assert isinstance(result, Timestamp)
assert result == Timestamp('2018-01-22')
result = op(td, NaT)
assert result is NaT
```

## Next Steps


---

*Source: test_arithmetic.py:79 | Complexity: Intermediate | Last updated: 2026-06-02*