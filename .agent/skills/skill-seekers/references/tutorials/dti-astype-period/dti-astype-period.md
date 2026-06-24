# How To: Dti Astype Period

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti astype period

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = DatetimeIndex(...)

```python
idx = DatetimeIndex([NaT, '2011-01-01', '2011-02-01'], name='idx')
```

### Step 2: Assign res = idx.astype(...)

```python
res = idx.astype('period[M]')
```

### Step 3: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['NaT', '2011-01', '2011-02'], freq='M', name='idx')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp)
```

### Step 5: Assign res = idx.astype(...)

```python
res = idx.astype('period[3M]')
```

### Step 6: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['NaT', '2011-01', '2011-02'], freq='3M', name='idx')
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, exp)
```


## Complete Example

```python
# Workflow
idx = DatetimeIndex([NaT, '2011-01-01', '2011-02-01'], name='idx')
res = idx.astype('period[M]')
exp = PeriodIndex(['NaT', '2011-01', '2011-02'], freq='M', name='idx')
tm.assert_index_equal(res, exp)
res = idx.astype('period[3M]')
exp = PeriodIndex(['NaT', '2011-01', '2011-02'], freq='3M', name='idx')
tm.assert_index_equal(res, exp)
```

## Next Steps


---

*Source: test_astype.py:301 | Complexity: Intermediate | Last updated: 2026-06-02*