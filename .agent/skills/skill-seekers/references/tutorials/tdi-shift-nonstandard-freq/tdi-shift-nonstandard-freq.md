# How To: Tdi Shift Nonstandard Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tdi shift nonstandard freq

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign tdi = pd.to_timedelta(...)

```python
tdi = pd.to_timedelta(range(5), unit='d')
```

### Step 2: Assign trange = value

```python
trange = tdi._with_freq('infer') + pd.offsets.Hour(1)
```

### Step 3: Assign result = trange.shift(...)

```python
result = trange.shift(3, freq='2D 1s')
```

### Step 4: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex(['6 days 01:00:03', '7 days 01:00:03', '8 days 01:00:03', '9 days 01:00:03', '10 days 01:00:03'], freq='D')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
tdi = pd.to_timedelta(range(5), unit='d')
trange = tdi._with_freq('infer') + pd.offsets.Hour(1)
result = trange.shift(3, freq='2D 1s')
expected = TimedeltaIndex(['6 days 01:00:03', '7 days 01:00:03', '8 days 01:00:03', '9 days 01:00:03', '10 days 01:00:03'], freq='D')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_shift.py:55 | Complexity: Intermediate | Last updated: 2026-06-02*