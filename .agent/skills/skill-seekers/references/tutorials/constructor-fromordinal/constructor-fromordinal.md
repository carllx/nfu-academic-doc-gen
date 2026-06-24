# How To: Constructor Fromordinal

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor fromordinal

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

### Step 1: Assign base = datetime(...)

```python
base = datetime(2000, 1, 1)
```

**Verification:**
```python
assert base == ts
```

### Step 2: Assign ts = Timestamp.fromordinal(...)

```python
ts = Timestamp.fromordinal(base.toordinal())
```

**Verification:**
```python
assert base.toordinal() == ts.toordinal()
```

### Step 3: Assign ts = Timestamp.fromordinal(...)

```python
ts = Timestamp.fromordinal(base.toordinal(), tz='US/Eastern')
```

**Verification:**
```python
assert Timestamp('2000-01-01', tz='US/Eastern') == ts
```

### Step 4: Assign dt = datetime(...)

```python
dt = datetime(2011, 4, 16, 0, 0)
```

**Verification:**
```python
assert base.toordinal() == ts.toordinal()
```

### Step 5: Assign ts = Timestamp.fromordinal(...)

```python
ts = Timestamp.fromordinal(dt.toordinal())
```

**Verification:**
```python
assert ts.to_pydatetime() == dt
```

### Step 6: Assign stamp = Timestamp(...)

```python
stamp = Timestamp('2011-4-16', tz='US/Eastern')
```

**Verification:**
```python
assert ts.to_pydatetime() == dt_tz
```

### Step 7: Assign dt_tz = stamp.to_pydatetime(...)

```python
dt_tz = stamp.to_pydatetime()
```

### Step 8: Assign ts = Timestamp.fromordinal(...)

```python
ts = Timestamp.fromordinal(dt_tz.toordinal(), tz='US/Eastern')
```

**Verification:**
```python
assert ts.to_pydatetime() == dt_tz
```


## Complete Example

```python
# Workflow
base = datetime(2000, 1, 1)
ts = Timestamp.fromordinal(base.toordinal())
assert base == ts
assert base.toordinal() == ts.toordinal()
ts = Timestamp.fromordinal(base.toordinal(), tz='US/Eastern')
assert Timestamp('2000-01-01', tz='US/Eastern') == ts
assert base.toordinal() == ts.toordinal()
dt = datetime(2011, 4, 16, 0, 0)
ts = Timestamp.fromordinal(dt.toordinal())
assert ts.to_pydatetime() == dt
stamp = Timestamp('2011-4-16', tz='US/Eastern')
dt_tz = stamp.to_pydatetime()
ts = Timestamp.fromordinal(dt_tz.toordinal(), tz='US/Eastern')
assert ts.to_pydatetime() == dt_tz
```

## Next Steps


---

*Source: test_constructors.py:359 | Complexity: Advanced | Last updated: 2026-06-02*