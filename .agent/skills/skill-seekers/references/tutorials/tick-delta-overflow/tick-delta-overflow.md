# How To: Tick Delta Overflow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tick delta overflow

## Prerequisites

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas._testing._hypothesis`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign tick = offsets.Day(...)

```python
tick = offsets.Day(10 ** 9)
```

### Step 2: Assign msg = "Cannot cast 1000000000 days 00:00:00 to unit='ns' without overflow"

```python
msg = "Cannot cast 1000000000 days 00:00:00 to unit='ns' without overflow"
```

### Step 3: Assign depr_msg = 'Day.delta is deprecated'

```python
depr_msg = 'Day.delta is deprecated'
```

### Step 4: tick.delta

```python
tick.delta
```


## Complete Example

```python
# Workflow
tick = offsets.Day(10 ** 9)
msg = "Cannot cast 1000000000 days 00:00:00 to unit='ns' without overflow"
depr_msg = 'Day.delta is deprecated'
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    with tm.assert_produces_warning(FutureWarning, match=depr_msg):
        tick.delta
```

## Next Steps


---

*Source: test_ticks.py:241 | Complexity: Intermediate | Last updated: 2026-06-02*