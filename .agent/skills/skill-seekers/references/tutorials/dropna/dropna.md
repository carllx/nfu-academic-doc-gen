# How To: Dropna

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate from_arrays: test dropna

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign exp = MultiIndex.from_arrays(...)

```python
exp = MultiIndex.from_arrays([[1, np.nan, 3, 5], [1, 2, np.nan, 5], ['a', 'b', 'c', 'e']])
```


## Complete Example

```python
# Workflow
exp = MultiIndex.from_arrays([[1, np.nan, 3, 5], [1, 2, np.nan, 5], ['a', 'b', 'c', 'e']])
```

## Next Steps


---

*Source: test_missing.py:30 | Complexity: Beginner | Last updated: 2026-06-02*