# How To: Categorical Series Repr Datetime

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical series repr datetime

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('2011-01-01 09:00', freq='h', periods=5)
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

### Step 3: Assign exp = '0   2011-01-01 09:00:00\n1   2011-01-01 10:00:00\n2   2011-01-01 11:00:00\n3   2011-01-01 12:00:00\n4   2011-01-01 13:00:00\ndtype: category\nCategories (5, datetime64[ns]): [2011-01-01 09:00:00, 2011-01-01 10:00:00, 2011-01-01 11:00:00,\n                                 2011-01-01 12:00:00, 2011-01-01 13:00:00]'

```python
exp = '0   2011-01-01 09:00:00\n1   2011-01-01 10:00:00\n2   2011-01-01 11:00:00\n3   2011-01-01 12:00:00\n4   2011-01-01 13:00:00\ndtype: category\nCategories (5, datetime64[ns]): [2011-01-01 09:00:00, 2011-01-01 10:00:00, 2011-01-01 11:00:00,\n                                 2011-01-01 12:00:00, 2011-01-01 13:00:00]'
```

**Verification:**
```python
assert repr(s) == exp
```

### Step 4: Assign idx = date_range(...)

```python
idx = date_range('2011-01-01 09:00', freq='h', periods=5, tz='US/Eastern')
```

### Step 5: Assign s = Series(...)

```python
s = Series(Categorical(idx))
```

### Step 6: Assign exp = '0   2011-01-01 09:00:00-05:00\n1   2011-01-01 10:00:00-05:00\n2   2011-01-01 11:00:00-05:00\n3   2011-01-01 12:00:00-05:00\n4   2011-01-01 13:00:00-05:00\ndtype: category\nCategories (5, datetime64[ns, US/Eastern]): [2011-01-01 09:00:00-05:00, 2011-01-01 10:00:00-05:00,\n                                             2011-01-01 11:00:00-05:00, 2011-01-01 12:00:00-05:00,\n                                             2011-01-01 13:00:00-05:00]'

```python
exp = '0   2011-01-01 09:00:00-05:00\n1   2011-01-01 10:00:00-05:00\n2   2011-01-01 11:00:00-05:00\n3   2011-01-01 12:00:00-05:00\n4   2011-01-01 13:00:00-05:00\ndtype: category\nCategories (5, datetime64[ns, US/Eastern]): [2011-01-01 09:00:00-05:00, 2011-01-01 10:00:00-05:00,\n                                             2011-01-01 11:00:00-05:00, 2011-01-01 12:00:00-05:00,\n                                             2011-01-01 13:00:00-05:00]'
```

**Verification:**
```python
assert repr(s) == exp
```


## Complete Example

```python
# Workflow
idx = date_range('2011-01-01 09:00', freq='h', periods=5)
s = Series(Categorical(idx))
exp = '0   2011-01-01 09:00:00\n1   2011-01-01 10:00:00\n2   2011-01-01 11:00:00\n3   2011-01-01 12:00:00\n4   2011-01-01 13:00:00\ndtype: category\nCategories (5, datetime64[ns]): [2011-01-01 09:00:00, 2011-01-01 10:00:00, 2011-01-01 11:00:00,\n                                 2011-01-01 12:00:00, 2011-01-01 13:00:00]'
assert repr(s) == exp
idx = date_range('2011-01-01 09:00', freq='h', periods=5, tz='US/Eastern')
s = Series(Categorical(idx))
exp = '0   2011-01-01 09:00:00-05:00\n1   2011-01-01 10:00:00-05:00\n2   2011-01-01 11:00:00-05:00\n3   2011-01-01 12:00:00-05:00\n4   2011-01-01 13:00:00-05:00\ndtype: category\nCategories (5, datetime64[ns, US/Eastern]): [2011-01-01 09:00:00-05:00, 2011-01-01 10:00:00-05:00,\n                                             2011-01-01 11:00:00-05:00, 2011-01-01 12:00:00-05:00,\n                                             2011-01-01 13:00:00-05:00]'
assert repr(s) == exp
```

## Next Steps


---

*Source: test_formats.py:396 | Complexity: Intermediate | Last updated: 2026-06-02*