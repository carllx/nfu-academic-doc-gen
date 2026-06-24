# How To: Fy5253Qtr Onoffset Nearest

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fy5253qtr onoffset nearest

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.relativedelta`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('1985-09-02 23:57:46.232550356-0300', tz='Atlantic/Bermuda')
```

**Verification:**
```python
assert fast == slow
```

### Step 2: Assign offset = FY5253Quarter(...)

```python
offset = FY5253Quarter(n=3, qtr_with_extra_week=1, startingMonth=2, variation='nearest', weekday=0)
```

### Step 3: Assign fast = offset.is_on_offset(...)

```python
fast = offset.is_on_offset(ts)
```

### Step 4: Assign slow = value

```python
slow = ts + offset - offset == ts
```

**Verification:**
```python
assert fast == slow
```


## Complete Example

```python
# Workflow
ts = Timestamp('1985-09-02 23:57:46.232550356-0300', tz='Atlantic/Bermuda')
offset = FY5253Quarter(n=3, qtr_with_extra_week=1, startingMonth=2, variation='nearest', weekday=0)
fast = offset.is_on_offset(ts)
slow = ts + offset - offset == ts
assert fast == slow
```

## Next Steps


---

*Source: test_fiscal.py:637 | Complexity: Intermediate | Last updated: 2026-06-02*