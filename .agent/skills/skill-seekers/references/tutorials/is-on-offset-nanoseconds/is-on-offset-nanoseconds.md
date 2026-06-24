# How To: Is On Offset Nanoseconds

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test is on offset nanoseconds

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`

**Setup Required:**
```python
# Fixtures: n, week, date, tz
```

## Step-by-Step Guide

### Step 1: Assign offset = WeekOfMonth(...)

```python
offset = WeekOfMonth(n=n, week=week, weekday=0)
```

**Verification:**
```python
assert fast == slow
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp(date, tz=tz)
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
# Setup
# Fixtures: n, week, date, tz

# Workflow
offset = WeekOfMonth(n=n, week=week, weekday=0)
ts = Timestamp(date, tz=tz)
fast = offset.is_on_offset(ts)
slow = ts + offset - offset == ts
assert fast == slow
```

## Next Steps


---

*Source: test_week.py:251 | Complexity: Intermediate | Last updated: 2026-06-02*