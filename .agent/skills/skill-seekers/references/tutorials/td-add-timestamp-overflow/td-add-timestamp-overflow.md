# How To: Td Add Timestamp Overflow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test td add timestamp overflow

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp.as_unit(...)

```python
ts = Timestamp('1700-01-01').as_unit('ns')
```

### Step 2: Assign msg = "Cannot cast 259987 from D to 'ns' without overflow."

```python
msg = "Cannot cast 259987 from D to 'ns' without overflow."
```

### Step 3: Assign msg = "Cannot cast 259987 days 00:00:00 to unit='ns' without overflow"

```python
msg = "Cannot cast 259987 days 00:00:00 to unit='ns' without overflow"
```

### Step 4: ts + Timedelta(13 * 19999, unit='D')

```python
ts + Timedelta(13 * 19999, unit='D')
```

### Step 5: ts + timedelta(days=13 * 19999)

```python
ts + timedelta(days=13 * 19999)
```


## Complete Example

```python
# Workflow
ts = Timestamp('1700-01-01').as_unit('ns')
msg = "Cannot cast 259987 from D to 'ns' without overflow."
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    ts + Timedelta(13 * 19999, unit='D')
msg = "Cannot cast 259987 days 00:00:00 to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    ts + timedelta(days=13 * 19999)
```

## Next Steps


---

*Source: test_arithmetic.py:101 | Complexity: Intermediate | Last updated: 2026-06-02*