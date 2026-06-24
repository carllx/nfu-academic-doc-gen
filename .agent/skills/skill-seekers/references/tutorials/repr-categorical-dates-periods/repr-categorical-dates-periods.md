# How To: Repr Categorical Dates Periods

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repr categorical dates periods

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dt = date_range(...)

```python
dt = date_range('2011-01-01 09:00', freq='h', periods=5, tz='US/Eastern')
```

**Verification:**
```python
assert repr(df) == exp
```

### Step 2: Assign p = period_range(...)

```python
p = period_range('2011-01', freq='M', periods=5)
```

**Verification:**
```python
assert repr(df2) == exp
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'dt': dt, 'p': p})
```

### Step 4: Assign exp = '                         dt        p\n0 2011-01-01 09:00:00-05:00  2011-01\n1 2011-01-01 10:00:00-05:00  2011-02\n2 2011-01-01 11:00:00-05:00  2011-03\n3 2011-01-01 12:00:00-05:00  2011-04\n4 2011-01-01 13:00:00-05:00  2011-05'

```python
exp = '                         dt        p\n0 2011-01-01 09:00:00-05:00  2011-01\n1 2011-01-01 10:00:00-05:00  2011-02\n2 2011-01-01 11:00:00-05:00  2011-03\n3 2011-01-01 12:00:00-05:00  2011-04\n4 2011-01-01 13:00:00-05:00  2011-05'
```

**Verification:**
```python
assert repr(df) == exp
```

### Step 5: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'dt': Categorical(dt), 'p': Categorical(p)})
```

**Verification:**
```python
assert repr(df2) == exp
```


## Complete Example

```python
# Workflow
dt = date_range('2011-01-01 09:00', freq='h', periods=5, tz='US/Eastern')
p = period_range('2011-01', freq='M', periods=5)
df = DataFrame({'dt': dt, 'p': p})
exp = '                         dt        p\n0 2011-01-01 09:00:00-05:00  2011-01\n1 2011-01-01 10:00:00-05:00  2011-02\n2 2011-01-01 11:00:00-05:00  2011-03\n3 2011-01-01 12:00:00-05:00  2011-04\n4 2011-01-01 13:00:00-05:00  2011-05'
assert repr(df) == exp
df2 = DataFrame({'dt': Categorical(dt), 'p': Categorical(p)})
assert repr(df2) == exp
```

## Next Steps


---

*Source: test_repr.py:328 | Complexity: Intermediate | Last updated: 2026-06-02*