# How To: Weekmask And Holidays

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weekmask and holidays

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries.holiday`


## Step-by-Step Guide

### Step 1: Assign weekmask_egypt = 'Sun Mon Tue Wed Thu'

```python
weekmask_egypt = 'Sun Mon Tue Wed Thu'
```

**Verification:**
```python
assert xp_egypt == dt + 2 * bday_egypt
```

### Step 2: Assign holidays = value

```python
holidays = ['2012-05-01', datetime(2013, 5, 1), np.datetime64('2014-05-01')]
```

### Step 3: Assign bday_egypt = CDay(...)

```python
bday_egypt = CDay(holidays=holidays, weekmask=weekmask_egypt)
```

### Step 4: Assign dt = datetime(...)

```python
dt = datetime(2013, 4, 30)
```

### Step 5: Assign xp_egypt = datetime(...)

```python
xp_egypt = datetime(2013, 5, 5)
```

**Verification:**
```python
assert xp_egypt == dt + 2 * bday_egypt
```


## Complete Example

```python
# Workflow
weekmask_egypt = 'Sun Mon Tue Wed Thu'
holidays = ['2012-05-01', datetime(2013, 5, 1), np.datetime64('2014-05-01')]
bday_egypt = CDay(holidays=holidays, weekmask=weekmask_egypt)
dt = datetime(2013, 4, 30)
xp_egypt = datetime(2013, 5, 5)
assert xp_egypt == dt + 2 * bday_egypt
```

## Next Steps


---

*Source: test_custom_business_day.py:70 | Complexity: Intermediate | Last updated: 2026-06-02*