# How To: Addition Subtraction Types

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test addition subtraction types

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dt = datetime(...)

```python
dt = datetime(2014, 3, 4)
```

**Verification:**
```python
assert type(ts - dt) == Timedelta
```

### Step 2: Assign td = timedelta(...)

```python
td = timedelta(seconds=1)
```

**Verification:**
```python
assert type(ts + td) == Timestamp
```

### Step 3: Assign ts = Timestamp(...)

```python
ts = Timestamp(dt)
```

**Verification:**
```python
assert type(ts - td) == Timestamp
```

### Step 4: Assign msg = 'Addition/subtraction of integers'

```python
msg = 'Addition/subtraction of integers'
```

**Verification:**
```python
assert type(ts + td64) == Timestamp
```

### Step 5: Assign td64 = np.timedelta64(...)

```python
td64 = np.timedelta64(1, 'D')
```

**Verification:**
```python
assert type(ts - td64) == Timestamp
```

### Step 6: ts + 1

```python
ts + 1
```

### Step 7: ts - 1

```python
ts - 1
```


## Complete Example

```python
# Workflow
dt = datetime(2014, 3, 4)
td = timedelta(seconds=1)
ts = Timestamp(dt)
msg = 'Addition/subtraction of integers'
with pytest.raises(TypeError, match=msg):
    ts + 1
with pytest.raises(TypeError, match=msg):
    ts - 1
assert type(ts - dt) == Timedelta
assert type(ts + td) == Timestamp
assert type(ts - td) == Timestamp
td64 = np.timedelta64(1, 'D')
assert type(ts + td64) == Timestamp
assert type(ts - td64) == Timestamp
```

## Next Steps


---

*Source: test_arithmetic.py:153 | Complexity: Intermediate | Last updated: 2026-06-02*