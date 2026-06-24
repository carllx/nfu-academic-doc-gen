# How To: Frame Datetime64 Duplicated

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame datetime64 duplicated

## Prerequisites

**Required Modules:**
- `re`
- `sys`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dates = date_range(...)

```python
dates = date_range('2010-07-01', end='2010-08-05')
```

**Verification:**
```python
assert (-result).all()
```

### Step 2: Assign tst = DataFrame(...)

```python
tst = DataFrame({'symbol': 'AAA', 'date': dates})
```

**Verification:**
```python
assert (-result).all()
```

### Step 3: Assign result = tst.duplicated(...)

```python
result = tst.duplicated(['date', 'symbol'])
```

**Verification:**
```python
assert (-result).all()
```

### Step 4: Assign tst = DataFrame(...)

```python
tst = DataFrame({'date': dates})
```

### Step 5: Assign result = tst.date.duplicated(...)

```python
result = tst.date.duplicated()
```

**Verification:**
```python
assert (-result).all()
```


## Complete Example

```python
# Workflow
dates = date_range('2010-07-01', end='2010-08-05')
tst = DataFrame({'symbol': 'AAA', 'date': dates})
result = tst.duplicated(['date', 'symbol'])
assert (-result).all()
tst = DataFrame({'date': dates})
result = tst.date.duplicated()
assert (-result).all()
```

## Next Steps


---

*Source: test_duplicated.py:108 | Complexity: Intermediate | Last updated: 2026-06-02*