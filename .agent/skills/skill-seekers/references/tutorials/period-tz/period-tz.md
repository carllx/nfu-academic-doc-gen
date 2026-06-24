# How To: Period Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test period tz

## Prerequisites

**Required Modules:**
- `contextlib`
- `datetime`
- `locale`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign msg = 'PeriodIndex\\.format is deprecated'

```python
msg = 'PeriodIndex\\.format is deprecated'
```

**Verification:**
```python
assert per.format()[0] == '2012-12-31 23:00'
```

### Step 2: Assign dt = pd.to_datetime(...)

```python
dt = pd.to_datetime(['2013-01-01 00:00:00+01:00'], utc=True)
```

**Verification:**
```python
assert per.format()[0] == '2013-01-01 00:00'
```

### Step 3: Assign dt = dt.tz_convert(...)

```python
dt = dt.tz_convert('Europe/Paris')
```

### Step 4: Assign per = dt.to_period(...)

```python
per = dt.to_period(freq='h')
```

**Verification:**
```python
assert per.format()[0] == '2012-12-31 23:00'
```

### Step 5: Assign per = dt.to_period(...)

```python
per = dt.to_period(freq='h')
```

**Verification:**
```python
assert per.format()[0] == '2013-01-01 00:00'
```


## Complete Example

```python
# Workflow
msg = 'PeriodIndex\\.format is deprecated'
dt = pd.to_datetime(['2013-01-01 00:00:00+01:00'], utc=True)
with tm.assert_produces_warning(UserWarning, match='will drop timezone'):
    per = dt.to_period(freq='h')
with tm.assert_produces_warning(FutureWarning, match=msg):
    assert per.format()[0] == '2012-12-31 23:00'
dt = dt.tz_convert('Europe/Paris')
with tm.assert_produces_warning(UserWarning, match='will drop timezone'):
    per = dt.to_period(freq='h')
with tm.assert_produces_warning(FutureWarning, match=msg):
    assert per.format()[0] == '2013-01-01 00:00'
```

## Next Steps


---

*Source: test_formats.py:267 | Complexity: Intermediate | Last updated: 2026-06-02*