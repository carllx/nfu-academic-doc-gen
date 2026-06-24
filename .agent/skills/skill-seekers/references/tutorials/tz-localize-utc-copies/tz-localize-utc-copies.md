# How To: Tz Localize Utc Copies

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tz localize utc copies

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `zoneinfo`

**Setup Required:**
```python
# Fixtures: utc_fixture
```

## Step-by-Step Guide

### Step 1: Assign times = value

```python
times = ['2015-03-08 01:00', '2015-03-08 02:00', '2015-03-08 03:00']
```

**Verification:**
```python
assert not tm.shares_memory(res, index)
```

### Step 2: Assign index = DatetimeIndex(...)

```python
index = DatetimeIndex(times)
```

**Verification:**
```python
assert not tm.shares_memory(index._data, res2)
```

### Step 3: Assign res = index.tz_localize(...)

```python
res = index.tz_localize(utc_fixture)
```

**Verification:**
```python
assert not tm.shares_memory(res, index)
```

### Step 4: Assign res2 = index._data.tz_localize(...)

```python
res2 = index._data.tz_localize(utc_fixture)
```

**Verification:**
```python
assert not tm.shares_memory(index._data, res2)
```


## Complete Example

```python
# Setup
# Fixtures: utc_fixture

# Workflow
times = ['2015-03-08 01:00', '2015-03-08 02:00', '2015-03-08 03:00']
index = DatetimeIndex(times)
res = index.tz_localize(utc_fixture)
assert not tm.shares_memory(res, index)
res2 = index._data.tz_localize(utc_fixture)
assert not tm.shares_memory(index._data, res2)
```

## Next Steps


---

*Source: test_tz_localize.py:63 | Complexity: Intermediate | Last updated: 2026-06-02*