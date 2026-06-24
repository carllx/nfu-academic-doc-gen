# How To: Dti To Pydatetime

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti to pydatetime

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.parser`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexes.datetimes.test_timezones`


## Step-by-Step Guide

### Step 1: Assign dt = dateutil.parser.parse(...)

```python
dt = dateutil.parser.parse('2012-06-13T01:39:00Z')
```

**Verification:**
```python
assert result.tz is timezone.utc
```

### Step 2: Assign dt = dt.replace(...)

```python
dt = dt.replace(tzinfo=tzlocal())
```

**Verification:**
```python
assert result.tz is timezone.utc
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array([dt], dtype=object)
```

### Step 4: Assign result = to_datetime(...)

```python
result = to_datetime(arr, utc=True)
```

**Verification:**
```python
assert result.tz is timezone.utc
```

### Step 5: Assign rng = date_range(...)

```python
rng = date_range('2012-11-03 03:00', '2012-11-05 03:00', tz=tzlocal())
```

### Step 6: Assign arr = rng.to_pydatetime(...)

```python
arr = rng.to_pydatetime()
```

### Step 7: Assign result = to_datetime(...)

```python
result = to_datetime(arr, utc=True)
```

**Verification:**
```python
assert result.tz is timezone.utc
```


## Complete Example

```python
# Workflow
dt = dateutil.parser.parse('2012-06-13T01:39:00Z')
dt = dt.replace(tzinfo=tzlocal())
arr = np.array([dt], dtype=object)
result = to_datetime(arr, utc=True)
assert result.tz is timezone.utc
rng = date_range('2012-11-03 03:00', '2012-11-05 03:00', tz=tzlocal())
arr = rng.to_pydatetime()
result = to_datetime(arr, utc=True)
assert result.tz is timezone.utc
```

## Next Steps


---

*Source: test_to_pydatetime.py:23 | Complexity: Intermediate | Last updated: 2026-06-02*