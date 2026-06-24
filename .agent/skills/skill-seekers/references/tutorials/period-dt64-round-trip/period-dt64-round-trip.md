# How To: Period Dt64 Round Trip

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test period dt64 round trip

## Prerequisites

**Required Modules:**
- `dateutil.tz`
- `dateutil.tz`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.ccalendar`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('1/1/2000', '1/7/2002', freq='B')
```

### Step 2: Assign pi = dti.to_period(...)

```python
pi = dti.to_period()
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pi.to_timestamp(), dti)
```

### Step 4: Assign dti = date_range(...)

```python
dti = date_range('1/1/2000', '1/7/2002', freq='B')
```

### Step 5: Assign pi = dti.to_period(...)

```python
pi = dti.to_period(freq='h')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pi.to_timestamp(), dti)
```


## Complete Example

```python
# Workflow
dti = date_range('1/1/2000', '1/7/2002', freq='B')
pi = dti.to_period()
tm.assert_index_equal(pi.to_timestamp(), dti)
dti = date_range('1/1/2000', '1/7/2002', freq='B')
pi = dti.to_period(freq='h')
tm.assert_index_equal(pi.to_timestamp(), dti)
```

## Next Steps


---

*Source: test_to_period.py:131 | Complexity: Intermediate | Last updated: 2026-06-02*