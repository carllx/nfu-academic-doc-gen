# How To: Overflow Offset

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test overflow offset

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign stamp = Timestamp(...)

```python
stamp = Timestamp('2000/1/1')
```

**Verification:**
```python
assert stamp + offset_no_overflow == expected
```

### Step 2: Assign offset_no_overflow = value

```python
offset_no_overflow = to_offset('D') * 100
```

**Verification:**
```python
assert offset_no_overflow + stamp == expected
```

### Step 3: Assign expected = Timestamp(...)

```python
expected = Timestamp('2000/04/10')
```

**Verification:**
```python
assert stamp - offset_no_overflow == expected
```

### Step 4: Assign expected = Timestamp(...)

```python
expected = Timestamp('1999/09/23')
```

**Verification:**
```python
assert stamp - offset_no_overflow == expected
```


## Complete Example

```python
# Workflow
stamp = Timestamp('2000/1/1')
offset_no_overflow = to_offset('D') * 100
expected = Timestamp('2000/04/10')
assert stamp + offset_no_overflow == expected
assert offset_no_overflow + stamp == expected
expected = Timestamp('1999/09/23')
assert stamp - offset_no_overflow == expected
```

## Next Steps


---

*Source: test_arithmetic.py:25 | Complexity: Intermediate | Last updated: 2026-06-02*