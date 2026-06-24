# How To: Is On Offset Weekday None

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test is on offset weekday none

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
# Fixtures: n, date
```

## Step-by-Step Guide

### Step 1: Assign offset = Week(...)

```python
offset = Week(n=n, weekday=None)
```

**Verification:**
```python
assert fast == slow
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp(date, tz='Africa/Lusaka')
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
# Fixtures: n, date

# Workflow
offset = Week(n=n, weekday=None)
ts = Timestamp(date, tz='Africa/Lusaka')
fast = offset.is_on_offset(ts)
slow = ts + offset - offset == ts
assert fast == slow
```

## Next Steps


---

*Source: test_week.py:131 | Complexity: Intermediate | Last updated: 2026-06-02*