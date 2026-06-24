# How To: Repr Floats

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Series: test repr floats

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign markers = Series(...)

```python
markers = Series([1, 2], index=IntervalIndex([Interval(left, right) for left, right in zip(Index([329.973, 345.137], dtype='float64'), Index([345.137, 360.191], dtype='float64'))]))
```


## Complete Example

```python
# Workflow
markers = Series([1, 2], index=IntervalIndex([Interval(left, right) for left, right in zip(Index([329.973, 345.137], dtype='float64'), Index([345.137, 360.191], dtype='float64'))]))
```

## Next Steps


---

*Source: test_formats.py:46 | Complexity: Beginner | Last updated: 2026-06-02*