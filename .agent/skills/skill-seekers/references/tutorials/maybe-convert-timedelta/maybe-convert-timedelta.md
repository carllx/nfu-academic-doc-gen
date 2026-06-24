# How To: Maybe Convert Timedelta

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test maybe convert timedelta

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign pi = PeriodIndex(...)

```python
pi = PeriodIndex(['2000', '2001'], freq='D')
```

**Verification:**
```python
assert pi._maybe_convert_timedelta(offset) == 2
```

### Step 2: Assign offset = offsets.Day(...)

```python
offset = offsets.Day(2)
```

**Verification:**
```python
assert pi._maybe_convert_timedelta(2) == 2
```

### Step 3: Assign offset = offsets.BusinessDay(...)

```python
offset = offsets.BusinessDay()
```

### Step 4: Assign msg = 'Input has different freq=B from PeriodIndex\\(freq=D\\)'

```python
msg = 'Input has different freq=B from PeriodIndex\\(freq=D\\)'
```

### Step 5: Call pi._maybe_convert_timedelta()

```python
pi._maybe_convert_timedelta(offset)
```


## Complete Example

```python
# Workflow
pi = PeriodIndex(['2000', '2001'], freq='D')
offset = offsets.Day(2)
assert pi._maybe_convert_timedelta(offset) == 2
assert pi._maybe_convert_timedelta(2) == 2
offset = offsets.BusinessDay()
msg = 'Input has different freq=B from PeriodIndex\\(freq=D\\)'
with pytest.raises(ValueError, match=msg):
    pi._maybe_convert_timedelta(offset)
```

## Next Steps


---

*Source: test_period.py:193 | Complexity: Intermediate | Last updated: 2026-06-02*