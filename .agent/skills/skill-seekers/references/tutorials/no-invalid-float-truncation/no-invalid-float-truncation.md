# How To: No Invalid Float Truncation

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test no invalid float truncation

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: start, end, freq
```

## Step-by-Step Guide

### Step 1: Assign expected = IntervalIndex.from_breaks(...)

```python
expected = IntervalIndex.from_breaks(breaks)
```

### Step 2: Assign result = interval_range(...)

```python
result = interval_range(start=start, end=end, periods=4, freq=freq)
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 4: Assign breaks = value

```python
breaks = [0.5, 1.5, 2.5, 3.5, 4.5]
```

### Step 5: Assign breaks = value

```python
breaks = [0.5, 2.0, 3.5, 5.0, 6.5]
```


## Complete Example

```python
# Setup
# Fixtures: start, end, freq

# Workflow
if freq is None:
    breaks = [0.5, 1.5, 2.5, 3.5, 4.5]
else:
    breaks = [0.5, 2.0, 3.5, 5.0, 6.5]
expected = IntervalIndex.from_breaks(breaks)
result = interval_range(start=start, end=end, periods=4, freq=freq)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_interval_range.py:156 | Complexity: Intermediate | Last updated: 2026-06-02*