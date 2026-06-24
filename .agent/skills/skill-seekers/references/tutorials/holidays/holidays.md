# How To: Holidays

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test holidays

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

### Step 1: Assign holidays = value

```python
holidays = ['2012-05-01', datetime(2013, 5, 1), np.datetime64('2014-05-01')]
```

**Verification:**
```python
assert rs == xp
```

### Step 2: Assign tday = CDay(...)

```python
tday = CDay(holidays=holidays)
```

### Step 3: Assign dt = datetime(...)

```python
dt = datetime(year, 4, 30)
```

### Step 4: Assign xp = datetime(...)

```python
xp = datetime(year, 5, 2)
```

### Step 5: Assign rs = value

```python
rs = dt + tday
```

**Verification:**
```python
assert rs == xp
```


## Complete Example

```python
# Workflow
holidays = ['2012-05-01', datetime(2013, 5, 1), np.datetime64('2014-05-01')]
tday = CDay(holidays=holidays)
for year in range(2012, 2015):
    dt = datetime(year, 4, 30)
    xp = datetime(year, 5, 2)
    rs = dt + tday
    assert rs == xp
```

## Next Steps


---

*Source: test_custom_business_day.py:41 | Complexity: Intermediate | Last updated: 2026-06-02*