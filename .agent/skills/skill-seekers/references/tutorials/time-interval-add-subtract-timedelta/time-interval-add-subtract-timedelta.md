# How To: Time Interval Add Subtract Timedelta

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test time interval add subtract timedelta

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: interval, delta, method
```

## Step-by-Step Guide

### Step 1: Assign result = getattr(...)

```python
result = getattr(interval, method)(delta)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign left = getattr(...)

```python
left = getattr(interval.left, method)(delta)
```

### Step 3: Assign right = getattr(...)

```python
right = getattr(interval.right, method)(delta)
```

### Step 4: Assign expected = Interval(...)

```python
expected = Interval(left, right)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: interval, delta, method

# Workflow
result = getattr(interval, method)(delta)
left = getattr(interval.left, method)(delta)
right = getattr(interval.right, method)(delta)
expected = Interval(left, right)
assert result == expected
```

## Next Steps


---

*Source: test_arithmetic.py:125 | Complexity: Intermediate | Last updated: 2026-06-02*