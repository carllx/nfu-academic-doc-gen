# How To: Constructor Str Infer Reso

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor str infer reso

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
ts = Timestamp('01/30/2023')
```

**Verification:**
```python
assert ts.unit == 's'
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp('2015Q1')
```

**Verification:**
```python
assert ts.unit == 's'
```

### Step 3: Assign ts = Timestamp(...)

```python
ts = Timestamp('2016-01-01 1:30:01 PM')
```

**Verification:**
```python
assert ts.unit == 's'
```

### Step 4: Assign ts = Timestamp(...)

```python
ts = Timestamp('2016 June 3 15:25:01.345')
```

**Verification:**
```python
assert ts.unit == 'ms'
```

### Step 5: Assign ts = Timestamp(...)

```python
ts = Timestamp('300-01-01')
```

**Verification:**
```python
assert ts.unit == 's'
```

### Step 6: Assign ts = Timestamp(...)

```python
ts = Timestamp('300 June 1:30:01.300')
```

**Verification:**
```python
assert ts.unit == 'ms'
```

### Step 7: Assign ts = Timestamp(...)

```python
ts = Timestamp('01-01-2013T00:00:00.000000000+0000')
```

**Verification:**
```python
assert ts.unit == 'ns'
```

### Step 8: Assign ts = Timestamp(...)

```python
ts = Timestamp('2016/01/02 03:04:05.001000 UTC')
```

**Verification:**
```python
assert ts.unit == 'us'
```

### Step 9: Assign ts = Timestamp(...)

```python
ts = Timestamp('01-01-2013T00:00:00.000000002100+0000')
```

**Verification:**
```python
assert ts == Timestamp('01-01-2013T00:00:00.000000002+0000')
```

### Step 10: Assign ts = Timestamp(...)

```python
ts = Timestamp('2020-01-01 00:00+00:00')
```

**Verification:**
```python
assert ts.unit == 'ns'
```

### Step 11: Assign ts = Timestamp(...)

```python
ts = Timestamp('2020-01-01 00+00:00')
```

**Verification:**
```python
assert ts.unit == 's'
```


## Complete Example

```python
# Workflow
ts = Timestamp('01/30/2023')
assert ts.unit == 's'
ts = Timestamp('2015Q1')
assert ts.unit == 's'
ts = Timestamp('2016-01-01 1:30:01 PM')
assert ts.unit == 's'
ts = Timestamp('2016 June 3 15:25:01.345')
assert ts.unit == 'ms'
ts = Timestamp('300-01-01')
assert ts.unit == 's'
ts = Timestamp('300 June 1:30:01.300')
assert ts.unit == 'ms'
ts = Timestamp('01-01-2013T00:00:00.000000000+0000')
assert ts.unit == 'ns'
ts = Timestamp('2016/01/02 03:04:05.001000 UTC')
assert ts.unit == 'us'
ts = Timestamp('01-01-2013T00:00:00.000000002100+0000')
assert ts == Timestamp('01-01-2013T00:00:00.000000002+0000')
assert ts.unit == 'ns'
ts = Timestamp('2020-01-01 00:00+00:00')
assert ts.unit == 's'
ts = Timestamp('2020-01-01 00+00:00')
assert ts.unit == 's'
```

## Next Steps


---

*Source: test_constructors.py:433 | Complexity: Advanced | Last updated: 2026-06-02*