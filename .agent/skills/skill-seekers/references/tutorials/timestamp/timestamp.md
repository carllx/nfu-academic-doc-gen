# How To: Timestamp

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timestamp

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytz`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: fixed_now_ts
```

## Step-by-Step Guide

### Step 1: Assign ts = fixed_now_ts

```python
ts = fixed_now_ts
```

**Verification:**
```python
assert ts.timestamp() == uts.timestamp()
```

### Step 2: Assign uts = ts.replace(...)

```python
uts = ts.replace(tzinfo=utc)
```

**Verification:**
```python
assert tsc.timestamp() == utsc.timestamp()
```

### Step 3: Assign tsc = Timestamp(...)

```python
tsc = Timestamp('2014-10-11 11:00:01.12345678', tz='US/Central')
```

**Verification:**
```python
assert dt.timestamp() == ts.timestamp()
```

### Step 4: Assign utsc = tsc.tz_convert(...)

```python
utsc = tsc.tz_convert('UTC')
```

**Verification:**
```python
assert tsc.timestamp() == utsc.timestamp()
```

### Step 5: Assign dt = ts.to_pydatetime(...)

```python
dt = ts.to_pydatetime()
```

**Verification:**
```python
assert dt.timestamp() == ts.timestamp()
```


## Complete Example

```python
# Setup
# Fixtures: fixed_now_ts

# Workflow
ts = fixed_now_ts
uts = ts.replace(tzinfo=utc)
assert ts.timestamp() == uts.timestamp()
tsc = Timestamp('2014-10-11 11:00:01.12345678', tz='US/Central')
utsc = tsc.tz_convert('UTC')
assert tsc.timestamp() == utsc.timestamp()
with tm.set_timezone('UTC'):
    dt = ts.to_pydatetime()
    assert dt.timestamp() == ts.timestamp()
```

## Next Steps


---

*Source: test_timestamp_method.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*