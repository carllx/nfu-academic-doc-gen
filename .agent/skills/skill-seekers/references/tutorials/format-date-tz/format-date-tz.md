# How To: Format Date Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test format date tz

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = pd.to_datetime(...)

```python
dti = pd.to_datetime([datetime(2013, 1, 1)], utc=True)
```

**Verification:**
```python
assert formatted[0] == '2013-01-01 00:00:00+00:00'
```

### Step 2: Assign msg = 'DatetimeIndex.format is deprecated'

```python
msg = 'DatetimeIndex.format is deprecated'
```

**Verification:**
```python
assert formatted[0] == '2013-01-01 00:00:00+00:00'
```

### Step 3: Assign dti = pd.to_datetime(...)

```python
dti = pd.to_datetime([datetime(2013, 1, 1), NaT], utc=True)
```

**Verification:**
```python
assert formatted[0] == '2013-01-01 00:00:00+00:00'
```

### Step 4: Assign formatted = dti.format(...)

```python
formatted = dti.format()
```

### Step 5: Assign formatted = dti.format(...)

```python
formatted = dti.format()
```


## Complete Example

```python
# Workflow
dti = pd.to_datetime([datetime(2013, 1, 1)], utc=True)
msg = 'DatetimeIndex.format is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    formatted = dti.format()
assert formatted[0] == '2013-01-01 00:00:00+00:00'
dti = pd.to_datetime([datetime(2013, 1, 1), NaT], utc=True)
with tm.assert_produces_warning(FutureWarning, match=msg):
    formatted = dti.format()
assert formatted[0] == '2013-01-01 00:00:00+00:00'
```

## Next Steps


---

*Source: test_formats.py:338 | Complexity: Intermediate | Last updated: 2026-06-02*