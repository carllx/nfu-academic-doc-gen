# How To: Now

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test now

## Prerequisites

**Required Modules:**
- `calendar`
- `datetime`
- `zoneinfo`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas.compat`
- `pandas.errors`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign ts_from_string = Timestamp(...)

```python
ts_from_string = Timestamp('now')
```

**Verification:**
```python
assert abs(ts_from_method - ts_from_string) < delta
```

### Step 2: Assign ts_from_method = Timestamp.now(...)

```python
ts_from_method = Timestamp.now()
```

**Verification:**
```python
assert abs(ts_datetime - ts_from_method) < delta
```

### Step 3: Assign ts_datetime = datetime.now(...)

```python
ts_datetime = datetime.now()
```

**Verification:**
```python
assert abs(ts_from_method_tz - ts_from_string_tz) < delta
```

### Step 4: Assign ts_from_string_tz = Timestamp(...)

```python
ts_from_string_tz = Timestamp('now', tz='US/Eastern')
```

**Verification:**
```python
assert abs(ts_from_string_tz.tz_localize(None) - ts_from_method_tz.tz_localize(None)) < delta
```

### Step 5: Assign ts_from_method_tz = Timestamp.now(...)

```python
ts_from_method_tz = Timestamp.now(tz='US/Eastern')
```

### Step 6: Assign delta = Timedelta(...)

```python
delta = Timedelta(seconds=1)
```

**Verification:**
```python
assert abs(ts_from_method - ts_from_string) < delta
```


## Complete Example

```python
# Workflow
ts_from_string = Timestamp('now')
ts_from_method = Timestamp.now()
ts_datetime = datetime.now()
ts_from_string_tz = Timestamp('now', tz='US/Eastern')
ts_from_method_tz = Timestamp.now(tz='US/Eastern')
delta = Timedelta(seconds=1)
assert abs(ts_from_method - ts_from_string) < delta
assert abs(ts_datetime - ts_from_method) < delta
assert abs(ts_from_method_tz - ts_from_string_tz) < delta
assert abs(ts_from_string_tz.tz_localize(None) - ts_from_method_tz.tz_localize(None)) < delta
```

## Next Steps


---

*Source: test_constructors.py:381 | Complexity: Intermediate | Last updated: 2026-06-02*