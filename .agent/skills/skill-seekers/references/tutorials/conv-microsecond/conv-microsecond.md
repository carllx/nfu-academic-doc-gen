# How To: Conv Microsecond

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test conv microsecond

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign per = Period(...)

```python
per = Period('2020-01-30 15:57:27.576166', freq='us')
```

**Verification:**
```python
assert per.ordinal == 1580399847576166
```

### Step 2: Assign start = value

```python
start = per.start_time
```

**Verification:**
```python
assert start == expected
```

### Step 3: Assign expected = Timestamp(...)

```python
expected = Timestamp('2020-01-30 15:57:27.576166')
```

**Verification:**
```python
assert start._value == per.ordinal * 1000
```

### Step 4: Assign per2 = Period(...)

```python
per2 = Period('2300-01-01', 'us')
```

### Step 5: Assign msg = '2300-01-01'

```python
msg = '2300-01-01'
```

### Step 6: per2.start_time

```python
per2.start_time
```

### Step 7: per2.end_time

```python
per2.end_time
```


## Complete Example

```python
# Workflow
per = Period('2020-01-30 15:57:27.576166', freq='us')
assert per.ordinal == 1580399847576166
start = per.start_time
expected = Timestamp('2020-01-30 15:57:27.576166')
assert start == expected
assert start._value == per.ordinal * 1000
per2 = Period('2300-01-01', 'us')
msg = '2300-01-01'
with pytest.raises(OutOfBoundsDatetime, match=msg):
    per2.start_time
with pytest.raises(OutOfBoundsDatetime, match=msg):
    per2.end_time
```

## Next Steps


---

*Source: test_asfreq.py:691 | Complexity: Intermediate | Last updated: 2026-06-02*