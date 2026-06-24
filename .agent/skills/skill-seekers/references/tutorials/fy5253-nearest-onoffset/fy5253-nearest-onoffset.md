# How To: Fy5253 Nearest Onoffset

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fy5253 nearest onoffset

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

### Step 1: Assign offset = FY5253(...)

```python
offset = FY5253(n=3, startingMonth=7, variation='nearest', weekday=2)
```

**Verification:**
```python
assert fast == slow
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp('2032-07-28 00:12:59.035729419+0000', tz='Africa/Dakar')
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
offset = FY5253(n=3, startingMonth=7, variation='nearest', weekday=2)
ts = Timestamp('2032-07-28 00:12:59.035729419+0000', tz='Africa/Dakar')
fast = offset.is_on_offset(ts)
slow = ts + offset - offset == ts
assert fast == slow
```

## Next Steps


---

*Source: test_fiscal.py:628 | Complexity: Intermediate | Last updated: 2026-06-02*