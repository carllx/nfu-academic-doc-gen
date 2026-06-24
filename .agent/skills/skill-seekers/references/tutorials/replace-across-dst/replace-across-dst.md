# How To: Replace Across Dst

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test replace across dst

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas.util._test_decorators`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz, normalize
```

## Step-by-Step Guide

### Step 1: Assign ts_naive = Timestamp(...)

```python
ts_naive = Timestamp('2017-12-03 16:03:30')
```

**Verification:**
```python
assert ts_aware == normalize(ts_aware)
```

### Step 2: Assign ts_aware = conversion.localize_pydatetime(...)

```python
ts_aware = conversion.localize_pydatetime(ts_naive, tz)
```

**Verification:**
```python
assert (ts2.hour, ts2.minute) == (ts_aware.hour, ts_aware.minute)
```

### Step 3: Assign ts2 = ts_aware.replace(...)

```python
ts2 = ts_aware.replace(month=6)
```

**Verification:**
```python
assert ts2 == ts2b
```

### Step 4: Assign ts2b = normalize(...)

```python
ts2b = normalize(ts2)
```

**Verification:**
```python
assert ts2 == ts2b
```


## Complete Example

```python
# Setup
# Fixtures: tz, normalize

# Workflow
ts_naive = Timestamp('2017-12-03 16:03:30')
ts_aware = conversion.localize_pydatetime(ts_naive, tz)
assert ts_aware == normalize(ts_aware)
ts2 = ts_aware.replace(month=6)
assert (ts2.hour, ts2.minute) == (ts_aware.hour, ts_aware.minute)
ts2b = normalize(ts2)
assert ts2 == ts2b
```

## Next Steps


---

*Source: test_replace.py:141 | Complexity: Intermediate | Last updated: 2026-06-02*