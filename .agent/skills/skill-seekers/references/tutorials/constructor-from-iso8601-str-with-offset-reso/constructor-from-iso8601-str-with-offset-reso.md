# How To: Constructor From Iso8601 Str With Offset Reso

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor from iso8601 str with offset reso

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

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2016-01-01 04:05:06-01:00')
```

**Verification:**
```python
assert ts.unit == 's'
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp('2016-01-01 04:05:06.000-01:00')
```

**Verification:**
```python
assert ts.unit == 'ms'
```

### Step 3: Assign ts = Timestamp(...)

```python
ts = Timestamp('2016-01-01 04:05:06.000000-01:00')
```

**Verification:**
```python
assert ts.unit == 'us'
```

### Step 4: Assign ts = Timestamp(...)

```python
ts = Timestamp('2016-01-01 04:05:06.000000001-01:00')
```

**Verification:**
```python
assert ts.unit == 'ns'
```


## Complete Example

```python
# Workflow
ts = Timestamp('2016-01-01 04:05:06-01:00')
assert ts.unit == 's'
ts = Timestamp('2016-01-01 04:05:06.000-01:00')
assert ts.unit == 'ms'
ts = Timestamp('2016-01-01 04:05:06.000000-01:00')
assert ts.unit == 'us'
ts = Timestamp('2016-01-01 04:05:06.000000001-01:00')
assert ts.unit == 'ns'
```

## Next Steps


---

*Source: test_constructors.py:501 | Complexity: Intermediate | Last updated: 2026-06-02*