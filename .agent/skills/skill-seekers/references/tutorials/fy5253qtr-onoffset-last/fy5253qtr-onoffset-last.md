# How To: Fy5253Qtr Onoffset Last

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fy5253qtr onoffset last

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

### Step 1: Assign offset = FY5253Quarter(...)

```python
offset = FY5253Quarter(n=-2, qtr_with_extra_week=1, startingMonth=7, variation='last', weekday=2)
```

**Verification:**
```python
assert fast == slow
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp('2011-01-26 19:03:40.331096129+0200', tz='Africa/Windhoek')
```

### Step 3: Assign slow = value

```python
slow = ts + offset - offset == ts
```

### Step 4: Assign fast = offset.is_on_offset(...)

```python
fast = offset.is_on_offset(ts)
```

**Verification:**
```python
assert fast == slow
```


## Complete Example

```python
# Workflow
offset = FY5253Quarter(n=-2, qtr_with_extra_week=1, startingMonth=7, variation='last', weekday=2)
ts = Timestamp('2011-01-26 19:03:40.331096129+0200', tz='Africa/Windhoek')
slow = ts + offset - offset == ts
fast = offset.is_on_offset(ts)
assert fast == slow
```

## Next Steps


---

*Source: test_fiscal.py:648 | Complexity: Intermediate | Last updated: 2026-06-02*