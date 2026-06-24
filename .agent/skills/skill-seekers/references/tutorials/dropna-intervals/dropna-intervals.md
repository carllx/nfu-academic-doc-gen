# How To: Dropna Intervals

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Series: test dropna intervals

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([np.nan, 1, 2, 3], IntervalIndex.from_arrays([np.nan, 0, 1, 2], [np.nan, 1, 2, 3]))
```


## Complete Example

```python
# Workflow
ser = Series([np.nan, 1, 2, 3], IntervalIndex.from_arrays([np.nan, 0, 1, 2], [np.nan, 1, 2, 3]))
```

## Next Steps


---

*Source: test_dropna.py:54 | Complexity: Beginner | Last updated: 2026-06-02*