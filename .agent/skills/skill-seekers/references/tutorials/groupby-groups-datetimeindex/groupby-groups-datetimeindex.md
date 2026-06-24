# How To: Groupby Groups Datetimeindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby groups datetimeindex

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.groupby.ops`


## Step-by-Step Guide

### Step 1: Assign periods = 1000

```python
periods = 1000
```

**Verification:**
```python
assert isinstance(next(iter(groups.keys())), datetime)
```

### Step 2: Assign ind = date_range(...)

```python
ind = date_range(start='2012/1/1', freq='5min', periods=periods)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'high': np.arange(periods), 'low': np.arange(periods)}, index=ind)
```

### Step 4: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(lambda x: datetime(x.year, x.month, x.day))
```

### Step 5: Assign groups = value

```python
groups = grouped.groups
```

**Verification:**
```python
assert isinstance(next(iter(groups.keys())), datetime)
```


## Complete Example

```python
# Workflow
periods = 1000
ind = date_range(start='2012/1/1', freq='5min', periods=periods)
df = DataFrame({'high': np.arange(periods), 'low': np.arange(periods)}, index=ind)
grouped = df.groupby(lambda x: datetime(x.year, x.month, x.day))
groups = grouped.groups
assert isinstance(next(iter(groups.keys())), datetime)
```

## Next Steps


---

*Source: test_timegrouper.py:512 | Complexity: Intermediate | Last updated: 2026-06-02*