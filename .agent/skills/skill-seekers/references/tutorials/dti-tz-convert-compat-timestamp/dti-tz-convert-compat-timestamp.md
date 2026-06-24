# How To: Dti Tz Convert Compat Timestamp

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dti tz convert compat timestamp

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: prefix
```

## Step-by-Step Guide

### Step 1: Assign strdates = value

```python
strdates = ['1/1/2012', '3/1/2012', '4/1/2012']
```

**Verification:**
```python
assert conv == expected
```

### Step 2: Assign idx = DatetimeIndex(...)

```python
idx = DatetimeIndex(strdates, tz=prefix + 'US/Eastern')
```

### Step 3: Assign conv = unknown.tz_convert(...)

```python
conv = idx[0].tz_convert(prefix + 'US/Pacific')
```

### Step 4: Assign expected = value

```python
expected = idx.tz_convert(prefix + 'US/Pacific')[0]
```

**Verification:**
```python
assert conv == expected
```


## Complete Example

```python
# Setup
# Fixtures: prefix

# Workflow
strdates = ['1/1/2012', '3/1/2012', '4/1/2012']
idx = DatetimeIndex(strdates, tz=prefix + 'US/Eastern')
conv = idx[0].tz_convert(prefix + 'US/Pacific')
expected = idx.tz_convert(prefix + 'US/Pacific')[0]
assert conv == expected
```

## Next Steps


---

*Source: test_tz_convert.py:58 | Complexity: Intermediate | Last updated: 2026-06-02*