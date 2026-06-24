# How To: Constructor Errors Tz

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor errors tz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`

**Setup Required:**
```python
# Fixtures: tz_left, tz_right
```

## Step-by-Step Guide

### Step 1: Assign left = Timestamp(...)

```python
left = Timestamp('2017-01-01', tz=tz_left)
```

### Step 2: Assign right = Timestamp(...)

```python
right = Timestamp('2017-01-02', tz=tz_right)
```

### Step 3: Assign error = TypeError

```python
error = TypeError
```

### Step 4: Assign msg = 'Cannot compare tz-naive and tz-aware timestamps'

```python
msg = 'Cannot compare tz-naive and tz-aware timestamps'
```

### Step 5: Assign error = ValueError

```python
error = ValueError
```

### Step 6: Assign msg = 'left and right must have the same time zone'

```python
msg = 'left and right must have the same time zone'
```

### Step 7: Call Interval()

```python
Interval(left, right)
```


## Complete Example

```python
# Setup
# Fixtures: tz_left, tz_right

# Workflow
left = Timestamp('2017-01-01', tz=tz_left)
right = Timestamp('2017-01-02', tz=tz_right)
if tz_left is None or tz_right is None:
    error = TypeError
    msg = 'Cannot compare tz-naive and tz-aware timestamps'
else:
    error = ValueError
    msg = 'left and right must have the same time zone'
with pytest.raises(error, match=msg):
    Interval(left, right)
```

## Next Steps


---

*Source: test_constructors.py:39 | Complexity: Intermediate | Last updated: 2026-06-02*