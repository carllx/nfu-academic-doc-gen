# How To: Last Week Of Month On Offset

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test last week of month on offset

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
# Fixtures: n, weekday, date, tz
```

## Step-by-Step Guide

### Step 1: Assign offset = LastWeekOfMonth(...)

```python
offset = LastWeekOfMonth(n=n, weekday=weekday)
```

**Verification:**
```python
assert fast == slow
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp(date, tz=tz)
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
# Setup
# Fixtures: n, weekday, date, tz

# Workflow
offset = LastWeekOfMonth(n=n, weekday=weekday)
ts = Timestamp(date, tz=tz)
slow = ts + offset - offset == ts
fast = offset.is_on_offset(ts)
assert fast == slow
```

## Next Steps


---

*Source: test_week.py:340 | Complexity: Intermediate | Last updated: 2026-06-02*