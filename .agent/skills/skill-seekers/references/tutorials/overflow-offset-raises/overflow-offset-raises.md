# How To: Overflow Offset Raises

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test overflow offset raises

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

### Step 1: Assign stamp = Timestamp.as_unit(...)

```python
stamp = Timestamp('2017-01-13 00:00:00').as_unit('ns')
```

### Step 2: Assign offset_overflow = value

```python
offset_overflow = 20169940 * offsets.Day(1)
```

### Step 3: Assign lmsg2 = "Cannot cast -?20169940 days \\+?00:00:00 to unit='ns' without overflow"

```python
lmsg2 = "Cannot cast -?20169940 days \\+?00:00:00 to unit='ns' without overflow"
```

### Step 4: Assign stamp = Timestamp.as_unit(...)

```python
stamp = Timestamp('2000/1/1').as_unit('ns')
```

### Step 5: Assign offset_overflow = value

```python
offset_overflow = to_offset('D') * 100 ** 5
```

### Step 6: Assign lmsg3 = "Cannot cast -?10000000000 days \\+?00:00:00 to unit='ns' without overflow"

```python
lmsg3 = "Cannot cast -?10000000000 days \\+?00:00:00 to unit='ns' without overflow"
```

### Step 7: stamp + offset_overflow

```python
stamp + offset_overflow
```

### Step 8: offset_overflow + stamp

```python
offset_overflow + stamp
```

### Step 9: stamp - offset_overflow

```python
stamp - offset_overflow
```

### Step 10: stamp + offset_overflow

```python
stamp + offset_overflow
```

### Step 11: offset_overflow + stamp

```python
offset_overflow + stamp
```

### Step 12: stamp - offset_overflow

```python
stamp - offset_overflow
```


## Complete Example

```python
# Workflow
stamp = Timestamp('2017-01-13 00:00:00').as_unit('ns')
offset_overflow = 20169940 * offsets.Day(1)
lmsg2 = "Cannot cast -?20169940 days \\+?00:00:00 to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=lmsg2):
    stamp + offset_overflow
with pytest.raises(OutOfBoundsTimedelta, match=lmsg2):
    offset_overflow + stamp
with pytest.raises(OutOfBoundsTimedelta, match=lmsg2):
    stamp - offset_overflow
stamp = Timestamp('2000/1/1').as_unit('ns')
offset_overflow = to_offset('D') * 100 ** 5
lmsg3 = "Cannot cast -?10000000000 days \\+?00:00:00 to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=lmsg3):
    stamp + offset_overflow
with pytest.raises(OutOfBoundsTimedelta, match=lmsg3):
    offset_overflow + stamp
with pytest.raises(OutOfBoundsTimedelta, match=lmsg3):
    stamp - offset_overflow
```

## Next Steps


---

*Source: test_arithmetic.py:39 | Complexity: Advanced | Last updated: 2026-06-02*