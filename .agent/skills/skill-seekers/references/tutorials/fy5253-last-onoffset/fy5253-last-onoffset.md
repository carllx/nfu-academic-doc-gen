# How To: Fy5253 Last Onoffset

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fy5253 last onoffset

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
offset = FY5253(n=-5, startingMonth=5, variation='last', weekday=0)
```

**Verification:**
```python
assert fast == slow
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp('1984-05-28 06:29:43.955911354+0200', tz='Europe/San_Marino')
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
offset = FY5253(n=-5, startingMonth=5, variation='last', weekday=0)
ts = Timestamp('1984-05-28 06:29:43.955911354+0200', tz='Europe/San_Marino')
fast = offset.is_on_offset(ts)
slow = ts + offset - offset == ts
assert fast == slow
```

## Next Steps


---

*Source: test_fiscal.py:619 | Complexity: Intermediate | Last updated: 2026-06-02*