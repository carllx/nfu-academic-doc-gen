# How To: Class Ops

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test class ops

## Prerequisites

**Required Modules:**
- `calendar`
- `datetime`
- `locale`
- `time`
- `unicodedata`
- `dateutil.tz`
- `hypothesis`
- `numpy`
- `pytest`
- `pytz`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.timezones`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.tseries`
- `pandas.tseries.frequencies`


## Step-by-Step Guide

### Step 1: Call compare()

```python
compare(Timestamp.now(), datetime.now())
```

**Verification:**
```python
assert int((Timestamp(x)._value - Timestamp(y)._value) / 1000000000.0) == 0
```

### Step 2: Call compare()

```python
compare(Timestamp.now('UTC'), datetime.now(pytz.timezone('UTC')))
```

**Verification:**
```python
assert ts_utc.timestamp() == current_time
```

### Step 3: Call compare()

```python
compare(Timestamp.now('UTC'), datetime.now(tzutc()))
```

### Step 4: Call compare()

```python
compare(Timestamp.utcnow(), datetime.now(timezone.utc))
```

### Step 5: Call compare()

```python
compare(Timestamp.today(), datetime.today())
```

### Step 6: Assign current_time = calendar.timegm(...)

```python
current_time = calendar.timegm(datetime.now().utctimetuple())
```

### Step 7: Assign ts_utc = Timestamp.utcfromtimestamp(...)

```python
ts_utc = Timestamp.utcfromtimestamp(current_time)
```

**Verification:**
```python
assert ts_utc.timestamp() == current_time
```

### Step 8: Call compare()

```python
compare(Timestamp.fromtimestamp(current_time), datetime.fromtimestamp(current_time))
```

### Step 9: Call compare()

```python
compare(Timestamp.fromtimestamp(current_time, 'UTC'), datetime.fromtimestamp(current_time, utc))
```

### Step 10: Call compare()

```python
compare(Timestamp.fromtimestamp(current_time, tz='UTC'), datetime.fromtimestamp(current_time, utc))
```

### Step 11: Assign date_component = datetime.now(...)

```python
date_component = datetime.now(timezone.utc)
```

### Step 12: Assign time_component = unknown.time(...)

```python
time_component = (date_component + timedelta(minutes=10)).time()
```

### Step 13: Call compare()

```python
compare(Timestamp.combine(date_component, time_component), datetime.combine(date_component, time_component))
```

**Verification:**
```python
assert int((Timestamp(x)._value - Timestamp(y)._value) / 1000000000.0) == 0
```


## Complete Example

```python
# Workflow
def compare(x, y):
    assert int((Timestamp(x)._value - Timestamp(y)._value) / 1000000000.0) == 0
compare(Timestamp.now(), datetime.now())
compare(Timestamp.now('UTC'), datetime.now(pytz.timezone('UTC')))
compare(Timestamp.now('UTC'), datetime.now(tzutc()))
compare(Timestamp.utcnow(), datetime.now(timezone.utc))
compare(Timestamp.today(), datetime.today())
current_time = calendar.timegm(datetime.now().utctimetuple())
ts_utc = Timestamp.utcfromtimestamp(current_time)
assert ts_utc.timestamp() == current_time
compare(Timestamp.fromtimestamp(current_time), datetime.fromtimestamp(current_time))
compare(Timestamp.fromtimestamp(current_time, 'UTC'), datetime.fromtimestamp(current_time, utc))
compare(Timestamp.fromtimestamp(current_time, tz='UTC'), datetime.fromtimestamp(current_time, utc))
date_component = datetime.now(timezone.utc)
time_component = (date_component + timedelta(minutes=10)).time()
compare(Timestamp.combine(date_component, time_component), datetime.combine(date_component, time_component))
```

## Next Steps


---

*Source: test_timestamp.py:308 | Complexity: Advanced | Last updated: 2026-06-02*