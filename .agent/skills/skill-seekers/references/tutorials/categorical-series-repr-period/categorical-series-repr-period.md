# How To: Categorical Series Repr Period

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical series repr period

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = period_range(...)

```python
idx = period_range('2011-01-01 09:00', freq='h', periods=5)
```

**Verification:**
```python
assert repr(s) == exp
```

### Step 2: Assign s = Series(...)

```python
s = Series(Categorical(idx))
```

**Verification:**
```python
assert repr(s) == exp
```

### Step 3: Assign exp = '0    2011-01-01 09:00\n1    2011-01-01 10:00\n2    2011-01-01 11:00\n3    2011-01-01 12:00\n4    2011-01-01 13:00\ndtype: category\nCategories (5, period[h]): [2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00,\n                            2011-01-01 13:00]'

```python
exp = '0    2011-01-01 09:00\n1    2011-01-01 10:00\n2    2011-01-01 11:00\n3    2011-01-01 12:00\n4    2011-01-01 13:00\ndtype: category\nCategories (5, period[h]): [2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00,\n                            2011-01-01 13:00]'
```

**Verification:**
```python
assert repr(s) == exp
```

### Step 4: Assign idx = period_range(...)

```python
idx = period_range('2011-01', freq='M', periods=5)
```

### Step 5: Assign s = Series(...)

```python
s = Series(Categorical(idx))
```

### Step 6: Assign exp = '0    2011-01\n1    2011-02\n2    2011-03\n3    2011-04\n4    2011-05\ndtype: category\nCategories (5, period[M]): [2011-01, 2011-02, 2011-03, 2011-04, 2011-05]'

```python
exp = '0    2011-01\n1    2011-02\n2    2011-03\n3    2011-04\n4    2011-05\ndtype: category\nCategories (5, period[M]): [2011-01, 2011-02, 2011-03, 2011-04, 2011-05]'
```

**Verification:**
```python
assert repr(s) == exp
```


## Complete Example

```python
# Workflow
idx = period_range('2011-01-01 09:00', freq='h', periods=5)
s = Series(Categorical(idx))
exp = '0    2011-01-01 09:00\n1    2011-01-01 10:00\n2    2011-01-01 11:00\n3    2011-01-01 12:00\n4    2011-01-01 13:00\ndtype: category\nCategories (5, period[h]): [2011-01-01 09:00, 2011-01-01 10:00, 2011-01-01 11:00, 2011-01-01 12:00,\n                            2011-01-01 13:00]'
assert repr(s) == exp
idx = period_range('2011-01', freq='M', periods=5)
s = Series(Categorical(idx))
exp = '0    2011-01\n1    2011-02\n2    2011-03\n3    2011-04\n4    2011-05\ndtype: category\nCategories (5, period[M]): [2011-01, 2011-02, 2011-03, 2011-04, 2011-05]'
assert repr(s) == exp
```

## Next Steps


---

*Source: test_formats.py:452 | Complexity: Intermediate | Last updated: 2026-06-02*